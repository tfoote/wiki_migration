## Introduction

Given a bagfile of \<\<MsgLink(calibration_msgs/RobotMeasurement)\>\>
collected using the
[pr2_calibration_executive](pr2_calibration_executive) package (or
similar), pr2_calibration_estimation uses this data along with several
configuration configuration files to estimate various parameters for the
PR2.

\'\'Technical Explanation:\'\' This is a multi-step nonlinear optimizer
that uses scipy\'s levenberg-marquardt optimizer,
[ scipy.optimize.leastsq](http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html ),
to estimate various parameters of the PR2 using a bundle adjustment like
framework.

## Stability

This package is still unstable, and does not have a released API.

## Concepts

This stack is still very experimental, and we have not standardized (let
alone even reviewed) many of the internal APIs in this stack. However,
it seems that many people are still interested in porting this unstable
code to other robot platforms. We are providing the information below to
help others port this stack to their robots, even though it is an
unstable stack.

### Launching the Estimator

The main goal of the pr2_calibration_estimation package is to provide a
reconfigurable nonlinear optimizer for estimating calibration parameters
for some defined robot. For the PR2, the estimator is launched using
[ pr2_calibration_launch/estimate_params/config_pr2_beta/estimate_pr2_beta.launch](https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_calibration/trunk/pr2_calibration_launch/estimate_params/estimate_pr2_beta.launch ).
This launch file loads the estimation configuration onto the parameter
server and then launches the estimator (multistep_cov_estimator.py).

#### Estimator Command Line Usage

\'\'\'\`multistep_cov_estimator.py\`\'\'\'\` \[bagfile\]
\[target_dir\]\`

-   \`\[bagfile\]\` - Path to the bag that contains calibration samples.
    These messages must be of type
    \<\<MsgLink(calibration_msgs/RobotMeasurement)\>\> under the topic
    &ldquo;/robot_measurement&rdquo;
-   \`\[target_dir\]\` - Directory at which to store intermediate data
    files after each calibration step

#### Estimation Configuration (Parameter Server)

The estimator looks for it\'s configuration in the
\`/calibration_config\` namespace. The PR2\'s configuration is stored in
[ pr2_calibration_launch/estimate_params/head_then_arms_params.launch]( https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_calibration/trunk/pr2_calibration_launch/estimate_params/head_then_arms_params.launch )

-   \`initial_system\` - yaml blob that defines all of the robot\'s
    primitives
-   \`sensors\` - Every parameter in this namespace must be a yaml blob
    that defines sensors on the robot.
-   \`cal_steps\` - Defines each of the calibration steps. Each step is
    defined by a namespace within \`cal_steps\`, and the steps are
    executed in alphabetical order by namespace names.
-   \`use_cov\` (\`bool\`) - Specify whether or not to use measurement
    covariances during this step. If \`True\`, then covariances are used
-   \`free_params\` - yaml blob that defines which parameters are being
    estimated during this step
-   \`sensors\` - list of sensor_ids that defines which sensors to use
    during this calibration step. Any sensor specified must have a full
    definition in the higher level \`sensors\` namespace.
-   \`output_filename\` - Identifier for the results of this calibration
    step. This name is prepended to the step\'s results, and stored in
    the estimator\'s previously defined \`\[target_dir\]\`

### The Calibration Bagfile

The estimator relies on calibration samples in the specified bagfile in
order to run the calibration. These messages must be of type
\<\<MsgLink(calibration_msgs/RobotMeasurement)\>\> under the topic
\`/robot_measurement\`. Below is a description of all of the fields, and
what they mean:

-   \`sample_id\` - This simply a string identifier to help the user
    understand where this calibration sample came from. It doesn\'t even
    have to be unique across samples
-   \`target_id\` - Specifies which target the sensors in the sample are
    looking at. This must correspond to the name of a checkerboard
    primitive. For the PR2, this can be either \`small_cb_4x5\` or
    \`large_cb_7x6\`.
-   \`M_cam\` - Stores data from a single camera measurement
-   \`header\` - Not Used
-   \`sensor_id\` - Name of the camera sensor. This must correspond to a
    camera primitive defined for the robot. (See
    [#Rectified_Cameras](#Rectified_Cameras))
-   \`image_points\` - Stores the corners of the detected checkerboard
    target. This list is ordered, and must correspond to the same
    ordering of corners as openCV\'s checkerboard detector would detect
    the checkerboard specified in \`target_id\`.
-   \`cam_info\` - Store the intrinsics for this camera
-   \`M_laser\` - Stores data for a tilting laser sensor
-   \`header\` - Not used
-   \`laser_id\` - Name of the tilting laser. Must correspond to a
    tilting laser primitive defined for the robot. See
    [#Tilting_Lasers-1](#Tilting_Lasers-1).
-   \`joint_points\` - Each joint point corresponds to a tilt, bearing,
    and range for a single detected corner.
-   \`M_chain\` - Stores data for a specific kinematic chain
-   \`header\` - Not used
-   \`chain_id\` - Name of the chain. Must correspond to a chain
    primitive defined for the robot. See [#DH_Chains](#DH_Chains)
-   \`chain_state\` - Store the state of the joints that are a part of
    this chain. Must be ordered from root to tip of the chain and cannot
    have any joints that don\'t correspond to this chain

### Defining the Robot\'s Primitives

The calibration estimator relies on a yaml file that stores the
configuration of the robot\'s various kinematic and sensor primitives
that we may want to estimate. For the PR2, this file is
[ pr2_calibration_launch/estimate_params/config_pr2_beta/system.yaml]( https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_calibration/tags/boxturtle/pr2_calibration_launch/estimate_params/config_pr2_beta/system.yaml ).
The currently support primitives are dh_chains, tilting_lasers,
transforms, and rectified cameras. Although not necessarily a \"robot
primitive\", checkerboard intrinsics are also defined in this file.

#### DH Chains

A DH Chain primitive is used to represent a kinematic linkage using
[ Denavit-Hartenberg parameters](http://en.wikipedia.org/wiki/Denavit-Hartenberg_Parameters ).
Each DH Chain primitive must be included as a dictionary element under
the \`dh_chains\` section of the config file. The parameters defined
below are used in
[ pr2_calibration_estimation/dh_chain.py](https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_calibration/tags/boxturtle/pr2_calibration_estimation/src/pr2_calibration_estimation/dh_chain.py )

Example: ```
right_arm_chain:
   dh:
   - [   0,  -pi/2, .1, 0      ]    # r_shoulder_pan_joint
   - [ pi/2,  pi/2,  0, 0      ]    # r_shoulder_lift_joint
   - [   0,  -pi/2,  0, .4     ]    # r_upper_arm_joint
   - [   0,   pi/2,  0, 0      ]    # r_elbow_flex_joint
   - [   0,  -pi/2,  0, .321   ]    # r_forearm_roll_joint
   - [   0,   pi/2,  0, 0      ]    # r_wrist_flex_joint
   - [   0,    0,    0, 0      ]    # r_wrist_roll_joint
   cov:
     joint_angles: [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001]
   gearing: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
```

-   \'\'\'dh\'\'\' - Each list item under \`dh\` stores the 4 DH
    parameters for a link. They are ordered as \[theta, alpha, a, d\].
    In the example above, there are 7 links.
-   \'\'\'cov/joint_angles\'\'\' - Defines a standard deviation (in
    radians) for each joint angle. This list must be the same length as
    the dh parameter list.
-   \'\'\'gearing\'\'\' - Defines a prescalar for each joint angle,
    before applying forward kinematics. This list must be the same
    length as the dh parameter list. In general, these values are known
    extremely well (since you can count the gear teeth in the
    transmission). However, it is important to estimate these parameters
    when dealing with belts and drums.

Note that we have not defined where this kinematic chain is rooted on
the robot. This is done later, when defining sensors.

#### Transforms

A transform primitive is a full 6 dof transformation in a robot system.
As defined here, it is very unclear where and how these transforms
attach to actual robot frames. Later, when we define sensors, we can
attach these transforms before and after dh chains.

6 Examples: ```
head_plate_frame_joint:    [   .0232, .0, .0645, 0, 0, 0]
  double_stereo_frame_joint: [ 0, 0, .003, 0, 0, 0]
  wide_stereo_frame_joint:   [ 0, .03, .0305, 0, 0, 0  ]
  narrow_stereo_frame_joint: [ 0, .06, .0305, 0, 0, 0  ]
  wide_stereo_optical_frame_joint:    [0, 0, 0, -1.20919, 1.20919, -1.20919]
  narrow_stereo_optical_frame_joint:  [0, 0, 0, -1.20919, 1.20919, -1.20919]
```

Each transform is defined by a list with 6 elements:

-   \'\'\'Elements 0:2\'\'\' - Translation terms. Elements 0,1,2
    correspond to an x,y,z translation vector
-   \'\'\'Elements 3:5\'\'\' - Rotation terms. Elements 3,4,5 correspond
    to an x,y,z rotation vector. The direction of the vector is the axis
    of rotation, and the magnitude of the rotation vector is the
    rotation angle. See
    [ Wikipedia: Rotation Representation](http://en.wikipedia.org/wiki/Rotation_representation#Euler_axis_and_angle_.28rotation_vector.29 )
-   Why are we using this rotation representation? We could very well
    have used rotation matrices or quaternions. Both of these
    representations introduce constraints on the system, which we were
    hoping to avoid. Ideally, we would completely avoid optimizing in a
    specific rotation space, and instead, operate directly on the
    rotations themselves, using incremental rotations. See
    [ Skew Parameters](http://en.wikipedia.org/wiki/Rotation_matrix#Skew_parameters_via_Cayley.27s_formula )

#### Tilting Lasers

The tilting laser primitive is used to represent a laser rangefinder
(such as the
[ UTM-30lx](http://www.hokuyo-aut.jp/02sensor/07scanner/utm_30lx.html ))
that is actuated.

Example: ```
tilt_laser:
    before_joint: [ .09893, 0,  .227, 0, 0, 0]
    after_joint:  [  0, 0,  .03,  0, 0, 0]
    gearing: 1.0
    cov:
      bearing: 0.0005
      range: 0.005
      tilt: 0.0005
```

![](attachment:tilting_laser.png)

-   \'\'\'before_joint\'\'\' - Transform from the system origin to the
    joint axis of the tilting platform. The tilting platform rotates
    around the y-axis of the resulting frame
-   \'\'\'after_joint\'\'\' - Transform from the rotating axis on the
    tilting platform to the optical center of the laser rangefinder. We
    assume that a a 0 degree bearing measurement from the laser
    rangefinder is along the x axis of the resulting frame, and a 90
    degress bearing measurement is along the y axis of the resulting
    frame.
-   \'\'\'gearing\'\'\' - Prescalar for the tilting joint, before
    applying forward kinematics. Similar to the \'\'gearing\'\' element
    in the dh chain, except we only have 1 joint, and thus don\'t need a
    list.
-   \'\'\'cov\'\'\'
-   \'\'\'bearing\'\'\' - !StDev for the bearing angle for the tilting
    laser (in radians)
-   \'\'\'range\'\'\' - !StDev for range measurement for the tilting
    laser (in radians)
-   \'\'\'tilt\'\'\' - !StDev for tilting angle for the tilting laser
    platform (in radians)

#### Rectified Cameras

The recified camera primitive is used to represent a monocular camera
that has already been rectified. We assume that the distortion
correction is perfect, and we only have estimate parameters associated
with the pinhole camera model.

Example: ```
wide_left_rect:
    baseline_shift: 0.0
    f_shift: 0.0
    cx_shift: 0.0
    cy_shift: 0.0
    cov: {u: 0.125, v: 0.125}
```

-   \'\'\'baseline_shift\'\'\' - Value to add to the \`-baseline\*Tx\`
    term in the projection matrix (\`camera_info.P\[3\]\`)
-   \'\'\'f_shift\'\'\' - Value to add to the focal length term in the
    projetion matrix (\`camera_info.P\[0\]\` & \`camera_info.P\[5\]\`)
-   \'\'\'cx_shift\'\'\' - Value to add to the cx term in the projetion
    matrix (\`camera_info.P\[2\]\`)
-   \'\'\'cy_shift\'\'\' - Value to add to the cy term in the projetion
    matrix (\`camera_info.P\[6\]\`)
-   \'\'\'cov\'\'\'
-   \'\'\'u\'\'\' - !StDev of uncertainty along u axis of the image (in
    pixels)
-   \'\'\'v\'\'\' - !StDev of uncertainty along v axis of the image (in
    pixels)

#### Checkerboards

Although the checkerboards themselves aren\'t really a part of the
robot, they still have parameters that need to be defined and could be
estimated. Thus this file becomes a convenient location to define them.

2 Examples: ```
small_cb_4x5:
    corners_x: 4
    corners_y: 5
    spacing_x: .025
    spacing_y: .025
  large_cb_7x6:
    corners_x: 7
    corners_y: 6
    spacing_x: .108
    spacing_y: .108
```

-   \'\'\'corners_x\'\'\' - Number of corners along the x-axis of the
    checkerboard. This is an integer parameter, and will not be changed
    by the estimator.
-   \'\'\'spacing_x\'\'\' - The x-axis spacing between checkerboard
    corners.

corners_y and spacing_y have the same semantics as corners_x and
spacing_x

### Defining the Robot\'s Sensors

Once we have a set of primitives defined for the robot, we need to
define a set of sensors that are attached to the robot. The sensors
simply string various primitives together into actual measurement
models. There currently are three types of sensors: \`camera_chains\`,
\`tilting_lasers\`, \`chains\`.

The sensors used in the PR2 estimation are defined at
[ pr2_calibration_launch/estimate_params/config_pr2_beta/sensors.yaml ]( https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_calibration/tags/boxturtle/pr2_calibration_launch/estimate_params/config_pr2_beta/sensors.yaml ).
This is a yaml file broken down by sensor type. For each sensor type,
there is a list of sensors.

#### Camera Chain

This sensor is used to define a camera that is attached to an actuated
linkage. The standard example of this is a camera on a pan-tilt
platform:

```
camera_chains:
  - camera_id: forearm_right_rect
    sensor_id: forearm_right_rect
    chain:
      before_chain: [r_shoulder_pan_joint]
      chain_id:     right_arm_chain
      after_chain:  [r_forearm_roll_adj, r_forearm_cam_frame_joint,
                     r_forearm_cam_optical_frame_joint]
      dh_link_num:  4
```

-   \'\'\'sensor_id\'\'\' - Unique identifier for this sensor
-   \'\'\'camera_id\'\'\' - Monocular camera being used for this sensor.
    Must match a rectified camera primitive
-   \'\'\'chain\'\'\' - (Collectively define the linkage that the camera
    is attached to)
-   \'\'\'before_chain\'\'\' - Ordered list of transforms to apply
    before attaching DH Chain. Must all be transform primitives
-   \'\'\'chain_id\'\'\' - DH chain primitive to attach to the end of
    the \'\'before chain\'\' tranforms.
-   \'\'\'dh_link_num\'\'\' - Define how many DH links to use. In many
    cases, we don\'t want to use the entire DH Chain. In this example,
    the forearm camera is attached to the DH link indexed at 4 (which is
    the forearm_roll_link).
-   \'\'\'after_chain\'\'\' - Transforms to apply after applying the DH
    chain. The camera is then attached to the end of these transforms.
    We are assuming a &ldquo;Z Forward, X Right, Y Down&rdquo; camera

This sensor will only be used with a sample
(\<\<MsgLink(calibration_msgs/RobotMeasurement)\>\>) with the following
requirements:

-   The message must have a !CameraMeasurement that matches the
    sensor\'s \`camera_id\`
-   The message must have a !ChainMeasurement that matches sensor\'s
    \`chain_id\`

#### Chains

A chain sensor is a sensor that can hold a checkerboard.

Example: ```
chains:
  - sensor_id:    left_arm_chain
    before_chain: [l_shoulder_pan_joint]
    chain_id:     left_arm_chain
    after_chain:  [left_arm_tip_adj, left_arm_cb]
    dh_link_num:  6
```

-   \'\'\'sensor_id\'\'\' - Unique identifier for this sensor
-   The \'\'\'before_chain\'\'\', \'\'\'chain_id\'\'\', and
    \'\'\'after_chain\'\'\' have the same meaning as in the
    camera_chain. The checkerboard target is attached the the kinematic
    chain after after_chain transforms.

This sensor will only be used with a sample
(\<\<MsgLink(calibration_msgs/RobotMeasurement)\>\>) with the following
requirements:

-   The message must have a !ChainMeasurement that matches sensor\'s
    \`chain_id\`
-   The message\'s \`chain_id\` must match the sensor\'s \`chain_id\`.
    This ensures that the target is in fact being held with the
    specified chain.

#### Tilting Lasers

All the information that we need about a tilting laser is already in
robot primitive definitions. Thus, all we need to do is specify the name
of the tilting laser primitive, along with a unique sensor_id.

Example: ```
tilting_lasers:
    - sensor_id: tilt_laser
      laser_id:  tilt_laser
```

This sensor will only be used with a sample
(\<\<MsgLink(calibration_msgs/RobotMeasurement)\>\>) with the following
requirements:

-   The message must have a !LaserMeasurement that matches sensor\'s
    \`laser_id\`

### Defining Which Parameters to Estimate

For each estimation step, we need to specify which parameters we want to
estimate. This is done using a yaml file that looks extremely to the
primitives definition file, except that instead of having values for all
the parameters, it is filled with \`0\`s and \`1\`s. All parameters with
\`1\`s will be estimated. These are defined for the pr2 as
[ pr2_calibration_launch/estimate_params/config_pr2_beta/free\_\*.yaml](https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_calibration/tags/boxturtle/pr2_calibration_launch/estimate_params/config_pr2_beta ).

## How the estimation works

The main thing that the package does is take all of these previously
specified configuration files and generate a Jacobian based on the
measurements in the previously collected calibration bagfile
(\`cal_measurements.bag\`). The following diagram gives an overview of
what this Jacobian looks like:

![](attachment:jacobian.png)

### Rows

There is one blockrow for each
\<\<MsgLink(calibration_msgs/RobotMeasurement)\>\> on the
\`robot_measurement\` topic. Each of the messages is called a sample.
For each sample, there are multiple sensor measurements inside, where
each sensor is its own sub-blockrow. Each sensor has multiple rows,
where the number of rows is determined based on the number of feature
points detected, and the type of measurement. For instance, a tilting
laser has 3 rows per feature point (cartesian x,y,z) and a camera has 2
rows per feature point (image u,v).

### Columns

The columns are separated into two sections: system parameters and
checkerboard poses.

-   \'\'\'System parameters\'\'\' This section is based off of the
    \`system.yaml\` file passed into the estimation. This contains all
    of various parameters that define the robot system: transforms, dh
    parameters, tilting laser kinematics, stereo baselines, etc. These
    columns answer the question of \'\'\"If I change parameter X in my
    system, how does the error residual of my samples change?\"\'\'.
-   \'\'\'Checkerboard Poses\'\'\' This section defines a checkerboard
    pose for each robot measurement. This answers the question of
    \'\'\"If I move checkerboard J, how does the error residual of my
    samples change?\"\'\' Note that this part of the Jacobian is block
    diagonal. That is, altering the 1st checkerboard pose does not
    affect the 2nd sample.
