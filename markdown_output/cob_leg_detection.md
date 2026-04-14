## Introduction

The cob_leg_detection package provides tracking mechanisms for detecting
people on the basis of trained data for a leg tracking process obtained
from the active scanner devices. This software is based on the
<http://wiki.ros.org/leg_detector> approach and implementation. It is
furthermore adapted to the Care-O-bot platform specifications and
visualization needs and is upgraded to the indigo release.

## Quick Start

To use the leg tracker function to detect and track people clone the
repository and required dependencies to your catkin environment and
build it according to the instructions. Run the launch file:

```
roslaunch cob_leg_detection leg_detector.launch
```

Please check the settings for a laser scanner data and its topic in the
`cob_leg_detection/launch/leg_detector.launch` file.

## Detailed Description

The leg detector obtains incoming messages from the laser scanner and
uses trained data to classify the groups of laser records as possible
legs. To visualize the tracking data for people and their legs, please
run Rviz and add a laser scanner plug-in.

### Detection

According to reliability of the derived information which is set due to
the parameters and configuration settings in `LegDetection.cfg` file
(e.g. the number of points in one group) the reliability of each leg is
set. If the two legs with the high reliability are found near to each
other and their leg pair separation satisfies the configuration
parameters (e.g. separation distance between two legs lies normally at
about 10 -- 50 cm), the new user will be detected and assigned a unique
user id. Each new user will be saved in a special list and the user data
(e.g. user position relative to a scanner frame, user velocity or user
legs position) will be transferred to a tracking filter.

### Tracking

The tracking filter is base on the Kalman Filter approach. It uses the
incoming data from the list of the detected people to keep tracking of
their estimate position state and the variance or the uncertainty of the
estimate. The filter is used to reduce the inaccuracies of the user
position obtained from the noisy input data of the laser scanner. If the
revised data satisfy the configuration parameters of the filter, the new
user data will be accordingly wrapped in a `cob_perception_msgs/People`
message and published on a /leg_detection/people topic. Otherwise the
detected user will be erased from the list and the user data will be
deleted from the published message. This will lead to a new tracking
process for the lost user where it gets a new user id.
