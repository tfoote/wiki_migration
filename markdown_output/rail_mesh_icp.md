## About

The intended use for `rail_mesh_icp` is to allow RGBD sensing
platforms using ROS to match a mesh model (e.g. an STL file) to point
clouds. This is useful in cases where an accurate estimate of the
model's 6-DoF pose in the point cloud is needed (e.g.
grasping/manipulation).

<<MsgSrvDoc(rail_mesh_icp)>>

## Nodes

```clearsilver
node.0 {
  name = template_matcher_node
  desc = `template_matcher_node` matches a model (source) point cloud to a target point cloud using service calls to the `icp_matcher_node` and an estimate of the object's 6-DoF pose. This 6-DoF pose estimate can come from an external detector via service calls for dynamic objects or predefined in a launch file for static objects. The target point clouds can either be raw point clouds from a [[http://docs.ros.org/melodic/api/sensor_msgs/html/msg/PointCloud2.html|sensor_msgs/PointCloud2]] topic or pre-processed point clouds included in the service calls.
  sub {
    0.name = <~/pcl_topic parameter>
    0.type = sensor_msgs/PointCloud2
    0.desc = Incoming point cloud data.
  }
  pub {
    0.name = ~/template_points
    0.type = sensor_msgs/PointCloud2
    0.desc = Source point cloud for matching published when debugging.
  }
  pub {
    1.name = ~/target_points
    1.type = sensor_msgs/PointCloud2
    1.desc = Target point cloud for matching published when debugging.
  }
  pub {
    2.name = ~/matched_template_points
    2.type = sensor_msgs/PointCloud2
    2.desc = Source point cloud transformed by the approximated transform to match to the target point cloud published when debugging.
  }
  srv {
    0.name = ~/match_template
    0.type = rail_mesh_icp/TemplateMatch
    0.desc = Matches a source point cloud to a target point cloud using an initial pose estimate, returning the final approximated pose and matching error between point clouds. Both the initial pose estimate and target point cloud can be predefined values/topics or provided at execution in the service calls depending on the use case.
  }
  param {
    0.name = ~/debug
    0.type = bool
    0.desc = Flag to publish debugging point clouds like `~/matched_template_points`.
    0.default = true
  }
  param {
    1.name = ~/visualize
    1.type = bool
    1.desc = Flag to publish approximated matching frame `~/template_frame` parameter.
    1.default = true
  }
  param {
    2.name = ~/pcl_topic
    2.type = string
    2.desc = Target point cloud topic to match source point cloud to when `~/pre_processed_cloud` is false.
    2.default = "/head_camera/depth_registered/points"
  }
  param {
    3.name = ~/pre_processed_cloud
    3.type = bool
    3.desc = Flag set to match the source point cloud (template) to the `target_cloud` provided in the `~/match_template` service. When false, matches the source point cloud to point clouds from `~/pcl_topic`.
    3.default = false
  }
  param {
    4.name = ~/template_file
    4.type = string
    4.desc = Name of the source template point cloud file in the `cad_models` folder with a ".pcd" file extension.
    4.default = "corner.pcd"
  }
  param {
    5.name = ~/matching_frame
    5.type = string
    5.desc = Frame in which the source and target point clouds are matched (target point cloud transformed to this frame for matching).
    5.default = "/map"
  }
  param {
    6.name = ~/initial_estimate_string
    6.type = string
    6.desc = "X Y Z Roll Pitch Yaw" pose of the template point cloud in the `~/matching_frame` frame used as the initial estimate when the `latch_initial` parameter is true.
    6.default = "0 0 0 0 0 0"
  }
  param {
    7.name = ~/latch_initial
    7.type = bool
    7.desc = Flag set to latch the initial pose estimate specified as a launch parameter in `~/initial_estimate_string`. When false, uses the `initial_estimate` transform provided in the `~/match_template` service.
    7.default = true
  }
  param {
    8.name = ~/template_offset_string
    8.type = string
    8.desc = "X Y Z Roll Pitch Yaw" optional additional transform between a matching template and the approximated output pose. This is useful when the matching template frame is not centered at a desired point (i.e. not a handle for manipulation).
    8.default = "0 0 0 0 0 0"
  }
  param {
    9.name = ~/template_frame
    9.type = string
    9.desc = Child coordinate frame used to designate approximated matching pose that is visualized when `~/visualize` is true.
    9.default = "template_pose"
  }
}
node.1 {
  name = icp_matcher_node
  desc = `icp_matcher_node` matches a template point cloud to a target point cloud using PCL's Iterative Closest Point (ICP) class template [[http://docs.pointclouds.org/trunk/classpcl_1_1_iterative_closest_point.html|pcl::IterativeClosestPoint]].
  srv {
    0.name = /icp_match_clouds
    0.type = rail_mesh_icp/ICPMatch
    0.desc = Matches a template point cloud to a target point cloud, returning the matched point cloud, approximate transform from template to target point cloud, and matching error between point clouds.
  }
  param {
    0.name = /icp_matcher_node/iterations
    0.type = int
    0.desc = Max number of iterations to fit template cloud to the target cloud. See [[http://docs.pointclouds.org/trunk/classpcl_1_1_iterative_closest_point.html|pcl::IterativeClosestPoint]] for more information.
    0.default = 50
  }
  param {
    1.name = /icp_matcher_node/max_distance
    1.type = float
    1.desc = Max allowable distance for matches in meters. See [[http://docs.pointclouds.org/trunk/classpcl_1_1_iterative_closest_point.html|pcl::IterativeClosestPoint]] for more information.
    1.default = 1.0
  }
  param {
    2.name = /icp_matcher_node/trans_epsilon
    2.type = float
    2.desc = Set the transformation epsilon (maximum allowable translation squared difference between two consecutive transformations) in order for an optimization to be considered as having converged to the final solution. See [[http://docs.pointclouds.org/trunk/classpcl_1_1_iterative_closest_point.html|pcl::IterativeClosestPoint]] for more information.
    2.default = 1e-8
  }
  param {
    3.name = /icp_matcher_node/fit_epsilon
    3.type = float
    3.desc = Set the maximum allowed Euclidean error between two consecutive steps in the ICP loop, before the algorithm is considered to have converged. See [[http://docs.pointclouds.org/trunk/classpcl_1_1_iterative_closest_point.html|pcl::IterativeClosestPoint]] for more information.
    3.default = 1e-8
  }
}
node.2 {
  name = mesh_sampler_node
  desc = `mesh_sampler_node` uniformly samples a polygon mesh in PLY format to create a point cloud of the mesh file. Inputs are the mesh file and outputs are the sampled point cloud. Sampling resolution and number of samples can be changed, use `-h` when running the node for more information.
}
```

## Installation

To install the `rail_mesh_icp` package, you can install from source
with the following commands:

. ```shell
cd /(your catkin workspace)/src
git clone https://github.com/GT-RAIL/rail_mesh_icp.git
cd ..
catkin build rail_mesh_icp
```

## Making the Mesh (Source) Cloud

1\. After you have mesh model for your object, convert it to a PLY (i.e.
`.ply`) file format so the mesh sampling tool

can read the file format and convert it to a point cloud. In Ubuntu,
\[Mesh Lab\](<http://meshlab.sourceforge.net>) allows you to import many
mesh model formats (e.g. STL, PLY, DAE) and convert them to PLY via the
`Import Mesh` and `Export Mesh` options.

1\. With the mesh model in PLY format, you can call the mesh sampling
tool via `rosrun rail_mesh_icp mesh_sampler_node

\[INPUT_MESH_MODEL\].ply \[OUTPUT_POINT_CLOUD\].pcd`. Optional
arguments, like sampling density, are detailed using `-h`.

1\. If the sampling tool was successful, there should now be a `.pcd`
file in the `cad_models` folder.

## Running a demo using the Fetch platform

1\. An example launch file to match the `corner.pcd` template in the
`cad_models` folder to a static environment object is
`template_match_demo.launch`. It's intended use is with the
[Fetchit Challenge](https://github.com/fetchrobotics/fetch_gazebo/tree/gazebo9/fetchit_challenge)
environment. Please follow tutorials found
[here](http://docs.fetchrobotics.com/gazebo.html) to install the
environment and robot simulator. 1. Launch a simulation of the fetch and
simulation environment using `roslaunch fetchit_challenge
main.launch`. 1. Launch the navigation stack to enable localization via
`roslaunch fetch_navigation build_map.launch`. 1. AFTER launching
navigation, teleop the Fetch to face the front corver of the large
recangular machine using keyboard teleop via `rosrun
teleop_twist_keyboard teleop_twist_keyboard.py` making sure the
Fetch's published point cloud under topic
`/head_camera/depth_registered/points` clearly captures the corner of
the machine as shown below:

![\|width="600"](attachment:align.png)

1\. Start the template matching and icp nodes using the demo launch file
via `roslaunch rail_mesh_icp template_match_demo.launch`. This should
launch a version of the generic template matching node (i.e.
`template_matcher_node`) specific to matching the `corner` template
along with an ICP matching node (i.e. `icp_matcher_node`)
automatically. 1. Verify that the new `initial_estimate` frame in tf
is near the corner of the schunk machine. This initial guess is used to
initialize the `template_matcher_node` for ICP. If the
`initial_estimate` is off by more than 0.1 m and/or 20 degrees along
each axis, ICP might not find a registration between the template and
viewing point cloud. If the estimate is too far, adjust it in the launch
file (i.e. adjust variable `initial_estimate` inside
`template_match_demo.launch`). This can also be done faster using
`static_transform_publisher` directly. 1. A service call to detect the
corner via `rosservice call
/template_matcher_demo_node/match_template` will start the template
matching. Once matched, an estimated frame named `template_pose`
should appear in tf with the x-axis aligned to the center of the
cylindrical part of the machine as shown below:

![\|width="600"](attachment:match.png)

1\. Note that this `template pose` can be changed arbitrarily with
respect to the matched template using the `template_offset` launch
argument. Additionally, if `debug` is enabled you can view the target,
template, and matched template point clouds in rviz by subscribing to
`target_points`, `template_points`, `matched_template_points`,
respectively.

## Matching to other templates (bin, handle, etc.)

1\. To do this, simply create another launch similar to the
`template_match_demo.launch` which is currently set up specifically
for the machine matched in the demo. The main changes will be updating
`initial_estimate`, `template_offset`, `provide_processed_cloud`,
`latch_initial_estimate`, and `template_filename`. 1. Note that for
moveable objects in the environment, the `initial_estimate` can be
given along with each `match_template` service call.
