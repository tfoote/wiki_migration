## Overview

This package provides a node for tracking the position of objects of
interest as described in
[this paper](http://www.sim.informatik.tu-darmstadt.de/publ/download/2010_rcs_worldmodel.pdf)


```
@INPROCEEDINGS{Meyer:2010:WorldModel,
  author = {J. Meyer and P. Schnitzspan and S. Kohlbrecher and K. Petersen and O. Schwahn and M. Andriluka and U. Klingauf and S. Roth and B. Schiele and O. von Stryk},
  title = {A Semantic World Model for Urban Search and Rescue Based on Heterogeneous Sensors},
  year = {2011},
  pages = {180 -- 193},
  editor = {Ruiz-del-Solar, Javier and Chown, Eric and Ploeger, Paul G.},
  series = {Lecture Notes in Computer Science, Lecture Notes in Artificial Intelligence},
  booktitle = {RoboCup 2010: Robot Soccer World Cup XIV},
  url = {https://springerlink3.metapress.com/content/n515v876ll57334l/resource-secured/?target=fulltext.pdf&sid=yyw2tr55m2on31z0hpufyw55&sh=www.springerlink.com},
}
```



## ROS API



```clearsilver
node.0 {
name = hector_object_tracker
desc = `hector_object_tracker` is the central node of `hector_worldmodel`. It maintains a list of known objects in the environment and implements the association of incoming observations (percepts) and tracking. The observations have to be provided by at least one external node which implements a detector for certain object classes. 

sub {
  0.name = worldmodel/image_percept
  0.type = hector_worldmodel_msgs/ImagePercept
  0.desc = An observation of an object represented by image coordinates, a camera info and an estimated distance (optional).
  1.name = worldmodel/pose_percept
  1.type = hector_worldmodel_msgs/PosePercept
  1.desc = An observation of an object represented by a 3D pose.
  2.name = worldmodel/update
  2.type = hector_worldmodel_msgs/ObjectModel
  2.desc = Update the object model with another model. Objects will be either added or fused.
  3.name = syscommand
  3.type = std_msgs/String
  3.desc = System command. If the string equals "reset" the object database is cleared.
}

pub {
   0.name = worldmodel/object
   0.type = hector_worldmodel_msgs/Object
   0.desc = Published for every update of an existing object or if a new object has been added.
   1.name = worldmodel/objects
   1.type = hector_worldmodel_msgs/ObjectModel
   1.desc = The complete list of objects (latched). Republished for every update of the database.
   2.name = visualization_marker
   2.type = visualization_msgs/Marker
   2.desc = Single marker publisher for each tracked object.
   3.name = visualization_marker_array
   3.type = visualization_msgs/MarkerArray
   3.desc = Marker array publisher with annotated markers for each objects for visualization in [[rviz]]. 
}

srv {
  0.name = worldmodel/get_object_model
  0.type = hector_worldmodel_msgs/GetObjectModel
  0.desc = Returns the latest state of the object model. Used by the [[hector_worldmodel_geotiff_plugins]].
  1.name = worldmodel/set_object_state
  1.type = hector_worldmodel_msgs/SetObjectState
  1.desc = Sets the internal state of an object (`PENDING`, `ACTIVE`, `CONFIRMED`, `DISCARDED`, ...). This state information is for interaction with a state machine and influences whether the object information is still updated or not.
  2.name = worldmodel/set_object_name
  2.type = hector_worldmodel_msgs/SetObjectName
  2.desc = Sets the `name` field of an object identified by its `object_id`.
  3.name = worldmodel/add_object
  3.type = hector_worldmodel_msgs/AddObject
  3.desc = Adds an object to the model or updates an existing one (without fusion).
}

srv_called {
  0.name = get_distance_to_obstacle
  0.type = hector_nav_msgs/GetDistanceToObstacle
  0.desc = Returns the distance to the next obstacle in the map in the direction of a view ray to project percepts. This service is implemented in [[hector_mapping]]. Service name can be overridden by the `[class_id/]distance_to_obstacle_service` parameter.
  1.name = get_normal
  1.type = hector_nav_msgs/GetNormal
  1.desc = Returns the normal vector of the wall at a certain position. Used to fill the orientation of an object in the database, e.g. if there are objects at both sides of a wall. Service name has to be set explicitly with the `[class_id/]get_normal_service` parameter.
  2.name = as specified by parameters
  2.type = hector_worldmodel_msgs/VerifyPercept
  2.desc = Plugin interface for percept verification services called for every incoming <<MsgLink(hector_worldmodel_msgs/ImagePercept)>> or <<MsgLink(hector_worldmodel_msgs/PosePercept)>>. Service servers can confirm or discard the percept based on its position in the camera frame (e.g. for thermal self-filtering). The list of verification services to be called has to be specified in the `[class_id/]verification_services` parameter.
  3.name = as specified by parameters
  3.type = hector_worldmodel_msgs/VerifyObject
  3.desc = Plugin interface for object estimate verification called for every incoming <<MsgLink(hector_worldmodel_msgs/ImagePercept)>> or <<MsgLink(hector_worldmodel_msgs/PosePercept)>>. Service servers can confirm or discard the percept based on its mapped position and full state information. The list of verification services to be called has to be specified in the `[class_id/]verification_services` parameter.
}

param {
  0 {
    name = ~frame_id
    type = string
    desc = The `frame_id` of the frame in which the objects are modeled.
    default = map
  }
  1 {
    name = ~worldmodel_ns
    type = string
    desc = The namespace prefix for all worldmodel related topics and services.
    default = worldmodel
  }
  2 {
    name = ~publish_interval
    type = double
    desc = If greater than 0, republish the object model every x seconds.
    default = 0.0
  }
  3 {
    name = ~[class_id/]project_objects
    type = boolean
    desc = Project objects to the next obstacle in the map using the ` get_distance_to_obstacle` service.
    default = false
  }
  4 {
    name = ~[class_id/]with_orientation
    type = boolean
    desc = Consider the orientation of objects as given in the percept or by the `get_normal` service during the association step.
    default = false
  }
  5 {
    name = ~[class_id/]default_distance
    type = double
    desc = Default object distance considered for image percepts without distance information (`msg.distance == 0.0`) if `project_objects` is false.
    default = 1.0
  }
  6 {
    name = ~[class_id/]distance_variance
    type = double
    desc = Assumed variance of observations in distance (given in m^2).
    default = 1.0^2
  }
  7 {
    name = ~[class_id/]angle_variance
    type = double
    desc = Assumed variance of observations in (opening) angle (given in rad^2).
    default = (10 degrees)^2
  }
  8 {
    name = ~[class_id/]min_height
    type = double
    desc = Minimum z coordinate of objects. Percepts with a z coordinate which is smaller than this value will be discarded.
    default = -999.9
  }
  9 {
    name = ~[class_id/]max_height
    type = double
    desc = Maximum z coordinate of objects. Percepts with a z coordinate which is greater than this value will be discarded.
    default = 999.9
  }
  10 {
    name = ~[class_id/]pending_support
    type = double
    desc = Minimum support (added support of all percepts associated to the same object) where the object is automatically switched to the `PENDING` state.
    default = 0
  }
  11 {
    name = ~[class_id/]active_support
    type = double
    desc = Minimum support (added support of all percepts associated to the same object) where the object is automatically switched to the `ACTIVE` state.
    default = 0
  }
  12 {
    name = ~[class_id/]inactive_support
    type = double
    desc = If the support (added support of all percepts associated to the same object) drops below this value the object is automatically switched to the `INACTIVE` state.
    default = 0
  }
  13 {
    name = ~[class_id/]min_distance_between_objects
    type = double
    desc = Objects which are closer to a `CONFIRMED` object than this distance will automatically be set to `DISCARDED` state.
    default = 0
  }
  14 {
    name = ~[class_id/]marker_color
    type = double[]
    desc = Color of the marker published for objects of this class (r,g,b,optionally a).
    default = [0.8, 0, 0, 1.0] (red)
  }
  15 {
    name = ~[class_id/]distance_to_obstacle_service
    type = string
    desc = The <<SrvLink(hector_nav_msgs/GetDistanceToObstacle)>> service to call for percepts of this class if `project_objects` parameter is enabled.
    default = get_distance_to_obstacle
  }
  16 {
    name = ~[class_id/]get_normal_service
    type = string
    desc = The <<SrvLink(hector_nav_msgs/GetNormal)>> service to call for percepts of this class. The return value overwrites the orientation given in the percept message.
    default = empty
  }
  17 {
    name = ~negative_update[i]/topic
    type = string
    desc = The name of a <<MsgLink(sensor_msgs/CameraInfo)>> topic to subscribe to. For each incoming message the support of every object within the field of view and within a certain minimal and maximum distance will be decreased.
  }
  18 {
    name = ~negative_update[i]/class_id
    type = string
    desc = Only apply this negative update for objects of class `class_id`.
  }
  19 {
    name = ~negative_update[i]/min_distance
    type = double
    desc = Minimum estimated distance of the object
    default = 0
  }
  20 {
    name = ~negative_update[i]/max_distance
    type = double
    desc = Maximum estimated distance of the object
    default = 0
  }
  21 {
    name = ~negative_update[i]/ignore_border_pixels
    type = double
    desc = Minimum distance of the object from the image border in pixels
    default = 0
  }
  22 {
    name = ~negative_update[i]/not_seen_duration
    type = double
    desc = Only apply negative update if the object had no associated percept within the last x seconds.
    default = 0 (off)
  }
}
}
```

 See
[object_tracker.launch](https://github.com/tu-darmstadt-ros-pkg/hector_worldmodel/blob/catkin/hector_object_tracker/launch/object_tracker.launch)
for a sample configuration.
