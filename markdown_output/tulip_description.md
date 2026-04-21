# Package Summary

In this package the geometric, inertial and visual properties of
[TUlip](Robots/TUlip) are described in urdf files. It is used by the
package [tulip_gazebo](tulip_gazebo)

## Tf-tree

![](attachment:tulip_tf_tree.png) Above is an overview of the
transformation tree. This tree shows all joints and their links in
between. The offsets between the joints are indicated as well. The
transformation tree is constructed as follows:

-   **Torso**: this is the *base_link* of the transformation tree. A IMU
    sensor is attached to the torso. Six transformation trees are
    connected to the torso:
-   **Left leg**: the left leg consists of six revolute joints:
    *left_hip_yaw*, *left_hip_roll*, *left_hip_pitch*,
    *left_knee_pitch*, *left_ankle_pitch* and *left_ankle_roll*. These
    joints connect three actual links on the robot: *left_upperleg*,
    *left_lowerleg* and *left_foot*, and three 'massless' virtual
    links: *left_hipRoll2hipYaw*, *left_hipPitch2hipRoll*,
    *left_ankleRoll2anklePitch*. The left leg is connected to the torso
    through *left_hip_yaw*. At each corner of the left foot a force
    sensor is placed.
-   **Right leg**: the right leg consists of six revolute joints:
    *right_hip_yaw*, *right_hip_roll*, *right_hip_pitch*,
    *right_knee_pitch*, *right_ankle_pitch* and *right_ankle_roll*.
    These joints connect three actual links on the robot:
    *right_upperleg*, *right_lowerleg* and *right_foot*, and three
    'massless' virtual links: *right_hipRoll2hipYaw*,
    *right_hipPitch2hipRoll*, *right_ankleRoll2anklePitch*. The right
    leg is connected to the torso through *right_hip_yaw*. At each
    corner of the right foot a force sensor is placed.
-   **Left arm**: the left arm consists of two links: *left_upperArm*
    and *left_lowerArm* interconnect by a fixed joint:
    *left_elbow_roll*. The left arm is connected through a revolute
    joint: *left_shoulder_pitch* with the link: *left_shldrDnmxl* which
    is connected to the torso through a fixed joint:
    *left_torso2shldrDnmxl*.
-   **Right arm**: the right arm consists of two links: *right_upperArm*
    and *right_lowerArm* interconnect by a fixed joint:
    *right_elbow_roll*. The right arm is connected through a revolute
    joint: *right_shoulder_pitch* with the link: *right_shldrDnmxl*
    which is connected to the torso through a fixed joint:
    *right_torso2shldrDnmxl*.
-   **Neck**: The neck consists of three links: *torso2neckYaw*,
    *neckYaw2neckPitch* and *neckPitch2head* interconnected by two
    revolute joints: *neck_yaw* and *neck_pitch*. The head of the robot,
    which has two cameras for stereo vision, is connected to the neck
    through a fixed joint: *neck2headfix*. The neck and head are
    connected to the torso with the fixed joint: *neckDnmxlfix*.
-   **Logo**: The logo on the chest of the robot consists of two links:
    *tuelogo_blue* and *tuelogo_pink* interconnected by a fixed joint:
    *logofix2*. The logo is connected to the torso with a fixed joint:
    *logofix*.

## Folders and files

### Folder: "Media"

**materials/scripts:** Contains scripts for material properties of
TUlip.

### Folder: "meshes"

Contains the Collada meshes (dae) of all links of TUlip.

### Folder: "urdf"

Contains xacro macros that generate the urdf model of TUlip. The main
xacro macro is tulip.xacro. Also contains an urdf model of a soccer
ball.
