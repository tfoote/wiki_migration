## Kobuki Udev Rules

<<IncludeCSTemplate(TutorialCSHeaderTemplate)>>

Connection to the kobuki base is via usb enabled by an ftdi usb-serial
converter which is always pre-flashed at the factory with the serial id
`kobuki`. For convenience, to enable the device to appear on
`/dev/kobuki`, use the following script to copy across the udev rule
and restart udev (you'll need your sudo password):



```
> rosrun kobuki_ftdi create_udev_rules
```



**Non ROS users**

In case you are not in a ROS environment, you will need to build the
package first, in order to get the create_udev_rules script.

To do so navigate to the package folder and do 

```
> make udev
```



## Flashing Ftdi Chips

Included also in kobuki_ftdi are the programs we use to scan and flash
the chip. If you are interested in doing a similar operation for another
device you might want to check these out (also check the doxygen) - take
care though, slightly different ftdi usb to serial versions can cause
problems and leave you with lovely bricks!

You can also find more detailed information on how to flash the chip (as
is usually done at Yujin's factory) in the doxygen api.
