## Safe Base Controller

The \`safe_base_controller\` is a modified \`base_controller\` for the
PR2. It subscribes to a topic where velocity limits for the base can be
specified (implemented in a deadman manner, limits greater than zero
have to be periodically granted otherwise the limit will timeout and the
base stop).

To use this controller the robot has to be started with the
\`safe_base_controller\` in the package path. This can be either
achieved by checking out and compiling the package as the \`ros\` user
or by starting the robot with \`sudo robot start -e\`. See
\`controller_manager\` help for more info.

Once the robot has been started and the controller is visible (\`rosrun
pr2_controller_manager pr2_controller_manager list-types\`) you can
start the safe_base_controller with the provided launch file.

## Nodes

```clearsilver
node.0{
name=safe_base_controller
desc=The safe_base_controller "node" is started by the controller manager as a realtime controller. Below only new parameters are listed, the ones already included in the original base_controller are omitted.
param {
  0.name= ~timeout_vel_limits
  0.type= seconds
  0.desc= When the last command_limits message is older than timeout, the base is stopped. (Similar to the parameter timeout which stops the base if no new command message arrives.)
}
pub {
}
sub {
  0.name= command
  0.type= geometry_msgs/Twist
  0.desc= Message which contains the requested velocities with which the base should drive.
  1.name= command_limits
  1.type= safe_base_controller/TwistLimits
  1.desc= Specifies the maximum velocities the base is allowed to drive. Needs to be send constantly otherwise base will not be allowed to move.
}
srv {
}
```
