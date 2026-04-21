Radial menu on ROS1 for quick, accurate and intuitive selection by a
joystick from 10+ items

![screenshot\|width=800](https://raw.githubusercontent.com/yoshito-n-students/radial_menu_ros/images/images/screenshot_v0_1_4.png)

## Usage

Subscribe both joy and menu state messages using
[message_filters::TimeSynchronizer](http://wiki.ros.org/message_filters#Time_Synchronizer),
watch which menu items are selected and process the joy messages when
the menu is disabled (i.e. the menu does not own the joy messages). See
an example node graph below or
[example_teleop_node.cpp](https://github.com/yoshito-n-students/radial_menu_ros/blob/master/radial_menu_example/src/example_teleop_node.cpp).
The teleop_node in the graph can be replaced to your node.

![example_node_graph\|width=600](https://raw.githubusercontent.com/yoshito-n-students/radial_menu_ros/images/images/example_integration_v0_2_1.png)

## Meta Pkg: radial_menu

A meta-package depending radial_menu_backend, radial_menu_model,
radial_menu_msgs and radial_menu_rviz

## Pkg: radial_menu_backend

```clearsilver
name = Nodelet: Backend
desc = Updates radial menu state based on joystick input
sub {
 0.name = joy
 0.type = sensor_msgs/Joy
 0.desc = Joystick input
}
pub {
 0.name = radial_menu_state
 0.type = radial_menu_msgs/msg/State
 0.desc = The stamp in a message is copied from the source joy message
}
param {
 0.name = menu_description
 0.type = string
 0.desc = Tree structure of the menu in xml format (see the next section for details)
 1.name = ~allow_multi_selection
 1.type = bool
 1.default = false
 1.desc = If false, current selected items will be deselected when a new item is selected
 2.name = ~reset_on_enabling
 2.type = bool
 2.default = false
 2.desc = If true, current selected items will be deselected when enabling the menu
 3.name = ~reset_on_disabling
 3.type = bool
 3.default = false
 3.desc = If true, current selected items will be deselected when disabling the menu
 4.name = ~auto_select
 4.type = bool
 4.default = false
 4.desc = If true, the last pointed item will be autonomously selected. Disable the menu before unpoint not to select
 5.name = ~enable_button
 5.type = int
 5.default = 1
 5.desc = Button to keep enabling the menu. PS4's circle button as default.
 6.name = ~select_button
 6.type = int
 6.default = 5
 6.desc = Button to select or deselect an item or descend the menu. PS4's R1 button as default.
 7.name = ~ascend_button
 7.type = int
 7.default = 4
 7.desc = Button to ascend the menu. PS4's L1 button as default,
 8.name = ~pointing_axis_v
 8.type = int
 8.default = 1
 8.desc = Vertical axis to point an item. PS4's LEFT Y axis as default.
 9.name = ~pointing_axis_h
 9.type = int
 9.default = 0
 9.desc = Horizontal axis to point an item. PS4's LEFT X axis as default.
 10.name = ~invert_pointing_axis_v
 10.type = bool
 10.default = false
 10.desc = If true, invert the value of vertical pointing axis
 11.name = ~invert_pointing_axis_h
 11.type = bool
 11.default = false
 11.desc = If true, invert the value of horizontal pointing axis
 12.name = ~pointing_axis_threshold
 12.type = double
 12.default = 0.5
 12.desc = Threshold value of axis input to enable pointing
}
```

### Example of the param menu_description

```xml
<!-- A simple example -->

<!-- An element must have the attribute 'name'.               -->
<!-- The 'name' of the root element indicates the menu title. -->
<item name="MoveCmd">
    <!-- An element can have child elements -->
    <item name="Front" />
    <item name="Left" />
    <item name="Back" />
    <item name="Right" />
</item>

<!-- Multiple root elements are not allowed -->
``` ```xml
<!-- A complex example -->

<!-- An element can optionally have the attribute 'display'. -->
<!-- Possible values are;                                    -->
<!--   * 'name' (default): displays the item name            -->
<!--   * 'alttxt': displays an alternative text              -->
<!--   * 'image': displays an image                          -->
<item name="Reboot" display="alttxt" alttxt="&#xF021;">
    <item name="Base" display="image" imgurl="package://radial_menu_resources/images/base.bmp">
        <item name="Wheels" display="image" imgurl="file://Photos/wheels.png" />
        <item name="Cameras">
            <item name="Front" />
            ...
        </item>
    </item>
    <item name="Arm">
        ...
    </item>
</item>
```

## Pkg: radial_menu_rviz

```clearsilver
name = Rviz plugin: RadialMenu
desc = Visualizes subscribed menu states as a radial menu when the menu is being enabled. Supports display types of items.
``` ```clearsilver
name = Rviz plugin: HorizontalMenu
desc = Always visualizes subscribed menu states as a single-lined menu. Displays item names regardless of their display types.
```

## Pkg: radial_menu_model

Contains an implementatin of menu tree model, which is commonly used in
the backend and rviz packages

## Pkg: radial_menu_msgs

Defines <<MsgLink(radial_menu_msgs/State)>>

## Pkg: radial_menu_examples

Provides a
[full example](https://github.com/yoshito-n-students/radial_menu_ros/blob/master/radial_menu_example/launch/example_full.launch)
which requires a joystick and a
[Rviz frontend example](https://github.com/yoshito-n-students/radial_menu_ros/blob/master/radial_menu_example/launch/example_rviz.launch)
which does not
