![Caption of the feature_tracker in manual selection mode\|width=\"500\"](attachment:feature_tracker_img1.png)

## Detailled Description

The feature_tracker package is a versatile tool to detect and track
point features in a RGB-D video stream. The framework can be easily
modified to use different detection & tracking algorithms. The current
implementation uses Kanade-Lucas-Tomasi algorithm (opencv
implementation) to first detect corner features on the first frame and
then track them in consecutive frames. it maintains a constant number of
features by detecting new ones.

Detection and tracking use only RGB data and provide the coordinates in
image space. The 3-D Euclidean space coordinates corresponding to each
tracked feature is obtained from the registered depth channel.

The feature_tracker can define a ROI between a max and a min allowed
depth. It can also use an external mask that we use to define the area
of the image occluded by the robot (self-occlussion mask).
