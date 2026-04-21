## Package: psen_scan_v2

The **psen_scan_v2** package is a ROS integration driver for the
PSENscan safety laser scanner product. It lets you integrate the laser
scanner data into your ROS Environment easily. Using the standard
[sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html)
message format ensures compatibility with other
laserscan-post-processing nodes such as
[gmapping](http://wiki.ros.org/gmapping).

  -- --------- -- ----------------------------------------------------------------------------------------------------------- -- --------- --
     \<40%\>      ![PILZ safety laser scanner](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/PSENscan.jpg)      \<40%\>   
  -- --------- -- ----------------------------------------------------------------------------------------------------------- -- --------- --

**Common features:**

-   compliant and approved in accordance with (EN/IEC 61496-1: Type 3,
    EN ISO 13849-1: PL d, IEC 61508: SIL 2)
-   opening angle: 275°
-   operating range: 3.0 or 5.5 m safety zone
-   40 m warning zone, reaction time: 62 ms
-   Protection type: IP65
-   Dimensions (H x W x D) in mm: 152 x 102 x 112.5

**Light versions Additional features**:

-   Muting
-   EDM
-   Override

## Supported Devices

PSENscan firmware \>= 3.1.0 is supported on the following models:

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------- -- -------------------------- --
     \<24%\> **Type**                                                                                                                                                             **Features**                                                                                                                          \<10%\> **Order number**   
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
     **sensor_ip**      *string*      \"192.168.0.10\"      IP-Address of safety laser scanner.   
  -- --------------- -- ---------- -- ------------------ -- ------------------------------------- --

### Optional Parameters

  -- ----------------- -- ---------- -- ------------------------ -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Name**             **type**      \<20%\> **default**         **description**                                                                                                                                                                                   
     **tf_prefix**        *string*      \"laser_1\"                 Name of this scanner that can be changed to differentiate between multiple devices. By convention this is used as tf prefix.                                                                      
     **angle_start**      *double*      -2.398 (= -137.4 deg))      Start angle of measurement. (Radian)                                                                                                                                                              
     **angle_end**        *double*      2.398 (= 137.4 deg))        End angle of measurement. It is included in the measurements. (Radian)                                                                                                                            
     **intensities**      *bool*        false                       Publish intensities. If this is enabled, the resolution needs to be increased (at least 0.2 deg).                                                                                                 
     **resolution**       *double*      0.0017 (= 0.1 deg))         Scan angle resolution. (Radian) The value is rounded to a multiple of 0.1 deg and has to be in the range \[0.1, 10\] degrees.                                                                     
     **config_file**      *string*      \"\"                        Full path to a scanner config file. If a file is provided the configured zonesets and active zone markers are published, see [here](#Importing_the_zoneset_configuration) for more information.   
  -- ----------------- -- ---------- -- ------------------------ -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### Expert Parameters (optional)

  -- --------------------------- -- ---------- -- ------------- -- ------------------------------------------------------------------------------------ --
     **Name**                       **type**      **default**      **description**                                                                      
     **host_ip**                    *string*      \"auto\"         IP-Address of host machine. The IP of the local machine is used by default.          
     **host_udp_port_data**         *int*         55115            UDP Port on which monitoring frames (scans) should be received.                      
     **host_udp_port_control**      *int*         55116            UDP Port used to send commands (start/stop) and receive the corresponding replies.   
     **fragmented_scans**           *bool*        false            Publish scan data as soon as a UDP packet is ready, do not wait for a full scan.     
     **rviz**                       *bool*        true             Start a preconfigured rviz visualizing the scan data.                                
  -- --------------------------- -- ---------- -- ------------- -- ------------------------------------------------------------------------------------ --

### Published Topics

**/\<name\>/scan**
([sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html))

-   If *fragmented_scans* is set to false (default) the driver will
    publish complete scan rounds from the PSENscan safety laser scanner
    as a single message.
-   If *fragmented_scans* is enabled the driver will send the
    measurement data as soon as they arrive, instead of waiting for the
    scan round to be completed. This way the scan data is received
    sooner but is split into several sensor messages.

```wiki
'''Hint: 1: Scan rounds and fragments that contain no measurement data are not published. This can happen with smaller scan ranges.'''
```

```wiki
'''Hint: 2: Frequency of the laser scan messages is about 33hz for the combined and 200hz for the fragmented scans.'''
```

**/\<name\>/zoneconfiguration**
([psen_scan_v2/ZoneSetConfiguration](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/ZoneSetConfiguration.html))

```wiki
'''Hint: 1: Will not be advertised if no config_file is provided.'''
```

**/\<name\>/active_zoneset**
([std_msgs/UInt8](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/UInt8.html))

-   This topic contains the id of the currently active zoneset of the
    PSENscan safety laser scanner.

```wiki
'''Hint: 1: If no zonesets are configured the driver will publish "0" as default.'''
```

**/\<name\>/active_zoneset_markers**
([visualization_msgs/MarkerArray](http://docs.ros.org/en/noetic/api/visualization_msgs/html/msg/MarkerArray.html))

-   The markers published represent the currently active zoneset as
    triangle lists. They can be viewed e.g. in rviz.

```wiki
'''Hint: 1: Uses the topics /<name>/zoneconfiguration and /<name>/active_zoneset to calculate the vizualization and updates in the same frequency as those topics.'''
```

```wiki
'''Hint: 2: Will not be advertised if no config_file is provided.'''
```

**/\<name\>/io_states**
([psen_scan_v2/IOState](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/IOState.html))

-   The state published represents the current input and output state of
    the scanner IOs. A list of all available IOs can be found
    [here](#Transferred_IOs)

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
     \<40%\>      ![PILZ safety laser scanner frames\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/frames.png)      \<40%\>   
  -- --------- -- --------------------------------------------------------------------------------------------------------------------------- -- --------- --

### Defining the scan range

You can adjust the scan field to your needs by changing *angle_start*
and *angle_end*. The published
[sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html)
will only contain data within the given angle limits. Both limits are
defined within the *laser_1*frame as shown in the image below.

  -- --------- -- -------------------------------------------------------------------------------------------------------------------- -- --------- --
     \<40%\>      ![Limit visualization\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/angle_limits.png)      \<40%\>   
  -- --------- -- -------------------------------------------------------------------------------------------------------------------- -- --------- --

### Timestamp details

The timestamps of the scan data published are computed to be close to
reality and processing speed of incoming data was optimized to reduce
the time for the scan data to be published. This should suffice for
localization and slam algorithms. If you application benefits from
getting the scan data any sooner there are two possibilities:

-   Use fragmented scans. This will publish the individual frames
    received by the PSENscan safety laser scanner immediately instead of
    waiting for a scan round to be completed and combined to a single
    laser scan message.
-   Use the tcp_nodelay flag in your ROS subscriber. This will disable
    the nagle\'s algorithm, which is a TCP optimization. This algorithm
    can produce a jitter of about 20ms in the ros topic.
-   The cpp API of ROS does not support disabling this on the publisher
    side. If you don\'t have control over the subscriber e.g. due to
    using a third party package you can create a python node which acts
    as a repeater for the scan topic. rospy subscriber and publisher
    both allow setting this flag and thus can disable it for this driver
    and the third party package.

### Transferred IOs

The state of inputs and outputs of the PSENscan safety laser scanner are
published as
[psen_scan_v2/IOState](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/IOState.html).
The topic at **/\<name\>/io_states** is latched and always gives the
most recent pin state. On changes at the physical IOs, the changes are
logged to the console and the new state is published to the topic.

The
[input pin state](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/InputPinState.html)
contains information about

-   muting
-   override
-   zone set switching inputs

The
[output pin state](http://docs.ros.org/en/noetic/api/psen_scan_v2/html/msg/OutputPinState.html)
consists of

-   OSSD safety states
-   warning output
-   reference points violation

Please see the message descriptions for full lists of bits.

### Importing the zoneset configuration

Once you setup the scanner and created a configuration according to our
[tutorial](http://wiki.ros.org/psen_scan_v2/Tutorials/SettingUpPSENscanHW#Create_a_new_configuration)
you can use an exported xml configuration file within ROS. The
configured zonesets will be published.

The zonesets you created in the Pilz configurator:

  -- --------- -- ----------------------------------------------------------------------------------------------------------------------------------------- -- --------- --
     \<40%\>      ![configurator_screenshot\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/zones_screenshot_configurator.png)      \<40%\>   
  -- --------- -- ----------------------------------------------------------------------------------------------------------------------------------------- -- --------- --

will be exactly the same in ROS:

  -- --------- -- --------------------------------------------------------------------------------------------------------------------------------- -- --------- --
     \<40%\>      ![configurator_screenshot\|width=700](https://raw.githubusercontent.com/PilzDE/psen_scan_v2/main/img/zones_screenshot_rviz.png)      \<40%\>   
  -- --------- -- --------------------------------------------------------------------------------------------------------------------------------- -- --------- --

You can try this out with: ```wiki
'''Hint: 1: Scan rounds and fragments that contain no measurement data are not published. This can happen with smaller scan ranges.'''
```0

If you want to use the configuration node in your launchfile add a
section such as:

```wiki
'''Hint: 1: Scan rounds and fragments that contain no measurement data are not published. This can happen with smaller scan ranges.'''
```1

### Visualizing the active zoneset

For visualizing the active zoneset in RViz you can run the
**active_zoneset_node**. It will publish markers on the
**\<name\>/active_zoneset_markers** topic like shown in the RViz
screenshot above.

## Report a Bug

\<\<GitHubIssues(PilzDE/psen_scan_v2)\>\>

## Further information

You need further information? Our international hotline staff will
support you individually about our ROS packages at ros@pilz.de or visit
us at <https://pilz.com>.

Pilz is an international-scale, innovative automation technology
company. Pilz uses its solutions to create safety for man, machine and
the environment. In addition to the head office in Ostfildern near
Stuttgart, the family business is represented by over 2,400 employees at
42 subsidiaries and branches on all continents.

The company\'s products include sensor technology, electronic monitoring
relays, safety relays, configurable and programmable control systems,
automation solutions with motion control, systems for industrial
communication as well as visualization solutions and operator terminals.

Pilz solutions can be used in all areas of mechanical engineering,
including the packaging and automotive sector, plus the railway
technology, press and wind energy sectors. These solutions ensure that
baggage handling systems run safely at airports and funiculars or roller
coasters travel safely; they guarantee fire protection an energy supply
in buildings.
