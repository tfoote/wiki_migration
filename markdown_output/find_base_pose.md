find_base_pose is a PR2-specific package that does search to infer
base-poses that guarantee reachability of given points in the map frame
(Inverse Capability/Reachability Map).

It can for example be used to find a base pose that allows the right
hand to follow an opening trajectory for a cabinet door and the left
hand to grasp something from within.

Currently, it is always searching in the order of distance to the
current robot pose, slightly prefering translation to rotation. Do not
be surprised when the robot does not turn around to reach something
behind him but instead grasps blindy behind him - there are no policies
like additional visibility implemented yet.

To make sure a grasping pose is reachable after navigation, make sure to
drive a little further that just far enough or query find_base_pose with
padded grasp poses, such as creating 4 poses 5cm around the actual grasp
point in addition.
