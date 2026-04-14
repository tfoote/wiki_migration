Package ds_pr2_fridge_handle_detector makes use of torso-mounted Kinect
sensor on a PR2 robot and detects the pose of the center of the handle
of the refrigerator.

![](attachment:torso_kinect_handles.png)

# Usage:

## Start torso kinect:

```
roslaunch kinect_launch openni_node_kinect_torso_c2.launch (works for Bosch's PR2 robot, please change for your configuration accordingly)
```

## Start handle detector

```
roslaunch ds_pr2_fridge_handle_detector handle_detector.launch
```

The handles will be published on a topic:
\'\'\'drawer_handles_detector/handle_projected_inliers/output\'\'\'
which you can use for viewing in rviz.

The topic is fed directly to Perception3d.cpp of
[ias_drawer_executive](ias_drawer_executive) and used in the fridge
opening cycle.
