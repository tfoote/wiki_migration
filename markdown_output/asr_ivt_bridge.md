![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This package contains a library which is used to convert image data
structures between ROS and [IVT](http://ivt.sourceforge.net/).

![\|width=\"600\",height=\"323\"](attachment:Diagramm1.png)

## Functionality

The structure of this library is based on the
[cv_bridge](cv_bridge)-package, for more information you can check out
the documentation for that.

## Usage

### Needed packages

-   [asr_ivt](asr_ivt)

## ROS Nodes

### Topics/Services

As this package only contains a library there are no
subscribed/published topics or services.

## Tutorials

Include\'\' ivt_image.h\'\' and/or \'\'ivt_calibration.h\'\' to your
code, depending on what you want to convert (images or camera
calibrations).

------------------------------------------------------------------------

\'\'\'Convert an image\'\'\'

To convert a \'\'sensor_msgs::Image\'\' to a \'\'CByteImag\'\'e of the
IVT-library call one of the following functions (notice that the
\'\'toIvtCopy\'\'-functions create a copy of the input messages while
the other ones try to share the data if possible):

```
IvtImagePtr toIvtCopy(const sensor_msgs::ImageConstPtr& source, const std::string& encoding = std::string());
IvtImagePtr toIvtCopy(const sensor_msgs::Image& source, const std::string& encoding = std::string());
``` or

```
IvtImageConstPtr toIvtShare(const sensor_msgs::ImageConstPtr& source, const std::string& encoding = std::string());
IvtImageConstPtr toIvtShare(const sensor_msgs::Image& source, const boost::shared_ptr<void const>& tracked_object, const std::string& encoding = std::string());
``` The return-value is a
\'\'!IvtImagePtr\'\'-object, which contains a \'\'CByteImage\*\'\'
member called image.

To convert such an \'\'!IvtImage\'\' back to ROS call one of the
following member functions:

```
sensor_msgs::ImagePtr toImageMsg() const;
void toImageMsg(sensor_msgs::Image& ros_image) const;
```

------------------------------------------------------------------------

\'\'\'Convert camera calibration messages:\'\'\'

To convert a ROS \'\'sensor_msgs::!CameraInfo\'\' to an IVT
\'\'CCalibration\'\' instantiate either an \'\'!IvtCalibration\'\' or an
\'\'!IvtStereoCalibration\'\' object (depends on your camera system:
mono or stereo). Then call one of the provided member functions with the
ROS-!CameraInfo-message you want to convert (for a stereo system you
have to provide messages of both cameras of course):

```
bool fromCameraInfo(const sensor_msgs::CameraInfo& msg);
bool fromCameraInfo(const sensor_msgs::CameraInfoConstPtr& msg);
``` in case of a mono camera system and

```
bool fromCameraInfo(const sensor_msgs::CameraInfo& left, const sensor_msgs::CameraInfo& right);
bool fromCameraInfo(const sensor_msgs::CameraInfoConstPtr& left, const sensor_msgs::CameraInfoConstPtr& right);
``` in case of a stereo one.

The converted message can be obtained with the provided getter-functions
(depends again on your used camera system):

```
boost::shared_ptr<CCalibration> getCalibration(bool forRectifiedImages=false) const;
boost::shared_ptr<CStereoCalibration> getStereoCalibration(bool forRectifiedImages=false) const;
```
