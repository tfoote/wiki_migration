## Nodes



```clearsilver
node.0{
name=skin_safe_base

param {
}
pub {
  0.name= command_limits
  0.type= safe_base_controller/TwistLimits
  0.desc= Specifies the maximum velocities the base is allowed to drive. Is send constantly otherwise base will not be allowed to move.
}
sub {
  0.name= ~<name>/skin_data
  0.type= skin_driver/skin_meas
  0.desc= Raw skin measurement with configuration data
}
srv {
}
```


