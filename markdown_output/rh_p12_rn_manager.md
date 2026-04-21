*ROS Software Maintainer: [ROBOTIS](http://wiki.ros.org/ROBOTIS)*

## ROBOTIS e-Manual

-   [ROBOTIS e-Manual for RH-P12-RN](http://emanual.robotis.com/docs/en/platform/rh_p12_rn/examples/#examples)

## ROS API



```clearsilver
node.0 {
name= rh_p12_rn_manager

param{
  0{
    name= gazebo
    type= bool
    default= false
    desc= Configure whether to run the program in gazebo mode.
  }
  1{
    name= offset_file_path
    type= string
    default= ""
    desc= This path indicates the location of the file that contains offset data of each joint and initial posture data for offset adjustment.
  }
  2{
    name= robot_file_path
    type= string
    default= ""
    desc= This path indicates the location of .robot file that contains robot description data.
  }
  3{
    name= init_file_path
    type= string
    default= ""
    desc= This path indicates the location of the file that contains initialization information of each joint.
  }
  4{
    name= device_name
    type= string
    default= "/dev/ttyUSB0"
    desc= This port name is used to open the communication port of OpenCR that manages Dynamixel power supply.
  }
  5{
    name= baud_rate
    type= int
    default= "2000000"
    desc= This baud rate is used to open the communication port of OpenCR that manages Dynamixel power supply.
  }
}

}
```



## Using Libraries

Each library has publishers and subscribers. Please refer to the
information on the link.

-   [robotis_controller](robotis_controller)
-   [rh_p12_rn_base_module](rh_p12_rn_base_module)
