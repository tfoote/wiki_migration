

```clearsilver
name = slam_backend
desc = The SLAM Backend provides an interface to graph construction and optimization tools. It essentially forms the map of our SLAM system and uses pose estimates from the visual odometry to form the nodes of a graph. It also corrects drift in the VO estimates when the Place Recognition node flags a match between views.

sub {
  0.name = vo/transform
  0.type = geometry_msgs/PoseWithCovarianceStamped
  0.desc = The robot's pose, twist and covariances calculated by the visual odometry node
  1.name = add_loop_closure
  1.type = slam_backend/AddLoopClosure
  1.desc = Message (from geometric_verification) which triggers the addition of both an interpolated vertex between existing nodes and an edge between the interpolated node and a new node corresponding to the robot's latest position, following the detection of a loop closure event.
}
pub {
  0.name = node_added
  0.type = slam_backend/NodeAdded
  0.desc = Notifies the image cache that a node has been added to the graph, transmits the timestamp of the VO message that triggered the addition together with the Vertex ID allocated to the node by the graph constructor.
  1.name = vertex_vis
  1.type = visualization_msgs/Marker
  1.desc = Publishes ellipses which denote the location and uncertainty of nodes in the SLAM graph.  Yellow ellipses denote standard vertexes generated as the result of integrating visual odometry.  Red ellipses are interpolated vertexes created when a loop closure event occurs.
  2.name = edge_vis
  2.type = visualization_msgs/Marker
  2.desc = Publishes white lines denoting edges between vertexes in the slam graph generated from visual odometry.
  2.name = loop_closure_vis
  2.type = visualization_msgs/Marker
  2.desc = Publishes red lines denoting edges between vertexes in the slam graph generated from loop closure events.
}
param {
  0.name = ~vo_topic
  0.type = string
  0.desc = The topic on which visual odometry is published
  0.default = /vo/odometry
  1.name = ~slam_map_frame
  1.type = string
  1.desc = Name of the world frame in which the map lives
  1.default = /slam_map
  2.name = ~node_sep
  2.type = double
  2.desc = Cumulative distance (in metres, in the visual odometry frame) which the robot should travel before creatig a new vertex in the graph.
  2.default = 1.0
  3.name = ~graph_publish_rate
  3.type = double
  3.desc = How often (in Hz) to publish visualization messages to rviz.
  3.default = 4
}
```



## Note about g2o compatibility

Using the latest version of libg2o (installed in package
ros-fuerte-libg2o) means this package will not compile. Instead download
the stable version of g2o from svn on openslam.org, remove the ros
version of the library and compile against the openslam version instead.
You may need to add the library directory using LD_LIBRARY_PATH
environment variable.
