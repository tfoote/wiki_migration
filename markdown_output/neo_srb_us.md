repository: <git://github.com/neobotix/neo_driver>

## SRB US

The SRB US is a wrapper package for converting messages from the
[Serial Relayboard](ser) into ros messages.

## Topics to publish/subscribe



```clearsilver

sub {
  0.name = /srb_us_measurements
  0.type = neo_msgs/USSensors
}
pub {
  0.name = /range_us
  0.type = sensor_msgs/Range
  0.desc = publishes messages from the us board
}
```


