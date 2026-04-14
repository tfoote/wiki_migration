## Documentation

Automatically import all entities simulated in
[ROS-enabled Gazebo](gazebo_ros) or described in a set of SDF files into
[rviz](rviz) through the [TF](rviz/DisplayTypes/TF) and
[Marker](rviz/DisplayTypes/Marker) plugin. Furthermore add objects from
a SDF as MoveIt collision objects.

This package contains the following (Python) nodes:

-   \'\'gazebo2tf_node.py\'\' translates /gazebo/link_states to TF in a
    hierarchical manner corresponding to SDF \<include\>.
-   \'\'gazebo2marker_node.py\'\' retrieves the current gazebo models
    from /gazebo/model_states, parses their corresponding SDF file and
    sends visualization_msgs/Marker messages for each link (either
    visual or collision) to /visualization_marker used by the rviz
    Marker plugin (fixed frame is gazebo_world). With this solution no
    plugin for either gazebo or rviz is required, only already available
    interfaces are used.
-   \'\'sdf2marker_node.py\'\' loads a specified SDF model and publishes
    it as rviz Marker. Note that an accordingly named TF must exist
    (e.g.
    `rosrun tf2_ros static_transform_publisher 0 0 0  0 0 0 1 world SDF_model_link_name`)
    or fixed frame adjusted.
-   \'\'sdf2tfstatic_node.py\'\' publish all relations between SDF links
    (according to model joints) to static TF.
-   \'\'sdf2extract_tfstatic_node.py\'\' publish a selected relation
    between two SDF links as static TF.
-   \'\'sdf2moveit_collision.py\'\' add objects from a SDF as MoveIt
    collision objects (with the ability to ignore submodels).

[Here is a small usage example](http://andreasbihlmaier.github.io/2014/02/19/gazebo2rviz.html)
