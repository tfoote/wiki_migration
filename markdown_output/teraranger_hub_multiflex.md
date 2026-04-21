![](attachment:teraranger_hub_multiflex.jpg)

## Supported Hardware

This node works with TeraRanger Multiflex you can find more information
below.

-   [TeraRanger Multiflex](http://www.teraranger.com/products/teraranger-multiflex)

## API Stability

## Nodes



```clearsilver
name=teraranger_hub_multiflex
desc=TeraRanger Multiflex is the modular solution for indoor distance sensing applications up to 2m range. Plug and play sensor modules on one flexible bus making it easy to create custom configurations and to place sensors where needed. An array of calibrated distances in millimeters is streamed from the Multiflex Hub. It’s the ideal – and higher performance – alternative to ultrasound for robot collision avoidance and a myriad other shorter range distance sensing requirements, all in one convenient and easy to use kit.
pub {
  0.name = /teraranger_hub_multiflex
  0.type = sensor_msgs/Range
  0.desc = Provides range readings from all sensors consecutively
}
param {
  group.0 {
     name=Static Parameters
         0.name = _portname
         0.type = str, default: "/dev/ttyACM0"
         0.desc = The device path to open.
          }
  group.1 {
         name=Dynamic Parameters
         0.name = ~Sensor_0
         0.desc = activate sensor 0
         0.type = bool
         0.default = True
         1.name = ~Sensor_1
         1.desc = activate sensor 1
         1.type = bool
         1.default = True
         2.name = ~Sensor_2
         2.desc = activate sensor 2
         2.type = bool
         2.default = True
         3.name = ~Sensor_3
         3.desc = activate sensor 3
         3.type = bool
         3.default = True
         4.name = ~Sensor_4
         4.desc = activate sensor 4
         4.type = bool
         4.default = True
         5.name = ~Sensor_5
         5.desc = activate sensor 5
         5.type = bool
         5.default = True
         6.name = ~Sensor_6
         6.desc = activate sensor 6
         6.type = bool
         6.default = True
         7.name = ~Sensor_7
         7.desc = activate sensor 7
         7.type = bool
         7.default = True
         }
}
```



## Running

To launch a node simply run: 

```
rosrun teraranger_hub_multiflex teraranger_hub_multiflex_node
```


