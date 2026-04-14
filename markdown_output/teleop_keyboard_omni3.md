Motion Analysis of 3 wheeled omnidirectional robot:
<https://yainnoware.blogspot.com/2019/03/three-wheeled-holonomic-robot-theory.html>

## Installing

```
cd ~/catkin_ws/src
git clone https://github.com/YugAjmera/teleop_keyboard_omni3
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
source ~/.bashrc
```

## Running

```
rosrun teleop_keyboard_omni3 teleop_keyboard_omni3.py
```

## Controls

See the on-screen instructions:

```
Reading from the keyboard !
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >


anything else : stop

q/z : increase/decrease max speeds by 10%

CTRL-C to quit
```
