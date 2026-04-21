## About

The `rail_grasp_collection` package contains nodes to collect
demonstration grasps for detected point cloud objects. These
demonstrations can then be used to build object models for recognition
and manipulation using the [rail_recognition](rail_recognition) package.
Demonstrations are stored in a grasp database, handled by
[graspdb](graspdb).

## Nodes



```clearsilver
node.0 {
  name = rail_grasp_collection
  desc = Collect demonstrated grasps with associated point clouds and store them in the grasp database.
  sub {
    0.name = segmented_objects_topic param
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Incoming segmented object data.
  }
  pub {
    0.name = rail_grasp_collection/debug
    0.type = sensor_msgs/PointCloud2
    0.desc = Debug publisher for the segmented point cloud collected on calling the grasp_and_store action.
  }
  act_called {
    0.name = gripper_action_server param
    0.type = rail_manipulation_msgs/GripperAction
    0.desc = Close gripper action.
    1.name = lift_action_server param
    1.type = rail_manipulation_msgs/LiftAction
    1.desc = End effector lifting action.
    2.name = verify_grasp_action_server param
    2.type = rail_manipulation_msgs/VerifyGraspAction
    2.desc = Determine whether or not a grasp was successful.
  }
  goal {
    0.name = rail_grasp_collection/grasp_and_store
    0.type = rail_pick_and_place_msgs/GraspAndStoreGoal
    0.desc = Execute a grasp and store the result in the grasp database.
  }
  result {
    0.name = rail_grasp_collection/grasp_and_store
    0.type = rail_pick_and_place_msgs/GraspAndStoreResult
    0.desc = Grasp collection result.
  }
  param {
    0.name = debug
    0.type = bool
    0.desc = Display debugging information if true.
    0.default = false
    1.name = robot_fixed_frame_id
    1.type = string
    1.desc = Fixed coordinate frame within the robot's coordinate system.
    1.default = "base_footprint"
    2.name = eef_frame_id
    2.type = string
    2.desc = End effector coordinate frame, used for storing grasp poses.
    2.default = "eef_link"
    3.name = segmented_objects_topic
    3.type = string
    3.desc = Topic for incoming segmented object data.
    3.default = "/segmentation/segmented_objects"
    4.name = gripper_action_server
    4.type = string
    4.desc = Action server topic for controlling the robot's end effector.
    4.default = "/manipulation/gripper"
    5.name = lift_action_server
    5.type = string
    5.desc = Action server topic for raising the end effector.
    5.default = "/manipulation/lift"
    6.name = verify_grasp_action_server
    6.type = string
    6.desc = Action server topic for verifying whether or not a grasp was successful.
    6.default = "/manipulation/verify_grasp"
    7.name = /graspdb/host
    7.type = string
    7.desc = Grasp database host ip.
    7.default = "127.0.0.1"
    8.name = /graspdb/port
    8.type = int
    8.desc = Grasp database port.
    8.default = graspdb::Client::DEFAULT_PORT
    9.name = /graspdb/user
    9.type = string
    9.desc = Grasp database username.
    9.default = "ros"
    10.name = /graspdb/password
    10.type = string
    10.desc = Grasp database password.
    10.default = ""
    11.name = /graspdb/db
    11.type = string
    11.desc = Grasp database name.
    11.default = "graspdb"
  }
}
node.1 {
  name = rail_grasp_retriever
  desc = Retrieve stored grasps from the grasp database training set.
  pub {
    0.name = rail_grasp_retriever/point_cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = Retrieved point cloud.
    1.name = rail_grasp_retriever/pose
    1.type = geometry_msgs/PoseStamped
    1.desc = Retrieved grasp pose.
  }
  goal {
    0.name = rail_grasp_retriever/retrieve_grasp
    0.type = rail_pick_and_place_msgs/RetrieveGraspDemonstrationGoal
    0.desc = Retrieve a specified grasp demonstration from the grasp database.
  }
  result {
    0.name = rail_grasp_retriever/retrieve_grasp
    0.type = rail_pick_and_place_msgs/RetrieveGraspDemonstrationResult
    0.desc = Retrieved grasp result.
  }
  param {
    0.name = /graspdb/host
    0.type = string
    0.desc = Grasp database host ip.
    0.default = "127.0.0.1"
    1.name = /graspdb/port
    1.type = int
    1.desc = Grasp database port.
    1.default = graspdb::Client::DEFAULT_PORT
    2.name = /graspdb/user
    2.type = string
    2.desc = Grasp database username.
    2.default = "ros"
    3.name = /graspdb/password
    3.type = string
    3.desc = Grasp database password.
    3.default = ""
    4.name = /graspdb/db
    4.type = string
    4.desc = Grasp database name.
    4.default = "graspdb"
  }
}
```



## Installation

To install the `rail_pick_and_place` package, you can install from
source with the following commands: . 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/rail_pick_and_place.git
cd ..
catkin_make
catkin_make install
```



## Startup

The `rail_grasp_collection` package contains launch files for
launching either the rail_grasp_collection node or the
rail_grasp_retriever node individually, and for launching both nodes
together. These can be launched with the following commands,
respectively:

. 

```
roslaunch rail_grasp_collection rail_grasp_collection.launch
```



. 

```
roslaunch rail_grasp_collection rail_grasp_retriever.launch
```



. 

```
roslaunch rail_grasp_collection rail_grasp_collection_and_retriever.launch
```



Grasp collection can also be run and executed with an rviz plugin found
in [rail_pick_and_place_tools](rail_pick_and_place_tools).
