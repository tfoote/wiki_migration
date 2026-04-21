![](attachment:laser_ortho_projector.png)

## Usage

The package is intended as an intermediary step to transform laser data,
before passing it to another node that performs scan-matching (for
example, [laser_scan_matcher](laser_scan_matcher) or
[slam_gmapping](slam_gmapping)). It works under the assumption that the
environment is rectilinear in the z-dimension, meaning that obstacles
look the same, regardless of the height where they are observed. This
assumption typically holds for indoor spaces.

The orthogonal projector can be used for vehicles with varying roll-,
pitch-, and z-pose that travel in indoor environments.

Alternatively, it can be used for vehicles that travel in 2D, but have a
laser scanner that is mounted at an angle to the horizontal plane.

## Details

Laser scan data is often used to calculate the motion of mobile robots
in static environments. Most scan-matching implementations assume that
the robot only moves in the xy plane, and calculate the translation and
rotation that best maps two sets of points from consecutive laser scans
onto each other.

Attempting to apply this technique directly to robots in 3D presents two
key challenges. The additional degrees of freedom (z, pitch, roll)
impose a greater computational cost. More importantly, the data obtained
by statically-mounted planar laser scanners is not sufficient to
correctly determine the change in the 3D pose.

In most indoor environments, obstacles look the same regardless of the
height. If we know the 3D orientation of the laser scanner, we can
reduce the problem of 3D scan matching to 2D by projecting the scans
onto the xy-plane.

We begin by calculating the Cartesian coordinates of the points in the
laser scan, in a base frame of the robot. Next, we discard the z-values
of the points, to obtain the set of points in the horizontal plane.

We also calculate a transformation between the world frame and a
orthogonally-projected base frame of the robot (labeled `/base_ortho`
in the figure above), and publish it as a [tf](tf) transform.

Note that projecting the scan from an arbitrary roll and pitch results
in points that are no longer equal angles apart. Thus, we pubish the
projected scan as a <<MsgLink(pcl/PointCloudXYZ)>>. The point cloud
is published in the base_ortho frame of reference.

## Example

You can run the [laser_ortho_projector](laser_ortho_projector) on a
pre-recorded bag file that comes with the package. First, make sure you
have the [scan_tools](scan_tools) stack downloaded and installed by
following the instructions [here](scan_tools#Installing).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz tf rosbag
```



Finally, run the demo:



```shell
roslaunch laser_ortho_projector demo.launch
```



You should see the input laser scan and the orthogonally projected scan
displayed in [rviz](rviz), similar to the video below:

[Youtube](https://www.youtube.com/watch?v=jHsdwQbqc8Y)

## Nodes & Nodelets

Two drivers are available: `laser_ortho_projector_node` and
`laser_ortho_projector_nodelet`. Their parameters and topics are
identical.



```clearsilver
 name = laser_ortho_projector_node / laser_ortho_projector_nodelet
 desc = The `laser_ortho_projector_node` takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and outputs their orthogonal projections in the xy-plane.
 sub {
   0{
    name = scan
    type = sensor_msgs/LaserScan
    desc = Scans from a laser range-finder
    }
   1{
    name = imu
    type = sensor_msgs/IMU
    desc = Optional IMU data for the orientation of the `base_link` frame. If not provided, the orientation of the `base_link` frame needs to be provided as a transform using `tf`.
    }
  }
 pub {
   0{
    name = ~cloud_ortho
    type = sensor_msgs/PointCloud
    desc = The projected laser scan, in Cartesian coordinates, in the `base_ortho` frame (orthogonal projection of the `base_link` frame.
   }
  }
  
 param{
    0.name = ~fixed_frame
    0.type = string
    0.default = `"/world"`
    0.desc = the name of the fixed frame

    1.name = ~base_frame
    1.type = string
    1.default = `"base_link"`
    1.desc = the name of the vehicle base frame

    2.name = ~ortho_frame
    2.type = string
    2.default = `"base_ortho"`
    2.desc = the name of the orthogonally-projected frame
 
    2.name = ~publish_tf
    2.type = bool
    2.default = `false`
    2.desc = whether to publish the tf between the `fixed_frame` and the `base_ortho` frames as a `tf`>>.

    3.name = ~use_imu
    3.type = bool
    3.default = `true`
    3.desc = whether to use IMU data for the orientation of the `base_link` frame. If set to `false`, the orientation of the `base_link` frame needs to be provided as a transform using `tf`.
 }
  
 req_tf{
  0{
    from = base_link
    to = laser
    desc = the pose of the laser in in reference to the base frame
  }
  1{
    from = world
    to = base_link
    desc = the pose of the bae link in the fixed frame. Not needed if IMU data is provided.
  }
 }

 prov_tf{
  0{
    from = world
    to = base_ortho
    desc = the pose of the projected base frame in the world frame
  }
 }
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
