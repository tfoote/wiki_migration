This repository will contain the ROS packages of the robotics research
group at the
[School of Computer Science and Engineering (CSE)](http://www.cse.unsw.edu.au)
at the University of New South Wales, Australia.

## History

The \'\'\'crosbot\'\'\' packages were originally part of the
\'\'\'CASRobot\'\'\' software suite developed within the
[ARC Centre of Excellence for Autonomous Systems (CAS)](http://www.cas.edu.au)
in the School of Computer Science and Engineering (CSE) for research and
teaching purposes.

Many of these components have now been ported to ROS and will continue
to be maintained and developed as ROS packages. To date, the focus of
the robotics team at CSE has been on
[Robocup Rescue](http://wiki.robocup.org/wiki/Robot_League) related
challenges and consequently the focus of these packages reflects these
origins. In particular there are a number of packages for mapping and
localisation, as well as interfaces for semi-autonomous robot control.

## Available Software

### Crosbot Base

This includes mobile base control and a packages that can be used as
alternatives to the standard ROS 2D navigation stack.

### SLAM

These SLAM modules can be used as a replacement for the standard
gmapping packages. They offer further functionality such as embedding of
landmarks and components in the map.

### Odometry and Positioning

Wheel encoders and odometry cannot always be relied on, especially in a
urban search and rescue type environment. These packages use iterative
closest point (ICP) algorithms to provide accurate positioning.

### Robot GUI

User interface and visualisation tools that can be used to provide
semi-autonomous control of a robot.
