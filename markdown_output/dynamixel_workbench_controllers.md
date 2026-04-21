*ROS Software Maintainer: [ROBOTIS](http://wiki.ros.org/ROBOTIS)*

## ROBOTIS e-Manual

-   [ROBOTIS e-Manual for Dynamixel-Workbench](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)

## ROS API

```clearsilver
node.0 {
name= position_control

pub{
  0{
   name= dynamixel_state
   type= dynamixel_workbench_msgs/DynamixelStateList
   desc= Provides some states for connected Dynamixel by reading [[http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/|control table]].
  }
}

srv{
  0{
    name= joint_command
    type= dynamixel_workbench_msgs/JointCommand
    desc= Get commands and write value to Goal Position address in control table of connected Dynamixel
  }
}

param{
  0{
    name= /device_name
    type= String
    default= /dev/ttyUSB0
    desc= Configure USB port name  
  }
  1{
    name= /baud_rate
    type= uint32_t
    default= 57600
    desc= Configure baud rate for connecting Dynamixel
  }
  2{
    name= /scan_range
    type= uint8_t
    default= 10
    desc= Configure scan range for connecting Dynamixel
  }
  3{
    name= /profile_velocity
    type= uint32_t
    default= 200
    desc= Velocity Value of Profile
  }
  4{
    name= /profile_acceleration
    type= uint32_t
    default= 50
    desc= Acceleration Value of Profile
  }

}
```

```clearsilver
node.1 {
name= velocity_control

pub{
  0{
   name= dynamixel_state
   type= dynamixel_workbench_msgs/DynamixelStateList
   desc= Provides some states for connected Dynamixel by reading [[http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/|control table]].
  }
}

srv{
  0{
    name= velocity_command
    type= dynamixel_workbench_msgs/WheelCommand
    desc= Get commands and write value to Goal Velocity or Moving Speed address in control table of connected Dynamixel
  }
}

param{
  0{
    name= /device_name
    type= String
    default= /dev/ttyUSB0
    desc= Configure USB port name  
  }
  1{
    name= /baud_rate
    type= uint32_t
    default= 57600
    desc= Configure baud rate for connecting Dynamixel
  }
  2{
    name= /left_wheel
    type= uint8_t
    default= 1
    desc= Configure ID of Dynamixel
  }
  3{
    name= /right_wheel
    type= uint8_t
    default= 2
    desc= Configure ID of Dynamixel
  }
  4{
    name= /profile_velocity
    type= uint32_t
    default= 200
    desc= Velocity Value of Profile
  }
  5{
    name= /profile_acceleration
    type= uint32_t
    default= 50
    desc= Acceleration Value of Profile
  }

}
```

```clearsilver
node.2 {
name= torque_control

pub{
  0{
   name= dynamixel_state
   type= dynamixel_workbench_msgs/DynamixelStateList
   desc= Provides some states for connected Dynamixel by reading [[http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/|control table]].
  }
}

srv{
  0{
    name= joint_command
    type= dynamixel_workbench_msgs/JointCommand
    desc= Get commands and write value to Goal Current address in control table of connected Dynamixel
  }
}

param{
  0{
    name= /device_name
    type= String
    default= /dev/ttyUSB0
    desc= Configure USB port name  
  }
  1{
    name= /baud_rate
    type= uint32_t
    default= 3000000
    desc= Configure baud rate for connecting Dynamixel
  }
  2{
    name= /pan_id
    type= uint8_t
    default= 1
    desc= Configure ID of Dynamixel
  }
  3{
    name= /tilt_id
    type= uint8_t
    default= 2
    desc= Configure ID of Dynamixel
  }
  4{
    name= /p_gain
    type= float
    default= 0.003
    desc= Set p gain for PID feedback control
  }
  5{
    name= /d_gain
    type= float
    default= 0.00002
    desc= Set d gain for PID feedback control
  }

}
```

```clearsilver
node.3 {
name= multi_port

pub{
  0{
   name= dynamixel_state
   type= dynamixel_workbench_msgs/DynamixelStateList
   desc= Provides some states for connected Dynamixel by reading [[http://emanual.robotis.com/docs/en/dxl/x/xm430-w350/|control table]].
  }
}

srv{
  0{
    name= joint_command
    type= dynamixel_workbench_msgs/JointCommand
    desc= Get commands and write value to Goal Current address in control table of connected Dynamixel
  }
}

param{
  0{
    name= /pan_device_name
    type= String
    default= /dev/ttyUSB0
    desc= Configure USB port name
  }
  1{
    name= /pan_baud_rate
    type= uint32_t
    default= 57600
    desc= Configure baud rate for connecting Dynamixel
  }
  2{
    name= /tilt_device_name
    type= String
    default= /dev/ttyUSB1
    desc= Configure USB port name 
  }
  3{
    name= /tilt_baud_rate
    type= uint32_t
    default= 57600
    desc= Configure baud rate for connecting Dynamixel
  }
  4{
    name= /scan_range
    type= uint8_t
    default= 10
    desc= Configure scan range for connecting Dynamixel
  }
  5{
    name= /profile_velocity
    type= uint32_t
    default= 200
    desc= Velocity Value of Profile
  }
  6{
    name= /profile_acceleration
    type= uint32_t
    default= 50
    desc= Acceleration Value of Profile
  }

}
```

## Tutorials

-   [dynamixel workbench controllers tutorials](dynamixel_workbench_controllers/Tutorials) -
    This tutorial describes how to run controllers with tutorial
    packages.
