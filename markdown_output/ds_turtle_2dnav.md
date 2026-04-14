# Description

This package provides an action server which translates semantic
positions to goal poses. The mappings are provided in a .yaml file that
is given to the action server a priori.

To run this package for the busbot: ```
roslaunch ds_turtle_2dnav drive_to_action_server.launch
``` This will
launch the /busbot_drive_to_action action server.
