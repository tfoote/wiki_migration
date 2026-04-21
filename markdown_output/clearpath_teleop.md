## Nodes



```clearsilver
node {
 0{
 name = teleop.py
 desc = The `teleop.py` node consumes Joy messages and produces Twist commands for a mobile base.
 sub {
  0{
  name= joy
  type= joy/Joy
  desc= Receives joystick state.
  }
 }
 pub {
  0{
  name= cmd_vel
  type= geometry_msgs/Twist
  desc= Outputs motion command.
  }
 }
 param {
  0{
  name= ~turn_scale
  type= double
  desc= Amount by which to multiply 0..1 joystick x-axis in order to obtain turn speed command in rads/s.
  }
  1{
  name= ~drive_scale
  type= double
  desc= Amount by which to multiply 0..1 joystick y-axis in order to obtain linear drive speed command in m/s.
  }
  2{
  name= ~deadman_button
  type= int
  default= 0
  desc= Index of button which must be depressed in order to broadcast command messages.
  }
  3{
  name= ~hz
  type= double
  default= 20
  desc= Frequency with which to broadcast command messages.
  }
 }
 }
}
```


