This package is barely usable alone since it provides only templates to
create more structured launch files in the derived packages (cf.
[qb_device_bringup](https://index.ros.org/p/qb_device_bringup)).

## Launch files

The two launch file templates come in help when loading the description
package of a device. It could seem unlikely to split the two files (and
actually they are often called sequentially), but it guarantees in a
[multi-device system](https://index.ros.org/p/qb_chain) to be able to
load every single robot description in each device namespace (which is
required to setup their control nodes) and to load the whole robot model
complete with
[joint_state_publisher](https://index.ros.org/p/joint_state_publisher),
[robot_state_publisher](https://index.ros.org/p/robot_state_publisher)
and [rviz](https://index.ros.org/p/rviz) only once.


```wiki
Please, use these "macros" whenever is possible to improve '''robustness''', '''readability''' and '''maintenance''' of derived packages.
```



<a id="load_description_template"></a>

### load_description_template

This basic launch file just loads the
[urdf](https://index.ros.org/p/urdf) xml robot description in the
`robot_description` ROS param by providing few configuration
arguments.

#### Parameters

- `model_name` (`string`): The name of the
  [xacro](https://index.ros.org/p/xacro) URDF model file to be loaded,
  without extension (e.g. `qb_device` if it is
  `qb_device.urdf.xacro.`). The file must be located in the `urdf/`
  subdirectory of the selected `_description` package.
- `namespace` (`string`): The namespace prefix of joints and links,
  necessary with many devices (e.g. `my_device` creates a robot model
  composed by `my_device_joint_\...` and `my_device_link_\...`
  elements).
- `package_prefix` (`string`): The base package name prefix (without
  "_description") where robot models are stored (e.g. `qb_device`
  if it is `qb_device_description`).

<a id="state_publisher_template"></a>

### state_publisher_template

This launch file starts the
[joint_state_publisher](https://index.ros.org/p/joint_state_publisher)
and the
[robot_state_publisher](https://index.ros.org/p/robot_state_publisher)
for the given `robot_description` loaded in the Parameter Server
(under the current namespace). If specified also starts
[rviz](https://index.ros.org/p/rviz).

#### Parameters

- `frequency` (`int`, default: `100`): The publish frequency in `Hz`
  of the joint state and the robot state publishers.
- `package_prefix` (`string`): The base package name prefix (without
  "_description") where robot models are stored (e.g. `qb_device`
  if it is `qb_device_description`).
- `rviz_config` (`string`): The name of the
  [rviz](https://index.ros.org/p/rviz) config file to be loaded, without
  extension (e.g. `qb_device` if it is `qb_device.rviz.`). The file
  must be located in the `rviz/` subdirectory of the selected
  `_description` package.
- `source_list_names` (`string`, default: `[joint_states]`): The joint
  state source list for the
  [joint_state_publisher](https://index.ros.org/p/joint_state_publisher)
  (including square braces).
- `use_joint_state_gui` (`bool`, default: `false`): Selects whether to
  load the
  [joint_state_publisher](https://index.ros.org/p/joint_state_publisher)
  joint state GUI.
- `use_rviz` (`bool`, default: `true`): Selects whether to load
  [rviz](https://index.ros.org/p/rviz).
