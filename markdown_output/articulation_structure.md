## Tutorials on Articulated Objects

## Nodes

```clearsilver
name = structure_learner
desc = This node receives trajectories of all parts of a kinematic object in form of <<MsgLink(articulation_msgs/ArticulatedObjectMsg Message)>> messages. For every pair of object parts, it fits the motion between these two parts to all known model classes, and selects the the kinematic structure that maximizes the BIC (Bayesian Information Criterion). The node publishes the result again in form of a <<MsgLink(articulation_msgs/ArticulatedObjectMsg)>> message, now containing additionally the individual link models. 
srv {
  0.name = track
  0.type = articulation_msgs/ArticulatedObjectSrv
  0.desc = Request: pose trajectories of all parts of an articulated object, as observed by the robot. Response: the resulting kinematic model, after model fitting and structure selection.
}
param {
  0.name = ~sigma_position
  0.type = float
  0.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the orientation of the observed trajectories. Unit: meters.
  0.default = 0.01
  1.name = ~sigma_orientation
  1.type = float
  1.desc = This parameter specifies the standard deviation of the assumed Gaussian noise in the Cartesian position of the observed trajectories. Unit: radians.
  1.default = 4*PI (=ignore orientation)
  2.name = ~filter_models
  2.type = string
  2.desc = This parameter specifies which model classes are considered during model fitting and model selection. See the section on model classes for a complete list of available models. See the tutorial for how to add custom model classes.
  2.default = "rigid prismatic rotational"
}
```

## References

-   Jürgen Sturm, Advait Jain, Cyrill Stachniss, Charlie Kemp, Wolfram
    Burgard. Operating Articulated Objects Based on Experience. In Proc.
    of the International Conference on Intelligent Robot Systems (IROS),
    Anchorage, USA, 2010. \[
    [pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm10iros.pdf)
    \] \[
    [bibtex](http://www.informatik.uni-freiburg.de/~sturm/media/publications-sturm.bib)
    \]
-   Jürgen Sturm, Kurt Konolige, Cyrill Stachniss, Wolfram Burgard.
    Vision-based Detection for Learning Articulation Models of Cabinet
    Doors and Drawers in Household Environments. In Proc. of the IEEE
    International Conference on Robotics and Automation (ICRA),
    Anchorage, USA, 2010. \[
    [pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm10icra.pdf)
    \] \[
    [bibtex](http://www.informatik.uni-freiburg.de/~sturm/media/publications-sturm.bib)
    \]
-   Jürgen Sturm, Cyrill Stachniss, Vijay Pradeep, Christian Plagemann,
    Kurt Konolige, Wolfram Burgard. Learning Kinematic Models for
    Articulated Objects. In Proc. of the International Joint Conference
    on Artificial Intelligence (IJCAI), Pasadena, USA, 2009. \[
    [pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm09ijcai.pdf)
    \] \[
    [bibtex](http://www.informatik.uni-freiburg.de/~sturm/media/publications-sturm.bib)
    \]

## More Information

More information (including videos, papers, presentations) can be found
on the homepage of
[Jürgen Sturm](http://vision.in.tum.de/members/sturmju).

## Report a Bug

If you run into any problems, please feel free to contact Juergen Sturm
\<juergen.sturm@in.tum.de\>.
