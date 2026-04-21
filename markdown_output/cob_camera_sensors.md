The *cob_camera_sensors* package is a collection of ROS compatible
drivers for the cameras installed on Care-O-bot 3. These include two
color cameras (either of type *AVT Pike C145* or *AVT Prosilica
GC1380CH*) and one *Swissranger 4000* time-of-flight sensor from Mesa
Imaging or the *Microsoft Kinect* sensor. All camera types are supported
for Windows and Linux. To enable Windows compatibility, remove all
`-D__LINUX__` flags from *CMakeLists.txt* located at
*cob_driver/cob_camera_sensors*. The two Prosilica GC1380CH are natively
supported by ROS with the *prosilica_camera* package. The binaries of
the *prosilica_camera* package are executed within the related launch
files. The same holds for the Kinect whose driver is located in the
*openni_camera* package.

Setting the camera parameters for the *AVT Pike C145* and *Swissranger
4000* is different from the suggested ROS standard. Instead of setting
all parameters within the ROS launch file, camera specific parameters
are set within IPA specific configuration files. This originates from
IPA internal requirements to maintain backward compatibility to existing
components. The ROS launch file only holds parameters related to the
camera setup (e.g. specifying the used camera types) and a link to the
IPA internal configuration file.

## Quick launch guide

In order to launch the camera nodes, do the following (Replace `cob3-2`
with your personal Care-O-bot identifier)

For running all cameras

```
export ROBOT=cob3-2
roslaunch cob_camera_sensors all_cameras.launch
``` For running the left or right color cameras

```
roslaunch cob_camera_sensors left.launch
roslaunch cob_camera_sensors right.launch
``` For running the depth imaging camera

```
roslaunch cob_camera_sensors cam3d.launch
``` In order to check if everything is running
launch the image viewer

To show the color images

```
rosrun image_view image_view image:=/stereo/left/image_color
``` and

```
rosrun image_view image_view image:=/stereo/right/image_color
``` For quitting do not close the viewer window,
but hit `CTRL-C` on your console

To show the time-of-flight images

```
roslaunch cob_camera_sensors tof_camera_viewer.launch
``` For quitting do not close the viewer window,
but hit `CTRL-C` on your console

## Code API

/\*12.name= /sr4000/image_grey 12.type= sensor_msgs/Image 12.desc=
Intensity images of tof camera 13.name= /sr4000/image_xyz 13.type=
sensor_msgs/Image 13.desc= XYZ data of tof camera 14.name=
/sr4000/camera_info 14.type= sensor_msgs/CameraInfo 14.desc= Camera
intrinsics of tof camera

-   / ```clearsilver

name = cob_camera_sensors
desc = Provides access to the two color cameras and the time-of-flight sensor mounted on Care-O-Bot's head module.

pub {
0.name= /stereo/left/image_color
0.type= sensor_msgs/Image
0.desc= Color images of color camera
1.name= /stereo/left/camera_info
1.type= sensor_msgs/CameraInfo
1.desc= Camera intrinsics of color camera
6.name= /stereo/right/image_color
6.type= sensor_msgs/Image
6.desc= Color images of color camera
7.name= /stereo/right/camera_info
7.type= sensor_msgs/CameraInfo
7.desc= Camera intrinsics of color camera
11.name= /cam3d/depth/camera_info
11.type= sensor_msgs/CameraInfo
11.desc= Camera intrinsics of depth camera
12.name= /cam3d/depth/image
12.type= sensor_msgs/Image
12.desc= single channel floating point (float32) depth image, containing the depth in meters
13.name= /cam3d/depth/points
13.type= sensor_msgs/PointCloud2
13.desc= point cloud without color information
14.name= /cam3d/rgb/camera_info
14.type= sensor_msgs/CameraInfo
14.desc= Camera parameters for the RGB camera (only available with Kinect)
15.name= /cam3d/rgb/image_color
15.type= sensor_msgs/Image
15.desc= RGB image (only available with Kinect)
16.name= /cam3d/rgb/image_mono
16.type= sensor_msgs/Image
16.desc= Intensity images of Swissranger camera or grayscale image of Kinect
17.name= /cam3d/rgb/points
17.type= sensor_msgs/PointCloud2
17.desc= point cloud containing RGB value for each point (only available with Kinect)
}
param {
group.0 {
name=Parameters
desc=
0.name= ~ip_address
0.default= 169.254.47.10
0.type= str
0.desc=URL defining which camera to connect to with which IP address.
8.name= ~trigger_mode
8.default= streaming
8.type= str
8.desc=Sets the trigger mode.
}
```

## IPA configuration files

The IPA configuration file is located at
*cob_driver/cob_camera_sensors/common/files* in a folder related to your
sensor setup e.g. *cob3-1* or *cob3-2*. The configuration is XML-based.
It holds one XML-tag for each camera e.g. `<AVTPikeCam_0>` for a AVT
Pike C145 camera. The number within the tag-name is used to
differentiate several camera of the same type. Here is an excerpt from
the IPA configuration file of one of our Care-O-bots.

```
<!-- Camera sensors initialization file -->
<LibCameraSensors>

<AVTPikeCam_0>
  <!-- Holds the 64-Bit GUID of a connected node -->
  <!-- A GUID consists of a 32-Bit high part that holds the VendorId (Highest 24 Bits) -->
  <!-- and the ChipIdHigh (8 Bits) and a 32-Bit low part that holds the ChipIdLow. -->
  <!-- The GUID is unique for all FireWire devices on the world. -->
  <GUID high="000A4701" low="10077005" />

  <!-- The master initializes and releases the camera library and is -->
  <!-- respnsible for emitting the trigger signal to other cameras -->
  <!-- The slave is synchronizing its image acquisition with the trigger signal -->
  <!-- Valid roles: MASTER oR SLAVE -->
  <Role value="MASTER" />

  <!-- Valid values: appropriate framerte or AUTO and DEFAULT -->
  <FrameRate fps="3" />

    <!-- Valid values: FORMAT_0, FORMAT_1, FORMAT_2 ,FORMAT_7, DEFAULT-->
  <VideoFormat type="FORMAT_7" />

  <!-- Valid values: MODE_0 - MODE_7, DEFAULT -->
  <VideoMode type="MODE_0" />
  ...
<AVTPikeCam_0/>
<LibCameraSensors/>
``` Each tag within the IPA configuration file has
a short explanation of its functionality. Please feel free to examine
one of the Care-O-bot configuration files to get an impression of the
possible settings.

Camera intrinsics may be set for each camera within the designated tags.
The information is later published with the images using the ROS *Camera
Publisher* from the *image_transport* package. The user has the
possibility of specifying different intrinsic for one camera. This is
related to stereo vision, where intrinsics are optimize to fit to
another camera. Within the ROS node that publishes camera images, the
non-optimized intrinsic are published with the images. Extrinsic specify
the rotation and translation relative to another camera. These
parameters are not yet published and for IPA internal usage only.

For each camera there is also a related `<VirtualXXXCam_X>` tag. This is
also related to backward compatibility issues and not used within ROS.
Originally, it provided support for loading saved image data from disk
and using it as if it came from a real camera device. However, ROS
already provides more sophisticated means to record and play back data
using [rosbag](rosbag) and [bag files](Bags).

## ROS launch files

ROS launch files are located in
`cob_driver/cob_camera_sensors/ros/launch` and hold information about
the overall sensor setup not related to a specific camera. There is a
launch file to start each camera independently
(`cam3d.launch, left.launch, right.launch`) and a launch file to start
all Care-O-bot cameras at once (`all_cameras.launch`). Before you can
start these launch files, you have to specify your robot id via
`export ROBOT=cob3-1` for example. Each launch file specifies the
location of the related IPA configuration file and the used color camera
or time-of-flight camera type. The robot specific launch and
configuration files are located in the
`cob_driver/cob_camera_sensors/ros/launch/$ROBOT` folders. The following
camera types are supported:

-   **CAM_SWISSRANGER** - For Mesa Swissranger 3000/4000 time-of-flight
    camera
-   **CAM_AVTPIKE** - For AVT Pike 145C color camera
-   **Prosilica GC1380CH GigE** - Through the ROS driver
-   **Kinect** - Through the ROS driver

The Prosilica GC1380CH color camera is supported through the ROS
*prosilica_camera* package. To get more information, have a look at
their tutorial. The camera specific launch files have an additional
parameter specifying the camera\'s ID which is related to the number
within the tag-name in the IPA configuration file e.g.
*\<AVTPikeCam_0\>*.

Knowing the fundamentals, we are now ready to start up the cameras. The
following table sums up the built-in cameras for each Care-O-Bot.

  -- ----------- -- ----------------------------------------------- -- ------------------------------------------------------------- --
     **Robot**      **3D Sensor**                                      **Left/Right Camera Sensors**                                 
     cob3-1         [Kinect](cob_camera_sensors/Microsoft_Kinect)      [AVT Pike C145](cob_camera_sensors/AVT_Pike)                  
     cob3-2         [Kinect](cob_camera_sensors/Microsoft_Kinect)      [Prosilica GC1380CH GigE](cob_camera_sensors/AVT_Prosilica)   
     cob3-3         [Kinect](cob_camera_sensors/Microsoft_Kinect)      [Prosilica GC1380CH GigE](cob_camera_sensors/AVT_Prosilica)   
     cob3-4         [Kinect](cob_camera_sensors/Microsoft_Kinect)      [Prosilica GC1380CH GigE](cob_camera_sensors/AVT_Prosilica)   
     cob3-5         [Kinect](cob_camera_sensors/Microsoft_Kinect)      [Prosilica GC1380CH GigE](cob_camera_sensors/AVT_Prosilica)   
     cob3-6         [Kinect](cob_camera_sensors/Microsoft_Kinect)      [Prosilica GC1380CH GigE](cob_camera_sensors/AVT_Prosilica)   
  -- ----------- -- ----------------------------------------------- -- ------------------------------------------------------------- --

## AVT Pike C145

A detailed guide for configuring and starting the stereo pair of *Pike
C145* cameras can be found in the
[Care-O-Bot AVT Pike Guide](cob_camera_sensors/AVT_Pike).

## AVT Prosilica Gig E

A detailed guide for configuring and starting the stereo pair of
*Prosilica GC1380CH* cameras can be found in the
[Care-O-Bot AVT Prosilica Guide](cob_camera_sensors/AVT_Prosilica).

## Swissranger

Instructions for the usage of the Swissranger 3000 or 4000 sensor
mounted on the Care-O-Bot can be found at
[Care-O-Bot Swissranger Guide](cob_camera_sensors/Mesa_Swissranger).

## Kinect

Instructions for the usage of the Microsoft Kinect sensor mounted on the
Care-O-Bot can be found at
[Care-O-Bot Kinect Guide](cob_camera_sensors/Microsoft_Kinect).
