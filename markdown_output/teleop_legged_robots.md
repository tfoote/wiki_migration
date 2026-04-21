## Install

```
$ sudo apt-get install ros-$ROS_DISTRO-teleop-legged-robots
```

## Launch

```
$ roslaunch teleop_legged_robots teleop.launch
```

## Usage

```
Reading from the keyboard and Publishing to Twist and Pose!
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

Body pose:
---------------------------
1/2 : move the body forward/back (+/-x)
3/4 : move the body right/left (+/-y)

5/6 : move the body up/down (+/-z)

a/s : body's roll
d/f : body's pitch
g/h : body's yaw

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

r/v : increase/decrease body's pose translation by 10%
t/b : increase/decrease body's pose angular speed by 10%

CTRL-C to quit
```

The operation of teleop_legged_robots is represented in video below.
[Youtube](https://www.youtube.com/watch?v=VvZM1hyVEOo&t=18sg) The
package can be used for teleoperation of the multiple legged robots (see
video below). [Youtube](https://www.youtube.com/watch?v=Oy3aWgkpuaM)

## Inspiration

The package was created by the inspiration of
teleop_twist_keyboard(<https://github.com/ros-teleop/teleop_twist_keyboard/>)
