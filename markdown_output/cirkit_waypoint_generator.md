This package generate waypoints for 2D navigation by using /map and
/odom, or /amcl_pose. An example of using the packages can be seen in
[Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

## About

-   You can add waypoint \...
-   by clicking a point in `Rviz`
-   by a ROBOT's exploring with `amcl` running, which adds a waypoint
    at every `dist_th` meters proceeding.
-   Tips
-   You can see the pose (angular-z) of waypoints under conditions that
    `tf`s show up in `Rviz` and set `scale` to around 10.
-   You can tune the pose of a waypoint by dragging a circle around the
    box (stands for the specified waypoint), which is still unstable
    though\...

## Nodes

### waypoint_generator

Generate waypoints.

```clearsilver
sub {
  0.name= /tf
  0.type= tf/tfMessage
  0.desc= Transforms (/map, /odom)
  
  1.name= /amcl_pose
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= Robot's estimated pose in the map, with covariance.
}
```

```clearsilver
param{
  2.name=dist_th
  2.type=double
  2.desc=Threshold of distance[m] for adding new waypoint
  3.name=yaw_th
  3.type=double
  3.desc=threshold of yaw angle[rad] for adding new waypoint
}
```

### waypoint_saver

Save generated waypoints by `waypoint_generator` to a CSV file.

### waypoint_server

Load a CSV file saved by `waypoint_saver` and show the loaded
`waypoints` in `Rviz`.

## Usage

### generate waypoints

```
$ rosrun waypoint_generator waypoint_generator
```

If you have already had waypoints file as point.csv,

```
$ rosrun waypoint_generator waypoint_generator --load path/to/point.csv
```

The waypoint file format is below.

```
x, y, z, qx, qy, qz, qw, is_searching_area, reach_threshold
```

### save waypoint

```
$ rosrun waypoint_generator waypoint_saver
```

### modify_waypoint

If the waypoint area is searching area, the you can make last colum
`1`. If you set it correct, the marker color will be yellow. The
normal color is green.

### check waypoints

If you want to check the waypoints, run the command as follows.

```
rosrun waypoint_generator waypoint_server --load path/to/waypoints.csv
```
