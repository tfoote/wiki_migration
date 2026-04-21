## Package Organization

This package contains robot description and configuration files for
Maxwell, organized into subdirectories as follows:

-   *urdf*/ contains ([xacro](xacro) representations of) [urdf](urdf)
    descriptions of various parts of the Maxwell (arm, head, etc.), and
    the full robot.
-   *meshes*/ contains mesh files (.stl) for visualization and collision
    properties
-   *params*/ contains yaml specification files for the ArbotiX driver
    and diagnostics.
-   *launch*/ contains [roslaunch](roslaunch) files for starting up
    Maxwell, on real hardware, or in simulation.
-   *nodes*/ contains several python-based nodes, which currently have
    no home.

## Starting Up Maxwell

To start Maxwell, use one of the following launch files:

-   *bringup_maxwell.launch* connects to real hardware.
-   *head_camera.launch* starts the Asus Xtion on Maxwell.
-   *fake_maxwell.launch* starts a simulated version of the ArbotiX
    node. This can be useful for testing arm code.

## Interacting with Maxwell

### Moving the Base

The base uses a standard \<\<MsgLink(geometry_msgs/Twist)\>\> message on
the *cmd_vel* topic to set desired velocity.

### Moving the Arm

See [maxwell_arm_navigation](maxwell_arm_navigation) and
[maxwell_interactive_markers](maxwell_interactive_markers).

### Accessing Sensor Information

  -- ---------------------------- -- -------------------------- --
     **Sensor Data**                 **Topic Name**             
     base: position                  */odom* and */tf*          
     camera: 2D color image          */camera/rgb/image*        
     camera: 2D grayscale image      */camera/rgb/image_mono*   
     camera: 3D point cloud          */camera/rgb/point*        
     joints: positions               */joint_states*            
  -- ---------------------------- -- -------------------------- --

Use of */camera/depth* is not recommended as most of our demos will use
the topics in the */camera/rgb* namespace.
