**Diamondback Users Please Note**

With the release of Diamondback, the Python Camshift function in OpenCV
somehow got broken and will crash with the following error:

```
TypeError: <unknown> is not a numpy array
```

right after selecting a region with the mouse to track. The only fix at
the moment seems to be to overlay the C-Turtle version of the
vision_opencv stack and then set your ROS_PACKAGE_PATH and PYTHONPATH
environment variables to pick up this version before Diamondback\'s
version. To do this on your machine, follow these steps:

```
$ sudo apt-get install ros-cturtle-vision-opencv
$ cd
$ echo -e "\nexport ROS_PACKAGE_PATH=/opt/ros/cturtle/stacks/vision_opencv:$ROS_PACKAGE_PATH" >> .bashrc
$ echo -e "\nexport PYTHONPATH=/opt/ros/cturtle/stacks/vision_opencv/opencv2/lib:$PYTHONPATH" >> .bashrc
$ source .bashrc
```

(The last command is only necessary in any currently open terminal
windows. The path changes will be automatically picked up in any new
terminal windows you launch in the future.)

## Documentation

Please see external documentation at
[http://www.pirobot.org/blog/0016/](http://www.pirobot.org/blog/0016).
