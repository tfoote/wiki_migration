# Dynamic Robot Butlering

## Authors: Tobias Kunz and Sachin Chitta

-   The dynamic robot butlering project intends to allow a robot to move
    a tray really fast while carrying an object on it, similar to what a
    butler carrying a tray would do. The resulting trajectories are
    available for playback on a PR2 robot.

```{=html}
<!-- -->
```
-   The play_trajectory package enables the playback of recorded
    trajectory messages that were sent to the joint trajectory
    controller for execution. Just resending the exact same message does
    not work because of timestamp and IDs inside the message. The
    \"play_trajecory\" node provided by this package listens on the
    \"/play_trajectory\" topic for replayed messages, converts them to
    the current time, and resends them as a new goal to the action
    server at \"/r_arm_controller/follow_joint_trajectory\".

```{=html}
<!-- -->
```
-   Use the instructions
    [here](http://kforge.ros.org/projects/tray_transfer/services/play_trajectory/)
    to get the package and make sure its in your ROS_PACKAGE_PATH.
    Compile the package using *rosmake play_trajectory*.

```{=html}
<!-- -->
```
-   The bag files in the \"trajectories\" folder contain trajectories
    for the right arm of the PR2 for quickly moving an object placed on
    a tray. For replaying those, follow these steps:
-   Have the right hand of the PR2 grasp the small calibration board of
    the PR2 on the non-slip tape.
-   Place an object in the center of the checkerboard pattern.
-   Start the \"play_trajectory\" node with \"rosrun play_trajectory
    play_trajectory\".
-   Play back one of the back by running \"rosbag play
    trajectories/\<file_name\>.bag -d 1\".

```{=html}
<!-- -->
```
-   The bag files contained in this package automatically play back on
    the \"/play_trajectory\" topic. If you record your own trajectories,
    you need to make sure to map the topic that they are played back on
    from \"/r_arm_controller/follow_joint_trajectory/goal\" to
    \"/play_trajectory\".
