## PoseConv Usage

Each of the methods in PoseConv converts a pose-like Python tuple, numpy
matrix or tuple, or ROS message into another. Each of the methods is
called using PoseConv.to\_%pose_type% where %pose_type% is in
PoseConv.POSE_TYPES. Notes on various types:

-   \'\'\*\_msg\'\' - refers to a ROS message of similar name.
-   \'\'homo_mat\'\' - homogeneous matrix 4x4 numpy.mat.
-   \'\'pos_rot\'\' - 3x1 numpy.mat position, 3x3 numpy.mat
-   \'\'pos_quat\'\' - list of length 3, list of length 4
-   \'\'pos_euler\'\' - list of length 3, list of length 3

The input parsing is fairly forgiving on the exact type and shape of the
Python/numpy arguments.

The first argument can optionally be a string, representing the designed
header \'\'frame_id\'\' if the requested type is a stamped message. The
\'\'stamp\'\' is always set as the current time and \'\'seq\'\' is 0.
After the optional header string, you can pass the pose. If the input
type is a tuple, you can pass either the complete tuple as one argument
or split it into two arguments.

```python
import roslib; roslib.load_manifest("hrl_geom")
from hrl_geom.pose_converter import PoseConv
pos_euler = [[0.1, 0.2, 0.3], [0.3, 0., 0.]]
twist_msg = PoseConv.to_twist_msg(pos_euler)
print twist_msg
#linear: 
#  x: 0.1
#  y: 0.2
#  z: 0.3
#angular: 
#  x: 0.3
#  y: 0.0
#  z: 0.0
homo_mat = PoseConv.to_homo_mat(twist_msg)
print homo_mat
#[[ 1.          0.          0.          0.1       ]
# [ 0.          0.95533649 -0.29552021  0.2       ]
# [-0.          0.29552021  0.95533649  0.3       ]
# [ 0.          0.          0.          1.        ]]
pos, rot = homo_mat[:3,3], homo_mat[:3,:3]
tf_stamped_msg = PoseConv.to_tf_stamped_msg("base_link", pos, rot)
print tf_stamped_msg
#header: 
#  seq: 0
#  stamp: 
#    secs: 1341611677
#    nsecs: 579762935
#  frame_id: base_link
#child_frame_id: ''
#transform: 
#  translation: 
#    x: 0.1
#    y: 0.2
#    z: 0.3
#  rotation: 
#    x: 0.149438132474
#    y: 0.0
#    z: 0.0
#    w: 0.988771077936
new_pos_euler = PoseConv.to_pos_euler(tf_stamped_msg)
print new_pos_euler
#([0.10000000000000001, 0.20000000000000001, 0.29999999999999999], (0.30000000000000004, -0.0, 0.0))
```

## Unit Testing

You can also run the main file to see some unit tests converting
everything to everything else:

```
roscore # if not running already
rosrun hrl_geom pose_converter.py
```
