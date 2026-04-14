## Overview

This package provides a [URDF](urdf) model of [Dingo](Robots/Dingo). For
an example launchfile to use in visualizing this model, see
[dingo_viz](dingo_viz).

![](attachment:dingo_rviz.png)

## Accessories

Dingo has a suite of optional payloads called accessories. These
payloads can be enabled and placed on Dingo using environment variables
specified at the time the [xacro](xacro) is rendered to URDF. Available
environment variables are described
[here](http://www.clearpathrobotics.com/assets/guides/melodic/dingo/description.html)

Please see [dingo_simulator](dingo_simulator) for more information on
simulating Dingo.
