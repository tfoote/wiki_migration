(!) This package is still experimental. Feedback from early users are
appreciated.

## Usage



```
% rqt
```

 And choose `Launch` from `Plugins` menu.

See [UserGuide](https://index.ros.org/p/rqt) for more options.

## Feature

Sample image using `KDE`:
![launch top window](doc/launch_topwidget_kde.png) Sample image using
`Gnome`: ![launch top window](doc/snap_rqt_launch_3.png)

### Feature implemented

Users can:

- See all `.launch` files on the local file system, and select one in
  the pulldown menu.
- See all nodes defined in a `.launch` file. In the image above,
  elements of each row are (from left):

  -- --------------------------- -- --------------------- -- ------------------- -- --------------------- -- ---------- -- ------------------- -- --------------------- --
     name of instantiated node      number of times run      start&stop button      restart-able button      pkg name      .launch file name      `ARG` input field   
  -- --------------------------- -- --------------------- -- ------------------- -- --------------------- -- ---------- -- ------------------- -- --------------------- --

- Run and stop nodes individually
- Change `ARG` element value in `.launch` file before the node gets
  started
- Start and stop all nodes at once

### What rqt_launch does NOT do

This list is just a clarification/disclaimer. Enhancement request is
welcomed at Bugtracker (link is available at `Package Summary` of this
page).

- Edit `.launch` file
- Show hierarchy of included `.launch` files \-- nodes that are
  defined in included files are shown on the same level without being
  noted so.
- Error or any print output in each node's process is not caught.
- a workaround is to use
  [rqt_console](https://index.ros.org/p/rqt_console) along with
  `rqt_launch`

### Difference between roslaunch

[As noted here](https://index.ros.org/p/roslaunch),
[roslaunch](https://index.ros.org/p/roslaunch) doesn't guarantee that
the nodes start running in any order. In `rqt_launch`, however, nodes
get started in the order in the `.launch` file (still doesn't mean
that each process finished initialization procedure in the started
order - it depends on how much time they take).

### Design discussion

- [Discussion about requirements](https://github.com/ros-visualization/rqt/issues/57)

## Links

- [SIG roslaunch](sig/roslaunch) - not necessarilly tied though.
