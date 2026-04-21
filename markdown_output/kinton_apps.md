\-\-\-\-\-\-\--

# IRI Uncalibrated Visual Servoing

------------------------------------------------------------------------

## Overview

This application implements an uncalibrated image-based visual servoing
approach developed at Institut de Robòtica i Informàtica Industrial (IRI
<http://www.iri.upc.edu/>). The aplications of this software are mainly
to maneuver a camera or a robot from an initial position to a desired
location simplified by an AR_tag., this can be done considering:

-   6DOF camera
-   9DOF quadrotor and arm

Details can also be found in this paper:

```
@INPROCEEDINGS{Santamaria_icra13,
  title = {Uncalibrated image-based visual servoing},
  author = {A. Santamaria-Navarro and J. Andrade-Cetto},
  year={2013},
  crossref = {icra13},
  pages={5227-5232},
}
```

------------------------------------------------------------------------

## Dependences

-   [iri_uncalibvs](iri_uncalibvs)
-   [ar_pose](ar_pose)
-   [kinton_robot](kinton_robot)

### Simulation

Although the [iri_uncalibvs](iri_uncalibvs) node can be used in a real
robotic settings, it is included in this section the
[hector_quadrotor](hector_quadrotor) stack to simulate the UAV
quadrotor.

-   [hector_quadrotor](hector_quadrotor)

------------------------------------------------------------------------

## Usage

This section indicates the steps to follow to run the application once
the related dependences have been acquired.

### Dynamic reconfigure

-   'activate': Activate the Iri uncalibrated visual servoing
    approach.
-   'quadrotor': Select between 6dof or the underactuated 4dof output
    for the quadrotor.
-   'arm_unina': Enables the use of a 5DOF arm (quadrotor-arm system)
-   'arm_catec': Enables the use of a 6DOF arm (quadrotor-arm system)
-   'lambda': Visual servo proportional control constant value.
-   'lambda_quadrotor': Quadrotor velocities proportional factor.
-   'lambda_arm': Arm velocities proportional factor.
-   'dist_to_tag': Desired final distance to tag (tag's z axis).
-   'random_points': Select between random or fixed original feature
    points.
-   'output_files': Save to a file the quadrotor poses.
-   'path': The path to save the quadrotor poses.
-   'traditional': Select between traditional or uncalibrated image
    jacobian.

### Simulation

-   Initialize the simulation:
-   `roslaunch iri_uncalibvs_sim iri_uncalibvs_sim_hector_all.launch`

This node launches all the required nodes to drive the quadrotor with or
without arm as well as to drive it automatically (with the uncalibrated
approach) o manually (with Xbox controller teleop).

------------------------------------------------------------------------

## Example Videos

This video shows the use of the provided software for both simulations
and a UAV quadrotor (Kinton robot).

[Youtube](https://www.youtube.com/watch?v=BZSmlxMGdfA)

This video shows the use of the uncalibrated image-based visual servo
addressing the problem of autonomously servoing a quadrotor-arm unmanned
aerial vehicle (UAV).

[Youtube](https://www.youtube.com/watch?v=rd3xYDedz04)

\-\-\-\-\-\-\--
