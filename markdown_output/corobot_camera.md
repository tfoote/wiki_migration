## Supported Hardware

This driver should works with every camera

## ROS API



```clearsilver
node.0 {
name=dynamic_sender
desc=`dynamic_sender` is a driver for cameras. This driver was designed to get camera images from a Corobot.
sub{
0.name= camera/set_videomode
0.type= corobot_msgs/videomode
0.desc= Set the video mode
1.name= camera/set_state
1.type= corobot_msgs/state
1.desc= Set the camera state
}
pub{
0.name= /camera/image_raw
0.type= sensor_msgs/Image
0.desc= Image of the camera
}
param{
0.name= device
0.default=  /dev/video0
0.type= string
0.desc= path to the camera
1.name= topic
1.type= string
1.default=  /camera/image_raw
1.desc= topic name for the image
2.name= width
2.type= int
2.default=  960
2.desc= width of the image
3.name= height
3.type= int
3.default=  720
3.desc= height of the image
4.name= fps
4.type= int
4.default=  30
4.desc= frames per second
5.name= camera_parameter_file
5.type= string
5.default=  ../camera_parameters.txt
5.desc= path to the configuration file for the camera
6.name= immediately
6.type= bool
6.default= true
6.desc= Start the camera automatically after the node starts
6.name= isjpeg
6.type= bool
6.default= false
6.desc= Setup the camera to send jpeg images
}
}
}
```


