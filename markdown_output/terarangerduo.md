![](attachment:terarangerone.jpg)

## Supported Hardware

This driver should work with any
[TeraRanger Duo distance sensor](http://www.teraranger.com/products/teraranger-duo/).

## API Stability

The ROS API of this driver is still in development so it might change in
the future.

## ROS API

```clearsilver
node.0 {
name=terarangerone_node
desc=`terarangerone_node` is a driver for the TeraRanger One ToF range finder.
pub{
0.name= terarangerone
0.type= terarangerone
0.desc= Traditional single return output which represents the output from the TeraRanger One.

}
param {
0.name= ~Environment
0.default= 1 (indoor)
0.type= int
0.desc= The environment where the device will operate. Can have the values: 0 - outdoor,  1 - indoor
1.name= ~Speed
1.default= 0
1.type= int
1.desc= Configures the speed modes of the system. 0 - Fast, 1 - Precise
}
}
```
