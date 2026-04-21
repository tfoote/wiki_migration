## Video

[Youtube](https://www.youtube.com/watch?v=u624jZ_cP14)

## Tutorials

Launch the following on Texas: 

```
roscd texas
roslaunch texas.launch
```



In different terminal after texas.launch completes:


```
roscd texas
roslaunch ps3_drive.launch
```



On local computer: 

```
export ROS_MASTER_URI=http://texas.willowgarage.com:11311
roscd joy
sudo chmod 777 /dev/input/js0
./joy_node
```


