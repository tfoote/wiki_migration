## Installation

The easiest way to get the mocap_nokov package in Ubuntu is using
`apt-get`: ```
$ sudo apt-get install ros-noetic-mocap-nokov
```

If you'd like to contribute to the package, feel free to check it out
from Github and submit pull requests.

## Configuring XINGYING Software

You will need to configure it for streaming of rigid bodies to the
(virtual)machine running the mocap_nokov ROS node.

1\. Open the View Menu -> Data Casting Pane, turn off the SDK Enable
checkbox. 2. Focus the local Address label and select the NIC Addresss
combox, choose the boradcast interface. 3. Focus the "SDK Streaming"
region, then enable the "SDK Enabled" checkbox.
![](attachment:xingying3.0.png)

## Configuring mocap_nokov

Once motion capture data is being streamed to the mocap_nokov node, the
mapping of trackables to ROS topics must be defined. A sample
configuration file called "mocap.yaml" is included with the package,
you can find it in the config directory of the package.

```
$ roscd mocap_nokov/config
$ vim mocap.yaml
```

### Selecting Rigid Bodies to Publish

Since multiple robots may be tracked by the Nokov system, the
mocap_nokov configuration allows for publishing poses and transforms for
each robot separately.

The robot must be set up as a RigidBody and id start from 1,arrange from
left to right

The server_address should set to XINGYING NIC Addresss, e.g 192.168.1.20

The published topics for each trackable can now be configured in
mocap_nokov. Each trackable that should be published in ROS can be
specified by its Trackable ID - the desired topics for the published
Pose, 2D Pose and the frame_id of the transform in tf can be configured.
```
rigid_bodies:
    '1':
        pose: Robot_1/pose
        pose2d: Robot_1/ground_pose
        frame_id: Robot_1/base_link
    '2':
        pose: Robot_2/pose
nokov_config:
        server_address: "192.168.1.20"
``` If any of the topics is left unconfigured,
nothing will be published for that datatype. E.g. for trackable "2",
no pose2d or frame_id is configured so no Pose2D or TF messages will be
published. ![](attachment:rostopic.png)

### Results

RViz visualzing the TF and the pose streamed from the nokov system
```
$ roslaunch mocap_nokov mocap.launch & rosrun rviz rviz
``` select the Global Options and set the Fixed
Frame to world, and you can add tf and pose to display, like this
![](attachment:rviz_only.png)

## Further reading

The Specific use cases are available for reference
<https://www.nokov.com>

## QA
