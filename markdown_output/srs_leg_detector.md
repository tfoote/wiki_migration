## About srs_human_sensing

SRS human sensing uses the laser range finders of the Care-O-bot to
locate a person arond the robot.

The results of the detection, i.e. the coordinates of the tracked people
are published to a topic,i.e **/tracked_people**

## Usage/Examples

To start the leg detector first make sure you have a source of laser
scans,e.g. a laser range finder or a bag file with suitable data and
then issue:

```
roslaunch srs_leg_detector srs_leg_detector_front.launch
```
