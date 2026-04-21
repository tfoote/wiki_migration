

```wiki
nao_ctrl is replaced by [[nao_driver]], now in the [[nao_robot]] stack. Please see the documentation there for the latest updates.
```



To run `nao_ctrl` on the actual Nao robot, you need to
[crosscompile ROS](nao/Tutorials/Cross-Compiling) for it first.
Alternatively, you can connect remotely without installing anything on
your Nao. The current version of `nao_ctrl` works with NaoQI version
1.6 or newer. Versions 0.1x are still compatible to NaoQI 1.3.

## Documentation

To start the teleoperation on the Nao, ssh on it and run:


```
cd ~/naoros/ros/nao_ctrl/scripts
source naoros.env
./nao_walker.py
```



The sensor reading node is started with: 

```
./nao_sensors.py
```



The control and sensor nodes should then connect to the running remote
nodes. Note that you can also run everything on your remote machine
(PC), connecting to your Nao (or a simulated Nao in Webots) via
Aldebaran's API. Just run 

```
./nao_walker --pip=ROBOT_IP --pport=NAOQI_PORT &
./nao_sensors --pip=ROBOT_IP --pport=NAOQI_PORT
```

 instead. This may be
slower, but avoids other problems e.g. when the times are not
synchronized between your Nao and PC.

## Nodes



```clearsilver
node.0 {
 name = nao_sensors
 desc = `nao_sensors` publishes the Nao's sensors (currently joint state, IMU, and odometry) by wrapping the Aldebaran Python NaoQI API.
 pub{
  0.name = torso_odometry
  0.type = nao_msgs/TorsoOdometry
  0.desc = Basic odometry of Nao's torso (6D)
  1.name = torso_imu
  1.type = nao_msgs/TorsoIMU
  1.desc = Raw and filtered data from Nao's internal IMU
  2.name = joint_states
  2.type = sensor_msgs/JointState
  2.desc = Measured state of all joints of Nao
 }
}
node.1 {
 name = nao_walker
 desc = `nao_walker` provides teleoperation with an omnidirectional walk by wrapping the Aldebaran Python NaoQI API. Accessing Nao's speech synthesis is also possible with the topic `speech`.
 sub{
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Omnidirectional velocity (x, y, and theta) for the walking engine
  1.name = motion_command_btn
  1.type = nao_msgs/MotionCommandBtn
  1.desc = discrete motion actions (e.g. "sit down", "stand up")
  2.name = head_angles
  2.type = nao_msgs/HeadAngles
  2.desc = desired joint angles for the head
  3.name = speech
  3.type = std_msgs/String
  3.desc = Text to be said over Nao's speech synthesis
 }

param {
  0.name = ~step_frequency
  0.type = double
  0.desc = Maximum fraction of Nao's step frequency to be used when walking (between 0 and 1). This controls how fast (and stable) Nao is walking.
  0.default = 0.5

  1.name = ~max_head_speed
  1.type = double
  1.desc = Maximum fraction of Nao's speed of changing head angles to be used for the `head_angles` topic (between 0 and 1).
  1.default = 0.2

  2.name = ~use_walk_pose
  2.type = boolean
  2.desc = Slowly move from init pose to walk pose before walking to avoid toppling over backwards (might improve stability for naoqi versions >= 1.10.10, not tested for other versions)
  2.default = False

  3.name = ~enable_foot_contact_protection
  3.type = boolean
  3.desc = Enable or disable foot contact protection in robot's motion configuration. If this parameter is not specified, the current setting will not be changed.
}
}
node.2 {
 name = nao_tactile
 desc = Publishes sensor data of Nao's tactile sensors and bumpers. A message is sent whenever the state of the touch sensors or bumpers change, and the full state (pressed / touched or not) is sent.
 pub{
  0.name = tactile touch
  0.type = nao_msgs/TactileTouch
  0.desc = Contains information about which tactile button on Nao's head was touched
  1.name = bumper
  1.type = nao_msgs/Bumper
  1.desc = Contains information about which bumper (left or right) was triggered.
 }
}
```


