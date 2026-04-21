## Overview

This tool was developed to convert CAD models to URDF models
semi-automatically. It makes use of the XML files exported by the
[SimMechanics Link](http://www.mathworks.com/products/simmechanics/description4.html)
. Mathworks, makers of !SimMechanics, have developed plugins for a
couple of leading CAD programs, including !SolidWorks, !ProEngineer and
Inventor.

For more information on using this package, please see the tutorial on
[converting SimMechanics to URDF](/Tutorials/Converting SimMechanics To URDF)

## Compatibility

This package has only been tested using !SimMechanics Link Version 3.2
with !ProEngineer 4.0 and 5.0.

## How it Works

The !SimMechanics Link creates an XML file (PhysicalModelingXMLFile) and
a collection of STL files. The XML describes all of the bodies,
reference frames, inertial frames and joints for the model. The script
`convert.py` takes this information and converts it to a URDF. However,
there are some tricks and caveats, which can maneuvered using a
parameter file. Not using a parameter file will result in a model that
looks correct when not moving, but possibly does not move correctly.

### General Usage

-   `rosrun simmechanics_to_urdf convert.py {XML File} [Paramater Yaml File] xml`

The parameter file is optional. The keyword xml tells the script to
output urdf/xml, as opposed to the other options described below.

### Tree vs. Graph

URDF allows robot descriptions to only follow a tree structure, meaning
that each link/body can have only one parent, and its position is
dependent on the position of its parent and the position of the joint
connecting it to its parent. This forces URDF descriptions to be in a
tree structure.

CAD files do not generally follow this restriction; one body can be
dependent on multiple bodies, or at the very least, aligned to multiple
bodies.

This creates two problems.

1\. The graph must be converted into a tree structure. This is done by
means of a breadth first traversal of the graph, starting from the root
link. However, this sometimes leads to improper dependencies, which can
be corrected with the parameter file, as described below.

2\. Fixed joints in CAD are not always fixed in the exported XML. To
best understand this, consider the example where you have bodies A, B
and C, all connected to each other. If C is connected to A in such a way
that it is constrained in the X and Z dimensions, and C is connected to
B so that it is constrained in the Y dimension, then effectively, C is
fixed/welded to both of those bodies. Thus removing the joint between B
and C (which is needed to make the tree structure) frees up the joint.
This also can be fixed with the parameter file.

## Naming Conventions

### Bodies/Links

Each Body element in the XML has a possibly non-unique name tag. These
are converted to ("%s%d", name tag, lowest unused natural number)

### Reference Frames

The exported XML includes three types of reference frames for each body.
"CG" refers to the center of gravity, "CS1" refers to the root
coordinate system for the STL, and all of the rest refer to joints
attaching points. The first two use TF frames named ("%s%s", body's
unique name, CG or CS1). All of the rest use the reference attribute of
the Frame.

The script also defines one extra reference frame for each body, named
("X%s", body's unique name). This is the origin for the Link element
in the URDF. It is defined to have the offset equal to the reference
frame of the joint connecting it to its parent, and the orientation
equal to that of CS1. In the URDF, the visual origin, collision origin
and all other relative offsets are calculated from this point.

### Joints

Joints follow a similar naming scheme to Links, ("%s%d", name tag,
lowest unused natural number). However, often they are referred to by a
their base connection frame. In the following snippet, the joint number
would be 11. 

```xml
<SimpleJoint>
	<name>"ENTERPRISEHULL--PHASERARRAY"</name>
	<nodeID>"44/5516/10606:-:44/5516"</nodeID>
	<status>""</status>
	<base>
	  <JointSide>
	    <name>""</name>
	    <connection>
	      <Frame ref="11"></Frame>
	    </connection>
	  </JointSide>
	</base>
	<follower>
	  <JointSide>
	    <name>""</name>
	    <connection>
	      <Frame ref="12"></Frame>
	    </connection>
	  </JointSide>
	</follower>
	...
</SimpleJoint>
```

 This was done out of convenience,
but is probably not the best way to refer to joints. However, in the
parameter file below, this will be referred to as the joint number.

## The Parameter File

All of the parameters are loaded in via a text file/yaml file. They are
NOT loaded into the parameter server.

### Root Parameters

-   `root` (String, default: first STL body in the file) - Changes the
    root node of the tree. Namespace: body's unique id.
-   `baseframe` (String, default: the origin) - Used for calculating the
    origin of the root node. Useful if connecting multiple models.
    Namespace: TF Frame

### STL Parameters

-   `filenameformat` (String, default: "%s") - Used for translating
    the filenames in the exported XML to the URDF filenames, using a
    formatting string. Example: "package:*my_package*folder/%sb" -
    resolves to the package name and adds a "b" at the end to indicate
    a binary stl.
-   `forcelowercase` (Boolean, default: False) - Used for translating
    the filenames\...if True, it forces all filenames to be lower case.
-   `scale` (String, default: None) - If this parameter is defined, the
    scale attribute of the mesh in the URDF will be set to its value.
    Example: "0.01 0.01 0.01" - if your meshes were saved using
    centimeters as units instead of meters.

### Redefining Joints

-   `remove` (Array, default: empty) - All of the joints in this list
    will be removed, i.e. will NOT be considered in the breadth first
    traversal of the graph. Namespace: joint number
-   `freeze` (Array, default: empty) - All of the joints in this list
    will be forced to be welds/fixed. Namespace: joint number
-   `freezeAll` (Boolean, default: False) - All of the joints except
    those redefined in the parameter file will be forced to be
    welds/fixed. \\
-   `redefinedjoints` (Map, default empty) - The keys are joint numbers
    of joints we wish to change some attributes of. The value is a map
    of attributes to change. 

```
redefinedjoints:
   12: {name: ARM_TRANSLATE, axis: "1 0 0", type: prismatic, limits: {effort: 30, velocity: 1.0, lower: -.18, upper: .18}}
   15: {name: ARM_ROTATE, axis: "0 0 1"}
```



### Adding Joints

-   `extrajoints` (Map, default: empty) - The keys are the names of new
    joints to create. The values are maps as well, with the following
    pairs
-   `pid` - Unique link name of parent
-   `cid` - Unique link name of child
-   `jorigin` - TF Frame of joint origin
-   `attributes` - Map of attributes of joint to set. i.e.
    `attributes: {axis: '1 0 0', type: continuous}`
-   `moreframes` (Array, default: empty) - An array of maps which define
    new transforms i.e.
    `- {offset: [0.0,0.0,-0.5], orientation: [0,0,0,1], parent: WORLD, child: NEWFRAME}`
