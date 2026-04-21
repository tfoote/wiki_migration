## Nodes

This package provide the `visualize` ROS Node that convert
[MTTD_msgs/People.msg](MTTD_msgs) to
[visualization_msgs/Markers.msg](visualization_msgs) compatible with
rviz.

In this way it's possible to visualize on rviz detected people (as
Markers) and relative Identification Number (ID).

![](attachment:visualize_screen.png)



```clearsilver
node.0{
 name = Visualize
 descr = People pose estimated and ID visualized on rviz

pub {
  0.name= /targets
  0.type= MTTD_msgs/People
  0.desc= Every marker rappresent a detected target (and his ID)
}
sub {
  0.name= /MTTDO1/peopledata
  0.type= geometry_msgs/PoseStamped
  0.desc=  Data about people detected (from [[ MTTD_interface | MTTD_interface ]])
}
}
```



## Roadmap

No roadmap or improvements scheduled (yet).
