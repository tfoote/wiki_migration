## Overview

The industrial_payload_manager package provides functionality for
managing payloads in planning scenes and RViz visualizations of
industrial robot operations by providing the following functionality:

-   Load payloads, payload_targets, and link_markers from URDF files
    into industrial_payload_manager/Payload messages
-   Dynamically insert, remove, or manipulate pose of payloads
-   Update RViz visualization marker array, attached collision objects
    in MoveIt! planning scene, and in the future attached collision
    objects in Tesseract planning scene.
-   industrial_payload_manager/Payload messages include information for
    payload geometry, Aruco marker locations, gripper targets for
    payload grasping, and inertial properties of payload
-   industrial_payload_manager/PayloadTarget messages include the
    desired final locations for payloads after manipulation
-   industrial_payload_manager/LinkMarkers message contains the pose of
    Aruco markers attached to a robot or workcell link
-   payload_transform_publisher script will publish all relevant
    transforms to /tf
-   !PayloadTransformListener Python class extends the standard
    !TransformListener with the ability to understand
    industrial_transform_listener/PayloadArray messages and include the
    relevant transforms in lookup

Source: <https://github.com/arminstitute/industrial_payload_manager>

**Warning: This software is under development. API and message formats
and subject to change.**

## Nodes

```clearsilver
node.0 {
  name = industrial_payload_manager
  desc = Provides core functionality for managing payloads in RViz and planning scenes
  sub {
    0.name = /payload
    0.type = industrial_payload_manager/PayloadArray
    0.desc = Contains array of Payload, !PayloadTarget, and !LinkMarkers messages
  }
  pub {
    1.name = /payload
    1.type = industrial_payload_manager/PayloadArray
    1.desc = Publishes updated payload messages if payload is changed by the manager
  }
  srv {
    2.name = /get_payload_array
    2.type = industrial_payload_manager/GetPayloadArray
    2.desc = Synchronously returns a !PayloadArray of active payloads
  }
  srv {
    3.name = /update_payload_pose
    3.type = industrial_payload_manager/UpdatePayloadPose
    3.desc = Updates the pose of a payload and the link the payload is attached
  }
  pub {
    4.name = /attached_collision_object
    4.type = moveit_msgs/AttachedCollisionObject
    4.desc = AttachedCollisionObject messages to update the MoveIt! planning scene with payloads
  }
  pub {
    5.name = /payload_marker_array
    5.type = visualization_msgs/MarkerArray
    5.desc = MarkerArray messages for RViz to show visual meshes of payloads
  }  
}
node.1 {
  name = urdf_to_payload
  desc = Loads URDF Xacro files to payload messages and publishes to /payload topic. The payloads must be carefully formatted so each Xacro file contains only one Payload, !PayloadTarget, or !LinkMarkers. The Payload Xacro URDF files may contain visual and collision geometry, Aruco markers, payload targets, and inertial parameters. Each Aruco marker and payload target must be in a sub-link connected by a fixed joint. Only on level of joints is allowed. See the test/load_payloads.launch file for examples of how to use the urdf_to_payload node.
  pub {
    0.name = /payload
    0.type = industrial_payload_manager/PayloadArray
    0.desc = Publishes the payloads loaded from URDF files
  }
}
node.2 {
  name = payload_trasform_publisher
  desc = Publishes payload transforms to /tf topic
  sub {
    0.name = /payload
    0.type = industrial_payload_manager/PayloadArray
    0.desc = The payloads to publish to /tf
  }
  pub {
    0.name = /tf
    0.type = tf/tfMessage
    0.desc = Transforms of relevant frames including all payloads, all Aruco markers, and all payload/gripper targets.
  }
}

License: BSD
```
