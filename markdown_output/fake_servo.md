## Overview

This package is intended to provide you ability to test your controller
infrastructure without hardware. It's simulate ideal servo (achieve
goal immediately).

## OROCOS API

### Input ports



```clearsilver
param {
  no_header= True
  0.name= dsrJntPos
  0.type= vector<double>
  0.desc= Setpoint for the servo algorithm. 
}
```



### Output ports



```clearsilver
param {
  no_header= True
  0.name= msrJntPos
  0.type= vector<double>
  0.desc= Measured position of joints.

  1.name= cmdJntPos
  1.type= vector<double>
  1.desc= Desired position of joints.
}
```



### Properties



```clearsilver
param {
  no_header= True
  0.name= number_of_joints
  0.type= int
  0.desc=Number of joints that will be controlled by fake_servo.
}
```


