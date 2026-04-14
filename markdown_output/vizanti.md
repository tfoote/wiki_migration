# Vizanti

\'\'\'Web Visualizer & Mission Planner for ROS\'\'\'

Vizanti is a web-based visualization and control tool developed for more
convenient operation of outdoor robots running the Robot Operating
System (ROS). The application attempts to replicate RViz\'s orthographic
2D view as closely as possible with a smartphone friendly interface. The
second goal is to allow planning and executing movement and mission
commands, i.e. goals and waypoints, with custom buttons and parameter
reconfigure.

![\|width=750](https://github.com/MoffKalast/vizanti/raw/ros1/public/assets/icon/preview.jpg)

## Installation

As a field tool, Vizanti is designed to operate just as well without
internet access, and as such the intended way is to host it on a robot,
with rosbridge autoconnecting to the host IP.

```bash
cd ~/catkin_ws/src
git clone https://github.com/MoffKalast/vizanti.git
cd ..
rosdep install --from-paths src --ignore-src
catkin_make
```

Or if rosdep fails for some reason, these are the main deps:
```bash
sudo apt install ros-noetic-rosbridge-suite python3-flask python3-waitress
```

Flask and Jinja2 are used for templating, rosbridge is required for
socket communication.

## Run

```bash
roslaunch vizanti server.launch
``` The web app can be accessed at
\`http:*\<host_ip\>:5000\`. Client settings are automatically saved in
localStorage. The satelite imagery renderer also uses the indexedDB to
store tiles for offline use (note that this is IP specific). By default
the rosbridge instance also occupies port 5001.*

If you\'re using a mobile device connected to a robot\'s hotspot that
doesn\'t have internet access, make sure to turn off mobile data. This
will prevent Android from sending packets to the wrong gateway.

------------------------------------------------------------------------

## Demo Videos

Desktop demo (SLAM, node manager, dynamic reconfigure):

\<\<Youtube(IM6ix1stPnc&rel=0)\>\>

Mobile demo (GPS navigation, OSM tile map):

\<\<Youtube(uXDBWc23ZdQ&rel=0)\>\>

## More info

You can find more setup info on the Github wiki:

\-
[Getting Started](https://github.com/MoffKalast/vizanti/wiki#getting-started)

\-
[Feature Guide](https://github.com/MoffKalast/vizanti/wiki/Feature-List)

\-
[Configuration Tips](https://github.com/MoffKalast/vizanti/wiki/Advanced-Configuration)

\-
[More Demo Videos](https://github.com/MoffKalast/vizanti/wiki/Demo-Videos)
