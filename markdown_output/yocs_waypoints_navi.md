## Use

You can pass the waypoints and/or goal through a YAML file passed as
parameter, or with RViz. For the later, you need to add the Publish
Point tool (disable the Single Click option), included with RViz Hydro.
Once running, the waypoints_navi node listen for these points and the 2D
Nav Goal.

-   To command the robot to go to a goal by passing through a series of
    waypoints, use the Publish Point tool to specify the points and then
    provide the final goal in the traditional way.
-   To command the robot to constantly loop through a series of
    waypoints, use the Publish Point tool to specify the loop points and
    finish by clicking again on the first point.
-   If you use the 2D Nav Goal while already moving, current goal/patrol
    will be cancelled.
