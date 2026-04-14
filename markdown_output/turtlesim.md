## Getting Started with Turtlesim

Start the roscore: ```
$ roscore
```

To install and start the turtlesim: ```
$ sudo apt-get install ros-$(rosversion -d)-turtlesim
``` Run
turtlesim: ```
$ rosrun turtlesim turtlesim_node
```

You\'ll see the turtlesim window:

![](attachment:turtlesim.png)

## Nodes == As of \'\'Hydro\'\' turtlesim uses the \[\[geometry_msgs\]\]/Twist message instead of its own custom one (\'\'turtlesim/Velocity\'\' in \'\'Groovy\'\' and older). Also the topic has been changed to \`cmd_vel\` (instead of \`command_velocity\` before).

```clearsilver
node.0 {
 name = turtlesim_node
 desc = `turtlesim_node` provides a simple simulator for teaching ROS concepts.
 sub{
  0.name= turtleX/cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= The linear and angular command velocity for turtleX. The turtle will execute a velocity command for 1 second then time out. Twist.linear.x is the forward velocity, Twist.linear.y is the strafe velocity, and Twist.angular.z is the angular velocity.
  }
 pub {
  0.name= turtleX/pose
  0.type= turtlesim/Pose
  0.desc= The x, y, theta, linear velocity, and angular velocity of turtleX.
 }
 srv {
  0.name= clear
  0.type= std_srvs/Empty
  0.desc= Clears the turtlesim background and sets the color to the value of the background parameters.
  1.name= reset
  1.type= std_srvs/Empty
  1.desc= Resets the turtlesim to the start configuration and sets the background color to the value of the background.
  2.name= kill
  2.type= turtlesim/Kill
  2.desc= Kills a turtle by name.
  3.name= spawn
  3.type= turtlesim/Spawn
  3.desc= Spawns a turtle at (x, y, theta) and returns the name of the turtle. Also will take name for argument but will fail if a duplicate name.
  4.name= turtleX/set_pen
  4.type= turtlesim/SetPen
  4.desc= Sets the pen's color (r g b), width (width), and  turns the pen on and off (off).
  5.name= turtleX/teleport_absolute
  5.type= turtlesim/TeleportAbsolute
  5.desc= Teleports the turtleX to (x, y, theta).
  6.name= turtleX/teleport_relative
  6.type= turtlesim/TeleportRelative
  6.desc= Teleports the turtleX a linear and angular distance from the turtles current position.
 }
 param {
  0.name= ~background_b
  0.default= 255
  0.type= int
  0.desc= Sets the blue channel of the background color.
  1.name= ~background_g
  1.default= 86
  1.type= int
  1.desc= Sets the green channel of the background color.
  2.name= ~background_r
  2.default= 69
  2.type= int
  2.desc= Sets the red channel of the background color.
 }
}
node.1{
 name = mimic
 desc = `mimic` provides a simple interface for making one turtlesim mimic another.
 sub{
  0.name= input
  0.type= turtlesim/Pose
  0.desc= The input topic for the `mimic` node. The topic must be remapped to the `pose` topic of the desired turtle to mimic. 
  }
 pub {
  0.name= output
  0.type= geometry_msgs/Twist
  0.desc= The output topic for the `mimic` node. The topic must be remapped to the `cmd_vel` topic of the mimicking turtle. 
 }
}
```

## Turtlesim Video Tutorials

### Python Tutorials

Linear Motion [Youtube](https://www.youtube.com/watch?v=4Lifb9Cg_9w)

Go to goal behavior
[Youtube](https://www.youtube.com/watch?v=D7ISrmszozk)

### C++ Tutorials

[Youtube](https://www.youtube.com/watch?v=qtVDso-iBNA)
[Youtube](https://www.youtube.com/watch?v=PGZMlzBlMmw)
[Youtube](https://www.youtube.com/watch?v=Ddqwq2WXFEk)
[Youtube](https://www.youtube.com/watch?v=Qh15Nol5htM)
[Youtube](https://www.youtube.com/watch?v=ehH8oLfsz-w)
