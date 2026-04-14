```wiki
'''[[urdf_parser_py]] is the current Python URDF parsing API for Indigo and later'''
```

## Usage

Contains Python object definitions which mirror
[urdf_parser](urdf_parser). The following lines produce a Model object
which self-contains the URDF information: ```python
model1 = create_model_from_file('robot.xml')
model2 = create_model_from_param('/robot_description')
```
