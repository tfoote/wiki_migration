The `lama_test` package provides a few launch files to test the
functionalities of the Large Maps Framework
([LaMa](Large Maps Framework)).

## Usage

To test the high-level node `dfs_explorer/explorer.py`:
```shell
roslaunch dfs_explorer explorer.py
``` This will load a small map with 3 vertices and
start exploring it. The exploration can be stopped and launched again.
The exploration will then continue and take into account the information
already available in the map. The node will launch an exploration either
based on a 360-degree laser scan (jockeys [nj_laser](nj_laser) and
[lj_laser](lj_laser)) with `roslaunch dfs_explorer explorer.py
__costmap:=false` or based on a laser-scan with less than 360°
(jockeys [nj_costmap](nj_costmap) and [lj_costmap](lj_costmap)) as
default.
