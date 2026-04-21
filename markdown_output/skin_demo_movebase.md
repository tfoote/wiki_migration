## Skin Demo Movebase

To teleop the robot touchlessly skin patches are installed on the back
and sides of the robot. Then driving actions need to be mapped to the
ids of skin patches (e.g. patches on the back of the robot are mapped to
the action 'drive forward' and patches on the left side of the robot
are mapped to the action 'drive right'). This is done by editing the
yaml file and mapping the skin patch ids to the actions fw, bw, right,
left, etc. See parameters below and sample yaml file.

When the software is started it publishes base_controller/command
messages like the teleop joystick package. If a sensor patch is
activated the robot starts to drive. The activation, i.e. how close e.g.
your hand is to the sensor, determines the speed with which robot will
move.

## Nodes

```clearsilver
node.0{
name=skin_demo_movebase
desc= The `skin_demo_movebase` node listens to skin_data messages and moves the base.

param {
  0.name= ~mapping/fw
  0.desc= Ids of patches that should trigger forward movement.
  1.name= ~mapping/bw
  1.desc= Ids of patches that should trigger forward movement.
  2.name= ~mapping/right
  2.desc= Ids of patches that should trigger movement to the right.
  3.name= ~mapping/left
  3.desc= Ids of patches that should trigger movement to the left.
  4.name= ~mapping/yawright
  4.desc= Ids of patches that should trigger turning to the right.
  5.name= ~mapping/yawleft
  5.desc= Ids of patches that should trigger turning to the left.
  6.name= ~num_sensors
  6.desc= Total number of sensor patches that are connected to the skin controller.
}
pub {
  0.name= /base_controller/command
  0.type= geometry_msgs/Twist
  0.desc= Command velocities to the base_controller.
}
sub {
  0.name= ~<name>/skin_data
  0.type= skin_driver/skin_meas
  0.desc= Raw skin measurement with configuration data.
}
srv {
}
```
