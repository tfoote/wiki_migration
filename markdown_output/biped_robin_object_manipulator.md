## Documentation

This package has one node which sends commands to RTAI to pickup and
place cups with the BipedRobin robot.

## Nodes



```clearsilver
node.0 {
  name = object_manipulator
  desc = This nodes provides services to pickup and place cups, and move the robot in a defined start posture. It calls services to move the robot and the gripper.
srv {
  0.name = pickup_srv
  0.type = biped_robin_msgs/PickupObjectService
  0.desc = When this service is called the robot picks up a cup at the coordinates specified in the PickupObjectService message.
  1.name = place_srv
  1.type = biped_robin_msgs/PickupObjectService
  1.desc = When this service is called the robot places up a cup at the coordinates specified in the PickupObjectService message.
  2.name = startPosture_srv
  2.type = std_srvs/Empty
  2.desc = This Services moves the robot in a defined start posture.
}
srv_called {
  0.name = movePostureCartesian_srv
  0.type = biped_robin_msgs/MovePostureCartesianService
  0.desc = This service moves the robot by sending the coordinates of the tcp, orientation of the robots upper body and angles of the two arms.
  1.name = hand_node/hand_srv
  1.type = sensorhand_speed/hand_cmd
  1.desc = Service to open and close the robot hand and setting the grip mode of the hand.
}
}
```


