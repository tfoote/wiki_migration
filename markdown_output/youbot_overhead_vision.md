## Nodes



```clearsilver
node.0 {
  name = image_calibration
  desc = `image_calibration` takes in two camera streams to create an occupancy map of the room and determine the position of a Kuka Youbot in that room.  The class stitches the camera streams together and performs background extraction to locate obstacles. Color calibration files are used to locate key markers placed on the Kuka Youbot and the robot heading and position are published to 'position_from_camera' topic. The occupancy map is published to the 'image_cal' topic.  The node handles both real Youbots and ones simulated in gazebo.  The 'runFromSimulation' param marks the source of the camera feeds.
  sub {
    0.name = /overhead_north/image_raw
    0.type =  sensor_msgs/Image
    0.desc = The raw image stream acquired from the north overhead camera.
    1.name = /overhead_south/image_raw
    1.type =  sensor_msgs/Image
    1.desc = The raw image stream acquired from the south overhead camera.
  }
  pub {
    0.name = /image_calibration/position_from_camera
    0.type = youbot_overhead_vision/PositionFromCamera
    0.desc = Current heading and position of the robot according to the overhead cameras
    1.name = /image_calibration/image_cal
    1.type = sensor_msgs/Image
    1.desc = Current occupancy map generated from the overhead cameras and the calibration files.
    
  }
  param {
    0.name = /image_calibration/runFromSimulation
    0.type = `boolean`
    0.desc = Determines whether the camera streams are simulated or real.
    
    1.name = /image_calibration/floor_cal
    1.type = `string` 
    1.desc = Locations of the calibration files containing the colors representing the floor in the real and simulated worlds. Used for background subtraction.
     
    2.name = /image_calibration/robot_lb_file
    2.type = `string`
    2.desc = Locations of the calibration files containing the colors representing the robot left back marker in the real and simulated worlds.
    
    3.name = /image_calibration/robot_rb_file
    3.type = `string`
    3.desc =Locations of the calibration files containing the colors representing the robot right back marker in the real and simulated worlds.
   
    4.name = /image_calibration/robot_lf_file
    4.type = `string`
    4.desc = Locations of the calibration files containing the colors representing the robot left front marker in the real and simulated worlds.
   
    5.name = /image_calibration/robot_rf_file
    5.type = `string`
    5.desc =Locations of the calibration files containing the colors representing the robot right front marker in the real and simulated worlds.
  }
}


node.1 {
  name = create_calibs
  desc = `create_calibs` allows users to easily create the calibration files used by the image_calibration node. The node creates a window with a camera feed from one of the overhead cameras. Color values can be added or removed from the different calibrations by using the mouse and keyboard commands, which are printed to the terminal. Calibration parameters, such as image blur and calibration accuracy, can be also modified using commands.     
    sub {
    0.name = /overhead_north/image_raw
    0.type =  sensor_msgs/Image
    0.desc = The raw image stream acquired from the north overhead camera.
    1.name = /overhead_south/image_raw
    1.type =  sensor_msgs/Image
    1.desc = The raw image stream acquired from the south overhead camera.
  }
  param {
     0.name = /create_calibs/runFromSimulation
    0.type = `boolean`
    0.desc = Determines whether the camera streams are simulated or real.
    
    1.name = /create_calibs/real_floor_cal
    1.type = `string` 
    2.name = /create_calibs/sim_floor_cal
    2.type = `string`
    2.desc = Locations of the calibration files containing the colors representing the floor in the real and simulated worlds. Used for background subtraction.
     
    3.name = /create_calibs/real_robot_lb_file
    3.type = `string`
    4.name = /create_calibs/sim_robot_lb_file
    4.type = `string`
    4.desc = Locations of the calibration files containing the colors representing the robot left back marker in the real and simulated worlds.
    
    5.name = /create_calibs/real_robot_rb_file
    5.type = `string`
    6.name = /create_calibs/sim_robot_rb_file
    6.type = `string`
    6.desc =Locations of the calibration files containing the colors representing the robot right back marker in the real and simulated worlds.
   
    7.name = /create_calibs/real_robot_lf_file
    7.type = `string`
    8.name = /create_calibs/sim_robot_lf_file
    8.type = `string`
    8.desc = Locations of the calibration files containing the colors representing the robot left front marker in the real and simulated worlds.
   
    9.name = /create_calibs/real_robot_rf_file
    9.type = `string`
    10.name = /create_calibs/sim_robot_rf_file
    10.type = `string`
    10.desc =Locations of the calibration files containing the colors representing the robot right front marker in the real and simulated worlds.
  }
}

node.2 {
  name = coord_conversion
  desc = `coord_conversion`  contains conversions for various coordinate systems, including the overhead camera map, the occupancy grid, and the real-world coordinate systems. This node is used by nodes in both youbot_overhead_vision and rrl_localization.
  
  srv{
    1.name = coord_conversion
    1.type = youbot_overhead_vision/CoordConversion
    1.desc = Takes in a conversion type (int), and a point in x,y coordinates, and returns the converted point x and y values. The different conversion types are: { 1 = Pixel to Meter | 2 = Meter to Pixel | 3 = Occupancy Grid to Meter}.
  }
}
```



## Startup

The `youbot_overhead_vision` package should be launched at the same
time as the 'rrl_localization' package with the use of the
'path_planner.launch' or the 'path_planner_sim.launch" launch files
depending on whether the camera streams are real or simulated. However,
the node can be run on its own by using one of the following commands:



```shell
rosmake youbot_overhead_vision
roslaunch youbot_overhead_vision youbot_overhead_vision.launch
```



or



```shell
rosmake youbot_overhead_vision
roslaunch youbot_overhead_vision youbot_overhead_vision_sim.launch
```



With the above node running, you can test video streaming with the
[image_view](image_view) package using the following command:



```shell
rosrun image_view image_view image:="/image_calibration/image_cal"
```



You may find that the two camera images do not align properly due to
different overhead camera positions. Changing this requires opening the
'image_calibration.h' and 'create_calibs.h' files, and changing the
SIM_OVERLAP and REAL_OVERLAP constants to match your real or simulated
camera streams overlaps.

You may also need to modify the calibration files. To do this, first
change the useFromSimulation parameter found in the
'youbot_overhead_vision_create_calibs.launch' launch file to 'true'
if the camera stream comes from gazebo, and 'false' otherwise. Then,
run the calibration creation tool using the following commands:



```shell
rosmake youbot_overhead_vision
roslaunch youbot_overhead_vision youbot_overhead_vision_create_calibs.launch
```



The calibration tool allows for both calibrating points, and setting
boundary regions through which the robot cannot drive through.
