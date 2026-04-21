<http://rtc-us-ros-pkg.svn.sourceforge.net/viewvc/rtc-us-ros-pkg/trunk/rtcus_mobile_robots/rtcus_navigation/>

## General Description

This package proposes a reusable, generic and modular navigation
software architecture. It is built as a framework library for c++ and it
is based on generic programming through c++ templates. This can help to
solve some important and prone problems like the semantic coherence in
the reutilization of navigation components.

Example: ```cxx
template<typename StateType, typename ObstaclesType, typename ActionType, typename GoalType, typename TTime>
  class NavigationNode;

//specific templated navigation node
class DwaNavigationNode: public NavigationNode<DynamicState2D, pcl::PointCloud<pcl::PointXY>, Twist2D, Pose2D, ros::Time> DwaNavigationNode;
```

A reusable architecture should be applicable to many different contexts
(world models, kinematic constraints, state representation, world
models, asynchronous communications, etc.). Current mobile robot
navigation architectures are built on software forces the developer to
use a set of the data types for the representation of concepts like the
state, the obstacle world model or the goal (the ROS navigation stack is
one example).

Some planning algorithms cannot be built over these data type
constraints because they contradict the own nature of the algorithm. For
instance, an obstacle algorithm avoidance that uses point clouds to
represent obstacles cannot be built over the ROS navigation stack since
it is high coupled with the grid-based costmap world model, another
example is if the obstacle avoidance algorithm accepts multiple goals or
a probabilistic description of the goal.

**Note**: This is still an unestable component in development. For an
stable API see the standard \[navigation\]. Here an example of
navigation node developed with this framework it is shown:

[Youtube](https://www.youtube.com/watch?v=8cfzUUonIic)

**Note**: this software is still in active delopment and will be renamed
soon to RNTL: mobile Robot Navigation Template Library.
