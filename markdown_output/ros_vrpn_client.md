## Demonstration Video

. [Youtube](https://www.youtube.com/watch?v=oOFkEIydl_4)

## Hardware Setup

-   There are a number of devices for which VRPN servers are available.
    See complete list on the VRPN
    [website](http://www.cs.unc.edu/Research/vrpn/).
-   We have tested this code with the
    [OptiTrack](http://www.naturalpoint.com/optitrack/) system from
    Natural Point, using the VRPN server implemented in the
    [Tracking Tools](http://www.naturalpoint.com/optitrack/products/tracking-tools/)
    software.
-   Currently, this code only publishes the position and orientation of
    the tracked objects (Not the velocities, accelerations etc.)
-   Some of the instructions below might be specific to the Tracking
    Tools software.

## Installation

-   Use the install_vrpn.sh scirpt in the package to download, compile,
    and install VRPN.
-   Please consult the
    [VRPN website](http://www.cs.unc.edu/Research/vrpn/) if your run
    into some trouble.

## Running the code

1\. Run node from command line to track an object whose name is
Trackable1: 

```
$ rosrun ros_vrpn_client ros_vrpn_client __name:=Trackable1 _vrpn_server_ip:=192.168.2.110
```

 1. visualize in rviz:


```
$ roslaunch ros_vrpn_client demo.launch
```

 1. check rate at which object is being tracked:


```
$ rostopic hz /Trackable1/pose
```

 We can track objects at 100Hz.

## TF coordinate frames

1\. /optitrak

-   world frame that we will use.
-   X axis is along the x axis of the clibration pattern.
-   Z axis is vertically up.

1\. Every tracked object has a coord frame whose TF name is the name of
the ros node (given from the launch file or command line).

-   Hitting "Reset To Current Orientation" in the Tracking Tools
    software (Trackable properties) aligns the object coord frame with
    the /optitrak frame.

## Nodes

### ros_vrpn_client

-   Run a new instance of this node for each tracked object.
-   The name of this node should be the same as the *Trackable* name
    published via VRPN, and will be the name of the TF coordinate frame
    for this object.



```clearsilver
pub {
 0.name= ros_vrpn_client/pose
 0.type= geometry_msgs/TransformStamped
 0.desc= Pose of the tracked object.
 1.name= /tf
 1.type= tf/tfMessage
 1.desc= TF message with coordinate transformation for the tracked object.
}
param {
 1.name= ~vrpn_server_ip
 1.type= string
 1.desc= IP address of the computer running the VRPN server.
 2.name= ~vrpn_port
 2.type= int
 2.default= 3883
 2.desc= port number for the VRPN.
}
```


