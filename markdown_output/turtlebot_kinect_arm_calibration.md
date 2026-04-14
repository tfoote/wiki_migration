## Documentation

Refer to the
[Tutorial](turtlebot_kinect_arm_calibration/Tutorials/CalibratingKinectToTurtleBotArm)
for instructions on how to calibrate a Kinect to the !TurtleBot arm.

## Video

[Youtube](https://www.youtube.com/watch?v=wB0v950Vciw)

## Files

`calibrate_turtlebot.launch` Calibrate a kinect on-board the !TurtleBot.

`calibration_old_kinect.launch` Calibrate an external kinect using the
diamondback-style OpenNI drivers.

`calibration_new_kinect.launch` Calibrate an external kinect using the
new electric-style OpenNI drivers.

## Nodes

```clearsilver
name = calibrate_kinect_checkerboard
desc = Detects a checkerboard in an image, and then waits for the user to move the arm to specified points on the checkerboard to determine the transform between the kinect and the robot
sub {
  0.name = /camera/rgb/image_mono
  0.type = sensor_msgs/image
  0.desc = Monochromatic image topic for the Kinect (this is used for detecting the checkerboard)

  1.name = /camera/rgb/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera info from Kinect.
}
pub {
  0.name = ~calibration_pattern_out
  0.type = sensor_msgs/Image
  0.desc = A color image with the detected calibration pattern and points on the image overlaid

  1.name = ~detector_cloud
  1.type = sensor_msgs/PointCloud2
  1.desc = (for debugging) A point cloud containing the corners of the checkerboard 

  2.name = ~physical_points
  2.type = sensor_msgs/PointCloud2
  2.desc = (for debugging) A point cloud containing the recorded positions of the gripper tip
}
param {
  0.name = ~fixed_frame
  0.type = string
  0.desc = Fixed frame to use in the calibration. The camera position will be calibrated to this frame.
  0.default = /base_link

  1.name = ~camera_frame
  1.type = string
  1.desc = Camera frame to use in the calibration. The final calibration will link this frame to the fixed_frame above. Note that this must be the '''parent''' of the camera TF tree.
  1.default = /camera_link

  2.name = ~target_frame
  2.type = string
  2.desc = Name of the TF frame to publish the position of the calibration pattern to
  2.default = /calibration_pattern

  3.name = ~tip_frame
  3.type = string
  3.desc = TF frame for the gripper link. The gripper tip offsets are based off this frame.
  3.default = /gripper_link

  5.name = ~checkerboard_width
  5.type = int
  5.desc = Width of the checkerboard. Note that this is the number of inside edges on the width, so this will generally be 1 less than the number of squares on the checkerboard.
  5.default = 6

  6.name = ~checkerboard_height
  6.type = int
  6.desc = Height of the checkerboard. Note that this is the number of inside edges on the height, so this will generally be 1 less than the number of squares on the checkerboard.
  6.default = 7

  7.name = ~checkerboard_grid
  7.type = double
  7.desc = Grid size of the checkerboard, in meters.
  7.default = 0.027

  8.name = ~gripper_tip_x
  8.type = double
  8.desc = x offset of the physical tip of the gripper from ~/tip_frame.
  8.default = -0.002

  9.name = ~gripper_tip_y
  9.type = double
  9.desc = y offset of the physical tip of the gripper from ~/tip_frame.
  9.default = -0.020

  10.name = ~gripper_tip_z
  10.type = double
  10.desc = z offset of the physical tip of the gripper from ~/tip_frame.
  10.default = -0.0185
}
req_tf {
  0.from = <fixed_frame>
  0.to   = <tip_frame>
  0.desc = Transform from the fixed frame used to the gripper tip link
}
prov_tf {
  0.from = <camera_frame>
  0.to   = <target_frame>
  0.desc = Transform from the camera frame to the calibration pattern
}
```
