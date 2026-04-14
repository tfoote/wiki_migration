## Overview

The ric_robot package is the main package which allows to communicate
and control the different robots which is made by
[RoboTiCan](http://www.robotican.net).

## Usage

### Launching the robot

Users can run the main robot launch file (e.g. lizi.launch or
komodo.launch) to initiate all the robot controllers and sensors with a
single command. ```
$ roslaunch ric_robot komodo.launch id:=<ID>
``` For example, running the launch
file with komodo id value of 1: ```
$ roslaunch ric_robot komodo.launch id:=1
``` This command
should be executed on the robot computer. For remote operation see the
[ric_base_station](ric_base_station) package. The id number sets the
robot name to be komodo\_\<ID\>, this is extremely important when
working with several robots as a group of robots. This allows giving
each robot in the group a unique name. The id argument can be any
desired id number. The id number affect the namespace and the robot
description file links and joint names. All the topics, services and
parameters will have a komodo\_\<ID\> prefix. The robot launch file is
also used to load nodes for the webcams, the Asus RGB-D camera, the
Hokuyo laser scanner and the robot arm launch file (komodo_arm.launch).

The robot launch file also loads the configuration file (e.g.
ric_robot/config/default_komodo.yaml) which contains various parameters
.

### Controlling the arm

To control the Komodo robot arm see the
[Controlling the Komodo arm](ric/Tutorials/Controlling the Komodo arm)
tutorial.

### Using the Laser scanner

See [hokuyo_node](hokuyo_node) for package details.

Relevant lines in the launch file: ```shell
<node pkg="hokuyo_node" type="hokuyo_node" name="hokuyo_node" output="screen">
      <param name="port" value="/dev/Hokuyo" />
      <param name="frame_id" value="komodo_$(arg id)_Laser_link" />
</node>
```

The readings are published on the \'\'\'/komodo\_\<ID\>/scan\'\'\'
topic.

### Using the depth sensor (ASUS Xtion PRO LIVE)

See [openni2_launch](openni2_launch) for package details.

Relevant lines in the launch file: ```shell
<include file="$(find openni2_launch)/launch/openni2.launch">
      <arg name="camera" value="komodo_$(arg id)_Asus_Camera" />
</include>
```

### Using the cameras

See [usb_cam](usb_cam) for package details.

Relevant lines in the launch file (for each camera):
```shell
<node pkg="usb_cam" type="usb_cam_node" name="arm_cam_node" output="screen"  respawn="true">
      <param name="~video_device" value="/dev/video0" />
      <param name="~camera_frame_id" value="komodo_$(arg id)_Arm_Camera_link" />
      <param name="~pixel_format" value="yuyv" />
      <param name="~image_width" value="320" />
      <param name="~image_height" value="240" />
</node>
```

### Reading the ultrasonic range finders

The Komodo and Lizi robots have three ultrasonic range finders (URF)
mounted on the sides and on the back of the robot. The range readings
are published under the following topics:

\'\'\'/komodo\_\<ID\>/Rangers/Left_URF\'\'\'

\'\'\'/komodo\_\<ID\>/Rangers/Rear_URF\'\'\'

\'\'\'/komodo\_\<ID\>/Rangers/Right_URF\'\'\'

## Nodes

```clearsilver
node {
  0{
    name = ric_node
    desc = This is the main robot node.
    pub{
       0{
        name= gps_pub
        type= sensor_msgs/NavSatFix
        desc= This topic publishes the GPS location of the robot.
      }
      1{
        name= imu_pub
        type= sensor_msgs/Imu
        desc= This topic publishes the orientation of the robot as measured by the internal IMU (Inertial Measurement Unit).
      }
      2{
        name= odom_pub
        type= nav_msgs/Odometry
        desc= This topic publishes the location and orientation of the robot based on the odometry computation of the wheels rotations.
      }
      3{
        name= Rangers/Left_URF
        type= sensor_msgs/Range
        desc= Left Ultrasonic Range Finder readings
      }
      4{
        name= Rangers/Rear_URF
        type= sensor_msgs/Range
        desc= Rear Ultrasonic Range Finder readings
      }
      5{
        name= Rangers/Right_URF
        type= sensor_msgs/Range
        desc= Right Ultrasonic Range Finder readings
      }
    }
    sub{
      0{
        name= cmd_vel
        type= geometry_msgs/Twist
        desc= The robot listens to this topic and set its forward and angular velocity accordingly.
      }

    }
    srv{
      0{
        name= set_odom
        type= ric_robot/set_odom
        desc= This service set the odometry of the robot to any desired location and orientation, it should receive three fields: float32 x,  float32 y, float32 theta.
      }
    }

    param {
      0{
        name= fuse_imu_roll_pitch
        type= boolean
        default= false
        desc= This parameter when true uses the IMU's roll and pitch measurements. If false it assumes the robot is on a horizontal surface.
      }
      1{
       name= fuse_imu_roll_pitch
        type= boolean
        default= false
        desc= This parameter when true uses the IMU's yaw measurement instead of the calculated odometry heading. If false uses the robot odometry to determine its heading.
      }
2{
       name= wheel_diameter
        type= double
        default= 0.14 for lizi, 0.254 for komodo
        desc= Robot wheels diameter im meters.
      }
 3{
     name= wheel_base_length
        type= double
        default= 0.275 for lizi, 0.402 for komodo
        desc= Robot width in meters.
      }
 4{
     name= encoder_cpr
        type= double
        default= 4288 for lizi4 model, 56000 for lizi2 model, 2048 for komodo
        desc= Wheels encoders cpr = (ppr*4)
      }
    }
  }
1{
 name = serial_node
    desc = This is an internal node that is responsible for the communication between the internal micro-controller and the computer. This node belongs to the rosserial_python package(http://wiki.ros.org/rosserial).

srv {
      0{
        name= reset_encoders
        type= std_srv/Empty
        desc= This service reset the encoder readings on the micro-controller counters.
      }
      1{
        name= ric_calib
        type= ric_robot/ric_calib
        desc= This service allows calibrating the IMU accelerometers and magnetometer and the Remote control. see the [[ric/Tutorials/Calibrating the robot IMU|Calibrating the robot IMU]] and [[ric/Tutorials/Calibrating the robot RC|Calibrating the robot RC]] tutorials.
      }
      2{
        name= restart
        type= std_srv/Empty
        desc= This service restart the micro-controller.
      }
      3{
        name= relays
        type= ric_robot/relays
        desc= This service allows to set the relays module outputs (only if you have a relay on your robot). e.g. some komodo robots have a front light connected to channel 1.
      }
}
param {
     0{
 name= pid_constants
        type= float array
        default= [0.02,0.2,0.0,0.5,1.0] for lizi, [0.02,0.08, 0.0, 0.05,1.0] for komodo
      desc= [kp, ki, kd, alpha(for velocity low-pass filter), control_dt (control loop interval in milliseconds)]

}
}
 pub{
      0{
        name= ric_status
        type= ric_robot/ric_status
        desc= This topic publishes the rover and sensors modules batteries voltages in Volts and the faults report. The faults parameter is constructed from 4 bits as follows: Bit 0 is set if the RC remote control is on and the robot is on manual control mode. Bit 1 is set if the communication with the motors driver is fault. Bit 2 is set if GPS location is not valid. Bit 3 is set if IMU readings are not valid. faults = (Bit 0)*1 + (Bit 1)*2 + (Bit 2)*4 + (Bit 3)*8. Note that the minimum voltage for the komodo sensors\arm battery is around 11.5V and for the rover  battery it is around 23V.
       }
       1{
        name= raw_gps
        type= ric_robot/ric_gps
        desc= Internal use topic.
       }
       2{
        name= ric_raw
        type= ric_robot/ric_raw
        desc= Internal use topic.
       }
}
sub{
  0{
        name= command
        type= ric_robot/ric_command
        desc= Instead of using the cmd_vel topic, one may want to directly command the robot motors. The ric_robot/ric_command message contains two fields: int32 left_wheel, int32 right_wheel . The values are in encoder ticks per second units.
      }
      1{
        name= pan_tilt
        type= ric_robot/ric_pan_tilt
        desc= This topic sends command to the Lizi robot pan tilt system that orients the RGB-D sensor. The ric_pan_tilt message contains two fields: float32 pan_angle and float32 tilt_angle. The values are in radians units. Note that the positive directions of the pan-tilt are left and up respectively. A single message is enough to set the required angles (no need for publishing these messages continuously). The pan angle range of motion is -35 to +35, and the tilt range is -30 to +30. These limitations are constrained by software.
      }
}
}
2{
 name = komodo_arm
    desc = This node have two main functions. The first function is to read the arm actuators states and publish them as a sensor_msgs/JointState message. The second function is to control the arm elevator.

srv {
      0{
        name= elevator_controller/set_position
        type= ric_robot/set_elevator
        desc= This service allows to set (override) the elevator position.
      }
      1{
        name= elevator_controller/home
        type= ric_robot/home_elevator
        desc= This service initiate the elevator homing procedure. 
      }
      
}

 pub{
      0{
        name= joint_states
        type= sensor_msgs/JointState
        desc= This topic publish the arm joints states as sensor_msgs/JointState message.
       }
}
sub{
  0{
        name= elevator_controller/pos_command
        type= ric_robot/ric_elevator_command
        desc= This topic listen to position commands for the arm elevator. Commanding the elevator is possible only after a successful homing procedure.
      }
}
```

## Report a Bug

\<\<GitHubIssues(robotican/ric)\>\>
