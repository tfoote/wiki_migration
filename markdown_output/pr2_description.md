This package contains the description of the PR2 robot. It supercedes
the older [pr2_defs](pr2_defs) package which was written for the alpha
hardware.

### Package organization

This package contains robot description files for PR2, organized into
subdirectories as follows:

-   `urdf/` contains ([xacro](xacro) representations of) [urdf](urdf)
    descriptions of various parts of the PR2 (arm, torso, etc.).
-   `robots/` contains ([xacro](xacro) representations of)
    [urdf](urdf) descriptions of the full robot, that refer to the
    macros in `urdf/`
-   `gazebo/` contains ([xacro](xacro) representations of)
    [urdf](urdf) descriptions of simulated PR2 components, like the
    simulated battery controller.
-   `meshes/` contains mesh files (`.stl`,`.dae`) for
    visualization and collision properties.

### Changes from Alpha URDFs

Some notable changes from [pr2_defs](pr2_defs):

-   updated `frame_id`: `base_laser` &rarr; `base_laser_link`
    (consistent with tilt_laser_link)
-   new `frame_id`:
    `{narrow,wide}_stereo_{l,r}_stereo_camera_optical_frame`
-   removed frame: `plug_holder` (might need to add back for
    plug_in_gazebo to work)

## PR2 Coordinate Frames

To see the PR2 URDF graphically, you can ```
rosrun xacro xacro `rospack find pr2_description`/robots/pr2.urdf.xacro > pr2.urdf
urdf_to_graphiz pr2.urdf
evince pr2.pdf
``` A
snapshot (r46956) is attached [here](attachment:pr2_description/pr2.pdf)
for reference.

In general, PR2 URDF contains a tree structured set of links and joints,
with `base_footprint` as the root link of the tree.

## Working with a Kinect

To use the original Kinect with the PR2 (either robot or simulation),
set the KINECT1 environment variable to true. ```
export KINECT1=true
```
To use a Kinect2 with the PR2 (either robot or simulation), set the
KINECT2 environment variable to true. ```
export KINECT2=true
``` If both
variables are set, the Kinect 2 will take precedence over the original
Kinect.

------------------------------------------------------------------------

[CategoryURDF](CategoryURDF)
