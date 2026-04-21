# Pepper-specific sensors

This package contains nodes and launch file to retrieve data from the
sensors specific to Pepper.

## Nodes

### Laser

Pepper has 6 laser sensors. Three of them watch the robot's
surroundings and project their line horizontally. They are called:

-   srd_front
-   srd_left
-   srd_right

Two of them project vertical lines in front of the robot and are called

-   ground_left (on the left side of the robot, project towards the
    right)
-   ground_right (on the right side of the robot, project towards the
    left)

The last one projects its line in front of the robot towards the ground
and is called:

-   shovel

```clearsilver
pub {
  0.name = ~pepper/laser/shovel/scan
  0.type = sensor_msgs/Laserscan
  0.desc = Laserscan topic for shovel laser

  1.name = ~pepper/laser/ground_left/scan
  1.type = sensor_msgs/Laserscan
  1.desc = Laserscan topic for ground left laser

  2.name = ~pepper/laser/ground_right/scan
  2.type = sensor_msgs/Laserscan
  2.desc = Laserscan topic for ground right laser

  3.name = ~pepper/laser/srd_front/scan
  3.type = sensor_msgs/Laserscan
  3.desc = Laserscan topic for surrounding front laser

  4.name = ~pepper/laser/srd_left/scan
  4.type = sensor_msgs/Laserscan
  4.desc = Laserscan topic for surrounding left laser

  5.name = ~pepper/laser/srd_right/scan
  5.type = sensor_msgs/Laserscan
  5.desc = Laserscan topic for surrounding right laser

  6.name = ~pepper/laser/shovel/pointcloud
  6.type = sensor_msgs/PointCloud2
  6.desc = Pointcloud2 topic for shovel laser

  7.name = ~pepper/laser/ground_left/pointcloud
  7.type = sensor_msgs/PointCloud2
  7.desc = Pointcloud2 topic for ground left laser

  8.name = ~pepper/laser/ground_right/pointcloud
  8.type = sensor_msgs/PointCloud2
  8.desc = Pointcloud2 topic for ground right laser

  9.name = ~pepper/laser/srd_front/pointcloud
  9.type = sensor_msgs/PointCloud2
  9.desc = Pointcloud2 topic for surrounding front laser

  10.name = ~pepper/laser/srd_left/pointcloud
  10.type = sensor_msgs/PointCloud2
  10.desc = Pointcloud2 topic for surrounding left laser

  11.name = ~pepper/laser/srd_right/pointcloud
  11.type = sensor_msgs/PointCloud2
  11.desc = Pointcloud2 topic for surrounding right laser
 }
param {
        0.name = pointcloud
        0.desc = Determines if the node should publish laser in sensor_msgs/PointCloud2 messages
        0.type = boolean
        0.default = True
        1.name = laserscan
        1.desc = Determines if the node should publish laser in sensor_msgs/Laserscan messages
        1.type = boolean
        1.default = False
    }
```

### Camera

Wraps the camera node from [naoqi_sensors](naoqi_sensors)

## Launch files

### Sonar

Starts two sonar nodes (from [naoqi_sensors](naoqi_sensors)) to get the
data from the front and the back sonar

### Laser

Starts the laser node

### Camera

Starts the camera node
