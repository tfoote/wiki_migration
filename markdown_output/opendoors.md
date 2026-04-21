

```wiki
/!\ Work in progress.
```



### Action API

The opendoors node provides an implementation of a `SimpleAcionServer`
(see [ actionlib documentation](actionlib )), that take in goals
containing `opendoors/GraspHandleGoal` messages. You can communicate
with the `move_arm` node over ROS directly, but the recommended way to
send goals to `move_arm` if you care about tracking their status is by
using the `SimpleActionClient`. Please see
[ actionlib documentation](actionlib ) for more information.

## Downloading

The opendoors package is a part of the [mit-ros-pkg](mit-ros-pkg)
repository. To download the most recent version of the stack without
downloading the whole repository use 

```
svn co `roslocate svn opendoors`
```



## Tutorials

The tutorials for this package are in the
[GraspHandleAction tutorial](opendoors/Tutorials)

## Videos

[Youtube](https://www.youtube.com/watch?v= QBLN7bywr_k)

In this video, the PR2 first finds the position the handle of the
cupboard by using point clouds from its laser scan. Then, it moves it
gripper 10cm away from where it thinks the cupboard handle is and opens
it gripper to prepare to grasp the handle. Then moves the arm 10cm
forward to get to the handle, where it finally closes the gripper.

[Youtube](https://www.youtube.com/watch?v= xdRunXqpQPE)

Here, PR2 is opening the cupboard door from a position where its right
elbow is to the right of the robot and its arm is bended.

[Youtube](https://www.youtube.com/watch?v= EXfgc5sM9x8)

Here, PR2 is opening the cupboard door from an initial arm configuration
in which PR2's shoulder joint is forced to move while bending the arm
to open door.

## Improvements

GraspAction is a simple action server that basically relies on move_arm
action service. In order to improve it to a complex action server that
people can use to open an cupboard, it is recommended that force
controller be used. One can use ee_cart_imped_action, which is a nicely
implemented force and torque controller for the arms of PR2. Secondly,
to make the action server robust a loop controller can be used. A simple
loop controller may adjust the force applied on PR2 arms based on the
position of the arms relative to the frame of the cupboard being opened.
For simple tracking purpose, tf package can be used. Thirdly, the
suggestions above can be made into an action server along with the
GraspHandle and tabletop_for_cupboard (object detection action that is
specifically designed to work with opening cupboards) action servers to
make one robust action service that works well with any type of cupboard
or doors.
