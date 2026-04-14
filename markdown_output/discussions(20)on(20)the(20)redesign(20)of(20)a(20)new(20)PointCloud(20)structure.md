## Overview

This package is a temporary home for the proposed new point cloud
messages and related infrastructure. The goal is to give users maximal
flexibility and ease in working with point clouds and channel data,
without sacrificing efficiency.

## Messages

The new \`PointCloud\` message interleaves all channels into a binary
blob, with info about structure in \`fields\`.

PointCloud.msg:

```
Header header

# Point data is stored as a binary blob.
PointField[] fields
uint8[]      data

# 2D structure of the point cloud. If the cloud is unordered,
# height is 1 and width is the length of the point cloud.
uint32 width
uint32 height

bool is_dense     # True if there are no invalid points
bool is_bigendian
``` PointField.msg:

```
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name
uint32 offset
uint8  datatype
``` Discussion:

-   (Patrick) Should PointCloud contain a stride field? Not strictly
    necessary - stride = data.size() / (width\*height) - but could be
    nice to see.
-   (Patrick) Is PointField an appropriate place for the datatype enum
    (INT8, etc.) or might we want to reuse that in other messages?

## Registering a user-defined point type

We provide macros for registering a user-defined point struct with the
publish/subscribe infrastructure. There are two versions. If your struct
is flat (only scalar data members) and all field names are standard, you
can use the concise form \`POINT_CLOUD_REGISTER_FLAT_POINT_STRUCT\`. If
your struct contains struct members, array members, or has any
non-standard named fields, you should use the more general
\`POINT_CLOUD_REGISTER_POINT_STRUCT\`. For example:

```
#include <stdint.h>
#include "point_cloud_redesign/register_point_struct.h"

namespace my_ns {

struct MyPoint
{
  float x;
  float y;
  float z;

  uint32_t w;
};

} // namespace my_ns

// Must be used in the global namespace with the fully-qualified name
// of the point type.
POINT_CLOUD_REGISTER_FLAT_POINT_STRUCT(
  my_ns::MyPoint,
  (float, x)
  (float, y)
  (float, z)
  (uint32_t, w));


namespace my_ns2 {

struct Position
{
  float x;
  float y;
  float z;
}

struct MyComplexPoint
{
  Position pos;
  uint32_t w;
  float normal[3];
};

} // namespace my_ns2

POINT_CLOUD_REGISTER_POINT_STRUCT(
  my_ns2::MyComplexPoint,
  (float,    pos.x,     x)
  (float,    pos.y,     y)
  (float,    pos.z,     z)
  (uint32_t, w,         w)
  (float,    normal[0], normal_x)
  (float,    normal[1], normal_y)
  (float,    normal[2], normal_z));
``` The registration list contains (datatype,
accessor, tag) 3-tuples. In the flat case, the accessor and tag are the
same.

The registration macro, incidentally, also registers the point struct
with
[Boost.Fusion](http://www.boost.org/doc/libs/1_40_0/libs/fusion/doc/html/index.html)
as an associative type, meaning you can access fields by tag:

```
#include <boost/fusion/sequence/intrinsic/at_key.hpp>

my_ns::MyPoint pt1 = {1.0, 2.5, 6.1, 42};
MyComplexPoint pt2 = {{1.0, 2.5, 6.1}, 42, {0.0, 1.0, 0.0}};

printf("pt1 has x = %f\n", pt1.x);
printf("pt2 has x = %f\n", pt2.pos.x);
// is identical to...
printf("pt1 has x = %f\n", boost::fusion::at_key<point_cloud::fields::x>(pt1));
printf("pt2 has x = %f\n", boost::fusion::at_key<point_cloud::fields::x>(pt2));
``` The syntax could be made less horrible; the
point is that this at least opens the possibility of writing generic
point cloud algorithms that operate efficiently on arbitrary
user-defined point types.

Limitations:

-   To be strictly portable, point type must be POD (Plain Old Data) -
    essentially a C struct.
-   (Lifted \"flatness\" requirement in r26301)

Discussion:

-   (Patrick) The POD restriction is hopefully not onerous?
-   \[Josh\] Is there a use-case for non-POD types? I can\'t think of a
    good reason for it.
-   (Patrick) People seemed to want hierarchically-defined point types.
    Does the proposed syntax look reasonable?
-   \[Josh} I\'m fine with it

## Publishing point clouds

There is a specialized \`point_cloud::Publisher\` for point clouds
([doc](http://www.ros.org/doc/api/point_cloud_redesign/html/classpoint__cloud_1_1Publisher.html)).
It\'s templated on a registered point type. The \`publish()\` methods
take point clouds as a container of points (plus dimensions for
structured clouds), where the container is anything recognized by
[Boost.Range](http://www.boost.org/doc/libs/1_40_0/libs/range/index.html).
That includes STL containers, fixed-size arrays, pairs of pointers or
iterators, etc.

Usage example:

```
#include "my_point.h"
#include <point_cloud_redesign/publisher.h>
#include <ros/ros.h>

int main(int argc, char** argv)
{
  std::vector<my_ns::MyPoint> pt_cloud;
  my_ns::MyPoint pt = {1.0, 2.5, 6.1, 42};
  pt_cloud.push_back(pt);

  ros::init(argc, argv, "point_cloud_publisher");
  ros::NodeHandle nh;
  point_cloud::Publisher<my_ns::MyPoint> pub;
  pub.advertise(nh, "cloud", 1);

  ros::Rate loop_rate(4);
  while (nh.ok()) {
    pub.publish(pt_cloud); // unordered, may be invalid points
    ros::spinOnce();
    loop_rate.sleep();
  }
}
``` Discussion:

-   (Patrick) Should the unordered version of \`publish()\` assume the
    point cloud is dense?
-   (Patrick) Doesn\'t currently follow convention of having a separate
    class with \`advertise()\`, \`subscriber()\` methods like
    \`NodeHandle\` and \`ImageTransport\`.
-   \[Josh\] I\'m liking this way more and more, may provide the option
    in the ROS api at some point. This is mainly due to the fact that
    we\'re creating all these custom publisher/subscribers and it\'d be
    nice to have a uniform API.
-   \[Josh\] Below you create a
    \`point_cloud::PointCloud\<my_ns::MyPoint\>\`, can the Publishing
    API take these as well?

## Subscribing to point clouds

There is a specialized \`point_cloud::Subscriber\` for point clouds
([doc](http://www.ros.org/doc/api/point_cloud_redesign/html/classpoint__cloud_1_1Subscriber.html)).
It\'s templated on a registered point type. The subscriber callback
takes a const-ptr to \`point_cloud::PointCloud\`
([doc](http://www.ros.org/doc/api/point_cloud_redesign/html/structpoint__cloud_1_1PointCloud.html))
which is also templated on the point type.

Usage example:

```
#include "my_point.h"
#include <point_cloud_redesign/subscriber.h>

void callback(const point_cloud::PointCloud<my_ns::MyPoint>::ConstPtr& msg)
{
  printf("Cloud: width = %u, height = %u\n", msg->width, msg->height);
  BOOST_FOREACH(const my_ns::MyPoint& pt, msg->points)
    printf("\t(%f, %f, %f, %u)\n", pt.x, pt.y, pt.z, pt.w);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "point_cloud_listener");
  ros::NodeHandle nh;
  point_cloud::Subscriber<my_ns::MyPoint> sub;
  sub.subscribe(nh, "cloud", 1, callback);
  ros::spin();
}
``` Limitations:

-   Is very unoptimized. Analysis of how to map serialized data to the
    point struct is only performed on the first message received, but
    for all messages we currently:
-   Deserialize into the \`point_cloud_redesign::PointCloud\` message
    type. There is no custom deserializer yet.
-   (Is it possible to write a stateful deserializer in ROS?)
-   \[Josh\] It may be possible, but I can\'t think of a way off the top
    of my head. If necessary we can provide a way.
-   For every field in every point, we perform an individual memcpy.
-   Does not handle conversions. You can\'t publish a field as a double
    then deserialize it to a float.
-   Can\'t currently specify alignment of point data. This probably
    means another traits class / registration macro. Do we only care
    about 16-byte alignment, or are there other allocation scenarios we
    want to support?
-   \[Josh\] Can we support a \`std::allocator\` (gross yes, but
    standard) as a template argument to \`PointCloud\`?

#### Ethan\'s Initial Reactions / Questions

Stride -\> my understanding was that there was not only a stride, but
there was a stride per PointField. This allows for either interleaved or
separate planes. I\'m not convinced that always interleaving is what we
want (I like 128 bit alignment for instance, and I don\'t like padding).
Is this infeasible for some reason? Perhaps as an alternative some sort
of point class that is a collection of the new new point clouds, but
does not have disgusting syntax. Then one could have a piece that is 128
bit aligned, and a piece that is unaligned and some weird size, and not
waste space on padding.

With all of the possible point structs how does one tell if a given
point is invalid or valid if the cloud is not dense?

Having loads of custom publishers / subscribers feels wrong (it\'s one
thing if it\'s just image_transport, it\'s another if you have to look
up the appropriate publisher type every time you want to publish
something). Can we get around this somehow? Would it require a ROS API
change? It seems like the hooks should be available to do whatever needs
to be done within a ROS publisher / subscriber. Template specialization
feels like the right solution here for C++. Of course this brings up:

How does other language support work?

For now I think 128-bit alignment is the most important, but I could
imagine scenarios where other alignments might be important. For example
256-bit is already potentially important for some graphics card
applications, and will be important in future versions of SSE (SSE5).

It seems like we need some enums to standardize names for fields. I
don\'t want one person using \"x\" and another using \"X\" for instance.
I\'d like all the normals called the same things, etc.

#### Notes 11/16/09

-   Useful to add point_stride, row_stride to account for padding
-   Ethan suggests a more flexible field layout. \`PointField\` would
    contain an offset to the first instance and a stride to each
    subsequent instance. This allows storing the data in planes, or
    having separate interleaved sections.
-   Or have \`PointCloud\` contain an array of binary blobs?
-   Just publish different planes as separate \`PointCloud\` messages?
-   Probably want to support time synching multiple point cloud topics,
    better model for distributed computation. E.g. node 1 publishes XYZ
    data, node 2 computes normals and publishes them as separate point
    cloud message, node 3 synchronizes both for point+normal
    computations.
-   Do this in \`point_cloud::Subscriber\`?
-   Will stress our time synchronizer:
-   Number of point cloud topics could be dynamic.
-   Synchronize messages before deserialization??
