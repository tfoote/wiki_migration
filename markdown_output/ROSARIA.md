## Installation and Getting Started

Instructions on downloading, building and getting started with RosAria
is covered in
[/Tutorials/How to use ROSARIA](/Tutorials/How to use ROSARIA).

To build and install RosAria, first install the ARIA library from Adept
MobileRobots at <http://robots.mobilerobots.com/wiki/Aria>. (If no
longer available, a modified fork of ARIA is also available by cloning
or forking the git repository at
<http://github.com/reedhedges/AriaCoda>).

Then obtain the source code to RosAria from
<https://github.com/amor-ros-pkg/rosaria>, and build using catkin. See
[/Tutorials/How to use ROSARIA](/Tutorials/How to use ROSARIA) for full
instructions.

Video walkthroughs are available at
[/Tutorials/Video Walkthroughs](/Tutorials/Video Walkthroughs).

## Reporting bugs and making feature requests

Bugs and requests can be added and tracked here:
<https://github.com/amor-ros-pkg/rosaria/issues>

Development is discussed and planned via the
[ros-sig-pioneer group](sig/robots/Pioneer)

## ROS API

These topics are by default provided under a `/RosAria/` topic
namespace or prefix. You can remap these to different names if desired
(see [Names](Names), [Remapping Arguments](Remapping Arguments) and
[the <remap> tag for launch files](roslaunch/XML/remap) for
information).

ROS topics are channels by which other nodes can communicate with
ROSARIA by sending or reading messages. For more information on ROS
topics, see [Topics](Topics) and [rostopic](rostopic).

ROS services are channels by which other nodes can cause specific events
to occur on the robot via ROSARIA. For more information on services, see
[Services](Services) and [rosservice](rosservice).

Parameters are used to configure the behavior of the !RosAria node
during initial startup of the node, such as how to connect to the robot
controller. They may be set on the command line when running
[rosrun](rosrun) or in a launch file when using [roslaunch](roslaunch).
Parameters are stored by the ROS parameter server. See also
[Parameter Server](Parameter Server), [rosparam](rosparam),
[rosrun](rosrun) and [roslaunch](roslaunch).

Some parameters can also be dynamically changed using
[dynamic_reconfigure](dynamic_reconfigure).



```clearsilver
 name = RosAria
 desc = Simple node that uses ARIA to control the robot

sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = receives new velocity commands. Desired velocities are set in ARIA; the robot will achieve and maintain these velocities.  ARIA will continue to send the velocity commands to the robot controller, but if no `cmd_vel` messages are received after 600ms (configurable or disabled  via `cmd_vel_timeout` parameter, see below), rosaria will stop the robot.  So `cmd_vel` commands are only needed to change velocity, or to to reset the watchdog timeout.
}

pub {
  0.name = pose
  0.type = nav_msgs/Odometry
  0.desc = publishes odometry information (rate depends on the robot, normally 10Hz)
}

pub {
  1.name = bumper_state
  1.type = rosaria/BumperState
  1.desc = publishes bumper states (thanks to Arturo Ribes of the Spanish National Research Council)
}

pub {
  2.name = sonar
  2.type = sensor_msgs/PointCloud
  2.desc = publishes sonar readings (thanks to Michiel Blokzijl of the Imperial College London).  Readings are taken if there are subscribers on the topic. When the last subscriber unsubscribes from both this and `sonar_pointcloud2` topic, sonars are turned off.  Only available on robots with sonar.  The point cloud is two dimensional, and its coordinate frame matches the robot position. X and Y are points on the plane of the robot. Z data is always 0.
}

pub {
  3.name = sonar_pointcloud2
  3.type = sensor_msgs/PointCloud2
  3.desc = publishes sonar readings as `sensor_msgs/PointCloud2` type.  Readings are taken if there are subscribers on the topic. When the last subscriber unsubscribes from both this and `sonar` topic, sonars are turned off.  Only available on robots with sonar.  The point cloud is two dimensional, and its coordinate frame matches the robot position. X and Y are points on the plane of the robot. Z data is always 0.
}

pub {
  4.name = battery_state_of_charge
  4.type = std_msgs/Float32
  4.desc = Battery state-of-charge percentage, range (0.0, 1.0).  Only published if robot type supports state of charge (e.g. Pioneer LX, Seekur, Seekur Jr.)
}

pub {
  5.name = battery_voltage
  5.type = std_msgs/Float64
  5.desc = Battery voltage measurement (DC volts).
}

pub {
  6.name = battery_recharge_state
  6.type = std_msgs/Int8
  6.desc = Recharging status. Only published on Pioneer LX robot.  0 if not charging, > 0 if recharging, and < 0 on error or no data.
}

pub {
  7.name = motors_state
  7.type = std_msgs/Bool
  7.desc = Indicates whether the motors are enabled (true) or disabled (false).  (You can use the enable_motors and disable_motors services to enable/disable the motors.)
}

pub {
  8.name = <lasername>_pointcloud
  8.type = sensor_msgs/PointCloud
  8.desc = Only published if `publish_aria_lasers` parameter is `true`.  Provides laser data as a point cloud.  <lasername> will be ARIA's identifier for the laser.  May be repeated with different laser names if multiple lasers are configured in ARIA robot parameter file(s).
}

pub {
  9.name = <lasername>_laserscan
  9.type = sensor_msgs/LaserScan
  9.desc = Only published if `publish_aria_lasers` parameter is `true`.  Provides laser data as a laserscan type.  <lasername> will be ARIA's identifier for the laser.  May be repeated with different laser names if multiple lasers are configured in ARIA robot parameter file(s).
}


srv {
  0.name = enable_motors
  0.type = std_srvs/Empty
  0.desc = Enable the motors.  May be used to re-enable motors if automatically disabled by an event such as e-stop button or bumper hit.  ROSARIA initially enables the motors after connecting to the robot.  Some robots (Seekur, Seekur Jr.) also have a separate physical MOTORS switch that must also be turned on.
}

srv {
  1.name = disable_motors
  1.type = std_srvs/Empty
  1.desc = Disable motors. Depending on the robot this may just disable motion commands, or it may also switch off power to the motors.  Use the enable_motors service to re-enable them.
}

param {
  0.name = ~port
  0.type = string
  0.desc = Serial port device the robot is is connected to, or a hostname and TCP port separated by a colon to do TCP communications (e.g 10.0.126.32:8101).  Set to /dev/ttyS0 for onboard computers with direct serial connection via COM1 serial port .  Set to /dev/ttyUSBx for use with a USB-serial adapter, where x is the appropriate interface index. (Use /dev/ttyS0 with onboard computer as installed by AMR in normal configuration, except Pioneer LX, which uses /dev/ttyUSB0)
  0.default = /dev/ttyUSB0
}

param {
  1.name = ~baud
  1.type = int
  1.desc = Explicit serial Baud rate.   All robots should use 9600 (unless explicitly set in firmware configuration) except Pioneer LX which uses 57600.  ARIA may switch to a higher baud rate if possible after connecting.
  1.default = Use ARIA default (internal defaults, `/etc/Aria.args file` if present, and `ARIAARGS` environment variable if set)
}

param {
  2.name = ~debug_aria
  2.type = bool
  2.desc = If given, ARIA logging is set to Verbose level, ARIA log output is redirected to a file (see ~aria_log_filename), and additional robot-communications logging is turned on (Note, this will generate lots of data, >100 log messages per second)
  2.default = false
}

param {
  3.name = ~aria_log_filename
  3.type = string
  3.desc = ARIA log file if ~debug_aria is set to true. Unused if ~debug_aria is set to false.
  3.default = Aria.log
}



param {
  5.name = ~publish_aria_lasers
  5.type = bool
  5.default = false
  5.desc = If `true`, then RosAria will use ARIA to connect to any lasers configured in [ARIA robot parameter files|http://robots.mobilerobots.com/wiki/ARIA_and_ARNL_Robot_Parameters] and publish two topics for each laser: one with PointCloud data, the other with LaserScan data (see above).  The topics will be named based on ARIA identifiers. (E.g. for a `p3dx-sh-lms1xx` robot with an LMS100 configured as Laser 1 in the ARIA robot parameter file (`p3dx-sh-lms1xx.p`), the topics `lms1XX_1_pointcloud` and `lms1XX_1_laserscan` will be published.)  See also http://robots.mobilerobots.com/wiki/How_ARIA_Connects_To_Lasers.  This feature is disabled by default. If not using this feature, use separate ROS nodes to provide laser data. 
}

param {
  6.name = trans_accel
  6.type = float
  6.desc = Set desired translation acceleration in m/s/s. May be set via dynamic_reconfigure
  6.default = none, use robot controller firmware configuration
}

param {
  7.name = trans_decel
  7.type = float
  7.desc = Set desired translation deceleration in m/s/s. May be set via dynamic_reconfigure
  7.default = none, use robot controller firmware configuration
}

param {
  8.name = rot_accel
  8.type = float
  8.desc = Set desired rotation acceleration in rad/s/s. May be set via dynamic_reconfigure
  8.default = none, use robot controller firmware configuration
}

param {
  9.name = rot_decel
  9.type = float
  9.desc = Set desired rotation acceleration in rad/s/s. May be set via dynamic_reconfigure
  9.default = none, use robot controller firmware configuration
}

param {
  10.name = lat_accel
  10.type = float
  10.desc = Set desired lateral (sideways) acceleration (applies to Seekur only) in m/s/s. May be set via dynamic_reconfigure
  10.default = none, use robot controller firmware configuration
}

param {
  11.name = lat_decel
  11.type = float
  11.desc = Set desired lateral (sideways) deceleration (applies to Seekur only) in m/s/s. Maybe set via dynamic_reconfigure
  11.default = none, use robot controller firmware configuration
}

param {
  12.name = TicksMM
  12.type = float
  12.desc = Change TicksMM odometry calibration parameter. See robot manual for information. Only available on robots with tunable odometry calibration (Pioneer 3, PeopleBot, PowerBot, AmigoBot).
  12.default = none, use robot controller firmware configuration
}

param {
  13.name = DriftFactor
  13.type = float
  13.desc = Change DriftFactor odometry calibration parameter. See robot manual for information. Only available on robots with tunable odometry calibration (Pioneer 3, PeopleBot, PowerBot, AmigoBot).
  13.default = none, use robot controller firmware configuration
}

param {
  14.name = RevCount
  14.type = float
  14.desc = Change RevCount odometry calibration parameter. See robot manual for information. Only available on robots with tunable odometry calibration (Pioneer 3, PeopleBot, PowerBot, AmigoBot).
  14.default = none, use robot controller firmware configuration
}

param {
  15.name = cmd_vel_timeout
  15.type = float
  15.default = 0.6 sec
  15.desc = If no `cmd_vel` command messages are received within this timeout period (in seconds), rosaria will command the robot to stop.   If 0, this behavior is disabled and the robot will continue to use the last commanded velocity until a new `cmd_vel` command is received.  Note that this is separate from the robot controller's own watchdog timeout, which protects against loss of communication between rosaria node and the robot controller.
}

param {
 16.name = odom_frame
 16.type = string
 16.default = odom
 16.desc = Name to use to publish robot odometric pose estimate origin tf. 
}

param {
 17.name = base_link_frame
 17.type = string
 17.default = base_link
 17.desc = Name to use to publish base_link tf. 
}

param {
 18.name = bumpers_frame
 18.type = string
 18.default = bumpers
 18.desc = Name to use to publish tf associated with bumper sensor data. 
}

param {
 19.name = sonar_frame
 19.type = string
 19.default = sonar
 19.desc = Name to use to publish tf associate with sonar sensor data. 
}
```



## Examples

-   Video Walkthroughs including how to build and run some example
    client programs are available at
    [/Tutorials/Video Walkthroughs](/Tutorials/Video Walkthroughs)
-   Examples that use RosAria to teleoperate a Pioneer from mobile
    phones are available at
    [/Tutorials/iPhone Teleop With ROSARIA](/Tutorials/iPhone Teleop With ROSARIA)
    and
    [/Tutorials/Android teleop Pioneer 3at](/Tutorials/Android teleop Pioneer 3at)
