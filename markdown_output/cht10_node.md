This ROS package is Driver for CHT-10 laser ranging sensor of LAX.

## Nodes

```clearsilver
node.0 {
  name=cht10_node
  desc=This ROS package is Driver for CHT-10 laser ranging sensor of LAX.
  
  pub{
    0.name= range
    0.type= sensor_msgs/Range
    0.desc= Provides range reading.
}
```

### Parameters

```clearsilver
param {
  no_header=False
  0.name= serialNumber
  0.default="/dev/ttyUSB0"
  0.type= str
  0.desc= The device path to open.
  1.name= frame_id
  1.default="laser"
  1.type= str
  1.desc= Frame id for sensor.
  2.name= baudRate
  2.default=115200
  2.type= int
  2.desc= baud rate for sensor.
}
```
