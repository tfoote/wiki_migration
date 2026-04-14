repository: <git://github.com/neobotix/neo_driver>

## SRB IR

The SRB IR is a wrapper package for converting messages from the
[Serial Relayboard](ser) into ros messages.

## Topics to publish/subscribe

```clearsilver

sub {
  0.name = /srb_ir_measurements
  0.type = neo_msgs/IRSensors
}
pub {
  0.name = /range_ir
  0.type = sensor_msgs/Range
  0.desc = publishes messages from the ir board
}
```
