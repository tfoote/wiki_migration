## Overview

The \`rgbd_self_filter\` allows efficient GPU-based self filtering of a
point cloud from an RGBD sensor (ex: Kinect) or stereo camera. The
filter renders the robot from the perspective of the sensor, and
subtracts any points that intersect with the robot\'s meshes.

Expected filter times are about 50-70ms for a 640x480 point cloud. This
is significantly faster than the [robot_self_filter](robot_self_filter).

The \`rgbd_self_filter\` is conceptually based on the
[camera_self_filter](camera_self_filter) by Christian Bersch.

![](attachment:rgbd_self_filter.png)

### Code

Code is here: <https://kforge.ros.org/rgbdselffilter/rgbd_self_filter>

## Setting Up RGBD Filter

To run the \`rgbd_self_filter\` with your robot, you will need:

-   A URDF file of your robot with STL meshes for all joints
-   A \<\<MsgLink(sensor_msgs/CameraInfo)\>\> topic that describes the
    RGBD camera.
-   Incoming \<\<MsgLink(sensor_msgs/PointCloud)\>\> or
    \<\<MsgLink(sensor_msgs/PointCloud2)\>\> messages.
-   Incoming \<\<MsgLink(sensor_msgs/PointCloud2)\>\> messages must have
    the \`width\` and \`height\` fields set properly.
-   Incoming \<\<MsgLink(sensor_msgs/PointCloud)\>\> messages must have
    the \"u\" and \"v\" channels filled out.
-   Camera info and point cloud messages do not need to by sync\'d.
-   For stereo cameras, the camera info should come from the left, or
    primary, camera.

## Running RGBD Filter

On the PR2, you will need to have a GPU installed on c2, and run \"X\"
on that computer.

-   Install DVI loopback cable on the GPU:
    <http://www.xtremesystems.org/forums/showthread.php?t=200444>
-   \"sudo apt-get install xserver-xorg\" and install nVidia drivers
-   Run \"sudo xinit\" on c2
-   Set \"DISPLAY\" environment variable to \":0\" for node For complete
    instructions, see [pr2_camera_self_filter](pr2_camera_self_filter).

If the filter is unable to start up an X window, it will fall back to a
passthrough filter.

Running the filter on a computer with a GPU running (like a desktop)
requires only setting the environment variable.

## How it Works

The RGBD filter renders the robot from the perspective of the given
sensor. Meshes can be inflated by a uniform scale. Inflated meshes are
inflated around the mesh barycenter.

Using the image coordinate (U/V) data from the incoming point cloud, the
filter checks the expected depth of the robot mesh at that U/V
coordinate. If the point cloud point is deeper, or if the point is
within the \"close_threshold\" of the depth, the point will be removed.

## ROS API

```clearsilver
name = rgbd_self_filter
desc = Self-filtering for robot point clouds
sub {
  0.name = camera_info
  0.type = sensor_msgs/CameraInfo
  0.desc = Camera info for the RGBD sensor
  1.name = points
  1.type = sensor_msgs/PointCloud
  1.desc = !PointCloud data to filter. This will be converted to a PCL type, so "points2" is preferred.
  2.name = points2
  2.type = sensor_msgs/PointCloud2
  2.desc = !PointCloud2 data. If the data is dense packed (width and height correct), the filter is more efficient because it doesn't have to calculate the U/V indices.
}
pub {
  0.name = points_mask
  0.type = sensor_msgs/PointCloud2
  0.desc = Filtered point cloud
  1.name = self_mark
  1.type = sensor_msgs/Image
  1.desc = Only if "~publish_mask" param is true. Mask image for debugging.

  2.name = points_debug
  2.type = sensor_msgs/PointCloud
  2.desc = Only if "~pub_debug_cloud" param is true. Point cloud of robot model's rendering.
}
param {
  0.name = ~close_threshold
  0.type = double
  0.desc = All points within this distance to robot meshes are removed.
  0.default = 0.02

  1.name = ~near_clip
  1.type = double
  1.desc = Near clip plane of rendering, all points closer than this removed.
  1.default = 0.3

  2.name = robot_description
  2.type = string
  2.desc = Valid URDF of your robot

  3.name = ~default_mesh_scale
  3.type = double
  3.desc = Robot meshes are "inflated" to remove points close to the meshes. Meshes are inflated by this scale.
  3.default = 1.05

  4.name = ~mesh_scales
  4.type = { str : double }
  4.desc = Meshes specified in this parameter will be inflated according to a custom scale.
  4.default = {}
}
```
