## Overview

The Merlin MiabotPRO is a small autonomous mobile robot featuring a high
precision drive train, dual processor design, onboard wireless
communications (Bluetooth,RF) with extensive support for additional
peripherals.

The Miabot has an onboard firmware API with PID and full feature access
via simple ASCII interface, making control of the robot from any
programming language/development platform very easy. The robot is widely
used internationally for advanced robotics research and development.

![\|height="225px;",width="225px;"](https://lh6.googleusercontent.com/pUCagu1hQvS562Z2qRcV6J8qZkPqrqpza9goACKmnPXBK0s1pR6IvUpM8JmbkqdvWfEP6GoZwHGlI0x9WxLLneA9H-HTQh1SJWutaeNZWBbMH6y5Yg)

miabotPro Mobile Robot - 65mm x 65mm x 65mm

## MiabotPRO Accessories

Supported accessories:

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <tablestyle="border: medium none; border-collapse: collapse;"style="border: 1px dotted rgb(170, 170, 170); vertical-align: top; padding: 7px;"> ![\|height="225px;",width="225px;"](https://lh5.googleusercontent.com/tUzAfjVUXLOxSISDlouBP6Zw9tyyz_GZoquydiobxuOEXtduwphKi7cGoaAmvZbTx2RJB2auXaCXyPax5bS6OmzCR-CVwmm3q0ovB8hRPRaFtKg38A) \*Intelligent Camera      <style="border: 1px dotted rgb(170, 170, 170); vertical-align: top; padding: 7px;"> ![\|height="225px;",width="225px;"](https://lh3.googleusercontent.com/SFSY230JB08oiD_yXJiCglUhAEhj1REipGBzkmbA7OeRBFRJBbQFOQGSS4w_ZGC9SbNjAe_k9g1jgXQU31GDr8KuGDupu7aVWDbZWQcdgfU8RFrriw) \*Compass      <style="border: 1px dotted rgb(170, 170, 170); vertical-align: top; padding: 7px;"> ![\|height="225px;",width="225px;"](https://lh3.googleusercontent.com/feJz14hJYzEh978y8tKlJv18Hfb2aC0tUMrvcYnKGUuET0RnMMy1dRrk4EalXv4BApOb6D4KBjIDrIdwToMlg1Pd2_qExO8UzOLEEnl_I05UYMTvSQ) \*Omni-Directional Sonar   
     <style="border: 1px dotted rgb(170, 170, 170); vertical-align: top; padding: 7px;"> ![\|height="225px;",width="225px;"](https://lh3.googleusercontent.com/L0xrhdoDE3SugLVb5KAx17hLfhHUFVPwYl59QDZ7pC7YXO-8WV2sisHhdrB_PMG0pta6hLE0iFf8wUSbbcvwKyfELu2aHNsv1POP3xskWljB3F2trw) \*Starboard                                                                             <style="border: 1px dotted rgb(170, 170, 170); vertical-align: top; padding: 7px;"> ![\|height="225px;",width="225px;"](https://lh5.googleusercontent.com/IFgyHZsOdZVvXOhlsvqDwWGTZ6Cq42qp8AsQSQNaJWTHpxkAm_oonadw1S4U8tp6HIAc4yOozC9HIwXRAVNg7eVj1eOK5UGs30H5iVOSs8hWZrDjZA) \*Gripper      <style="border: 1px dotted rgb(170, 170, 170); vertical-align: top; padding: 7px;"> ![\|height="225px;",width="225px;"](https://lh5.googleusercontent.com/eu5xFn2k1xcrn2BFGVX7Nn6LHQb3GMWlk6Dn6x-Z7R-3GhyL3t5H93ae18DxLrysBerUOrBbiPswRy89SIIFbTemwIG6S2JlMH6leu300FLyPuqphQ) \*Line Following Module    
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## ROS Miabot Driver Support (V1.0-Beta)

The Miabot PRO ROS driver implements the odometry source messages "odom"
and can process the geometry_msgs/Twist messages. The Miabot PRO driver
can initiate a TCP/IP link with the robot wirelessly using a couple of
methods. Either via a built in Bluetooth module (used when communication
with a small number of robots) or via a Bluetooth server (which is used
when communication with large numbers of robot e.g. over 7 upto around
50).

In either case a socket is initiated to communicate with the robot on a
given host/port combination. The following instructions illustrate how
to communicate using a Bluetooth dongle or built-in Bluetooth facility.

These instructions have been tested using Ubuntu Linux 10.04 and ROS
CTurtle.

## Internal/Dongle Bluetooth Setup

These instructions cover the use of a built in Bluetooth module or a
[USB Bluetooth dongle](http://www.merlinsystemscorp.co.uk/index.php/e-shop/merlin-wireless/bluetooth-usb-dongles/merlin-wireless-sena-ud100-bluetooth-usb-adapter.html).

Turn on the robot. Open up a terminal window and type:

. 

```
hcitool scan
```



Note the robot Bluetooth module, which normally begins with midxxx, and
then type:

. 

```
sudo rfcomm connect hci0 <bdaddr from hcitool>
```



This will block in terminal session with something like:

Connected /dev/rfcomm0 to 00:01:95:09:CA:82 on channel 1 Press CTRL-C
for hangup

Launch another terminal window to continue. The next stage is to convert
the serial rfcomm device into a TCP/IP socket. To do this we need to
install the useful ser2net utility:

. 

```
sudo apt-get install ser2net
```



Then configure the settings:

. 

```
add to the end of: /etc/ser2net.conf using your favourite editor (e3,nano etc)

3000:telnet:600:/dev/rfcomm0:19200 8DATABITS NONE 1STOPBIT banner
```



1.  (comment out any other port definitions on 3000)

Launch the program:

. 

```
ser2net
```



This will now run as a background process.

To check everything is working we can run up a terminal program such as
putty:

. 

```
sudo apt-get install putty

putty telnet://localhost:3000/

type: [t] and you will receive: <test#00>
```



This is an inbuilt test function within the robot, and will demonstrate
everything is working successfully. To close down the communication,
find the first window with the rfcomm connection and hit \^C. To
re-establish the connection just re-run the rfcomm line.

## ROS Miabot Driver Installation

. 

```
git init
git clone https://github.com/MerlinSystemsCorp/ROSMiabotDriver.git
```



-   Add the new directory location into the ROS package path variable
    (change /home/mark with your directory location):

. 

```
export ROS_PACKAGE_PATH=/home/mark/ROSMiabotDriver:/opt/ros/cturtle/stacks
```



Check the project builds correctly:

. 

```
rosmake ROSMiabotDriver
```



Launch the program:

. 

```
cd launch
./launch.sh
rosrun miabot miabot        (separate shell)

* optional Keyboard teleop of robot

rosrun miabot keyboard      (seperate shell)
```



## Other Features

Within the miabot program terminal you can type commands between '\['
and '\] which correspond to any of the API supported commands and
parameters. See \[3\] below in the resource links for more information.
Eventually all these features will be supported as parameters/messages
within ROS.

## Links to other resources

\[1\] [Manufacturers website](http:ww.merlinsystemscorp.co.uk)

\[2\]
[Command & parameter summary](https://docs.google.com/document/d/1Pq1nhnMzAoUc66VK6sDkUGyntGQ_PwUqz52x3oCIus0/edit?hl=en_GB)

\[3\] [Product page](http://www.merlinsystemscorp.co.uk/miabotpro)
