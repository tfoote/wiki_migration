## Installation

Note: This wiki did not include the steps to install this package, this
is the most up to date version I could find:
<https://github.com/epan-utbm/joystick_remapper>

If there is an official source, please edit this page to include it.

## Supported Hardware

Any joystick with a driver that publishes a <<MsgLink(joy/Joy)>>
message can be used with the `joystick_remapper`.

The joystick remapper is simply a node that listens to Joy messages and
republishes them on a different topic. Before republishing, it can
change the order of the axes or buttons. This allows two different types
of joysticks to behave the same way to a teleop node. In order to make
this work, the user must set up the map from one joystick to another.
There's a good example of this in the tutorial
[Using the Joystick Remapper](/Tutorials/UsingJoystickRemapper).

## API Stability

This is a relatively new and untested package. User feedback has
indicated that the way of defining a mapping is difficult to use. You
can expect it to change in an incompatible way in a future release of
this package.

## Launch File Example

This example shows how to remap a Logitech-type joystick to a PS3 button
mapping for controlling the PR2. 

```xml
<node pkg="joy" type="joy_node" name="logitech_joy" >
  <remap from="joy" to="logitech" />
</node>

<node pkg="joystick_remapper" type="joystick_remapper.py" name="logitech_to_ps3" >
  <remap from="joy_source" to="logitech" />
  <remap from="joy_des" to="joy" />
  <param name="button_mapping" type="str" value="8 -1 -1 9 -1 -1 -1 -1 6 7 4 5 3 2 1 0" />
  <param name="axis_mapping" type="str" value="=" />
</node>
```

 The above
example leaves the axes the same, but remaps the buttons on the
logitech. Let's look at the code. This launches the logitech joystick
using the joy_node. Since the joy node publishes to "joy", we remap
the output to another topic to avoid mixing the two joysticks before
they are properly remapped. The remapper must be configured with the
input and output topics. The defaults are "joy_source" and
"joy_dest" and these must be remapped. Here is where we configure the
button mapping of the joystick. The syntax for the remap string is as
follows: 

```
8 -1 -1 9
```

 Maps button 8 on the Logitech to
position 0 on the PS3 (remember that joystick buttons are indexed from
zero). The numbers in the list are the numbers for the Logitech joystick
buttons, and the order is the order in which they will appear in the
remapped output.

The "-1" button maps a button or axis to zero. In the above example,
the button #1 and #2 on the PS3 are always zero. No button on the
Logitech will command those buttons on the PS3.

This maps Logitech 9 to button 3 on the output. For a full mapping, see
[Using the Joystick Remapper](/Tutorials/UsingJoystickRemapper). Since
the axes are the same as on the Logitech and the PS3, they don't need
to be remapped. Use "=" as the remapping, or just leave it blank.

Detailed parameter and node descriptions are below.

## Nodes



```clearsilver
node {
 0{
 name = joystick_remapper.py
 desc = `joystick_remapper.py` listens to (<<MsgLink(joy/Joy)>>) messages and republishes them on a different topic.
 sub {
  0{
  name= joy_source
  type= joy/Joy
  desc= Topic on which joystick commands are arriving to be remapped.
  }
 }
 pub {
  0{
  name= joy_dest
  type= joy/Joy
  desc= Topic on which the remapped joystick events are sent out to be remapped.
  }
 }
 }
}
```



#### Parameters

The mapping parameters are given as strings, with each value in the
string giving the new axis or button number. The k\^th\^ integer
indicates which input button maps to the k\^th\^ output button. For
example: 

```
2 3 0 1
```

 Maps button (or axis) 2 to output
button 0, 3->1, 0->2 and 1->3. Any axis or buttons that are not
remapped are left in original order. Note that axes and button indices
start from zero.

If -1 is listed as the source button/axis then that button/axis will
always output zero.

If "=" is given as the remapping parameter, or none is given, the
joystick buttons or axes are not remapped.



```clearsilver
param_set {
  no_header = True
  0.name= button
  0.type= string
  0.desc= Buttons mapping.
  1.name= axis_mapping
  1.type= string
  1.desc= Same as `~button_mapping` for mapping the axes.
}
```



### Tutorials

See [Using the Joystick Remapper](/Tutorials/UsingJoystickRemapper).
