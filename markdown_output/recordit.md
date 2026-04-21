[Source link (temp)](https://github.com/ipa-jfh/robot_recorder)

**Look at me!**

![](attachment:pr2_waving.gif)

\... catch more attention with the tool \...

## RecordIt

![](attachment:ur_recordit.gif)

"An animation is worth a thousand lines of markdown."

The RecordIt tool allows to record any ROS application. The resulting 3D
animation can be visualized in the web or as well be converted into a
GIF.

[See 3D animation](https://ipa-jfh.github.io/urdf-animation/manipulator_ur5/result/)

[Get started with the tutorial](https://github.com/ipa-jfh/robot_recorder_tutorials)

## Further examples

![](attachment:prbt_scan_and_plan.gif)

[See 3D animation](https://ipa-jfh.github.io/urdf-animation/application_scan_and_plan/result/)

[See source code of application](https://github.com/rosin-project/automatica18_scan_and_plan_demo)

![](attachment:tb_circle.gif)

[See 3D animation](https://ipa-jfh.github.io/urdf-animation/mobile_robot_turtlebot3/result/)

## Use cases

-   Eye-catcher for ROS applications
-   Inspect CI test
-   Visual benchmarking

## Create a 3D web animation

The tool records the motion of the robot and saves it into a file. In
order to reduce the recorded data it does not use a fixed rate but key
frames.

![](attachment:pr2_keyframes.gif)

During a running application the internal and external motions are
extracted from the ROS topics `/joint_states` and `/tf
respectively`. The topics can be throttled by rate and by change to
reduce the recorded key frames.

The tool can either be used in automatic mode which records as long as
the node is running; or in manual mode, triggered via ROS services or
through a RViZ gui.

The recorded robot movements are saved in the JSON Object format which
can be directly feed into Three.js, a cross-browser library to display
animated 3D graphics. In combination with the urdf-loaders library,
which imports the ROS robot robot description into a Three.js scene, one
can visualize the animated robot in the web browser. The resulting web
page can easily be hosted on Github Pages or any other web server.

## Convert to a GIF

With only once click the animation can be converted to a GIF which can
be used e.g. for a README or a presentation.
