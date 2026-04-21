![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This Package contains a library which is used to convert point clouds
and images between ROS and
[HALCON](http://www.mvtec.com/products/halcon/) specific data
structures.

![\|width="600",height="299"](attachment:halcon_bridge_overview.png)

## Functionality

The structure of this library is mostly based on the
[cv_bridge](cv_bridge)-package, for more information you can check out
the documentation for that.

## Usage

### Needed packages

The package itself does not have any dependencies on external
ROS-packages (besides the default ones which come with the core
installation of ROS).

### Needed software

To be able to build this package and use it in your project you will
need to have a version of the
[HALCON](http://www.mvtec.com/products/halcon/) image processing library
installed. So far it was tested mainly with version 11 but in theory it
should work with higher versions as well as the basic structure of the
data types has not changed (build tests have been conducted with version
12 as well).

The environment variables *HALCONROOT* and *HALCONARCH* need to be set
correctly, otherwise cmake won't be able to find your HALCON
installation. Usually this should be the case if you have followed the
installation guide of HALCON.

### Needed hardware

You need to have a valid license for your HALCON installation; if you
obtained a usb-dongle for that reason you need to have it plugged in
during runtime or you will receive an exception.

### Start system

As this package only contains a library you should see 5. for more
information on how to use it.

## ROS Nodes

There are no subscribed/published topics or services and also no
configuration parameters.

## Tutorials

To use the functions offered by this library you need to set this
package as a dependency for your project first and then include either
halcon_image.h or halcon_pointcloud.h in your code depending on what you
want to convert.

------------------------------------------------------------------------

**Convert an image:**

To convert a *sensor_msgs::Image* to a *!HalconCpp::HImage* call one of
the following functions:



```
HalconImagePtr toHalconCopy(const sensor_msgs::ImageConstPtr& source)
HalconImagePtr toHalconCopy(const sensor_msgs::Image& source);
```

 The return-value is a *!HalconImagePtr *object,
which contains a* !HalconCpp::HImage*-Pointer as a member called
*image*.

To convert a *!HalconImage* to ROS again call one of the following
member functions:



```
sensor_msgs::ImagePtr toImageMsg() const;
void toImageMsg(sensor_msgs::Image& ros_image) const;
```



------------------------------------------------------------------------

**Convert a point cloud:**

This step is similar to the image conversion. The important functions
are



```
HalconPointcloudPtr toHalconCopy(const sensor_msgs::PointCloud2ConstPtr& source);
HalconPointcloudPtr toHalconCopy(const sensor_msgs::PointCloud2& source);
```

 to convert a *sensor_msgs::!PointCloud2* to a*
!HalconCpp::HObjectModel3D* (the member in the returned
*!HalconPointcloud* is called *model*).

To convert it back to ROS call:



```
sensor_msgs::PointCloud2Ptr toPointcloudMsg() const;
void toPointcloudMsg(sensor_msgs::PointCloud2& ros_pointcloud) const;
```


