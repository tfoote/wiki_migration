This package wraps jrl-walkgen. jrl-walkgen implements several pattern
generator algorithms. These algorithms aims at generating walking
trajectories for biped robots.

jrl-walkgen highly rely on jrl-dynamics for geometry, velocity and
dynamics computation.

## Supported algorithms

The following algorithms are supported:

-   *Morisawa2007*
-   *Kajita2003* usable with HRP-2 only for now.

Algorithm choice is done though the `algorithm` parameter of the
trajectory server node, see below.

## ROS API



```clearsilver
name = trajectory_server
desc = Trajectory generation node.

param {
  0.name = world_frame_id
  0.type = string
  0.desc = World frame name (i.e. the reference frame in which the trajectories are expressed).

  1.name = algorithm
  1.type = string
  1.desc = Pattern generator algorithm.
  1.default = Morisawa2007

  2.name = step
  2.type = Float64
  2.desc = Sampling step (seconds).
  2.default = 0.005

  3.name = /robot_description
  3.type = string
  3.desc = Robot model (URDF).
}

pub {
  0.name = com
  0.type = nav_msgs/Path
  0.desc = Center of mass trajectory.

  1.name = footprints
  1.type = visualization_msgs/MarkerArray
  1.desc = Footprints position.

  2.name = left_foot
  2.type = nav_msgs/Path
  2.desc = Left foot trajectory.

  3.name = right_foot
  3.type = nav_msgs/Path
  3.desc = Right foot trajectory.

  4.name = zmp
  4.type = nav_msgs/Path
  4.desc = ZMP trajectory.
}

srv {
  0.name = getPath
  0.type = walk_msgs/GetPath
  0.desc = Generate a trajectory from footprints positions.
}
```



## References

-   **M. Morisawa, S. Kajita, K. Kaneko, K. Harada, F. Kanehiro, K.
    Fujiwara, H. Hirukawa.** Pattern Generation of Biped Walking
    Constrained on Parametric Surface. In Proc. of the 2005 IEEE
    International Conference on Robotics and Automation (ICRA) \[
    [pdf](http://staff.aist.go.jp/k.kaneko/publications/2005_publications/ICRA2005-a588_WeP2-01_5.pdf)
    \]

```{=html}
<!-- -->
```
-   **S. Kajita, F. Kanehiro, K. Kaneko, K. Fujiwara, K. Harada, K.
    Yokoi and H. Hirukawa.** Biped Walking Pattern Generation by using
    Preview Control of Zero-Moment Point. In Proc. of the 2003 IEEE
    International Conference on Robotics and Automation (ICRA) \[
    [pdf](https://collab.cc.gatech.edu/humanoids/sites/edu.humanoids/files/biped_walking_pattern_generation_using_preview_control_and_zmp_shuuji_kajita.pdf)
    \]

```{=html}
<!-- -->
```
-   **A. Herdt, H. Diedam, P.-B. Wieber, D. Dimitrov, K. Mombaur, M.
    Diehl.** Online Walking Motion Generation with Automatic Foot Step
    Placement. In Advanced Robotics Vol. 24 Issue 5-6, pp. 719\--737 \[
    [pdf](http://hal.inria.fr/docs/00/46/41/25/PDF/paper.pdf) \]
