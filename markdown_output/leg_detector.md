## The Leg Detector

This leg detector package takes
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)s
as input and uses a machine-learning-trained classifier to detect groups
of laser readings as possible legs. Sadly, the training dataset has been
lost to Willow Garage history (it wasn't even available before they
closed). The code is in the repository for retraining, but is
unsupported at this time.

This node will publish
[people_msgs/msg/PositionMeasurementArray](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurementArray.html)s
for the individual legs, and it can also attempt to pair the legs
together and publish their average as an estimate of where the center of
one person is as a
[people_msgs/msg/PositionMeasurement](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurement.html).
The node will also optionally publish visualization Marker messages to
indicate where detections happened.

### Possible Usages

There are two ways to use the leg_detector: seeded and unseeded. In the
unseeded mode, the only input is the received sensor data. This can
provide many false positives, but works in many scenarios.

In the seeded mode, the algorithm will use another source of
!PositionMeasurement messages to guide the algorithm to possible
locations for people. Historically, this has been used with a face
detection algorithm that alerts the leg_detector that there is probably
a pair of legs underneath. This mode is enabled using the `use_seeds`
parameter.

### leg_detector

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  The laser scan to detect from.
- `people_tracker_filter`
  ([people_msgs/msg/PositionMeasurement](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurement.html)):
  !PositionMeasurements to use as the seeds (see above)

#### Published Topics

- `leg_tracker_measurements`
  ([people_msgs/msg/PositionMeasurementArray](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurementArray.html)):
  Estimates of where legs are
- `people_tracker_measurements`
  ([people_msgs/msg/PositionMeasurementArray](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurementArray.html)):
  Estimates of where people are
- `visualization_marker`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  Markers where legs and people are

#### Parameters

- `use_seeds` (`boolean`, default: `false`): Whether or not to require
  additional seeds
- `connection_threshold` (`double`, default: `0.06`): Groups of
  connected laser reads must be within this many meters of each other to
  be considered a group
- `min_points_per_group` (`int`, default: `5`): Number of points
  required for a group of laser reads to be considered a group
- `leg_reliability_limit` (`double`, default: `0.7`): Only publishes
  legs with reliability higher than this limit
- `publish_legs` (`boolean`, default: `True`): Whether to publish
  leg_tracker_measurements
- `publish_people` (`boolean`, default: `True`): Whether to publish
  people_tracker_measurements
- `publish_leg_markers` (`boolean`, default: `True`): Whether to publish
  legs as visualization markers
- `publish_people_markers` (`boolean`, default: `True`): Whether to
  publish people as visualization markers
- `no_observation_timeout` (`double`, default: `0.5`): Forget a cluster
  after this many seconds
- `max_second_leg_age` (`double`, default: `2.0`): seconds
- `max_track_jump` (`double`, default: `1.0`): x
- `max_meas_jump` (`double`, default: `0.75`): x
- `leg_pair_separation` (`double`, default: `1.0`): Pairs of legs can be
  at most this far from each other
- `fixed_frame` (`string`, default: `odom_combined`): Topics are
  published relative to this frame
- `kalman_p` (`double`, default: `4`): Used to smooth measurements
- `kalman_q` (`double`, default: `.002`): Used to smooth measurements
- `kalman_r` (`double`, default: `10`): Used to smooth measurements
