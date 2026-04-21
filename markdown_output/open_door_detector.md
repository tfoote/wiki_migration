## Documentation

See the open_door_detector node documentation.

## Nodes



```clearsilver
name = open_door_detector
desc = Provides a service to detect if a door is open. If this is the case, it returns the position of the middle of the door. Otherwise it returns position 0.

srv {
  0.name = detect_open_door
  0.type = open_door_detector/detect_open_door
  0.desc = This service detects if a door is open. It requires an aperture angle where a door could be open and a maximum distance between sensor and the wall/door. It returns the position of the middle of the door with respect to /camera_link if a door is detected. Otherwise it returns position 0.  
}
```



## Test open_door_detector

By calling 

```
roslaunch open_door_detector open_door_detector.launch
```

 one can start the node
open_door_detector which provides the detect_open_door service. By
calling 

```
rosservice call /detect_open_door [aperture_angle] [wall_distance]
```

 one can call the service to detect a
open door.
