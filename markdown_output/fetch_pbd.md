This package is based on PR2 Programming by Demonstration. This version
is for the Fetch Robot. The github repo is found at
<https://github.com/fetchrobotics/fetch_pbd>

The original
[PR2 Programming by Demonstration](https://github.com/PR2/pr2_pbd) was
done by [Maya Cakmak](http://www.mayacakmak.com/) and the
[Human-Centered Robotics Lab](https://hcrlab.cs.washington.edu/) at the
University of Washington.

This PbD is designed for Ubuntu 14.04 and ROS Indigo.

Clone this repository and build on the robot:



```
$ cd ~/catkin_ws/src git clone https://github.com/fetchrobotics/fetch_pbd.git
$ cd ~/catkin_ws catkin_make
```

 To make sure all dependencies are installed:



```
$ cd ~/catkin_ws source ~/devel/setup.bash rosdep update rosdep install --from-paths src --ignore-src --rosdistro=indigo -y
```

 To make changes to the web interface, you will
want to install all of the web dependencies:



```
$ roscd fetch_pbd_interaction cd web_interface/fetch-pbd-gui
$ ./install_web_dependencies.sh
```

 Note that the above adds the following paths to
the end of your /.bashrc file:



```
$ export NVM_DIR="/home/USERNAME/.nvm" [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
# This loads nvm
```

 You will want to source your /.bashrc file
again before running the software. Now all of the dependencies are
installed. After you make changes to the web interface, to build you can
run:



```
$ roscd fetch_pbd_interaction cd web_interface/fetch-pbd-gui ./build_frontend.sh
```

 Now when you roslaunch this software it will
run using your newly built changes!



```
$ source ~/catkin_ws/devel/setup.bash roslaunch fetch_pbd_interaction pbd.launch
```

 You can run the backend without the "social
gaze" head movements or without the sounds by passing arguments to the
launch file:



```
$ source ~/catkin_ws/devel/setup.bash roslaunch fetch_pbd_interaction pbd.launch social_gaze:=false play_sound:=false
```

 You can also pass arguments to the launch file
to save your actions to a json file or load them from a json file. This
behaviour is a bit complicated. It is recommended that you specify the
full path to files or else it will look in your .ros folder. If you
specify a from_file then actions will be loaded from that file. They
will replace the ones in your session database. Whatever was in your
session database will get stored in a timestamped file in your .ros
folder (not overwritten). If you specify a to_file then the session you
are starting will be saved to that file.



```
$ source ~/catkin_ws/devel/setup.bash roslaunch fetch_pbd_interaction pbd.launch from_file:=/full/path/from.json to_file:=/full/path/to.json
```

 In your browser go to **ROBOT_HOSTNAME:8080**
in your browser to use the GUI. There is a "mobile" interface, which
is the same but without the visualization. This can be useful for just
saving/deleting primitives.

The main page lists all the available actions.

![Main Page\|width=100%](attachment:main_page.png)

You can directly run/copy/delete actions from the main page. Or hit the
"Edit" button to see more information on that action.

On the "Current Action" screen, most of the buttons are pretty
self-explanatory. You can execute the entire action using the "Run"
button at the bottom of the screen. This will execute all of the
primitives in the order they appear in the Primitive List. You can click
on a specific primitive (either the marker or the list item), to
highlight the primitive.

![Select\|width=100%](attachment:select.png)

You can show/hide the markers for each primitive by clicking the marker
icon for the primitive in the Primitive List.

![Show/Hide Marker\|width=100%](attachment:hide_marker.png)

You can change the order of the primitives by dragging them to a new
position in the list.

![Switch Order\|width=100%](attachment:switch_order.png)

You can edit the position and orientation of certain primitives by
clicking the edit icon or by moving the interactive marker.

![Edit\|width=100%](attachment:edit.png)

You can change the frame that certain primitives are relative to by
right-clicking the marker.

![Choose Target\|width=100%](attachment:choose_target.png)

You can also change the name of the action.

![Rename\|width=100%](attachment:rename.png)

You can record objects in the environment using the "Record Objects"
button. The objects will appear in the viewer. Poses can be relative to
these objects in the environment.

![Record Objects\|width=100%](attachment:record.png)

![Change Target\|width=100%](attachment:change_target.png)

You can now (optionally) run Fetch PbD with a grasp suggestion service.
This is a service that takes in a point cloud for an object and returns
a PoseArray of possible grasps for that object. Fetch Pbd provides
feedback by publishing which grasp was chosen by the user. Any service
that adheres to the .srv interface defined by
[SuggestGrasps.srv](https://github.com/GT-RAIL/rail_manipulation_msgs/blob/develop/srv/SuggestGrasps.srv)
and optionally the feedback .msg interface,
[GraspFeedback.msg](https://github.com/GT-RAIL/rail_manipulation_msgs/blob/develop/msg/GraspFeedback.msg),
can be used. If you want to start Fetch PbD with a grasp suggestion
service: 

```
$ source ~/catkin_ws/devel/setup.bash roslaunch fetch_pbd_interaction pbd.launch grasp_suggestion_service:=grasp_service_name grasp_feedback_topic:=grasp_feedback
```

 The grasp_feedback_topic is optional
and can be excluded. Then in the interface you can right-click on
objects in the scene and add a grasp for that object. Initially a grasp
primitive is generated that is just a placeholder and does not specify
any poses. To use the grasp suggestion service to generate grasps, you
then right click the blue placeholder box and select "Generate
grasps". The service will return a list of grasp poses. Fetch PbD sets
a pre-grasp that is 15 cm away from the grasp. The first grasp generated
is shown and you can switch to other grasp options by right-clicking the
grasp marker and selecting one from the list.

![Add Grasp\|width=100%](attachment:add_grasp.png)

![Generate Grasps\|width=100%](attachment:generate_grasps.png)

![Change Grasp\|width=100%](attachment:change_grasp.png)

Grasps are executed like any other primitive and can be added to actions
in combination with other primitives.

You can also access the actions you've programmed through code. You
still need to run pbd_backend.launch.



```
$ source ~/catkin_ws/devel/setup.bash rosrun fetch_pbd_interaction demo.py
```



The pbd_interaction_node.py handles the interaction between speech/GUI
and the rest of the system. Changes happen through the update loop in
interaction.py and also through the callbacks from speech/GUI commands.
interaction.py also subscribes to updates from the pbd_world_node.py,
which notifies it of changes in objects in the world. Through callbacks
and the update loop, interaction.py hooks in to session.py. session.py
handles creating actions and primitives and saving them to the database.

The pbd_arm_control_node.py is how the robot's arm is controlled to
execute actions/primitives. It provides a lower level service interface
to move the arm. The interaction node interacts with this through the
interface in robot.py.

The pbd_world_node.py handles the robot's perception of the world.
Other nodes ask the world node about the state of the world and can both
send and subscribe to updates to the world. Its main function is to
provide a list of objects currently in the scene.

The social_gaze_server.py handles the movements of the robot's head.
This is also controlled through the robot.py interface. The sounds are
also provided through this interface.
