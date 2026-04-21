## The Leg Detector

This leg detector package takes <<MsgLink(sensor_msgs/LaserScan)>>s
as input and uses a machine-learning-trained classifier to detect groups
of laser readings as possible legs. Sadly, the training dataset has been
lost to Willow Garage history (it wasn't even available before they
closed). The code is in the repository for retraining, but is
unsupported at this time.

This node will publish
<<MsgLink(people_msgs/PositionMeasurementArray)>>s for the
individual legs, and it can also attempt to pair the legs together and
publish their average as an estimate of where the center of one person
is as a <<MsgLink(people_msgs/PositionMeasurement)>>. The node will
also optionally publish visualization Marker messages to indicate where
detections happened.

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



```clearsilver
name = leg_detector
desc = 
sub { 
  0.name = scan
  0.type = sensor_msgs/LaserScan
  0.desc = The laser scan to detect from. 
  1.name = people_tracker_filter
  1.type = people_msgs/PositionMeasurement
  1.desc = !PositionMeasurements to use as the seeds (see above)
}
pub {
  0.name = leg_tracker_measurements
  0.type = people_msgs/PositionMeasurementArray
  0.desc = Estimates of where legs are
  1.name = people_tracker_measurements
  1.type = people_msgs/PositionMeasurementArray
  1.desc = Estimates of where people are
  2.name = visualization_marker
  2.type = visualization_msgs/Marker
  2.desc = Markers where legs and people are
}
param { 
  0.name = use_seeds
  0.type = boolean
  0.desc = Whether or not to require additional seeds
  0.default = false
  1.name = connection_threshold
  1.type = double
  1.desc = Groups of connected laser reads must be within this many meters of each other to be considered a group
  1.default = 0.06
  2.name = min_points_per_group
  2.type = int
  2.desc = Number of points required for a group of laser reads to be considered a group
  2.default = 5
  3.name = leg_reliability_limit
  3.type = double 
  3.desc = Only publishes legs with reliability higher than this limit
  3.default = 0.7
  4.name = publish_legs
  4.type = boolean
  4.desc = Whether to publish leg_tracker_measurements
  4.default = True
  5.name = publish_people
  5.type = boolean
  5.desc = Whether to publish people_tracker_measurements
  5.default = True
  6.name = publish_leg_markers
  6.type = boolean
  6.desc = Whether to publish legs as visualization markers
  6.default = True
  7.name = publish_people_markers
  7.type = boolean
  7.desc = Whether to publish people as visualization markers
  7.default = True
  8.name = no_observation_timeout
  8.type = double
  8.desc = Forget a cluster after this many seconds
  8.default = 0.5
  9.name = max_second_leg_age
  9.type = double
  9.desc = seconds
  9.default = 2.0
  10.name = max_track_jump
  10.type = double
  10.desc = x
  10.default = 1.0
  11.name = max_meas_jump
  11.type = double
  11.desc = x
  11.default = 0.75
  12.name = leg_pair_separation
  12.type = double
  12.desc = Pairs of legs can be at most this far from each other
  12.default = 1.0
  13.name = fixed_frame
  13.type = string
  13.desc = Topics are published relative to this frame
  13.default = odom_combined
  14.name = kalman_p
  14.type = double
  14.desc = Used to smooth measurements
  14.default = 4
  15.name = kalman_q
  15.type =double
  15.desc =  Used to smooth measurements
  15.default =.002
  16.name = kalman_r
  16.type = double
  16.desc =Used to smooth measurements
  16.default = 10
}
```


