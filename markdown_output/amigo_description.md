# Package Summary

This package describes the visual and mechanical properties of the
[AMIGO robot](Robots/AMIGO). It is used by the package
[amigo_gazebo](amigo_gazebo).

## Tf-tree

[ {{attachment:tf-tree-small.png}}](attachment:tf-tree.png ) Above is an
overview of the transformation tree, in short tf-tree. This tree shows
the joints that are actuated and their links in between. A purple joint
is fixed, a blue joint is revolute, a red joint is prismatic and a green
joint is continuous. If the orientation of the joints changes this is
indicated by a picture of the new coordinate system. The offsets between
the joints are indicated as well, these changes apply after rotating the
coordinate system.

The four wheels each have a different orientation, the joints describe a
circle where the y-axis is always tangent to this circle, and the x-axis
is always pointing out of, or away from, the circle. The z-axis in these
orientations is always pointing up. The offset is unique for each of the
four wheels, for example the left rear wheel has a positive y offset and
a negative x offset.

Similarly the left shoulder_mount_joint has a negative y offset (y is
pointing in the opposite direction here) and the right
shoulder_mount_joint a positive y offset.

## Folders and files

### Folder: \"Description\"

**arm_extra_visuals:** In here all visual links and corresponding joints
in the arms that cannot be mapped to the tf-tree are found. So it
contains the black cylinders that seal the arms, the elbow links and
wrist links.

**arms:** All links and joints of the arms that are in the tf-tree above
can be found here.

**body:** All links and joints of the spindle, torso and bottomcovers
that are in the tf-tree can be found here. The bottomcovers have a
deviating bounding box because a normal one would be too inaccurate.
Therefore separate bounding boxes are added for the batteries and
computers on amigo. Also, in base_link all values are 0 because this
link only serves as a root to the tf-tree. The link for the spindle is
called 'torso_slider'.

**body_extra_visuals:** This folder contains all visual links and
corresponding joints of the body that cannot be mapped to the tf-tree.
This means it contains the links for the metal sliders next to and
behind the spindle, the objects that seal the body and the clavicles.

**head:** In here are all links and joints for the head of amigo.

**kinect:** The joints and links that represent the Kinect camera are in
here.

**laser:** The links and joints for the laser and tue-logo can be found
here.

**media:** This folder contains all the textures and corresponding
scripts.

**wheels:** All links and joints for the wheels are found here.

**gazebo:** Contains the relevant information about gazebo plugins and
the sensors in gazebo.

**sim_or_robot_xacro:** Depending on which files of these is included
during launch the description files for the robot in simulation or the
real robot are loaded.

**robot.urdf.xacro:** The main file that calls all other urdf.xacro
files.

**materials.urdf:** This file contains the definitions of colors and
textures for rviz.

**definitions.urdf:** Contains the definitions for the my_link and
my_joint macro's.

### Folder: \"Media\"

**materials/scripts:** Contains a script for each texture used in the
robot description.

**materials/textures:** The texture jpg files are in here.

**meshes:** Contains the mesh collada (dae) files.
