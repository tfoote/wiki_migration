## Introduction

This package provides a driver for the 3rd production of Xsens-MTi.
Compared to the other MTi drivers ([xsens_driver](xsens_driver) and
[lse_xsens_mti](lse_xsens_mti)), this simple but stable package, based
on hydro, focus only on the imu data instead of GPS data. If you have
any problem using ([xsens_driver](xsens_driver) and
[lse_xsens_mti](lse_xsens_mti)), try this one.

## Installation

Open a terminal: ```
$ sudo cd ~/catkin_ws/src
        $ git clone https://github.com/JJJJJJJack/xsens_reader.git
        $ cd ..
        $ catkin_make
        $ catkin_make install
```

## Run

Open a terminal: ```
$ sudo su
         $ cd ~/catkin_ws
         $ source devel/setup.bash
         $ roscore
```

Open another terminal: ```
$ sudo su
         $ cd ~/catkin_ws
         $ source devel
         $ rosrun xsens_reader xsens_reader -d /dev/ttyUSB0
```

## Note

\'\'\'\'\'Only for hydro\'\'\'\'\'

Try USB1 USB2 if you can\'t connect to the port.

xsens_reader publishes the sensor_msgs::Imu message of \"/xsens_data\".

run ```
$ rostopic echo /xsens_data
``` to show the message of MTi.

## Published Topics

```clearsilver
pub{
  0.name = /xsens_data
  0.type = sensor_msgs/Imu
  0.desc = orientation, angular velocity, and linear acceleration.
}
```
