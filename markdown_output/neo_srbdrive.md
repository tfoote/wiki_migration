repository: <git://github.com/neobotix/neo_driver>

## SRB Drive

The SRB Drive is a wrapper package for converting messages from the
[Serial Relayboard](ser) into ros messages.

## Topics to publish/subscribe

```clearsilver

sub {
  0.name = /drive_states
  0.type = neo_msgs/DriveStates
  0.desc = publishes joint states in the serial relayboard message format.
  1.name = /srb_lcd_display
  1.type = neo_msgs/LCDOut
  1.desc = sets lcd output
}
pub {
  0.name = /cmd_drives
  0.type = neo_msgs/DriveCmd
  0.desc = sets joint velocities in the serial relayboard message format.
  1.name = /joint_states
  1.type = sensor_msgs/JointStates
  1.desc = publishes the jointstates

}
```
