## Package: psen_scan_v2

The **psen_scan_v2** package is a ROS integration driver for the
PSENscan safety laser scanner product. It lets you integrate the laser
scanner data into your ROS Environment easily. Using the standard
[sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html)
message format ensures compatibility with other
laserscan-post-processing nodes such as
[gmapping](http://wiki.ros.org/gmapping).

  -- --------- -- ----------------------------------------------------------------------------------------------------------- -- --------- --
     <40%>      ![PILZ safety laser scanner](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/PSENscan.jpg)      <40%>   
  -- --------- -- ----------------------------------------------------------------------------------------------------------- -- --------- --

**Common features:**

- compliant and approved in accordance with (EN/IEC 61496-1: Type 3, EN
  ISO 13849-1: PL d, IEC 61508: SIL 2)
- opening angle: 275°
- operating range: 3.0 or 5.5 m safety zone
- 40 m warning zone, reaction time: 62 ms
- Protection type: IP65
- Dimensions (H x W x D) in mm: 152 x 102 x 112.5

**Light versions Additional features**:

- Muting
- EDM
- Override

## Supported Devices

PSENscan firmware >= 3.1.0 is supported on the following models:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------- -- -------------------------- --
     <24%> **Type**                                                                                                                                                             **Features**                                                                                                                          <10%> **Order number**   
     [PSEN sc L 3.0 08-12](https://www.pilz.com/de-DE/eshop/Sensorik/Optoelektronische-Sensoren/PSENscan-Sicherheits-Laserscanner/PSENscan/PSEN-sc-S-3-0-08-12/p/6D000020)        3.0 m safety zone, 8 or 12-pin exchangeable memory module                                                                             6D000012                   
     [PSEN sc L 5.5 08-12](https://www.pilz.com/de-DE/eshop/Sensorik/Optoelektronische-Sensoren/PSENscan-Sicherheits-Laserscanner/PSENscan/PSEN-sc-L-5-5-08-12/p/6D000013)        5.5 m safety zone, 8 or 12-pin exchangeable memory module                                                                             6D000013                   
                                                                                                                                                                                  \*Master versions\* Additional features: Muting, EDM, Override, restart in accordance with EN ISO 61496-3, vertical applications                                 
     [PSEN sc M 3.0 08-12](https://www.pilz.com/de-DE/eshop/Sensorik/Optoelektronische-Sensoren/PSENscan-Sicherheits-Laserscanner/PSENscan/PSEN-sc-M-3-0-08-12/p/6D000016)        3.0 m safety zone, 8 or 12-pin exchangeable memory module                                                                             6D000016                   
     [PSEN sc M 5.5 08-12](https://www.pilz.com/de-DE/eshop/Sensorik/Optoelektronische-Sensoren/PSENscan-Sicherheits-Laserscanner/PSENscan/PSEN-sc-M-5-5-08-12/p/6D000017)        5.5 m safety zone, 8 or 12-pin exchangeable memory module                                                                             6D000017                   
     [PSEN sc ME 5.5 08-17](https://www.pilz.com/de-DE/eshop/Sensorik/Optoelektronische-Sensoren/PSENscan-Sicherheits-Laserscanner/PSENscan/PSEN-sc-ME-5-5-08-17/p/6D000034)      Master Encoder, 5.5 m safety zone, 8/17-pin exchangeable memory                                                                       6D000019                   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------- -- -------------------------- --

## Usage

To start reading data from the safety laser scanner and publishing scans
execute **roslaunch psen_scan_v2 psen_scan_v2.launch** in a command
line. This will launch the ROS Node with the default configuration.

If you wish to set parameters from the command line, add them to the end
of the command as **parameter:=value**, separated by spaces.



```
roslaunch psen_scan_v2 psen_scan_v2.launch sensor_ip:=192.168.0.10
```



This example configures the safety laser scanner at 192.168.0.10 to send
it´s frames to the ROS node at localhost.

In order to create an application with your own launch file, you can
include the **bringup.launch**, where you can easily adjust the
configuration parameters. A more detailed explanation can be found in
the [tutorials](http://wiki.ros.org/psen_scan_v2/Tutorials/).

### Parameters

  -- --------------- -- ---------- -- ------------------ -- ------------------------------------- --
     **Name**           **type**      **default**           **description**                       
     **sensor_ip**      *string*      "192.168.0.10"      IP-Address of safety laser scanner.   
  -- --------------- -- ---------- -- ------------------ -- ------------------------------------- --

### Optional Parameters

  -- ----------------- -- ---------- -- ------------------------ -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Name**             **type**      <20%> **default**         **description**                                                                                                                                                                                                           
     **tf_prefix**        *string*      "laser_1"                 Name of this scanner that can be changed to differentiate between multiple devices. By convention this is used as tf prefix.                                                                                              
     **angle_start**      *double*      -2.398 (= -137.4 deg))      Start angle of measurement. (Radian)                                                                                                                                                                                      
     **angle_end**        *double*      2.398 (= 137.4 deg))        End angle of measurement. It is included in the measurements. (Radian)                                                                                                                                                    
     **intensities**      *bool*        false                       Publish intensities. If this is enabled, the resolution needs to be increased (at least 0.2 deg).                                                                                                                         
     **resolution**       *double*      0.0017 (= 0.1 deg))         Scan angle resolution. (Radian) The value is rounded to a multiple of 0.1 deg and has to be in the range \[0.1, 10\] degrees.                                                                                             
     **config_file**      *string*      ""                        Full path to a scanner config file. If a file is provided the configured zonesets and active zone markers are published, see [here](#importing-the-zoneset-configuration) for more information.   
  -- ----------------- -- ---------- -- ------------------------ -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### Expert Parameters (optional)

  -- --------------------------- -- ---------- -- ------------- -- ------------------------------------------------------------------------------------ --
     **Name**                       **type**      **default**      **description**                                                                      
     **host_ip**                    *string*      "auto"         IP-Address of host machine. The IP of the local machine is used by default.          
     **host_udp_port_data**         *int*         55115            UDP Port on which monitoring frames (scans) should be received.                      
     **host_udp_port_control**      *int*         55116            UDP Port used to send commands (start/stop) and receive the corresponding replies.   
     **fragmented_scans**           *bool*        false            Publish scan data as soon as a UDP packet is ready, do not wait for a full scan.     
     **rviz**                       *bool*        true             Start a preconfigured rviz visualizing the scan data.                                
  -- --------------------------- -- ---------- -- ------------- -- ------------------------------------------------------------------------------------ --

### Published Topics

**/<name>/scan**
([sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html))

- If *fragmented_scans* is set to false (default) the driver will
  publish complete scan rounds from the PSENscan safety laser scanner as
  a single message.
- If *fragmented_scans* is enabled the driver will send the measurement
  data as soon as they arrive, instead of waiting for the scan round to
  be completed. This way the scan data is received sooner but is split
  into several sensor messages.



```wiki
'''Hint: 1: Scan rounds and fragments that contain no measurement data are not published. This can happen with smaller scan ranges.'''
```





```wiki
'''Hint: 2: Frequency of the laser scan messages is about 33hz for the combined and 200hz for the fragmented scans.'''
```



**/<name>/zoneconfiguration**
([psen_scan_v2/ZoneSetConfiguration](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/ZoneSetConfiguration.html))



```wiki
'''Hint: 1: Will not be advertised if no config_file is provided.'''
```



**/<name>/active_zoneset**
([std_msgs/UInt8](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/UInt8.html))

- This topic contains the id of the currently active zoneset of the
  PSENscan safety laser scanner.



```wiki
'''Hint: 1: If no zonesets are configured the driver will publish "0" as default.'''
```



**/<name>/active_zoneset_markers**
([visualization_msgs/MarkerArray](http://docs.ros.org/en/noetic/api/visualization_msgs/html/msg/MarkerArray.html))

- The markers published represent the currently active zoneset as
  triangle lists. They can be viewed e.g. in rviz.



```wiki
'''Hint: 1: Uses the topics /<name>/zoneconfiguration and /<name>/active_zoneset to calculate the vizualization and updates in the same frequency as those topics.'''
```





```wiki
'''Hint: 2: Will not be advertised if no config_file is provided.'''
```



**/<name>/io_states**
([psen_scan_v2/IOState](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/IOState.html))

- The state published represents the current input and output state of
  the scanner IOs. A list of all available IOs can be found
  [here](#transferred-ios)



```wiki
'''Hint: 1: With every scan data of a monitoring frame the IO states are transferred from the PSENscan safety laser scanner. They are processed in the same way as the scan data.'''
```





```wiki
'''Hint: 2: By using <fragmented_scans=true> the driver will publish 1 IOStates while with <fragmented_scans=false> it will publish 6 IOStates per single publish of scan data.'''
```





```wiki
'''Hint: 3: The timesamps of all IO states are the same as the one of their corresponding `LaserScan` msg.'''
```



### TF Frames

The location of the TF frames is shown in the image below. These names
are defined by the aforementioned launchfile parameter **name**.
Changing them is necessary for instance when running multiple scanners.

  -- --------- -- --------------------------------------------------------------------------------------------------------------------------- -- --------- --
     <40%>      ![PILZ safety laser scanner frames\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/frames.png)      <40%>   
  -- --------- -- --------------------------------------------------------------------------------------------------------------------------- -- --------- --

### Defining the scan range

You can adjust the scan field to your needs by changing *angle_start*
and *angle_end*. The published
[sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html)
will only contain data within the given angle limits. Both limits are
defined within the *laser_1*frame as shown in the image below.

  -- --------- -- -------------------------------------------------------------------------------------------------------------------- -- --------- --
     <40%>      ![Limit visualization\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/angle_limits.png)      <40%>   
  -- --------- -- -------------------------------------------------------------------------------------------------------------------- -- --------- --

### Timestamp details

The timestamps of the scan data published are computed to be close to
reality and processing speed of incoming data was optimized to reduce
the time for the scan data to be published. This should suffice for
localization and slam algorithms. If you application benefits from
getting the scan data any sooner there are two possibilities:

- Use fragmented scans. This will publish the individual frames received
  by the PSENscan safety laser scanner immediately instead of waiting
  for a scan round to be completed and combined to a single laser scan
  message.
- Use the tcp_nodelay flag in your ROS subscriber. This will disable the
  nagle's algorithm, which is a TCP optimization. This algorithm can
  produce a jitter of about 20ms in the ros topic.
- The cpp API of ROS does not support disabling this on the publisher
  side. If you don't have control over the subscriber e.g. due to using
  a third party package you can create a python node which acts as a
  repeater for the scan topic. rospy subscriber and publisher both allow
  setting this flag and thus can disable it for this driver and the
  third party package.

### Transferred IOs

The state of inputs and outputs of the PSENscan safety laser scanner are
published as
[psen_scan_v2/IOState](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/IOState.html).
The topic at **/<name>/io_states** is latched and always gives the
most recent pin state. On changes at the physical IOs, the changes are
logged to the console and the new state is published to the topic.

The
[input pin state](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/InputPinState.html)
contains information about

- muting
- override
- zone set switching inputs

The
[output pin state](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/OutputPinState.html)
consists of

- OSSD safety states
- warning output
- reference points violation

Please see the message descriptions for full lists of bits.

### Importing the zoneset configuration

Once you setup the scanner and created a configuration according to our
[tutorial](http://wiki.ros.org/psen_scan_v2/Tutorials/SettingUpPSENscanHW#Create_a_new_configuration)
you can use an exported xml configuration file within ROS. The
configured zonesets will be published.

The zonesets you created in the Pilz configurator:

  -- --------- -- ----------------------------------------------------------------------------------------------------------------------------------------- -- --------- --
     <40%>      ![configurator_screenshot\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/zones_screenshot_configurator.png)      <40%>   
  -- --------- -- ----------------------------------------------------------------------------------------------------------------------------------------- -- --------- --

will be exactly the same in ROS:

  -- --------- -- --------------------------------------------------------------------------------------------------------------------------------- -- --------- --
     <40%>      ![configurator_screenshot\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/zones_screenshot_rviz.png)      <40%>   
  -- --------- -- --------------------------------------------------------------------------------------------------------------------------------- -- --------- --

You can try this out with: 

```bash
roslaunch psen_scan_v2 psen_scan_v2.lauch config_file:='full_path_to/example_config.xml'
```



If you want to use the configuration node in your launchfile add a
section such as:



```xml
<node ns="$(arg laser_ns)" name="config_server_node_$(arg laser_ns)" type="config_server_node" pkg="psen_scan_v2">
  <param name="config_file" value="$(arg config_file)" />
  <param name="frame_id" value="$(arg frame_id)" />
</node>
```



### Visualizing the active zoneset

For visualizing the active zoneset in RViz you can run the
**active_zoneset_node**. It will publish markers on the
**<name>/active_zoneset_markers** topic like shown in the RViz
screenshot above.

## Report a Bug

## Further information

You need further information? Our international hotline staff will
support you individually about our ROS packages at ros@pilz.de or visit
us at <https://pilz.com>.

Pilz is an international-scale, innovative automation technology
company. Pilz uses its solutions to create safety for man, machine and
the environment. In addition to the head office in Ostfildern near
Stuttgart, the family business is represented by over 2,400 employees at
42 subsidiaries and branches on all continents.

The company's products include sensor technology, electronic monitoring
relays, safety relays, configurable and programmable control systems,
automation solutions with motion control, systems for industrial
communication as well as visualization solutions and operator terminals.

Pilz solutions can be used in all areas of mechanical engineering,
including the packaging and automotive sector, plus the railway
technology, press and wind energy sectors. These solutions ensure that
baggage handling systems run safely at airports and funiculars or roller
coasters travel safely; they guarantee fire protection an energy supply
in buildings.

## Tutorials

### psen_scan_v2 Tutorials

- [How to set up a Pilz PSENscan laser scanner with Ethernet](#how-to-set-up-a-pilz-psenscan-laser-scanner-with-ethernet):
  Learn how to set up the PSENscan laser scanner with Ethernet for later
  use within the ROS environment.
- [How to set up ROS to communicate with the scanner](#how-to-set-up-ros-to-communicate-with-the-scanner):
  You learn how to set up the PILZ laser scanner with ROS and show the
  result in Rviz.
- [Launching multiple scanners](#launching-multiple-scanners):
  This tutorial explains how to use multiple scanners.



```wiki
'''Note:'''
The files for these tutorials are also available for download from [[https://github.com/PilzDE/pilz_tutorials|GitHub/pilz_tutorials]]
```





```wiki
'''Note:'''
If you experience any problems or have suggestions to improve the tutorials, please file an [[https://github.com/PilzDE/pilz_tutorials/issues|Issue on Github]].
```

## How to set up a Pilz PSENscan laser scanner with Ethernet

- **Description:** Learn how to set up the PSENscan laser scanner with
  Ethernet for later use within the ROS environment.
- **Keywords:** Industrial, Ethernet, laser scanner, PSENscan,
  psen_scan, psen_scan_v2
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [How to set up ROS to communicate with the scanner](#how-to-set-up-ros-to-communicate-with-the-scanner)



```wiki
'''WARNING'''

THE PILZ SOFTWARE IS PROVIDED AS-IS AND WITH NO WARRANTY (FOR MORE DETAILS SEE LICENSE). 

'''System or plant integrators only'''

This tutorial is solely intended for system or plant integrators only.
The system or plant integrator is responsible for taking into account the requirements from the respective current standard e.g. EN ISO 10218-2, EN ISO 61508 or taking equivalent measures.
```



### Introduction

In this tutorial you learn how to set up the PSENscan laser scanner with
Ethernet using the Pilz configuration tool, so that you are able to use
the PSENscan laser scanner in a later step within the ROS environment.

### Prerequisites

In order to complete this tutorial, you need the following:

- The operating manual. This tutorial does not replace the operating
  manual! Read it carefully first!
- [PSENscan Operating Manual sc M 3/5 series](https://www.pilz.com/download/open/PSEN_sc_M_Operat_Man_1005055-EN-02.pdf)
- [PSENscan Operating Manual sc L 3/5 series](https://www.pilz.com/download/open/PSEN_sc_L_Operat_Man_1005056-EN-01.pdf)

<!-- -->

- [A Safety laser scanner PSENscan](https://www.pilz.com/de-DE/eshop/0010600219713180PW/PSENscan#components),
  list of
  [ROS supported scanner models](https://github.com/PilzDE/psen_scan_v2)

<!-- -->

- A appropriate Ethernet cable and power cable for the PSENscan laser
  scanner have to be ordered separately. You can find the accesories for
  the laser scanner at the
  [online shop](https://www.pilz.com/en-INT/eshop/0010600219713180PW/PSENscan).
  Select your laser scanner and click at **Accesories**.

<!-- -->

- A 24V DC power supply.

<!-- -->

- A PC with Windows 7, 10 or XP (32 Bit and 64 Bit) operating system and
  Ethernet interface.

<!-- -->

- [The proper PSENscan Configurator software](https://www.pilz.com/de-INT/support/downloads#currentPage=1&SEARCH=psenscan%20configurator&pilz_group_type=download&search_connector=and&SORT=dmodified)
  installed on the PC.

### Setup connection between PSENscan and the PC

#### Connect the hardware

![Scanner](doc/laser_scanner.png)

- Connect the power cable to \[1\] or \[2\] depending on the number of
  pins of your cable.
- Connect the power supply to the blue and brown wires of the power
  cable
- Connect the PC via Ethernet adapter cable to \[4\]

The power supply must not exceed 24V DC. See the appropriate operating
manual for details on the wiring and pinouts.



```wiki
 * Connector [3] is not required here. This will be used to connect subscriber devices.
```



#### Search the network for the PSENscan laser scanner

- Start the PSENscan Configurator on your PC and activate select
  **Scanner \&rightarrow; Search device** in the upper menu bar to
  search the network for PSENscan laser scanners.
- Connected devices of the PSENscan laser scanner are listed under
  **Network environment**.
- Double-click the safety laser scanner from **Network environment**.



```wiki

 * The factory-set default IP address of the safety laser scanner: 192.168.0.10. 
 * The laser scanner and the host PC have to be in the same IP subnet.
```



The IP address of the scanner can also be changed afterwards. See next
chapter.

- The safety laser scanner is displayed in the work window with IP
  address, firmware version and status information.

#### Change the network IP address of the PSENscan laser scanner

- Select **Settings \&rightarrow; Change network settings**.

![Netw1](doc/Change_Network_Settings_1.png)

- Enter the password for the safety laser scanner

![Passwd](doc/Enter_PSENSCAN_PWD.png)

- You can find the password in the operating manual.
- Enter the network data for connecting to the network.

![IP](doc/Enter_PSENSCAN_IP.png)

- Click **OK** to continue.
- Finally the PSENscan safety laser scanner is displayed automatically
  with an updated IP address in the PSENscan Configurator.

![IPCHGRESULT](doc/Result_PSENSCAN_IP_Change.png)



```wiki

 * Alternatively you can change the IP address of your computer with the windows network settings.
```



#### Create a new configuration

To get raw non-safety-relevant scanner data in ROS, you still need to
setup at least one safety zone. The safety configuration is not visible
from ROS later on, but directly triggers the OSSD safety outputs of the
scanner to stop motion.

- Click at the home button in the upper left corner.

![attachment:Home.png](doc/Home.png)

- Click on **Create new configuration**.

![NEWCFG](doc/Create_NEW_PSENSCAN_config.png)

- Double click your product to proceed. You find the product id printed
  at side of the device.

![attachment:Catalogue.png](doc/Catalogue.png)

- Press the NEXT button on the upper right corner.

![attachment:PSENSCAN_next_button.png](doc/PSENSCAN_next_button.png)

- In the general properties tab choose the right number of pins for the
  power supply and evaluation device connection. It might be 8-pin or
  12-pin. You can count the pins at your connector \[2\] or \[1\] as
  shown in
  [Connect the hardware](#connect-the-hardware).

<!-- -->

- Choose a name for your configuration.

<!-- -->

- Press next until the configure zones dialog appears.

![attachment:Configure_PSENSCAN_Zones.png](doc/Configure_PSENSCAN_Zones.png)

- Configure a smaller safety zone and a larger warning zone. Use the
  right mouse button on the coordinate system to choose between safety
  zone and warning zone.

![attachment:Configure_PSENSCAN_Safety_and_warning_Zones.png](doc/Configure_PSENSCAN_Safety_and_warning_Zones.png)

- Click next and choose your scanner.
- Press next until the **Programming** dialog appears and press the
  button **Load**.
- After you pressed **Load** your configuration will be tested. There
  may occur several dialogs. Press **OK** on them until you are asked
  for a password. Use the same password like in the previous chapter.

<!-- -->

- Again answer the following dialogs with **OK** until the download
  dialog appears.

![DOWNLOAD](doc/Download_PSENSCAN_FIRMWARE.png)

- After the download is finished you will be asked for accepting or
  rejecting the new configuration. Press **Accept** button to proceed.

<!-- -->

- The finish dialog appears. Wait until the scanner has rebooted.

![FINISHED](doc/Config_PSENSCAN_finished.png)

- Press on **Monitoring** to display the 2d surroundings of the scanner.

![FINISHED](doc/Monitoring_PSENSCAB_TAB.png)

### How to proceed

From this point, you can connect your PSENscan to a machine running
Linux and proceed with the
[ROS package setup](#how-to-set-up-ros-to-communicate-with-the-scanner).

## How to set up ROS to communicate with the scanner

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [How to set up a Pilz PSENscan laser scanner with Ethernet](#how-to-set-up-a-pilz-psenscan-laser-scanner-with-ethernet).
- **Description:** You learn how to set up the PILZ laser scanner with
  ROS and show the result in Rviz.
- **Keywords:** PSENscan, psen_scan, psen_scan_v2
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Launching multiple scanners](#launching-multiple-scanners)



```wiki
'''WARNING'''

THE PILZ SOFTWARE IS PROVIDED AS-IS AND WITH NO WARRANTY (FOR MORE DETAILS SEE LICENSE).
```



### Introduction

This tutorial teaches you to set up and launch the ROS driver for the
PSENscan laser scanner. This includes creating a new ROS package to read
and display laser scanner data.

### Prerequisites



```
{#!wiki version melodic noetic

In order to complete this tutorial, you need the following:

{{{#!wiki version melodic

 * A workstation or a [[https://en.wikipedia.org/wiki/Virtual_machine|Virtual machine]] with [[http://releases.ubuntu.com/releases/18.04/|Ubuntu 18.04 LTS]] and [[http://wiki.ros.org/melodic|ROS melodic]] installed.
```





```wiki

 * A workstation or a [[https://en.wikipedia.org/wiki/Virtual_machine|Virtual machine]] with [[http://releases.ubuntu.com/releases/20.04/|Ubuntu 20.04 LTS]] and [[http://wiki.ros.org/noetic|ROS noetic]] installed.
```



- Completed the first ROS tutorial
  [create a catkin workspace](https://index.ros.org/p/catkin).
- An operable catkin workspace.
- An installed psen_scan_v2 package.



```
sudo apt update
sudo apt install ros-$ROS_DISTRO-psen-scan-v2
```



### Create a ROS package with the required files

Install the psen_scan_v2 package as in the previous tutorials described.

In your workspace, create a new package: 

```
cd ~/catkin_ws/src
catkin_create_pkg --rosdistro $ROS_DISTRO psen_scan_v2_tutorials psen_scan_v2
cd psen_scan_v2_tutorials
mkdir config
gedit config/scanner_config.yaml
```



Copy the following content and paste it into gedit. Do not forget to
save the new created file.

Source:
[scanner_config.yaml](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/config/scanner_config.yaml)



```yaml
sensor_ip: "192.168.0.10"    # Insert the IP of the laser scanner here.
## The following parameters are optional:
tf_prefix: laser_1           # This name is prefixed to the TF, where the scanner is mounted
angle_start: deg(-137.4)     # The angle of the first measurement
angle_end: deg(137.4)        # The angle of the last measurement
intensities: false           # Receive intensity values
resolution: deg(0.1)         # Scan resolution
host_ip: "auto"              # Change the IP to the IP of your PC.
host_udp_port_control: 55115 # The port on your pc used to start/stop the scanner
host_udp_port_data: 55116    # The port on your pc where the data is received
fragmented_scans: false      # Receive fragmented scans a.s.a.p. instead of full scan
```



Like in the last step create the file
`psen_scan_tutorials/launch/psen_scan_v2.launch` with the following
content by using gedit:



```
mkdir launch
gedit launch/psen_scan_v2.launch
```



Source:
[psen_scan_v2.launch](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/launch/psen_scan_v2.launch)



```xml
<?xml version="1.0"?>
<launch>
  <include file="$(find psen_scan_v2)/launch/bringup.launch" />
  <rosparam ns="laser_1" command="load" file="$(find psen_scan_v2_tutorials)/config/scanner_config.yaml" />

  <param name="robot_description"
         command="$(find xacro)/xacro '$(find psen_scan_v2_tutorials)/urdf/example.urdf.xacro'" />
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />

  <node name="$(anon rviz)" type="rviz" pkg="rviz"
        args="-d $(find psen_scan_v2)/config/config.rviz" />
</launch>
```



The code explained:



```xml
  <include file="$(find psen_scan_v2)/launch/bringup.launch" />
  <rosparam ns="laser_1" command="load" file="$(find psen_scan_v2_tutorials)/config/scanner_config.yaml" />
```



This starts the psen_scan_v2_node and loads the newly created config
file.

\



```xml
  <param name="robot_description"
         command="$(find xacro)/xacro '$(find psen_scan_v2_tutorials)/urdf/example.urdf.xacro'" />
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />
```



This loads the robot model from an `urdf.xacro`-file. It contains
geometric information of the scanner and TF frames.

\


```xml
  <node name="$(anon rviz)" type="rviz" pkg="rviz"
        args="-d $(find psen_scan_v2)/config/config.rviz" />
```



This starts rviz with a predefined configuration.

\

You need to additionally create the aforementioned `urdf.xacro`-file.



```
mkdir urdf
gedit urdf/example.urdf.xacro
```



This will later contain a description of your whole robot. For now it
only contains the one laser scanner. Which is created from the
`xacro:psen_scan` macro after this was included:



```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://ros.org/wiki/xacro" name="psen_scan">
   <xacro:include filename="$(find psen_scan_v2)/urdf/psen_scan.urdf.xacro" />
   <xacro:psen_scan prefix="laser_1" />
</robot>
```



### Required parameters

To launch the ROS driver, only one parameter is mandatory:

- **sensor_ip**

The IP of the laser scanner in the network. You have configured this in
the first tutorial using the configuration tool.

For an overview of all parameters, please visit
<https://github.com/PilzDE/psen_scan_v2/blob/main/README.md#usage>

### Start the PSENscan application

Now you can launch your newly created launchfile with the following
command: 

```
roslaunch psen_scan_v2_tutorials psen_scan_v2.launch
```





```wiki
 * Make sure your PC operates in the same IP subnet like the laser scanner.
 * Make sure to set the IP addresses according the parameters above. The previous tutorial showed how these could be altered.
```



This should launch rviz and look something like this:

![width=400](doc/rviz2.png)

The red lines show the detected surroundings of the scanner.

For comparison in reality the scanner was placed in an arrangement more
or less like this:

![width=400](doc/reality2.png)

Whatever your setup is, it should be comparable with the actual
environment of the scanner. The red x-axis in the rviz window can be
imagined as pointing out of the scanner in the direction of the display
in its front.

}}}}

### Conclusion

In this tutorial you created a basis for an application using the
PSENscan laser scanner together with ROS. In the next tutorial you learn
[how to connect to multiple scanners](#launching-multiple-scanners).

## Launching multiple scanners

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [How to set up a Pilz PSENscan laser scanner with Ethernet](#how-to-set-up-a-pilz-psenscan-laser-scanner-with-ethernet),
  [How to set up ROS to communicate with the scanner](#how-to-set-up-ros-to-communicate-with-the-scanner).
- **Description:** This tutorial explains how to use multiple scanners.
- **Keywords:** PSENscan, psen_scan, psen_scan_v2
- **Tutorial Level:** BEGINNER

### Introduction

This part will teach you how to start multiple scanners in master mode
with a single launchfile, by showing an example of how to launch two
scanners simultaneously.

### Prerequisites



```wiki
 Make sure to complete the preceding [[psen_scan_v2/Tutorials|tutorials]] successfully!
```



![attachment:Multiple_Scanners_Tutorial_Architecture.png](doc/Multiple_Scanners_Tutorial_Architecture.png)

Setup an architecture similar to that one shown in the picture above.

### Creating the config files

Navigate to your config folder:



```
roscd psen_scan_v2_tutorials/config
```

 We will reuse the first config-file from the
[previous tutorial](#how-to-set-up-ros-to-communicate-with-the-scanner)
and create a second config-file:



```
gedit scanner2_config.yaml
```

 Fill the yaml-file with key: value pairs that
match the parameters you would like to store. Here is an example:

Source:
[scanner2_config.yaml](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/config/scanner2_config.yaml)



```yaml
sensor_ip: "192.168.0.20"    # IP address of the laser scanner
tf_prefix: laser_2           # This name is prefixed to the TF, where the scanner is mounted
host_udp_port_control: 50505 # Make sure to use different ports than in the first scanner config.
host_udp_port_data: 50506
## The following parameters are optional
angle_start: deg(-137.4)     # The angle of the first measurement
angle_end: deg(137.4)        # The angle of the last measurement
intensities: false           # Receive intensity values
resolution: deg(0.1)         # Scan resolution
host_ip: "auto"              # Change the IP to the IP of your PC.
fragmented_scans: false      # Receive fragmented scans a.s.a.p. instead of full scan
```





```wiki
'''Note:''' You cannot assign adjacent IP addresses to different laser scanners, e.g. 192.168.0.10 and
192.168.0.11, because a single scanner takes up two IP-Adresses.
```

 

```wiki
'''Note:''' If all your scanners send data to the same host, they have to send to different ''host_udp_ports'' to avoid conflicts.
```




```wiki
'''Note:''' You need to choose unique ''names'' for each scanner to be able to position them
independently from one another inside your ROS environment.
```



### Creating the launch file

Create a new launch file inside your launch directory



```
roscd psen_scan_v2_tutorials/launch
gedit two_scanners.launch
```

 Here is an example launch file:

Source:
[two_scanners.launch](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/launch/two_scanners.launch)



```xml
<?xml version="1.0"?>

<launch>
  <include file="$(find psen_scan_v2)/launch/bringup.launch">
    <arg name="tf_prefix" value="laser_1" />
  </include>
  <rosparam ns="laser_1" command="load" file="$(find psen_scan_v2_tutorials)/config/scanner_config.yaml" />

  <include file="$(find psen_scan_v2)/launch/bringup.launch">
    <arg name="tf_prefix" value="laser_2" />
  </include>
  <rosparam ns="laser_2" command="load" file="$(find psen_scan_v2_tutorials)/config/scanner2_config.yaml" />

  <param name="robot_description"
         command="$(find xacro)/xacro '$(find psen_scan_v2_tutorials)/urdf/two_scanners.urdf.xacro'" />
  <node name="robot_state_publisher" pkg="robot_state_publisher"
        type="robot_state_publisher" />

  <node name="$(anon rviz)" type="rviz" pkg="rviz"
        args="-d $(find psen_scan_v2)/config/config.rviz" />
</launch>
```





```wiki
'''Note:''' The configuration has to be loaded into the node's namespaces. The node names are given by the ''name'' argument.
```



In this launch file we start two laser scanner nodes. Each node
publishes the data of the respective scanner on a separate topic.

### Creating the urdf.xacro file

Create a xacro file



```
roscd ../urdf
gedit two_scanners.urdf.xacro
```

 Here is an example launch file:

Source:
[two_scanners.urdf.xacro](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/urdf/two_scanners.urdf.xacro)



```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://ros.org/wiki/xacro" name="psen_scan">
  <xacro:include filename="$(find psen_scan_v2)/urdf/psen_scan.urdf.xacro" />
  <link name="base_link"/>

  <joint name="laser_1_base_link_joint" type="fixed">
    <parent link="base_link" />
    <child link="laser_1_mount_link" />
    <origin rpy="0 0 ${-pi/2}" xyz="0 -1 0"/>
  </joint>
  <xacro:psen_scan prefix="laser_1" />

  <joint name="laser_2_base_link_joint" type="fixed">
    <parent link="base_link" />
    <child link="laser_2_mount_link" />
    <origin rpy="0 0 ${pi/2}" xyz="0 1 0"/>
  </joint>
  <xacro:psen_scan prefix="laser_2" />
</robot>
```



This is the file, that will in future describe the full robot. Now it
contains the following aspects:

\

Source:
[two_scanners.urdf.xacro](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/urdf/two_scanners.urdf.xacro)



```xml
  <xacro:include filename="$(find psen_scan_v2)/urdf/psen_scan.urdf.xacro" />
  <link name="base_link"/>
```

 Imports our psen_scan macro and introduces a
`base_link`. This will later be the main coordinate frame of your
robot.

\

Source:
[two_scanners.urdf.xacro](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/urdf/two_scanners.urdf.xacro)



```xml
  <joint name="laser_1_base_link_joint" type="fixed">
    <parent link="base_link" />
    <child link="laser_1_mount_link" />
    <origin rpy="0 0 ${-pi/2}" xyz="0 -1 0"/>
  </joint>
  <xacro:psen_scan prefix="laser_1" />
```

 Uses the previously imported macro to create a
scanner instance and a joint to define its relation to the `base_link`
coordinate frame.

\

Source:
[two_scanners.urdf.xacro](https://github.com/PilzDE/pilz_tutorials/blob/master/psen_scan_v2_tutorials/urdf/two_scanners.urdf.xacro)



```xml
  <joint name="laser_2_base_link_joint" type="fixed">
    <parent link="base_link" />
    <child link="laser_2_mount_link" />
    <origin rpy="0 0 ${pi/2}" xyz="0 1 0"/>
  </joint>
  <xacro:psen_scan prefix="laser_2" />
```

 Same as above but for the second scanner.

\

### Start the application

Enter the following to start Rviz together with the ROS node for the
PSENscan application.



```
roslaunch psen_scan_v2_tutorials two_scanners.launch
```



- Rviz will only show a single scanner. To add a second scanner to the
  visualization you need to add a
  [LaserScan](https://index.ros.org/p/rviz) Object to Rviz and then
  choose "laser_2/scan" as it's topic.
- In the section **Global Options** in Rviz set **Fixed Frame** to
  **base_link**

![FINISHED](doc/Rviz_new_node_names.png)

### Conclusion

You are now able to launch multiple scanners in master mode at the same
time.
