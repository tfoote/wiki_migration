## Overview

The PR2 interactive object detection tool contains a graphical user
interface which allows a remote user to run scene segmentation and
object recognition on a PR2 robot. Recognition can be executed in a
fully autonomous or interactive way, utilizing the functionality of
[object_recognition_gui](object_recognition_gui). The results of these
steps can be used by
[pr2_interactive_manipulation](pr2_interactive_manipulation) to pick up
up the segmented or recognized objects.

## Starting the PR2 Interactive Object Recognition Tool

There are two options to run the user interface. One is to bring up
[pr2_interactive_manipulation](pr2_interactive_manipulation), which will
load all the components described here.

The other is to run the object detection part only, for which you will
have to do the following:

### On the robot

Start the following launch file: ```
roslaunch pr2_interactive_object_detection pr2_interactive_object_detection_robot.launch
```

Or, if you have a local Kinect: ```
roslaunch openni_camera openni_node.launch
roslaunch rgbd_assembler rgbd_kinect_assembler.launch
roslaunch household_objects_database objects_database_remote_server.launch
rosrun willow_tod recognition_node camera:=/camera/rgb points:=/camera/rgb/points -C detect_config.txt
```

Then start rviz and add \"Interactive Object Detection\", \"Object
Recognition popup window\"

### On the desktop

Start the following launch file: ```
roslaunch pr2_interactive_object_detection pr2_interactive_object_detection_desktop.launch
```

Note that this launch file will bring up rviz. The tool is implemented
as an [rviz plugin](rviz/UserGuide#Plugins). For everything to work, you
will have to add the following displays:

-   \'\'\'Interactive Object Detection/Interactive Object
    Detection\'\'\': This brings up a control dialog with buttons to
    trigger segmentation, object recognition and to make the robot\'s
    head look at a spot directly in front of the robot.

```{=html}
<!-- -->
```
-   \'\'\'Object Recognition GUI/Object Recognition Pop-Up Window\'\'\':
    This will create a pop-up window once interactive object recognition
    has been requested. It does not have to run in the same rviz
    instance as the control dialog.

Note that the control dialog does not contain any actual functionality
but redirects all user input to an additional node called
\'\'pr2_interactive_object_detection_backend\'\'. This allows the front
end to be replaced by other user interfaces.

## Using the PR2 Interactive Manipulation Tool

### Control Dialog

![](attachment:segmentation.png)

Dialog segmentation tab

![](attachment:recognition.png)

Dialog recognition tab

The Interactive Object Detection control dialog contains buttons to
trigger segmentation and recognition. All actions can be canceled while
they are being executed. In addition, it displays the current status of
the actions in the status bar as well as information about the results
of segmentation and recognition. Before performing the recognition step,
it is necessary to run the segmentation step.

The results of each step will immediately become available in other
tools like [pr2_interactive_manipulation](pr2_interactive_manipulation).

### Interactive Object Recognition

![](attachment:Screenshot-1.png)

The Interactive Object Recognition Dialog will automatically pop up once
it has been requested. It shows the scene as viewed by the robot\'s
camera with the meshes of all recognized objects being overlaid on top
of the camera image. When moving the mouse over this window, you will
see individual meshes being highlighted as you go over them.

-   \'\'\'Accept or reject matches\'\'\': If a mesh is displayed in
    \'\'red\'\' color, this means that it is considered a wrong
    recognition result and is going to be omitted, while \'\'green\'\'
    indicates a correct recognition result. You can switch between the
    two states by right-clicking on the object.

```{=html}
<!-- -->
```
-   \'\'\'Cycle through results\'\'\': For each segment, there will be a
    number of possibly matching objects. To cycle through these matches,
    left-click on the corresponding mesh.
