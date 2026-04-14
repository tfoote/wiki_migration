## 3D Interaction Cursor plugin for Rviz

This plugin allows you to control a 3D cursor in Rviz. The cursor is
able to grab interactive markers and move them in much the same way as
you would with the mouse.

## How to Use Interactive Markers with 3D cursor

The 3D cursor emulates the behavior of a 2D mouse for the original
interactive marker types:

-   MENU/BUTTON: These act in the normal way.
-   MOVE_AXIS: Translates along specified axis only (same as mouse).
-   MOVE_PLANE: Translates perpendicular to specified axis only (same as
    mouse).
-   ROTATE_AXIS: Rotates about specified axis (same as mouse).
-   MOVE_ROTATE: Translates perpendicular to, and rotates about,
    specified axis only (same as mouse). In addition, the 3D cursor
    supports the following interactive marker types:
-   MOVE_3D: Free 3-DOF translation, with no rotation.
-   ROTATE_3D: Free 3-DOF rotation, with no translation.
-   MOVE_ROTATE_3D: Full 6-DOF translation and rotation. The 3D cursor
    and the grasped marker move as a single rigid body, maintaining the
    original transform between the two, until released.

## How to Run / Test

Install the following debs: ```
sudo apt-get install ros-groovy-rviz-animated-view-controller
```

Add the following repositories to your catkin workspace:
```
- git: {local-name: ros_3d_interaction_cursor, uri: 'https://github.com/aleeper/ros_3d_interaction_cursor.git'}
- git: {local-name: razer_hydra, uri: 'https://github.com/aleeper/razer_hydra.git'}
- git: {local-name: interactive_markers, uri: 'https://github.com/ros-visualization/interactive_markers.git'}
- git: {local-name: rviz, uri: 'https://github.com/ros-visualization/rviz.git'}
```

You may also need
\`https:*github.com/ros-visualization/visualization_tutorials\`, which
unfortunately must go in a rosbuild workspace.*

Build your catkin workspace, and build interactive_marker_tutorials.

If you haven\'t configured udev rules for the hydra before, do:
```
roscd razer_hydra
./configure_udev_rules
``` and then plug your hydra in.

Then run: ```
roslaunch interaction_cursor_demo demo.launch
``` You can add the option
start_hydra:=false, or change the radius of the hydra workspace with
radius:=\<a number\>.

### Controls

Using the \"right\" hydra controller, the buttons are:

-   \'\'\'rb\'\'\' - \"grab\" and move the workspace
-   \'\'\'rt\'\'\' - grab interactive marker controls
-   \'\'\'joystick click\'\'\' - bring up interactive marker menus
-   \'\'\'joystick directions\'\'\' - navigate interactive marker menus
-   \'\'\'3\'\'\' - Select the currently highlighted menu entry
-   \'\'\'1\'\'\' - Close the interactive marker menu

The \"left\" controller also works, but it is not able to grab and move
the workspace.

## Support

Please send bug reports, feature requests, etc. to the
[GitHub Issue Tracker](https://github.com/aleeper/ros_3d_interaction_cursor/issues).
