![attachment:ncd_parser.png](doc/ncd_parser.png)

## Details

The ncd_parser package reads in .alog data
files from the New College Dataset and broadcasts the data in ROS. The
messages are broadcast in real time. Currently, the data extracted
includes the odometry of the robot and the readings from the left and
right SICK laser scanners. Additional transforms are provided between
the odometric frame and the two lasers, as described in the NCD paper.

To use the ncd_parser, you need to obtain an
.alog file from the New College Dataset
[website](http://www.robots.ox.ac.uk/NewCollegeData/).

## Example

You can run the ncd_parser on a small .alog
file included in the package for demo purposes. First, make sure you
have the [scan_tools](https://index.ros.org/p/scan_tools) stack
downloaded and installed by following the instructions
[here](https://index.ros.org/p/scan_tools).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz
```



Finally, run the demo:



```shell
roslaunch ncd_parser demo.launch
```



You should see a result similar to the video below.

[Youtube](https://www.youtube.com/watch?v=5Im-PNR_zI4)

## Nodes

### ncd_parser

The `ncd_parser` node treads in .alog data files from the New College
Dataset and broadcasts the data in ROS.

#### Published Topics

- `scan_left`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  The scan from the left SICK laser range-finder.
- `scan_right`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  The scan from the right SICK laser range-finder.

#### Parameters

- `start` (`double`, default: `0.0`): the start of the broadcast, in
  seconds. Messages in the .alog file prior to the start time are
  skipped.
- `end` (`double`, default: `-1.0`): the end of the broadcast, in
  seconds. Messages in the .alog file after to the end time are skipped.
  If set to `-1`, all messages in the file will be played.
- `rate` (`double`, default: `1.0`): the rate of publishing messages.
  `1.0` sets the rate to real-time.

#### Provided tf Transforms

- `map` → `odom`: the robot odometry reported in the .alog file
- `odom` → `laser_left`: pose of the left SICK laser in the robot frame
- `odom` → `laser_right`: pose of the right SICK laser in the robot
  frame

## Acknowledgements

`QuadTree_Alog.alog` used with the permission of Dr. Paul Newman,
Oxford University.

M. Smith, I. Baldwin, W. Churchill, R. Paul, and P. Newman, The new
college vision and laser data set, International Journal for Robotics
Research (IJRR), vol. 28, no. 5, pp. 595599, May 2009.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
