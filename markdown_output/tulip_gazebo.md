# Package Summary

This package contains the controller, sensor publishers and launch files
for the [TUlip](Robots/TUlip) simulation. To communicate with the gazebo
simulator in real-time, the
[pr2_controller_manager](pr2_controller_manager) infrastructure is used.
The geometric, inertial and visual properties of TUlip are described in
[tulip_description](tulip_description).

## Controller

Functionally the controllers manage TUlip\'s movement in simulation. The
structure of the controller is as follows: ```clearsilver
name = TUlipController
desc = Generic controller which parses <<MsgLink(sensor_msgs/JointState)>> messages and calculates the torques on the corresponding joints. The controller also returns the current position of the joints as <<MsgLink(sensor_msgs/JointState)>> messages. This generic controller is used as leg, arm and head controller. Currently, the desired joint angles are imported from a yaml parameter file. In the future, we may release our walking algorithm which publishes joint angles such that the controller can subscribe to these. 
pub {
   0{
    name = /joint_states
    type = sensor_msgs/JointState
    desc = Joint state data
    }
  }
```

## Sensors

TUlip has two cameras for stereo vision on its head, four force sensors
under each foot and an inertial measurement unit on its torso. The
structure of the sensors is as follows: ```clearsilver
name = Camera
desc = Generic sensor that publishes camera info and data.
pub {
   0{
    name = /camera/(left or right)/camera_info
    type = sensor_msgs/CameraInfo
    desc = Info of the left and right camera
    }
   1{
    name = /camera/(left or right)/image_raw
    type = sensor_msgs/Image
    desc = Raw image data of left and right camera
    }
  }
```
```clearsilver
name = Foot Sensor
desc = Generic footsensor that publishes foot sensor state and data.
pub {
   0{
    name = /(left or right)_(heel or toe)_(inner or outer)_foot_sensor/state
    type = gazebo_msgs/ContactsState
    desc = State of the foot sensor at all corners of each foot
    }
   1{
    name = /(left or right)_(heel or toe)_(inner or outer)_foot_sensor/state
    type = gazebo_msgs/ContactsState
    desc = Foot sensor data of at all corners of each foot
    }
  }
``` ```clearsilver
name = Inertial Measurement Unit
desc = Generic inertial measurement unit that publishes odometry data.
pub {
   0{
    name = /xsens_pose_ground_truth
    type = nav_msgs/Odometry
    desc = Odometry data of the torso of the robot
    }
  }
```

## Matlab

Besides publishing sensor data in the standard ROS message types, the
package publishes the sensor data also in a format which can be easily
imported in Mathworks Matlab. ```clearsilver
name = Matlab Publisher
desc = Generic publisher for sensor data which is easily accessible in Mathworks Matlab.
pub {
   0{
    name = /tulip_controller/matlab_joints
    type = tulip_gazebo/joint_state_message
    desc = Joint state data in Matlab readable format
    }
   1{
    name = /tulip_controller/matlab_footsens
    type = tulip_gazebo/footsens_state_message
    desc = Foot sensor data data in Matlab readable format
    }
   2{
    name = /tulip_controller/matlab_xsens
    type = tulip_gazebo/xsens_state_message
    desc = Odometry data in Matlab readable format
    }
  }
```

## Launch files

### start.launch

This file loads the [tulip_description](tulip_description), spawns it in
gazebo and launches the gazebo-gui. Furthermore, it starts the
[pr2_controller_manager](pr2_controller_manager) followed by the TUlip
simulation controllers.

### rviz.launch

This file loads the [tulip_description](tulip_description) and shows it
in rviz.
