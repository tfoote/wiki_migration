## Overview

This package introduces GUI Primitives for HRI that are designed to
visualize and illustrate objects detected by the robot. These primitives
also allow to interact with particular objects and give commands to the
robot via them. The primitives consists of
[Interactive Markers](http://www.ros.org/wiki/interactive_markers) and
are visualized in [RViz](http://www.ros.org/wiki/rviz).

All primitives have a context menu which allows some interaction and
setting of the visualization (ability to show description of the
primitive, add/remove manipulators for rotation and translation, etc.).

Following predefined types of primitives and are specified in
[srs_env_model/PrimitiveType](http://ros.org/doc/api/srs_env_model/html/msg/PrimitiveType.html)
message.

### Interaction Primitives

#### Billboard

-   Billboard represents a real world object which is hard to describe
    with some mesh.
-   The billboard is view facing and iẗ́s type is specified in
    [srs_interaction_primitives/BillboardType](http://ros.org/doc/api/srs_interaction_primitives/html/msg/BillboardType.html)
    message.
    ![\|width=40%](attachment:billboard-chair.png)![\|width=40%](attachment:billboard-person-head.png)
-   The billboard can also illustrate movement of the represented
    object, e.g. walking person.

![\|width=80%](attachment:billboard-person.png)

#### Bounding Box

-   Bounding Box illustrates dimensions of the object.
-   The bounding box is able visualize its dimensions as text labels.
-   The bounding box can be manually translated or rotated.

![\|width=70%](attachment:bbox.png)

#### Object

-   Object represents a detected or real-world object which has its mesh
    in an object database.
-   Possible pre-grasp positions can be shown around the object. The
    visualization of pre-grasp positions aids operator to move gripper
    to a correct position for the grasping.
-   The object can show its bounding box (if specified).
-   The object can be manually rotated, translated and scaled in the
    scene.

![\|width=70%](attachment:pre-grasp2.png)

![\|width=60%](attachment:object-with-bbox.png)

#### Unknown Object

-   Unknown Object represents obstacles, unreachable objects or
    dangerous places in the scene so that the operator will be able to
    avoid collisions or crashes of the robot.
-   The unknown object can be manually rotated, translated and scaled in
    the scene. ![\|width=80%](attachment:unknown.png)

#### Plane

-   Plane shows only a simple plane which can be tagged as table desk,
    wall, etc. ![\|width=80%](attachment:plane.png)

#### Plane Polygon

-   It's a variation of the Plane which is defined as a planar polygon.
-   The plane polygon is shown as a transparent plane with the polygon
    inside it. ![\|width=80%](attachment:plane-polygon.png)

### Others

#### Clickable positions

Clickable positions can be added to the scene using
*/clickable_positions* service or ClickablePositions action.

By clicking on the position are it's coordinates published on the
specified topic.

#### Robot's pose prediction

For visualization of robot's predicted movement positions is provided
service */robot_pose_prediction*. Position are visualized using
[Markers](http://www.ros.org/wiki/rviz/DisplayTypes/Marker).

Service takes 2 arguments:

-   **geometry_msgs/Pose\[\] positions** - predicted positions
-   **ttl** - markers lifetime

![\|width=80%](attachment:robot_pose_prediction.png)

## ROS API

### Nodes

  -- --------------------------------------- -- ---------------------- -- ------------------------------------------------------ --
     **Node Name**                              **Published Topics**      **Description**                                        
     interaction_primitives_service_server                                This node publishes interaction_primitives services.   
  -- --------------------------------------- -- ---------------------- -- ------------------------------------------------------ --

### Services

All services starts with prefix `/interaction_primitives`

  -- ------------------------------- -- ----------- -- --------------------------- -- ---------------------------------------------------- --
     **Service Name**                   **Input**      **Output**                     **Description**                                      
     /add_billboard                                                                   Adds billboard to the scene                          
     /add_bounding_box                                                                Adds Bounding Box to the scene                       
     /add_plane                                                                       Adds Plane to the scene                              
     /add_plane_polygon                                                               Adds Plane Polygon to the scene                      
     /add_object                                                                      Adds Object to the scene                             
     /add_unknown_object                                                              Adds Unknown Object to the scene                     
     /remove_primitive                                                                Removes primitive form the scene                     
     /change_description                                                                                                                   
     /change_pose                                                                     Changes primitive's description                     
     /change_scale                                                                    Changes primitive's scale                           
     /change_color                                                                    Changes primitive's color                           
     /change_direction                                                                Changes billboard's movement direction              
     /change_velocity                                                                 Changes billboard's movement velocity               
     /set_pregrasp_position                                                           Sets pre-grasp position                              
     /remove_pregrasp_position                                                        Removes pre-grasp position                           
     /get_update_topic                                                                Gets update topic for specified action (type)        
     /set_allow_object_interaction                                                    Allows od denies interaction with specified Object   
     /get_billboard                                    Gets billboard                                                                      
     /get_bounding_box                                 Ges Bounding Box                                                                    
     /get_plane                                        Gets Plane                                                                          
     /get_object                                       Gets Object                                                                         
     /get_unknown_object                               Gets Unknown Object                                                                 
     /clickable_positions                              Shows clickable positions                                                           
     /robot_pose_prediction                                                           Shows predicted positions of robot's movement       
  -- ------------------------------- -- ----------- -- --------------------------- -- ---------------------------------------------------- --

### Messages

  -- ----------------- -- --------------------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------- --
     **Msg Name**         **Content**                                                                                      **Description**                                                                  
     PrimitiveType        [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/PrimitiveType.html)         Types of Primitives                                                              
     BillboardType        [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/BillboardType.html)         Types of Billboard                                                               
     PoseType             [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/PoseType.html)              Specifies if the coordinates are in the center or in the base of the primitive   
     MenuClicked          [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/MenuClicked.html)           Message for update topic                                                         
     MovementChanged      [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/MovementChanged.html)       Message for update topic                                                         
     PoseChanged          [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/PoseChanged.html)           Message for update topic                                                         
     ScaleChanged         [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/ScaleChanged.html)          Message for update topic                                                         
     TagChanged           [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/TagChanged.html)            Message for update topic                                                         
     PositionClicked      [content](http://ros.org/doc/api/srs_interaction_primitives/html/msg/PositionsClicked.html)      Message for position clicked topic                                               
  -- ----------------- -- --------------------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------- --

### Published topics

All topics starts with prefix `interaction_primitives`.

  -- ----------------------------------------- -- -------------------------------------------- -- --------------------------------------------------------------- --
     **Topic Name**                               **Message**                                     **Description**                                                 
     /primitive_name/update/pose_changed          srs_interaction_primitives/PoseChanged          Publishes pose changes of the primitive                         
     /primitive_name/update/scale_changed         srs_interaction_primitives/ScaleChanged         Publishes scale changes of the primitive                        
     /primitive_name/update/menu_clicked          srs_interaction_primitives/MenuClicked          Publishes information about menu interaction of the primitive   
     /primitive_name/update/movement_changed      srs_interaction_primitives/MovementChanged      Publishes movement changes of the primitive (Billboard only)    
     /primitive_name/update/tag_changed           srs_interaction_primitives/TagChanged           Publishes tag changes of the primitive (Plane only)             
     /clickable_positions/topic_suffix            srs_interaction_primitives/PositionClicked      Publishes position which was clicked                            
  -- ----------------------------------------- -- -------------------------------------------- -- --------------------------------------------------------------- --

## Installation

Both components are in srs git in `srs_interaction_primitives` package
and can be compiled with ROS standard tool `rosmake`


```
rosmake srs_interaction_primitives
```



## Usage

### Adding primitives from C++



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```



### Using predefined services

-   Run service server 

```
rosrun srs_interaction_primitives interaction_primitives_service_server
```



```{=html}
<!-- -->
```
-   Run RViz 

```
rosrun rviz rviz
```



```{=html}
<!-- -->
```
-   Add **Interactive Marker Display** and set **Update Topic** to
    `/interaction_primitives/update`.

Now you can call services and add or update Primitives.

#### Calling services from bash

##### Add Bounding Box



```
rosservice call /interaction_primitives/add_bounding_box '{frame_id: /world, name: bbox, object_name: obj, description: "", 0, pose: { position: { x: -1, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } }, scale: { x: 1, y: 1, z: 1 }, color: { r: 1, g: 0, b: 0 }}'
```



##### Add Billboard



```
rosservice call /interaction_primitives/add_billboard '{frame_id: /world, name: billboard, type: 2, description: "this is billboard", velocity: 5.6, direction: {x: 1, y: 1, z: 0, w: 1}, 0, pose: {position: { x: -1, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } }, scale: { x: 1, y: 1, z: 1 }}'
```



##### Add Plane



```
rosservice call /interaction_primitives/add_plane '{frame_id: /world, name: plane, description: "", 0, pose: { position: { x: -1, y: 0, z: 5 }, orientation: { x: 0, y: 1, z: 0, w: 1 } }, scale: { x: 1, y: 1, z: 1 }, color: { r: 1, g: 0.3, b: 0, a: 1.0 }}'
```



##### Add Object



```
rosservice call /interaction_primitives/add_object '{frame_id: /world, name: table_obj, description: "My table", 0, pose: { position: { x: -1, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } }, scale: { x: 1, y: 1, z: 1 }, resource: "package://gazebo_worlds/Media/models/table.dae", use_material: false, color: {r: 1, g: 0, b: 1, a: 1 }}'
```



##### Add Unknown Object



```
rosservice call /interaction_primitives/add_unknown_object '{frame_id: /world, name: uobj, description: "", 0, pose: { position: { x: -1, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } }, scale: { x: 1, y: 1, z: 1 } }'
```



##### Add Object



```
rosservice call /interaction_primitives/add_object '{frame_id: /world, name: milk, description: "Detected milk", 0, pose: { position: { x: -1, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } }, bounding_box_lwh: {x: 1.0, y: 0.2, z: 0.1}, color: {r: 1, g: 1, b: 0}, resource: package://cob_gazebo_worlds/Media/models/milk_box.dae, use_material: True}'
```



##### Change pose



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

0

##### Change scale



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

1

##### Change color



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

2

##### Change description



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

3

##### Set pre-grasp position



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

4

##### Remove pre-grasp position



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

5

##### Remove object



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

6

#### Calling services from C++



```cplusplus

// Create Interactive Marker Server 
InteractiveMarkerServerPtr server;
server.reset(new InteractiveMarkerServer("test_primitives", "", false));

// Create billboard - /world is frame and my_billboard is primitives unique name
Billboard *billboard = new Billboard(server, "/world", "my_billboard");
billboard->setType(srs_interaction_primitives::BillboardType::PERSON); // type PERSON
billboard->setPose(pose); // actual position of the billboard
billboard->setPoseType(srs_interaction_primitives::PoseType::POSE_CENTER); // coordinates are int the center of the primitive
billboard->setScale(scale); // scale of the billboard
billboard->setDirection(direction); // actual movement direction
billboard->setVelocity(velocity); // actual movement velocity
billboard->setDescription("This is me!"); // description
billboard->insert(); // creates interaction primitive a inserts it into IMS
```

7
