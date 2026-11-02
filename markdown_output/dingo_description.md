## Overview

This package provides a [URDF](https://index.ros.org/p/urdf) model of
[Dingo](Robots/Dingo). For an example launchfile to use in visualizing
this model, see [dingo_viz](https://index.ros.org/p/dingo_viz).

![attachment:dingo_rviz.png](doc/dingo_rviz.png)

## Accessories

Dingo has a suite of optional payloads called accessories. These
payloads can be enabled and placed on Dingo using environment variables
specified at the time the [xacro](https://index.ros.org/p/xacro) is
rendered to URDF. Available environment variables are described
[here](http://www.clearpathrobotics.com/assets/guides/melodic/dingo/description.html)

Please see [dingo_simulator](https://index.ros.org/p/dingo_simulator)
for more information on simulating Dingo.
