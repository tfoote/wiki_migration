`openni_tracker` is now a unary stack. Previously it was a package in
[openni_kinect](openni_kinect).

![](attachment:nite.png)

## How to Use

`rosrun openni_tracker openni_tracker` - Independent node that does
not require other nodes to run (however, make sure your `Kinect` is
powered. For example, on `Turtlebot`, `kinect.launch` needs to be
run successfully).

Once running, stand in front of the Kinect and surrender (i.e. hit the
[Psi Pose](http://3.bp.blogspot.com/-t9FxKt9JUts/TWfK4juSF7I/AAAAAAAABBI/36-uvouIG7I/s320/PsiPose.gif).
You should see some variation on the following messages.

```
New User 1
Pose Psi detected for user 1
Calibration started for user 1
Calibration complete, start tracking user 1
Lost User 1
```

The user's pose will be published as a set of transforms (`/tf`) with
the following frame names.

-   `/head`
-   `/neck`
-   `/torso`
-   `/left_shoulder`
-   `/left_elbow`
-   `/left_hand`
-   `/right_shoulder`
-   `/right_elbow`
-   `/right_hand`
-   `/left_hip`
-   `/left_knee`
-   `/left_foot`
-   `/right_hip`
-   `/right_knee`
-   `/right_foot`

```clearsilver
name = Topics and Parameters
param {
  0.name = camera_frame_id
  0.type = string
  0.desc = The name of the frame that all `/tf` transforms will use as a parent.
  0.default = openni_depth_frame
}
```
