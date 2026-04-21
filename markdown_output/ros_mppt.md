# MPPT ROS Package

## Introduction

The aim of this package is to send splitted data from a MPPT device in
ros. The package reads holding values from the MPPT, which are sent
using ve-direct protocol via serial USB port.

## Installation

### From the distro repo



```
sudo apt-get install ros-kinetic-ros_mppt
```



### From sources

Clone the package from github repo into your catkin workspace and build
as usual 

```
$ git clone https://github.com/AaronPB/ros_mppt.git
```



## Customize the sender

Depending on the interested values from the serial communication
interface, it is possible to define more values into the package.

**MPPT Values:**

  -- ----------- -- ----------- -- --------------------------------------- -- ---------------------- --
     **Label**      **Units**      **Description**                            **Type of variable**   
     V              mV             Main (battery) voltage                     Float                  
     I              mA             Battery current                            Float                  
     VPV            mV             Panel voltage                              Float                  
     PPV            W              Panel power                                Float                  
     PID                           Product ID                                 String                 
     SER#                          Serial Number                              String                 
     HSDS                          Day sequence number (0 \... 364)           Int                    
     MPPT                          Tracker operation mode                     Int                    
     ERR                           Error code                                 Int                    
     CS                            State of operation                         Int                    
     H19            0.01 kW/h      Yield Total (user resettable counter)      Float                  
     H20            0.01 kW/h      Yield today                                Float                  
     H21            W              Maximum power today                        Float                  
     H22            0.01 kW/h      Yield yesterday                            Float                  
     H23            W              Maximum power yesterday                    Float                  
  -- ----------- -- ----------- -- --------------------------------------- -- ---------------------- --

### Add the interested values into vemppt_ros

Choose those values you want to send from the topic, and modify the
python file "vemppt_ros.py" adding them with this structure:

First, define the value where the other ones are already be defined:


```python
#Predefined values of msg
    msg.v_bat = -1
    msg.i_bat = -1
    msg.v_pv = -1
    msg.p_pv = -1
```



Then, add into the while loop the following lines of code:


```python
elif "V" in ve_read and "P" not in ve_read: #Filter
            try:
                ve_read = ve_read.split("\t") #Splitter
                msg.v_bat = float(ve_read[1]) * 0.001 #Value of splitted data
            except Exception as e: logging.error('Exception ocurred in V', exc_info=True) #Log info register in case of error
```



The first line is the filter, the "important filters" are already made
so you only need to put the label of the value into a string (see the
example).

The other line you have to care about, is the value of the splitted
data. Define it following the MPPT values table.

#### Example

Imagine you want to see the error codes that the mppt is sending.

First, we define it in the predefined msg values section in
vemppt_ros.py as msg.error_mppt:



```python
#Predefined values of msg
    msg.v_bat = -1
    msg.i_bat = -1
    msg.v_pv = -1
    msg.p_pv = -1
    msg.error_mppt = 0 #Let's say it has no error at the beginning
```



Then, we add the following lines of code into the while loop:


```python
elif "ERROR" in ve_read: #Filter with "ERROR" label
            try:
                ve_read = ve_read.split("\t") #Splitter (nothing changed)
                msg.error_mppt = int(ve_read[1]) #Value of splitted data (no operations needed, and defined as an integer)
            except Exception as e: logging.error('Exception ocurred in ERROR', exc_info=True) #Log info register in case of error ("V" modified to "ERROR")
```



The modified sender() method will looks like the following code:


```python
"""
    This file is part of ros_mppt.
    ros_mppt is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    ros_mppt is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with ros_mppt.  If not, see <https://www.gnu.org/licenses/>.
"""

def sender():
    pub = rospy.Publisher('mppt_channel', mppt, queue_size=10)
    rospy.init_node('ros_mppt', anonymous=True)
    r = rospy.Rate(10)
    msg = mppt()

    #Predefined values of msg
    msg.v_bat = -1
    msg.i_bat = -1
    msg.v_pv = -1
    msg.p_pv = -1
    msg.error_mppt = 0

    while not rospy.is_shutdown():

        try:
            ve_read = ser.readline().decode("utf-8")
        except: logging.warning('Skipping decoding from ve_read line: ' + ve_read)

        if "V" in ve_read and "P" not in ve_read:
            try:
                ve_read = ve_read.split("\t")
                msg.v_bat = float(ve_read[1]) * 0.001
            except Exception as e: logging.error('Exception ocurred in V', exc_info=True)
        elif "I" in ve_read and "P" not in ve_read:
            try:
                ve_read = ve_read.split("\t")
                msg.i_bat = float(ve_read[1]) * 0.001
            except Exception as e: logging.error('Exception ocurred in I', exc_info=True)
        elif "VPV" in ve_read:
            try
                ve_read = ve_read.split("\t") * 0.001
                msg.v_pv = float(ve_read[1])
            except Exception as e: logging.error('Exception ocurred in VPV', exc_info=True)
        elif "PPV" in ve_read:
            try:
                ve_read = ve_read.split("\t")
                msg.p_pv = float(ve_read[1])
            except Exception as e: logging.error('Exception ocurred in PPV', exc_info=True)
        #Our new mppt value
        elif "ERROR" in ve_read:
            try:
                ve_read = ve_read.split("\t")
                msg.error_mppt = int(ve_read[1])
            except Exception as e: logging.error('Exception ocurred in ERROR', exc_info=True)

        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()
```



Now, we have our new custom value created. But, we need to do something
else to send it to the topic: define it in the .msg file.

### Add new values in the .msg file

If you want to add more custom values to the mppt_channel topic you have
to defined those in the .msg file. Go to msg/mppt.msg in your catkin
workspace and add the new custom values into them:


```
float64 v_bat
float64 i_bat
float64 v_pv
float64 p_pv
```



Following our previous example, we need to define msg.error_mppt into
the mppt.msg file (as an integer): 

```
float64 v_bat
float64 i_bat
float64 v_pv
float64 p_pv
int32 error_mppt
```



You can also define your own custom values just as state values or
anything else. More info of .msg files at the Documentation section.

## Run ros_mppt

To run the package first make sure to build it (also important if you
made any changes at vemppt_ros.py): 

```
$ cd ~/catkin_ws
$ catkin_make
$ . ~/catkin_ws/devel/setup.bash
```

 Then, just
run roscore and vemppt_ros.py: 

```
$ git clone https://github.com/AaronPB/ros_mppt.git
```

0

If you want to save the topic, you can use the rosbag command:


```
$ git clone https://github.com/AaronPB/ros_mppt.git
```

1

More info about ros commands at the Documentation section.

## Documentation

### GitHub Repositories

[vemppt_reader\|class=blue solid](https://github.com/AaronPB/vemppt_reader)
MPPT data registration into a xls file for experimental purposes.

[ros_mppt\|class=blue solid](https://github.com/AaronPB/ros_mppt) MPPT
ROS package.

### Victron Energy Documents

#### VE Direct Protocol

\[\[<https://www.victronenergy.com.es/download-document/2036/ve.direct-protocol-3.25.pdf>\|\[PDF\]
VE.Direct Protocol\|class=blue solid\]\] VE.Direct Protocol - Version
3.25.

\[\[<https://www.victronenergy.com.es/download-document/4459/bluesolar-hex-protocol-mppt.pdf>\|\[PDF\]
BlueSolar HEX\|class=blue solid\]\] !BlueSolar HEX protocol MPPT.

\[\[<https://www.victronenergy.com/live/mppt-error-codes>\|\[WIKI\] MPPT
Solar Charger Error Codes\|class=blue solid\]\]

### ROS Wiki Information

\[\[<http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv#Introduction_to_msg_and_srv>\|\[WIKI\]
ROS MSG Formats\|class=blue solid\]\]

\[\[<http://wiki.ros.org/ROS/CommandLineTools>\|\[WIKI\] ROS
CommandLineTools\|class=blue solid\]\]

\[\[<http://wiki.ros.org/ROS/Tutorials/CreatingPackage>\|\[WIKI\] ROS
Basic Indications for packages\|class=blue solid\]\]
