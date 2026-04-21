Contains a mirror Python implementation of [kdl_parser](kdl_parser)
which takes URDF objects from [urdf_parser_python](urdf_parser_python)
and constructs KDL trees.

## Usage



```python
base_link = "/torso_lift_link"
end_link = "/r_gripper_tool_frame"
chain, joint_info = chain_from_param(base_link, end_link, "/robot_description")
# chain is a PyKDL Chain
# joint_info is a dictionary of lists of joint values and types
print chain.getNrOfSegments()
print joint_info["lim_mins"]
```


