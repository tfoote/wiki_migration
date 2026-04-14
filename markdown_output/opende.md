## Overview

Please see the [official ODE documentation](http://opende.sf.net/) for
information on how to develop with ODE. We have provided some
[some useful basic background material on the ODE solvers](physics_ode/ODE).

## Known Issues

-   Joint limits cannot approach \[-&pi;,+&pi;\]. This is currently a
    missing feature in ODE.
-   Joint friction not modeled.
-   Interpenetration tolerance between objects in contact defaults at
    1mm to prevent jittery behavior.
-   For more information on ODE limitations, see
    [ODE FAQ](http://www.ode.org/ode-latest-userguide.html#sec_12_0_0)
    and
    [collision FAQ.](http://opende.sourceforge.net/wiki/index.php/Manual_(Collision_Detection))
