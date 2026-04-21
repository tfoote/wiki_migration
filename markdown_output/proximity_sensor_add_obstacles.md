The proximity_sensor_add_obstacle package contains a node that can
insert obstacles that the proximity sensor has detected into the
collision map. Each patch can hold a configurable maximum number of
obstacles. When more obstacles are detected, old ones are overwritten.
You can also set a lifetime for obstacles since obstacles should
disappear from the collision map after a while when they cannot be
detected anymore.

In *conf/add_obstacles.yaml* there are the two parameters:

```
int_buffer_size: 10 // Number of maximum obstacles per patch
``` ```
dbl_expiration_time: 5.0 // Maximum lifetime per obstacle in seconds
``` Be careful with
editing these values when you have many patches in your proximity
sensor! Big values can cause a lot of CPU load for the environment
server!

To launch this node you first have to launch the tf node for the
proximity sensor.

```
roslaunch proximity_sensor_tf tf.launch
``` As the tf node is running the add_obstacle node
knows where to put the detected obstacles. Before you can actually
launch the add_obstacle node you first have to launch an environment
server, where the obstacles are added to. Normally this is done by an
application that you want to use for example in the package
[pr2_arm_teleop_skin](pr2_arm_teleop_skin). However if that is not the
case and you just want to start a new environment server you can use the
launch file in the package.

```
roslaunch proximity_sensor_add_obstacles environment_server.launch
``` Then you are ready to launch the node via

```
roslaunch proximity_sensor_add_obstacles add_obstacles.launch
```
