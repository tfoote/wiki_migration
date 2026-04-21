The proximity_sensor_tf package provides an own coordinate frame for
each patch of the proximity sensor.

The coordinate frames can be configured in the *conf/tf.yaml* file.
Since the patches are treated as circles, it is sufficient to enter for
each patch a position, a normal and the parent frame of the patch.

After you configured your transforms you can run the tf node with



```
roslaunch proximity_sensor_tf tf.launch
```


