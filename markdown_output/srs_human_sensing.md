Srs_human_sensing is a package for detection and tracking people in
vicinity of the robot. It is relying on information from the safety
laser scanners and the depth information sensor, i.e. Kinect sensor.
Additionally the srs_human_sensing module positions/rotates the robot in
a best way to confirm or reject human detection hypotheses generated
from the leg detection.

## Installation

The following modules have to be downloaded, their dependancis have to
be resolved, and finally they have to be compiled (rosmake \....)

-   srs_leg_detector
-   srs_human_sensing
-   cob_people_perception

## Usage

The sequence of starting commands for a test under simulation is as
follows:

-   roslaunch srs_scenarios srs_scenario_sim.launch
-   roslaunch srs_leg_detector srs_leg_detector_front.launch
-   rosrun srs_human_sensing fake_people_detection.py
-   rosrun srs_human_sensing hs.py
-   rosrun srs_body_detector srs_body_detector
-   rosrun srs_human_sensing sm_human_test.py

## Output

The output of human sensing is used in UI_PRI and UI_PRO through the
topics listed below.

-   /tracked_people
-   /people_detections_cloud
-   /people_tracker_filter
