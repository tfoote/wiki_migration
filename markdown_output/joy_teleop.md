## Usage

\`joy_teleop\` takes the output of the [joy_node](joy), and publishes
topics or calls actions according to it\'s configuration. An example of
using \`joy_teleop\` with TIAGo can be found on the video below.

![](attachment:joy_teleop_drawing.png)

## ROS API

The ROS API consists of the configuration file, the input topic, and the
several output topics and actionclients which get dyamically set up
according to the configuration file.

### Parameters

```clearsilver
param {
  0.name=~teleop
  0.type=array
  0.default=
  0.desc=Array of axis/button to topic and action bindings
}
```

#### Example configuration file

```yaml

teleop:
  move:
    type: topic
    message_type: geometry_msgs/Twist
    topic_name: cmd_vel
    axis_mappings:
      -
        axis: 1
        target: linear.x
        scale: 1.0
      -
        axis: 2
        target: angular.z
        scale: 1.0

  joy_priority:
    type: action
    action_name: joy_priority_action
    buttons: [9]

  joy_turbo_decrease:
    type: action
    action_name: joy_turbo_decrease
    buttons: [1, 4, 5]

  joy_turbo_increase:
    type: action
    action_name: joy_turbo_increase
    buttons: [3, 4, 5]

  torso_up:
    type: action
    action_name: /torso_controller/increment
    action_goal:
      increment_by: [0.05]
    buttons: [4] # right pad, top button

  torso_down:
    type: action
    action_name: /torso_controller/increment
    action_goal:
      increment_by: [-0.05]
    buttons: [6] # right pad, bottom button

  close_hand:
    type: action
    action_name: /play_motion
    action_goal:
      motion_name: 'close_hand'
      skip_planning: True
    buttons: [7]
```

### Topic interface

```clearsilver
sub {
  0.name=~joy
  0.type=sensor_msgs/Joy
  0.desc=Listens to the joystick state
}
```
