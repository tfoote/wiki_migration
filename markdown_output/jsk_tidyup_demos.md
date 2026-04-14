## Video

[Youtube](https://www.youtube.com/watch?v=Uejbqpxd-zo)

## Usage

To run the demos, do the following: ```
roslaunch jsk_tidyup_demos demo.launch
``` Then start
Python shell and type some commands. ```
roscd jsk_tidyup_demos/scripts
python
from demo import *
d = JskDemo()
d.demo1()
d.demo2()
d.demo3()
d.demo4()
``` If you
want to view the status of navigation, use rviz.
```
roslaunch 2dnav_pr2 rviz_move_base.launch
```

Note that jsk_tidyup_demo.launch and Python shell need to be executed on
the robot.
