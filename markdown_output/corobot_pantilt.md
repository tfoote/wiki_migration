## Supported Hardware

This driver should works with every pan tilt camera

## ROS API

```clearsilver
node.0 {
name=corobot_pantilt
desc=`corobot_pantilt` is a driver for pantilt cameras. This driver was designed to control the movement of a Corobot pantilt camera.
sub{
0.name= pantilt
0.type= corobot_msgs/PanTilt
0.desc= Pan and Tilt command
}
param{
0.name= device
0.type= string
0.default= /dev/video0
0.desc= path to the camera
1.name= script_path
1.type= string
1.default= init_camera.sh
1.desc= path to an initialization script necessary for the pantilt to work
}
}
}
```

## Troubleshooting

Here is a set of instructions in case you cannot control your pan tilt
camera:

1\. Install v4l-conf and unvcdynctrl ```
{
sudo apt-get install v4l-conf unvcdynctrl
```} 2.
Execute: ```
{
v4l-info /dev/video0
uvcdynctrl –cv
sudo chmod 777 /dev/video0
```}

3\. Disconnect the camera

4\. Reconnect it to another usb port

5\. The camera movement should now work
