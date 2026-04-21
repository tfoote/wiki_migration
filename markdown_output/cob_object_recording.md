# Tutorial

To record an object, first start a ROS master with


```
roscore
```



attach a Kinect or Asus camera to your computer and launch the driver,
e.g. for the openni stack with 

```
roslaunch openni_launch openni.launch camera:=cam3d
```

 or for the
openni2 stack with 

```
roslaunch openni2_launch openni2.launch camera:=cam3d
```


