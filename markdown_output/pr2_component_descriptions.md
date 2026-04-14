## Overview

\`pr2_component_descriptions\` holds the [urdf](urdf) files necessary
for PR2 components. During PR2 production and testing, these files are
used for running PR2 components using the [pr2_mechanism](pr2_mechanism)
stack.

The files in this package use the [xacro](xacro) macros from
[pr2_description](pr2_description).

### Robots

URDF files under \"robots\" are for robot assemblies or components. They
can be used by anyone who is using a sub-component of a PR2, like a
caster or a laser sled.

### Robot Motors

During production testing, we test the drive trains of many parts on the
PR2. These URDF files are used to run simple \"robots\", usually motor
and couplers only.

### Test Coverage

All files with the suffix \".urdf.xacro\" in the \`robots/\` or
\`robot_motors/\` directory are checked by both xacro and the URDF
parser. To run this test on any new files, run \"make test\" in the
package directory.
