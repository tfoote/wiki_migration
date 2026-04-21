## Disclaimer and condition of use

**Disclaimer**: this stack is not maintained by Aldebaran Robotics.
Stack maintainers do not hold copyright for the model information. This
stack is based on
[information freely available](http://projetromeo.com/index_en.html) and
is distributed with Aldebaran Robotics permission.

If you are using this robot to illustrate a document such as a
scientific publication, you should include the following copyright
notice: \"(c) Aldebaran Robotics\" near the figure.

## Documentation

Romeo is a 140-cm humanoid robot designed by
[Aldebaran Robotics](http://www.aldebaran-robotics.com/).

This package contains the following information:

-   [URDF model](urdf_parser) defining the robot kinematic chain and
    actuators/sensors information,
-   [SRDF model](srdf) containing the robot reference configuration and
    collision pairs.
-   [RCPDF](rcpdf) containing contact information (sole and toe
    information).

**The current model is based on the robot model v1.0.**

### Additional information

  -- -------------------------------------------- -- ------------------------------------------- -- -- --
                                                     **Stepping information with static toes**         
     Maximum forward step (X axis / front-rear)      0.245m (safe) / 0.32m (unsafe)                    
     Maximum lateral step (Y axis / left-right)      0.316141m                                         
  -- -------------------------------------------- -- ------------------------------------------- -- -- --

## URDF model

The URDF model contains the kinematic chain and meshes information. The
following screenshot has been taken in rviz with tf tree frame location
indicated. The pose is set to 0 for all degrees of freedom here.

![Romeo in RViz\|width=400](attachment:romeo.jpg)

The robot frames naming scheme follows the
[REP 105](http://www.ros.org/reps/rep-0105.html) and
[REP 120](http://www.ros.org/reps/rep-0120.html) documents.

Normalized naming can be considered as stable, intermediate links naming
may change when the package is updated.

![Romeo tf frames\|width=1600](attachment:frames.jpg)

## SRDF model

The SRDF model contains the half-sitting reference pose called
\`half_sitting\`. It is meant to used as a statically stable posture
where the center of mass is near the robot waist. It can be used to
safely initialize optimization problems or planning algorithms.

## RCPDF model

To be done.
