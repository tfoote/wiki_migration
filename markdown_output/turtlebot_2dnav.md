## Overview

This package provides an application that allows a Turtlebot to navigate
autonomously through a previously mapped environment.

## Running the Application

The [turtlebot_2dnav](turtlebot_2dnav) application can be run with the
following command:

```
roslaunch turtlebot_2dnav turtlebot_2dnav.launch map_file:=/my_map.yaml
```

## Interacting with the Application

The [navigation](navigation) stack that is the core of the
turtlebot_2dnav application can be commanded via [rviz](rviz),
[ros2djs](ros2djs), or through code.

### rviz

-   You can bring up rviz using turtlebot_2dnav configuration by running
    the following launch file: ```
roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
```

```{=html}
<!-- -->
```
-   The application is now up and ready to receive goals.
-   Click the \"2D Nav Goal\" button in the rviz GUI window.
-   Left click on the map at the location of the goal and drag to set
    orientation.

```{=html}
<!-- -->
```
-   [ Navigation and rviz tutorial](navigation/Tutorials/Using rviz with the Navigation Stack ):
    Provides additional information on using [rviz](rviz) with the
    [navigation](navigation) stack.

### ros2djs

-   When this package is launched, you can use the library
    [ ros2djs](ros2djs ) to integrate a plugin based on JSON in a
    webpage and create a client that is able to send goals to the
    navigation stack.

```{=html}
<!-- -->
```
-   In order to make ROS able to communicate with the webpage that uses
    ros2djs, we launch the web socket after the turtlebot_2dnav.
    ```
roslaunch rosbridge_server rosbridge_websocket.launch
```

```{=html}
<!-- -->
```
-   Go to the webpage
-   Double click in the map to send the goal to the stack navigation.

### Through Code

-   A tutorial on sending goals to the [navigation](navigation) stack
    with code can be found
    [ here](navigation/Tutorials/SendingSimpleGoals ).
