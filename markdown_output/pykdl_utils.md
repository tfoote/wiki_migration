## Usage

### kdl_parser.kdl_tree_from_urdf_model

Used to convert URDF objects into PyKDL.Tree objects.

```python
from urdf_parser_py.urdf import URDF
from pykdl_utils.kdl_parser import kdl_tree_from_urdf_model
robot = URDF.load_from_parameter_server(verbose=False)
tree = kdl_tree_from_urdf_model(robot)
print tree.getNrOfSegments()
chain = tree.getChain(base_link, end_link)
print chain.getNrOfJoints()
```

### kdl_kinematics.KDLKinematics

Provides wrappers for performing KDL functions on a designated kinematic
chain given a URDF representation of a robot.

```python
from urdf_parser_py.urdf import URDF
from pykdl_utils.kdl_kinematics import KDLKinematics
robot = URDF.from_parameter_server()
kdl_kin = KDLKinematics(robot, base_link, end_link)
q = kdl_kin.random_joint_angles()
pose = kdl_kin.forward(q) # forward kinematics (returns homogeneous 4x4 numpy.mat)
q_ik = kdl_kin.inverse(pose, q+0.3) # inverse kinematics
if q_ik is not None:
    pose_sol = kdl_kin.forward(q_ik) # should equal pose
J = kdl_kin.jacobian(q)
print 'q:', q
print 'q_ik:', q_ik
print 'pose:', pose
if q_ik is not None:
    print 'pose_sol:', pose_sol
print 'J:', J
```

## Unit Tests

For running all of the unit tests, you can either pass a URDF xml file
to use or leave it blank and have the URDF pulled from the parameter
*/robot_description* on the parameter server. ```
rosrun pykdl_utils kdl_parser.py [robot.xml]
rosrun pykdl_utils kdl_kinematics.py [robot.xml]
rosrun pykdl_utils joint_kinematics.py [robot.xml]
```
