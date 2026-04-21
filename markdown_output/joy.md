## Supported Hardware

This node should work with any joystick that is supported by Linux.

## API Stability

The ROS API of this node should be considered stable.

[Official Documentation](http://www.ros.org/doc/api/joy/html/)

## Nodes



```clearsilver

node.0 {
  name=joy_node
  desc=Provides a generic Linux joystick node.

  pub {
    0.name = joy
    0.type = sensor_msgs/Joy
    0.desc = Outputs the joystick state.
  }

  sub {
    0.name = joy/set_feedback
    0.type = sensor_msgs/JoyFeedbackArray
    0.desc = Force feedback control.
  }

  param {
    0.name = ~dev
    0.type = str
    0.default = "/dev/input/js0"
    0.desc = Linux joystick device from which to read joystick events.
    1.name = ~deadzone
    1.type = double
    1.default = 0.05
    1.desc = Amount by which the joystick has to move before it is considered to be off-center. This parameter is specified relative to an axis normalized between -1 and 1. Thus, 0.1 means that the joystick has to move 10% of the way to the edge of an axis's range before that axis will output a non-zero value. Linux does its own deadzone processing, so in many cases this value can be set to zero.
    2.name = ~autorepeat_rate
    2.type = double
    2.default = 0.0 (disabled)
    2.desc = Rate in Hz at which a joystick that has a non-changing state will resend the previously sent message.
    3.name = ~coalesce_interval
    3.type = double
    3.default = 0.001
    3.desc = Axis events that are received within coalesce_interval (seconds) of each other are sent out in a single ROS message. Since the kernel sends each axis motion as a separate event, coalescing greatly reduces the rate at which messages are sent. This option can also be used to limit the rate of outgoing messages. Button events are always sent out immediately to avoid missing button presses.
    4.name = ~default_trig_val
    4.type = bool
    4.default = false
    4.desc = When this parameter is ''false'', each button and axis will report a value of 0 until it gets pressed/touched. This might be a problem e.g. for the trigger axes which should report 1.0 in their default untouched position. Setting this parameter to ''true'' forces the driver to read the actual joystick button values on startup and report the correct values even before the buttons/axes were touched. There is a small probability that reading out the initial state will not work for some combinations of gamepads and kernel versions, and that is why this parameter is ''false'' by default.
    5.name = ~dev_ff
    5.type = str
    5.default = "/dev/input/event0" (<<Version(Noetic)>>: autodetection is tried if this parameter is not specified)
    5.desc = The device to use for accessing force feedback function. It is usually one of `/dev/input/event*` devices. You can use `udevadm monitor` command when plugging in the gamepad to tell the right event file name.
  }
}
```



## Using this Package

For an example of using **joy_node** to control a teleoperation node
with a joystick, see the [tutorials](joy/Tutorials).

In some cases, multiple joysticks may control a single robot. For
example, a user may use the default joystick to drive a robot, but a
second user may wish to use a different kind. Since the button mappings
on each joystick may be different, it will be necessary to remap buttons
on one joystick so they can match. See the
[Joystick Remapper](joystick_remapper) package for details.



```wiki
If you need to use the trigger axes (LT, RT), consider setting ''~default_trig_val'' to ''true''. If this parameter is not set, the triggers report a value of ''0.0'' until they are touched, which is wrong (because the value should be ''1.0'').
```



### Force feedback

Most gamepads offer a force feedback function that can vibrate the
gamepad. For it to work correctly, you have to specify correctly the
`dev_ff` parameter (on Noetic, when this parameter is empty, an
autodetection algorithm tries to guess it).

Once the force feedback device is correctly set, you can control the
force feedback using the `joy/set_feedback` topic. Before trying it
out, make sure the jumping gamepad on your table will not destroy
anything. An example usage can look like this:



```
rostopic pub -1 /joy/set_feedback sensor_msgs/JoyFeedbackArray "array: [ {type: 1, id: 0, intensity: 1.0} ]"
```



The `intensity` field specifies the strength of the vibrations. 0 is
no vibration, 1 is maximum.

#### Finding the correct force feedback device

If you do not know the correct value of the `dev_ff` parameter, here
are a few tips to figure it out.



```wiki
The name of the file you pass to `~dev_ff` parameter can change between reconnects of the gamepad or reboots of your computer. To get a reliable experience, a udev rule giving an explicit name to this device seems like to best solution. Treat the tips in this section just as something you want to use in the initial development phase when you are testing and developing a feature.
```



One way is to look into folder `/dev/input/by-id`.



```
ls -la /dev/input/by-id/
```



The output can look like this:



```
lrwxrwxrwx 1 root root  10 Aug 12 19:08 usb-Chicony_Electronics_Co._Ltd._Integrated_Camera_0001-event-if00 -> ../event14
...
lrwxrwxrwx 1 root root  10 Aug 19 16:02 usb-Microsoft_Controller_3039373132373036323336303438-event-joystick -> ../event18
lrwxrwxrwx 1 root root   6 Aug 19 16:02 usb-Microsoft_Controller_3039373132373036323336303438-joystick -> ../js0
```



The listing shows a few symbolic links, one of them pointing to your
`js0` device. The symlink will end with `-joystick`. Look for a
similarly named file, just ending with `-event-joystick`. You can
either directly pass this value to `dev_ff` (in this case
`/dev/input/by-id/usb-Microsoft_Controller_3039373132373036323336303438-event-joystick`),
or you can follow the symbolic link to one of the `/dev/input/event\*`
files and set the event file as the parameter value (which would be
`/dev/input/event18` in this example).

Some gamepads will not appear in the `/dev/input/by-id` listing - e.g.
Xbox ONE gamepad connected via the wireless dongle and `xow` driver.

In this case, the easiest way to find the force feedback event device is
to disconnect the gamepad (or dongle) and run



```
udevadm monitor
```



Here is an example output of this command after plugging the gamepad
back:



```
KERNEL[181478.230525] add      /devices/pci0000:00/0000:00:08.1/0000:06:00.4/usb6/6-2 (usb)
...
KERNEL[181481.500440] add      /devices/virtual/input/input24 (input)
KERNEL[181481.500573] add      /devices/virtual/input/input24/event18 (input)
KERNEL[181481.500659] add      /devices/virtual/input/input24/js0 (input)
UDEV  [181481.502263] add      /devices/virtual/input/input24 (input)
UDEV  [181481.512791] add      /devices/virtual/input/input24/js0 (input)
UDEV  [181481.551194] add      /devices/virtual/input/input24/event18 (input)
```



You can see that I have connected a gamepad that appeared as
`/dev/input/js0` with the force feedback device being
`/dev/input/event18`.

## Application

### Microsoft Xbox 360 Wireless Controller for Windows

Table of index number of `/joy.buttons`:

  -- ------- -- -------------------------------------- --
     Index      Button name on the actual controller   
     0          A                                      
     1          B                                      
     2          X                                      
     3          Y                                      
     4          LB                                     
     5          RB                                     
     7          start                                  
     8          power                                  
     10         cross key up                           
     11         cross key down                         
     12         cross key left                         
     13         cross key right                        
     14         back                                   
  -- ------- -- -------------------------------------- --

### Microsoft Xbox 360 Wireless Controller for Linux

Table of index number of `/joy.buttons`:

  -- ------- -- -------------------------------------- --
     Index      Button name on the actual controller   
     0          A                                      
     1          B                                      
     2          X                                      
     3          Y                                      
     4          LB                                     
     5          RB                                     
     6          back                                   
     7          start                                  
     8          power                                  
     9          Button stick left                      
     10         Button stick right                     
  -- ------- -- -------------------------------------- --

Table of index number of `/joy.axes`:

  -- ------- -- ------------------------------------ --
     Index      Axis name on the actual controller   
     0          Left/Right Axis stick left           
     1          Up/Down Axis stick left              
     2          Left/Right Axis stick right          
     3          Up/Down Axis stick right             
     4          RT                                   
     5          LT                                   
     6          cross key left/right                 
     7          cross key up/down                    
  -- ------- -- ------------------------------------ --

### Microsoft Xbox 360 Wired Controller for Linux

Table of index number of `/joy.buttons`:

  -- ------- -- -------------------------------------- --
     Index      Button name on the actual controller   
     0          A                                      
     1          B                                      
     2          X                                      
     3          Y                                      
     4          LB                                     
     5          RB                                     
     6          back                                   
     7          start                                  
     8          power                                  
     9          Button stick left                      
     10         Button stick right                     
  -- ------- -- -------------------------------------- --

Table of index number of `/joy.axes`:

  -- ------- -- ------------------------------------ --
     Index      Axis name on the actual controller   
     0          Left/Right Axis stick left           
     1          Up/Down Axis stick left              
     2          LT                                   
     3          Left/Right Axis stick right          
     4          Up/Down Axis stick right             
     5          RT                                   
     6          cross key left/right                 
     7          cross key up/down                    
  -- ------- -- ------------------------------------ --

### Logitech Wireless Gamepad F710 (DirectInput Mode)

Table of index number of `/joy.buttons`:

  -- ------- -- -------------------------------------- --
     Index      Button name on the actual controller   
     0          X                                      
     1          A                                      
     2          B                                      
     3          Y                                      
     4          LB                                     
     5          RB                                     
     6          LT                                     
     7          RT                                     
     8          back                                   
     9          start                                  
     10         Button stick left                      
     11         Button stick right                     
  -- ------- -- -------------------------------------- --

Table of index number of `/joy.axes`:

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------ --
     <tablestyle="margin:0.5em 0px 0px 0.5em;border-collapse:collapse;border:1px dotted rgb(211, 211, 211);"style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">Index      <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">Axis name on the actual controller   
     <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">0                                                                                                                  <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">Left/Right Axis stick left           
     <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">1                                                                                                                  <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">Up/Down Axis stick left              
     <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">2                                                                                                                  <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">Left/Right Axis stick right          
     <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">3                                                                                                                  <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">Up/Down Axis stick right             
     <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">4                                                                                                                  <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">cross key left/right                 
     <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">5                                                                                                                  <style="padding:0.25em 0.5em;border:1px dotted rgb(211, 211, 211);">cross key up/down                    
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------ --
