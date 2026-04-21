The \`segbot_gazebo_concert\` package provides a simple demo which
demonstrates running the [Robotics in Concert](rocon) framework with
multiple simulated robots in Gazebo.

## Installation

-   You\'ll need to install the [Robotics in Concert](rocon) framework.
    Follow the instructions at
    [rocon/Tutorials/indigo/Installation](rocon/Tutorials/indigo/Installation)
    to install \`hydro-devel\` sources into your catkin workspace.
-   Install all the code from the UTexas BWI project *(As of May 3 2014,
    this package is only available in \`ros-shadow-fixed\`)*:
    ```
sudo apt-get install ros-hydro-bwi-desktop
```
-   Install the UTexas Rocon code using this rosinstall entry:
    ```
- git: {local-name: bwi_guidance, uri: 'https://github.com/utexas-bwi/bwi_guidance.git', version: master}
- git: {local-name: rl_pursuit, uri: 'https://github.com/utexas-bwi/rl_pursuit.git', version: master}
- git: {local-name: segbot_rocon, uri: 'https://github.com/utexas-bwi/segbot_rocon.git', version: master}
```

### Running the demo

You can launch the Gazebo Concert Demo using the following command:
```
rocon_launch segbot_gazebo_concert gazebo.concert --screen
```

If all goes well, you should see 2 segway robots running around in
(not-so-perfect) squares inside the Gazebo visualizer.
