Building this package will check out and build a custom version of rviz
in a sibling directory. The customized rviz package has the same name as
stock rviz. This can cause build problems if the stock rviz has higher
precedence in ROS_PACKAGE_PATH. The path to the shared_autonomy stack
should come before the path to the standard visualization stack.

Example of a correct ROS_PACKAGE_PATH: 

```
/home/duhadway/bosch-ros-pkg/stacks/shared_autonomy:/opt/ros/cturtle/stacks
```


