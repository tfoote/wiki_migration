![\|align="right",width="280"](attachment:ptgreycams.png)

## Devices

This driver is regularly tested with the following devices:

- [Bumblebee2](http://ww2.ptgrey.com/stereo-vision/bumblebee-2)
- [Chameleon](http://ww2.ptgrey.com/USB2/chameleon)

It has also been successfully used with Blackfly, Flea3, and others.

## Usage

Install from apt, refresh udev:



```
sudo apt-get install ros-$ROS_DISTRO-pointgrey-camera-driver
```



List detected cameras:



```
rosrun pointgrey_camera_driver list_cameras
```



Launch camera:



```
roslaunch pointgrey_camera_driver bumblebee.launch
roslaunch pointgrey_camera_driver camera.launch
```



When multiple Point Grey cameras are in use at a time, specify the
serial number given by `list_cameras`:



```
roslaunch pointgrey_camera_driver camera.launch camera_serial:=12345678
```



## Parameters

Until better documentation is produced, please see the
[PointGrey.cfg](https://github.com/ros-drivers/pointgrey_camera_driver/blob/master/pointgrey_camera_driver/cfg/PointGrey.cfg)
file for the available parameters.

## Troubleshooting

When using Point Grey's GigE cameras, you may experience an issue with
dropped packets which results in `IMAGE_CONSISTENCY_ERROR` being
thrown by the !FlyCapture2 SDK. You can adjust the receive buffer
settings in Linux using `sysctl` to correct this. See
[this knowledge base article from Point Grey](http://www.ptgrey.com/KB/10016)
for more details.

Similarly, multiple USB cameras may require raising the amount of memory
allocated to the USB subsystem. The usbcore variable `usbfs_memory_mb`
should be set suitably large.
[This application note](http://www.ptgrey.com/tan/10685) describes two
common ways of setting it, via the kernel command line (edit
`/boot/grub.conf`), or module loading (`modprobe usbcore
usbfs_memory_mb=1024` for current session, or adding `options usbcore
usbfs_memory_mb=1000` to an appropriate `/etc/modprobe.d` file). It
should also be settable at runtime via
`/sys/module/usbcore/parameters/usbfs_memory_mb`
