## Overview

The package aims to give an optimal path for an agent to get its
destination in an obstacle environment. The agent starts from a random
position except the barrier area in the map, and then generates a
feasible path to its destination while avoiding all the obstacles.
Furthermore, it can support multiple agents to plan in the map.

## Quick Start

### Installation

```
cd catkin_ws/src
git clone http://github.com/micros-uav/micros_hopfield
cd ..
catkin_make
```

### Running

-Setup rviz ```
rosrun rviz rviz
``` set the config parameter in rviz :
File-open config-user.rviz -Run server node ```
source devel/setup.bash
rosrun micros_hopfield plan_server
```
\'\'\'Note:\'\'\'Run these commands under /catkin_ws directory for the
terrain map loading.

-Run Client node Open a new consol ```
source devel/setup.bash
rosrun micros_hopfield plan_client i
``` where i is
the client ID, i = 1,2,3\...

\'\'\'Note:\'\'\'run different clients in independent terminal.

### Result demo

![alt text\|width=700](https://cloud.githubusercontent.com/assets/11674154/8541617/243de8ec-24c2-11e5-9187-e21bb6d23943.png)

-   The green texture presents a terrain with different altitude

```{=html}
<!-- -->
```
-   The blue cylinder is an obstacle

```{=html}
<!-- -->
```
-   The red and blue lines are the pathes generated for two different
    agents

\'\'\'Note:\'\'\'The package is inspired by and adapted from \[1\].
Related details about neural network based path planning may also be
found in [\[2](http://www.mbfys.ru.nl/staff/s.gielen/path.pdf/)\],
[\[3](http://s3.amazonaws.com/academia.edu.documents/40402436/An_efficient_neural_network_approach_to_20151126-31384-62g0pu.pdf)\]
and
[\[4](https://www.researchgate.net/profile/Simon_Yang/publication/3413487_Neural_network_approaches_to_dynamic_collision-free_trajectory_generation/links/54a96c220cf257a6360d5594.pdf/)\].

## Reference

\[1\] Chonghong Fan, Youzhang Lu, Hong Liu, Shangteng Huang. Path
planning for mobile robot based on neural networks. Computer Engineering
and Application, 2004, 8: 86-89. (in Chinese)

\[2\] Roy Glasius, Andrzej Komoda, Stan C.A.M. Gielen. Neural network
dynamics for path planning and obstacle avoidance. Neural Networks,
1995, 8(1):125-133.

\[3\] Simon X. Yang, Max Meng. An efficient neural network approach to
dynamic robot motion planning. Neural Networks, 2000, 13(2):143-148.

\[4\] Simon X. Yang, Max Meng. Neural network approaches to dynamic
collision-free trajectory generation. IEEE SMC Part B, 2001, 31(3):
302-318.
