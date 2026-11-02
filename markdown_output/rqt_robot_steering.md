## Usage

![width=100%](doc/screenshot_rqt_robot_steering.png) This tool starts
publishing
[geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
message as soon as it's launched.

### Usage Example (with care-o-bot)

As noted, `rqt_robot_steering` publishes `geometry_msgs/Twist` as a
name of `/cmd_vel` by default. This name may vary per
robot/application; e.g. [Care-o-bot](Robots/Care-O-bot) also publishes
`geometry_msgs/Twist` but as `base_controller/command` (see
[cob_teleop](https://index.ros.org/p/cob_teleop). So, type that name
into the topic field at the top of `rqt_robot_steering` GUI and it
gets applied immediately.

To verify, use also [rqt_topic](https://index.ros.org/p/rqt_topic) (or
run from commandline `rostopic echo`) to see if the topics
`base_controller/command` are actually published.
