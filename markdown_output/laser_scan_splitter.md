![attachment:laser_scan_splitter.png](doc/laser_scan_splitter.png)

## Details

The laser_scan_splitter takes in a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
message and splits it into a number of other `LaserScan` messages.
Each of the resulting laser scans can be assigned an arbitrary
coordinate frame, and is published on a separate topic.

## Example

You can run the laser_scan_splitter
on a pre-recorded bag file that comes with the package. First, make sure
you have the [scan_tools](https://index.ros.org/p/scan_tools) stack
downloaded and installed by following the instructions
[here](https://index.ros.org/p/scan_tools).

Next, make sure you have the necessary tools installed:



```shell
rosmake rviz rosbag
```



Finally, run the demo:



```shell
roslaunch laser_scan_splitter demo.launch
```



You should see a result similar to the video below. The 3 laser scan
messages displayed in [rviz](https://index.ros.org/p/rviz) are obtained
by splitting the original scan.

[Youtube](https://www.youtube.com/watch?v=GTdiPjNym8k)

## Nodes & Nodelets

Two drivers are available: `laser_scan_splitter_node` and
`laser_scan_splitter_nodelet`. Their parameters and topics are
identical.

### laser_scan_splitter_node / laser_scan_splitter_nodelet

The `laser_scan_splitter_node` takes in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages, splits them, and outputs the resulting messages.

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Scans from a laser range-finder

#### Published Topics

- `~scan_[n]`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  An arbitrary number of topics containing the `LaserScan` segments.
  By default, the input beam is split in two, and `scan_1` and
  `scan_2` are published. The user can change the number of segments
  and their corresponding topic names using the parameters.

#### Parameters

- `~sizes` (`string`, default: `"256 256"`): the number of beams in
  each of the output scans. The string can contain an arbitrary number
  of sizes, but they must add up to the size of the input message. The
  default splits the laser scan into a left scan with 256 beams and a
  right scan with 256 beams.
- `~topics` (`string`, default: `"scan_1 scan_2"`): the published
  topic names. The topics are published private to the node. The string
  can contain an arbitrary number of topics, but note that the number of
  topics must match the number of sized and frames.
- `~frames` (`string`, default: `"laser laser"`): the frames in
  which the scans are published. The string can contain an arbitrary
  number of frames, but note that the number of frames must match the
  number of sized and topics.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/scan_tools/issues/) (requires
github account) or by emailing the maintainers.
