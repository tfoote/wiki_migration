This package is barely usable alone since it provides only templates to
create more structured launch files in the derived packages (cf.
[qb_hand](https://index.ros.org/p/qb_hand) and
[qb_move](https://index.ros.org/p/qb_move)).

## Launch files

The five launch file templates come in help when loading the description
package of a device. 

```wiki
Please, use these "macros" whenever is possible to improve '''robustness''', '''readability''' and '''maintenance''' of derived packages.
```



### component_bringup

This launch file calls the other templates
[load_description_template](https://index.ros.org/p/qb_device_description),
[controllers_bringup](#controllers_bringup)
and [control_bringup](#control_bringup) to
bringup a control node for a single device without starting
[joint_state_publisher](https://index.ros.org/p/joint_state_publisher),
[robot_state_publisher](https://index.ros.org/p/robot_state_publisher)
and [rviz](https://index.ros.org/p/rviz).

#### Parameters

Since the only difference w.r.t. the
[full_bringup](#full_bringup) launch file
is the includes of the
[load_description_template](https://index.ros.org/p/qb_device_description)
rather than the
[description_bringup](#description_bringup),
the parameters are exactly the same as the other a part from
`use_rviz` which is not used.

<a id="control_bringup"></a>

### control_bringup

This launch file starts the device control node with the given
parameters.

#### Parameters

- `control_action` (`string`, default: `empty string`): The type of the
  control action without the namespace prefix and the
  "_trajectory_controller/follow_joint_trajectory" suffix (e.g.
  `foo` if it is
  `<namespace>_foo_trajectory_controller/follow_joint_trajectory`).
  The namespace alone is not sufficient since a device can implement
  several distinct actions.
- `control_duration` (`double`, default: `0.01`): The duration of the
  control loop, in \[s\].
- `device_id` (`int`, default: `1`): The device ID, in range \[`1`,
  `128`\].
- `device_control` (`string`): The base package name prefix (without
  "_control") of the control node (e.g. `qb_device` if it is
  `qb_device_control`).
- `device_namespace` (`string`): The device namespace used to avoid name
  clashes among same-type devices. It must be the same prefix used in
  the description because the control node searches for structures with
  this prefix (e.g. joint names).
- `use_waypoints` (`bool`, default: `false`): Selects whether to
  automatically control the device by looping on the given waypoints. If
  `true` the waypoints are expected to be stored in the Parameter
  Server under `waypoints`.
- `waypoint_namespace` (`string`): The namespace prefix (without
  "_waypoints.yaml") of the waypoints configuration file (e.g.
  `my_device` if it is `my_device_waypoints.yaml`). The file must be
  located in the `config/` subdirectory of the selected `_control`
  package. In addition, the namespaced joint names inside should be
  consistent with the ones specified in the description bringup, usually
  the share the same namespace.
- `waypoint_settings` (`string`): The base package name prefix (without
  "_control") where the waypoint yaml file is stored (e.g.
  `qb_device` if it is `qb_device_control`).

<a id="controllers_bringup"></a>

### controllers_bringup

This launch file just calls the
[spawner_template](https://index.ros.org/p/qb_device_control) to bringup
the device controllers including the
[rqt_joint_trajectory_controller](https://index.ros.org/p/rqt_joint_trajectory_controller)
GUI if requested.

#### Parameters

- `controllers` (`string`): The list of names of the controllers to be
  spawned (e.g. `\*_trajectory_controller`)
- `controllers_namespace` (`string`): The namespace prefix (without
  "_controllers.yaml") of the controller configuration file,
  necessary with many devices (e.g. `my_device` if it is
  `my_device_controllers.yaml`). The file must be located in the
  `config/` subdirectory of the selected `_control` package. In
  addition, the joint names inside should be consistent with the ones
  specified in the description bringup, usually the share the same
  namespace.
- `controllers_settings` (`string`): The base package name prefix
  (without "_control") where controller settings are stored (e.g.
  `qb_device` if it is `qb_device_control`).
- `use_controller_gui` (`bool`, default: `false`): Selects whether to
  load joint trajectory controller GUI.

<a id="description_bringup"></a>

### description_bringup

This launch file packs together the
[load_description_template](https://index.ros.org/p/qb_device_description)
and the
[state_publisher_template](https://index.ros.org/p/qb_device_description)
to bringup all the device description including
[joint_state_publisher](https://index.ros.org/p/joint_state_publisher)
and
[robot_state_publisher](https://index.ros.org/p/robot_state_publisher).
If specified also starts [rviz](https://index.ros.org/p/rviz).

#### Parameters

- `device_description` (`string`): The base package name prefix (without
  "_description") where robot models are stored (e.g. `qb_device`
  if it is `qb_device_description`).
- `device_namespace` (`string`): The namespace prefix of joints and
  links, necessary with many devices (e.g. `my_device` creates a robot
  model composed by `my_device_joint_\...` and
  `my_device_link_\...` elements).
- `device_urdf` (`string`): The name of the
  [xacro](https://index.ros.org/p/xacro) URDF model file to be loaded,
  without extension (e.g. `qb_device` if it is
  `qb_device.urdf.xacro.`). The file must be located in the `urdf/`
  subdirectory of the selected `_description` package.
- `frequency` (`int`, default: `100`): The publish frequency in `Hz`
  of the joint state and the robot state publishers.
- `source_list` (`string`, default: `[joint_states]`): The joint state
  source list for the
  [joint_state_publisher](https://index.ros.org/p/joint_state_publisher)
  (including square braces).
- `use_rviz` (`bool`, default: `true`): Selects whether to load
  [rviz](https://index.ros.org/p/rviz). If `true`, searches for the
  configuration file with the same name as the one specified in
  `device_urdf` which must be located in the `rviz/` subdirectory of
  the selected `_description` package (i.e. it is recommended to
  create a specific file for each robot model). If not specified, uses
  the default configuration.

### full_bringup

This launch file calls the other templates
[description_bringup](#description_bringup),
[controllers_bringup](#controllers_bringup)
and [control_bringup](#control_bringup) to
bringup a complete control node for a single device.

#### Parameters

It provides basically the same configuration parameters as the other
launch files a part from `frequency` and `source_list` of the
[description_bringup](#description_bringup)
which are not exported outside.
