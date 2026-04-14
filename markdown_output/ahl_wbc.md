# What is Whole Body Control ?

Here,\'\'whole body control\'\' means a control framework proposed by
Prof. Oussama Khatib. The framework is also known as \'\'task space
control\'\', \'\'operational space control\'\', or \'\'operational space
formulation\'\'.

When you control a robot with many joints, it\'s hard to compute a
desired angle/torque set of joints. Traditional approach is inverse
kinematics(IK), which is a geometric solution. IK-based control is still
good, but here is a different approach, whole body control. ahl_wbc
computes a desired angle/torque set, given a desired
position/orientation of a robot\'s fingertip.

Therefore, if you used this framework, you could easily control complex
robots without using IK. Also, if the robot had torque sensor at each
joint, all of force, position and orientation of fingertip would be
controlled in hybrid way.

```
author    = {Oussama Khatib},
  title     = {A Unified Approach for Motion and Force Control of Robot Manipulators:	The Operational Space Formulation},
  year      = {1987},
  month     = {February},
  booktitle = {IEEE Journal of Robotics and Automation (RA-3)},
}
```

[Youtube](https://www.youtube.com/watch?v=7pHPHKFTwZs)

For more details, see github page.
