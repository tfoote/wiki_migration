## Documentation

See the robin_people_detection node documentation.

## Nodes



```clearsilver
name = robin_people_detection
desc = This Node provides two tf between /base_footprint and /dominant_person, and /base_footprint and /group. The dominant Person is calculated by a weighted function from x and y distances (costs = x + 0.4*y). The group includes the average position of all detected persons. The z-coordinate of both tf is set to zero, to get the footprint of the person/group.

req_tf {
  0.from = /base_footbrint
  0.to = /torso_X
  0.desc = Transformation between the base footprint of the robot/kinect to the torso (can be more than 1) of the persons to detect.  
}

prov_tf {
  0.from = /base_footbrint
  0.to = /dominant_person
  0.desc = Transformation from base footprint of the robot/kinect to the base footprint of the dominant person.
  1.from = /base_footbrint
  1.to = /group
  1.desc = Transformation from base footprint of the robot/kinect to the base footprint of the group of persons.
}

param {
  0.name = base_name
  0.type = string
  0.desc = Name of the parent frame for the provided transformations. Default: "/base_footprint".  
}
```



## Launch Files

Use roslaunch files to load this files.

-   **robin_people_detection.launch** - Launches
    [openni_tracker](openni_tracker), 3dsensor of the
    [turtlebot_bringup](turtlebot_bringup) package, rviz and the
    robin_people_detection node.

## Test People Detection

By calling 

```
roslaunch robin_people_detection robin_people_detection.launch
```

 one can test the people detection.
