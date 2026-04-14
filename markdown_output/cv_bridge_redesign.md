The redesigned C++ API is now included in [cv_bridge](cv_bridge). Please
see the documentation there; the released version differs slightly from
the proposal below.

[cv_bridge](cv_bridge) is the ROS user\'s gateway to the world of
OpenCV, and is used ubiquitously in vision nodes. Although it gets the
job done, I\'ve noticed some recurring issues that trip up new (and
sometimes old) users. I think the C++ API has enough room for
improvement to warrant a redesign.

## Problems with the current C++ cv_bridge

1\. Unpredictable memory ownership semantics. This is the biggest
problem, and has confused people with strange bugs in the past. For
example: ```cplusplus
class Example {
  sensor_msgs::CvBridge bridge_;
  IplImage* saved_image_;

  void imageCallback(const sensor_msgs::ImageConstPtr& image_msg)
  {
    // Save incoming image for later use
    saved_image_ = bridge_.imgMsgToCv(image_msg, "bgr8");
  }

  void foo()
  {
    // On some other event, do something with the most recent saved image
    cvSaveImage("foo.jpg", saved_image_);
  }
};
``` This will work, \'\'unless\'\'
\`image_msg\` already has \`bgr8\` encoding. In that case
\`saved_image\_\` does not copy the image data, but instead points to
data held by \`image_msg\` which is freed when the message goes out of
scope. Later \`foo()\` is called and probably segfaults. I\'ve seen
cases of nodes that worked one day, then segfaulted when another image
stream with the \"mined\" encoding was used. 1.#2 More counter-intuitive
ownership semantics: the returned \`IplImage\*\` from \`imgMsgToCv\` is
actually owned by the bridge, and must not be freed by the user. In
practice users look at the \`cv_bridge\` code samples; adapt them to
actually do something, creating more \`IplImage\*\` with intermediate
results; and then forget to free the images they created. 1. Need to
create a \`CvBridge\` instance for each image stream. Due to the above
behavior, ```cplusplus
void imageCallback(const sensor_msgs::ImageConstPtr& left_msg,
                   const sensor_msgs::ImageConstPtr& right_msg)
{
  sensor_msgs::CvBridge bridge;
  IplImage* left  = bridge.imgMsgToCv(left_msg, "bgr8");
  IplImage* right = bridge.imgMsgToCv(right_msg, "bgr8");
}
``` looks plausible but results in
unpredictable behavior. 1.#4 Lack of const-correctness. \`imgMsgToCv\`
returns an unqualified \`IplImage\*\`, which may point to \`const\`
message data. In that case users are free to modify the original message
data, and may not even realize they are doing it. I anticipate this
being another source of bugs as more image processing is done in
nodelets. 1. It still uses \`IplImage\*\`, when we\'ve been actively
pushing users towards the much safer and more convenient \`cv::Mat\`. 1.
Header and encoding information is not preserved with the returned
\`IplImage\*\`. When publishing, the encoding is specified again as an
argument to \`cvToImgMsg\`, and the header must be filled in separately.
Forgetting to copy the header to the new \`Image\` is a common mistake.

## Basic proposal

Note: the current implementation does not exactly match the API proposed
here, but it\'s essentially the same.

First we declare an analogue of \<\<MsgLink(sensor_msgs/Image)\>\> that
uses a \`cv::Mat\` for data storage. ```cplusplus
// File cv_bridge/cv_bridge.h

namespace cv_bridge {

class CvImage
{
public:
  roslib::Header header; //!< ROS header
  std::string encoding;  //!< Image encoding ("mono8", "bgr8", etc.)
  cv::Mat image;         //!< Image data for use with OpenCV

protected:
  // Allows sharing ownership with sensor_msgs::Image(Const)Ptr
  boost::shared_ptr<void const> tracked_object_;
};

typedef boost::shared_ptr<CvImage> CvImagePtr;
typedef boost::shared_ptr<CvImage const> CvImageConstPtr;

// ...

}
```

### ROS message to OpenCV

We will convert \<\<MsgLink(sensor_msgs/Image)\>\> messages into
\`CvImage\`, which addresses issues 5 and 6.

There are two basic use cases when converting a \`const
sensor_msgs::Image\`: 1. We want to modify the data in-place. We have to
make a copy. 1. We won\'t modify the data. We can safely share instead
of copying.

Sharing the message data (vision researchers are neurotic about avoiding
unnecessary copies) motivated the complexity of \`cv_bridge\`. Most of
the problems come from not distinguishing between the two cases. In the
proposed API we make them explicit: ```cplusplus
// Case 1: Always copy, returning a mutable CvImage
CvImagePtr toCvCopy(const sensor_msgs::ImageConstPtr& source,
                    const std::string& encoding = std::string());
CvImagePtr toCvCopy(const sensor_msgs::Image& source,
                    const std::string& encoding = std::string());

// Case 2: Share if possible, returning a const CvImage
CvImageConstPtr toCvShare(const sensor_msgs::ImageConstPtr& source,
                          const std::string& encoding = std::string());
```

The empty default for \`encoding\` takes the place of \`passthrough\`;
unless specified, the \`CvImage\` has the same encoding as the source.

In the shared case, we return a pointer to \`const CvImage\` to enforce
the immutability of the image data (issue 4). If the desired encoding
matches that of the source, \`toCvShare\` aliases the source image data.
It also sets \`CvImage::tracked_object\_\` to the \`source\` pointer,
ensuring the data is not deleted prematurely (issue 1). Note there is no
overload taking a \`const sensor_msgs::Image&\`, because then there\'s
no way to ensure the \`Image\` out-lives the \`CvImage\`.

Since there\'s no bridge object, and ownership is managed within
\`CvImage\`, we sidestep issues 2 and 3.

### OpenCV to ROS message

Now we\'ll add a couple methods to \`CvImage\` to go the other way:

```cplusplus
class CvImage
{
  sensor_msgs::ImagePtr toRos() const;

  // This overload is intended mainly for aggregate messages such as
  // stereo_msgs::DisparityImage, which contains a sensor_msgs::Image
  // as a data member.
  void toRos(sensor_msgs::Image& ros_image) const;
};
```

### Other functions

Analogous to
[cv::cvtColor](http://opencv.willowgarage.com/documentation/cpp/miscellaneous_image_transformations.html#index-211),
a convenience function for converting an image to another encoding:
```cplusplus
CvImagePtr cvtColor(const CvImageConstPtr& source,
                    const std::string& encoding);
```

And some functions for distinguishing categories of encodings. These
might be better located in \`sensor_msgs/image_encodings.h\`.
```cplusplus
bool isColor(const std::string& encoding);
bool isMono(const std::string& encoding);
bool isBayer(const std::string& encoding);
bool hasAlpha(const std::string& encoding);
int  numChannels(const std::string& encoding);
int  bitDepth(const std::string& encoding);
```

## Example usage

A complete example of a node that draws a circle on images and
republishes them. ```cplusplus
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

image_transport::Publisher pub;

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  cv_bridge::CvImagePtr cv_msg = cv_bridge::toCvCopy(msg, "bgr8");
  cv::circle(cv_msg->image, cv::Point(50, 50), 10, CV_RGB(255,0,0));
  pub.publish(cv_msg->toRos());
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "processor");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  pub = it.advertise("image_out", 1);
  image_transport::Subscriber sub = it.subscribe("image", 1, imageCallback);
  ros::spin();
}
```

A more complicated callback example. In this case we want to use color
if available, otherwise falling back to monochrome. We avoid copies for
\`bgr8\` and \`mono8\` encodings. In either case, we republish the
source image with color annotations. ```cplusplus
using namespace cv_bridge;

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  bool is_color = isColor(msg->encoding);
  CvImageConstPtr source = is_color ? toCvShare(msg, "bgr8")
                                    : toCvShare(msg, "mono8");

  // Do vision processing on source...

  // Now we create and publish an annotated color image
  CvImagePtr display = cvtColor(source, "bgr8");
  // Draw detected objects, etc. on display->image...
  pub.publish(display->toRos());
}
```

## Backwards compatibility

Since the proposal defines entirely new data structures and functions,
the original \`sensor_msgs::CvBridge\` can continue to exist as-is.
Eventually it would be deprecated and removed.

## Possible extensions

### Bayer support

The current \`cv_bridge\` doesn\'t support the Bayer encodings, as
debayering should normally be done by [image_proc](image_proc). But
maybe that would be a nice convenience?

### Using CvImage as a message type

By hooking into the [roscpp](roscpp) serialization API, it\'s possible
to make \`CvImage\` a real ROS message, wire-compatible with
\<\<MsgLink(sensor_msgs/Image)\>\>. This is already implemented in the
\`cv_bridge_redesign\` package, and it\'s quite nice; you can use
callbacks of the form ```cpluscplus
void imageCb(const cv_bridge::CvImageConstPtr& image_msg);
``` and publish \`CvImage\`
directly. No \`toCvCopy\`/\`toCvShared\`/\`toRos\` required! And when
publishing, we avoid the copy from converting to \`sensor_msgs::Image\`.

The big issue is how to make this play nice with
[image_transport](image_transport). \`image_transport\` \'\'could\'\' be
generalized, by templating the \`publish()\` and \`subscribe()\`
methods, but it\'s somewhat complicated and would require more coding
effort.
