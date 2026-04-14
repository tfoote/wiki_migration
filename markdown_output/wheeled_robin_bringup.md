## WheeledRobin Bringup

This package starts the WheeledRobin. There are several launch files for
different applications.

## Launch Files

Launch files are similar to the Turtlebot launch files with minor
differences. Use roslaunch files to load this files.

-   \'\'\'minimal.launch\'\'\' - The base launch file for !WheeledRobin.
    Starts the basic nodes ([wheeled_robin_node](wheeled_robin_node)),
    [robot_state_publisher](robot_state_publisher),
    [diagnostic_aggregator](diagnostic_aggregator), and
    [robot_pose_ekf](robot_pose_ekf).
-   \'\'\'minimal_fake.launch\'\'\' - Same as minimal.launch but does
    not load [wheeled_robin_node](wheeled_robin_node). Instead
    [fake_odom](fake_odom) is loaded.

```{=html}
<!-- -->
```
-   \'\'\'minimal_with_appmanager.launch\'\'\' - Same as minimal.launch
    but additional starts the !WheeledRobin app managers and loads the
    !WheeledRobin app list and parts of the Turtlebot app list.

```{=html}
<!-- -->
```
-   \'\'\'minimal_fake_with_appmanager.launch\'\'\' - Same as
    minimal_fake.launch with additional app manager.

```{=html}
<!-- -->
```
-   \'\'\'3dsensor.launch\'\'\' - The 3D sensor launch file. Starts all
    the nodes/nodelets required to use the Microsoft Kinect or ASUS
    Xtion as a laser scanner and camera: [openni_camera](openni_camera)
    and
    [depthimage_to_laserscan](http://www.ros.org/wiki/depthimage_to_laserscan).

```{=html}
<!-- -->
```
-   \'\'\'paired_public.launch\'\'\' - Starts a public ros master for an
    app manager. Typically not used alone, instead use bringup.concert!

## Concert Files

Concert files are similar to the Turtlebot launch files with minor
differences.Use rocon command to launch rocon files.

-   \'\'\'bringup.concert\'\'\' - Launches a private master at port
    11312 with minimal_with_appmanager.launch and a public master at
    11311 with paired_public.launch.
-   \'\'\'bringup_fake.concert\'\'\' - Same as bringup.concert but does
    launch minimal_fake_with_appmanger.launch instead of
    minimal_with_appmanager.launch.
