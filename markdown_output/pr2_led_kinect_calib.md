Calibrating the kinect extrinsics vs. the right arm led (fuerte):

1\) Get the package from
<https://github.com/ruehr/pr2_led_kinect_calib.git> , put it into your
package path and compile it.

2\) Launch a roscore and the robot. roscore roslaunch
/etc/ros/robot.launch

3\) Launch the led controllers: roslaunch pr2_bringup_tests
gripper_led_on.launch

4\) Launch the kinect: roslaunch rgbd_assembler openni_node_new.launch

6\) Bring the right gripper led into the front of the robot, visible by
the kinect (e.g. manually via moving the arm while runstopped). The area
around the gripper led should be slightly pointing down towards the
robot so as to avoid specular reflections from ceiling lights e.g.. The
calibration will only work if the kinect sees the led go brighter when
switched on, this is not the case when the gripper is seen as saturated
white due to light reflections. Since the head moves a specular
reflection may occur during the calibration, in which case the user is
currently not warned. <attachment:pr2_led.jpg>

5\) Run the calibration: rosrun pr2_led_kinect_calib
calibration_executive

The calibration routine will look at the led in different angles by
moving the head. After some observations were made, a transform is
calculated, it's called "kinect post", for convenience the RPY angles
are also displayed. The longer the calibration runs the more point
correspondances it will collect, so make sure you give it a few minutes
if you want to get a good calibration. You can watch how the values
change and ctrl-c it once they have more or less settled.

Finally, put the values x,y,z and RPY into the URDF file like:

New pose of head_mount_kinect_ir_link in head_mount_link translation: x:
-0.0324269 y: 0.0276795 z: 0.0946061 rotation: x: 0.00300591 y:
-0.00650463 z: -0.00603443 w: 0.999956

RPY 0.0060906 -0.0129728 -0.0121087

<joint name="head_mount_kinect_ir_joint" type="fixed"> <origin
rpy="0.0060906 -0.0129728 -0.0121087" xyz="-0.0324269 0.0276795
.0946061"/> <parent link="head_mount_link"/> <child
link="head_mount_kinect_ir_link"/> </joint>
