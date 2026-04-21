

```clearsilver
name = HRI Safe Remote Control System
desc = HRIs Safe Remote Control System (SRCS) is a medium to long-range wireless remote controller designed from the ground up to enable the safe operation of remote and automated systems. It provides a rugged, ergonomic, and easy to understand controller with a flexible receiver that both implement HRI’s proprietary SafetySense™ technology to ensure both consistent and reliable control. 
pub {
  0.name = joy
  0.type = sensor_msgs/Joy
  0.desc = Output from the joysticks on the safe remote control
  1.name = safety/emergency_stop
  1.type = std_msgs/UInt32
  1.desc = Discrete value representing the state of the E-STOP in the SRCS system.  A 1 indicates that the E-STOP has been activated, and a 0 indicates a safe operating condition  
}
```


