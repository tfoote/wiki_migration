## Launching Gripper Click Tool

The gripper click tool in this package is implemented as [rviz](rviz)
display. It will be integrated to the package
[pr2_gripper_click](pr2_gripper_click) in the future and will be started
as part of the
[pr2_interactive_manipulation](pr2_interactive_manipulation) package and
please refer to that package\'s document on how to start the entire
interactive manipulation pipeline then.

For now, please follow the steps as in below:

### On the robot

Start the following launch file: ```
roslaunch pr2_interactive_manipulation pr2_interactive_manipulation_robot.launch
```

### On the desktop

Run the grasp evaluation service node: ```
rosrun graspable_features grasp_evaluation_server
```

Start the following launch file: ```
roslaunch graspable_features pr2_interactive_manipulation_with_GripperClick_Voxelgrid_desktop.launch
```

Note that this launch file will bring up rviz. The PR2 Interactive
Manipulation tools are implemented as
[rviz plugins](rviz/UserGuide#Plugins). In particular, you will see the
**Interactive manipulation** dialog pop up:

![](attachment:interactive_manip_screenshot.png)

The launch file above will also instantiate all the other rviz displays
that you need, although some of them will be disabled on launch.

## Using Gripper Click Tool

The display will not display anything unless called by the interactive
manipulation pipeline. An image from the narrow angle robot camera will
be shown if called. Points which doesn\'t have associated depth
information will be marked in light red, and those are not usable for
grasp selection.

### Grasping

You just need to select a location, which is supposed to be roughly the
location on the object to be grasped, and drag an arrow, denoting the
projection of the gripper\'s approaching direction on the image plane

-   left click on a non-red point on the image to select the gripper
    location
-   drag to choose the approaching direction (projected to the image
    plane) ![](attachment:gripper_click_voxelgrid1.png)

If you want to approach the object perpendicular to the image plane,

-   left click on a non-red point on the image to select the gripper
    location
-   double click to finish the selection

![](attachment:gripper_click_voxelgrid2.png)

Possible 6-d gripper poses based on the user\'s input will be sampled
and evaluated. Some gripper pose suggestions will be made based on the
evaluation results and the gripper will be shown on the interface.

-   middle click to switch to the next available pose suggestion

![](attachment:gripper_click_voxelgrid3.png)

### Placing

Since it\'s not integrated with [pr2_gripper_click](pr2_gripper_click)
yet, there\'s no placing functionality in this tool. Simply open the
gripper, object will fall out of the robot hand.

## ROS API

### API Stability

-   ROS API is UNREVIEWED and UNSTABKE

### Services Offered

```clearsilver
srv{
 no_header = True
 0.name = /grasp_evaluation_server_node/evaluate_grasp
 0.type = graspable_features/EvaluateGrasp
 0.desc = This service takes in a point cloud and a list of grasp poses, which will be evaluated on this point cloud. A list of scores will be returned. The score of a grasp represents the possibility that this grasp is likely to succeed. It has a range of [0, 1]. 
}
```

## Technical Details

Please refer to Emma Zhang\'s intern presentation for technical details.
You can read the slide either from this
[link](https://docs.google.com/a/willowgarage.com/viewer?a=v&pid=explorer&chrome=true&srcid=0B6b9ztPGybotMzk2MjM3YTctNDc2MS00MWE2LTlmMmUtMGI5ZjRkYWE4YmQz&hl=en)
or the incoming intern blog post on <http://www.willowgarage.com/blog>
