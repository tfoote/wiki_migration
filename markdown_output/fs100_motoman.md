## Overview

Source: <https://github.com/DTU-AUT/fs100_motoman.git>

The fs100_motoman package was created together with the Technical
University of Denmark (DTU), Institute for Automation and Control
(<http://www.aut.elektro.dtu.dk/>). The reason for this package was to
provide an easy way to continuously stream a trajectory to the FS100
controller, to enable real-time sensor based control.

## Installation

The fs100_motoman package can be installed with 

```
sudo apt-get install ros-hydro-fs100-motoman
```


or by downloading the source code and compiling it.

## Design

The package is designed to enable continuous trajectory streaming. A
topic is used to transfer data from outside nodes to the mh5l_traj node.
Because of this, no feedback is givin for the trajectory points send,
and the user needs to subscribe to the joint_states topic to enable a
closed loop control. The node connect to the FS100 controller over
ethernet socket, and communicates with the simple message format. The
package includes the simple message format created by Southwest Research
Institute, and used in the MotoROS programs. When a point is recieved,
it is stored in a queue, that is executed as fast as possible. The
MotoROS can only recieve one point at a time, and will refuse subsequent
points until the first point has been proccessed.

## Performance

The fs100_motoman is able to stream points at 40 Hz. If points are
streamed at this rate, smooth motions can easily be performed. The
fs100_motoman has no speed violation check on the input given. This
allows the user to send a trajectory point with too large
position/velocity difference, triggering an error on the controller. The
user needs to keep this in mind when sending trajectory points, perhabs
do a filtering of the trajectory before streaming it.

## Nodes



```clearsilver
name = mh5l_traj
desc = Opens connection with FS100 controller with MotoROS installed. Publishes joint states in topics and subscribes to JointTrajectoryPoint topic for goal position. The robot has a reaction delay of ~0.2 sec.
sub {
  0.name = fs100_motoman/mh5l/joint_target
  0.type = trajectory_msgs/JointTrajectoryPoint
  0.desc = Data published to this topic is put into an internal queue, that is executed as fast as possible. Publishing faster than points can be executed can result in delayed movement. The Duration specified in the message contains the duration of the movement sent, not the duration from the start of the trajectory.
}
pub {
  0.name = fs100_motoman/mh5l/joint_state
  0.type = sensor_msgs/JointState
  0.desc = The current robot state. The data recieved from the FS100 controller is delayed ~0.2 sec.
}
srv {
  0.name = fs100_motoman/mh5l/reset_trajectory
  0.type = fs100_motoman/setReset
  0.desc = Resets the internal queue and variables (absolute time, sequence number).
}
param {
  0.name = IP
  0.type = string
  0.desc = The nodes expects an IP to be provided as an argument.
}
```



## Report a bug

Use github to report a bug and view current issues.
<https://github.com/DTU-AUT/fs100_motoman/issues>
