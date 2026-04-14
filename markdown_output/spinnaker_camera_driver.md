## Troubleshooting

USB cameras may require raising the amount of memory allocated to the
USB subsystem. The Spinnaker drivers may fail without warning, or may
give an error -1010 when this occurs. The usbcore variable
\`usbfs_memory_mb\` should be set suitably large.
[This application note](https://www.flir.com/support-center/iis/machine-vision/application-note/understanding-usbfs-on-linux)
describes two common ways of setting it, via the kernel command line
(edit \`/boot/grub.conf\`), or at runtime via
\`/sys/module/usbcore/parameters/usbfs_memory_mb\` . An older method
involving setting parameters in an appropriate file in
\`/etc/modprobe.d/\` is no longer applicable in recent Ubuntu systems
which have usbcore built into the kernel rather than loaded with
modprobe.

This driver is largely derived from the older Point Grey/Flycapture SDK,
and the
[troubleshooting suggestions](pointgrey_camera_driver#Troubleshooting)
on that wiki page may be relevant.
