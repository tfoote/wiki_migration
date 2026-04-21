## Documentation

This package provides a planner that generates both goals and associated
paths for the exploration of unknown environments. The package does not
provide a ROS node, but a library that can be used inside a ROS node. A
simple usage example is implemented in the
[hector_exploration_node](hector_exploration_node) package.

Video of use of the exploration planner in a real-world RoboCup Rescue
scenario: [Youtube](https://www.youtube.com/watch?v=olGZv05RLHI)

Video of use of the exploration planner in a simulated RoboCup Rescue
scenario: [Youtube](https://www.youtube.com/watch?v=cd2FGMBj8iw)

## References

An overview can also be obtained from the following paper (available
[here](https://www.sim.informatik.tu-darmstadt.de/publ/download/2013_RoboCup_Kohlbrecher_open_source_tools.pdf)):


```
@INPROCEEDINGS{2013:RoboCup,
  author = {S. Kohlbrecher and J. Meyer and T. Graber and K. Petersen and O. von Stryk and U. Klingauf},
  title = {Hector open source modules for autonomous mapping and navigation with rescue robots},
  year = {2013},
  pages = {to appear},
  publisher = {Springer},
  series = {Lecture Notes in Artificial Intelligence (LNAI)},
  booktitle = {Proc. RoboCup Symposium 2013},
```

 The exploration approach used is based on the
following paper (available
[here](https://www.uni-koblenz.de/~agas/Documents/Wirth2007ETA1.pdf)):


```
@inproceedings{wirth2007exploration,
  title={Exploration transform: A stable exploring algorithm for robots in rescue environments},
  author={Wirth, S. and Pellenz, J.},
  booktitle={Safety, Security and Rescue Robotics, 2007. SSRR 2007. IEEE International Workshop on},
  pages={1--5},
  year={2007},
  organization={IEEE}
}
```


