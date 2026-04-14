Contains a single ros node, \`manipulation_transforms_server\`. The node
keeps track of a transform between a pair of \"effector poses\" and a
corresponding rigidly held \"object pose\".

## Advertised services

All services are in the node\'s private namespace.

\`LoadInitialTransforms\` Ask the node to reload the current effector
and object poses from the parameter server. \`MapEffectorPosesToObject\`
Given the effector poses, return the corresponding object pose
\`MapObjectPoseToEffectors\` Given the object pose, return the current
effector poses

## Parameters

\`{obj,effector0,effector1}\_init_pose/position\` Vector representing
object/effector position; specified as \[x, y, z\]
\`{obj,effector0,effector1}\_init_pose/orientation\` Vector representing
object/effector orientation; specified as \[x, y, z, w\]
