# Usage

Warning: this package is currently under development.


```
$ rosrun pr2_pick_and_place_service pick_and_place_service.py
```



## Nodes



```clearsilver
srv{
  0.name= pick_and_place_detach_object
  0.type= pr2_pick_and_place_service/DetachObjectFromGripper
  0.desc= Opens the specified hand
  1.name= pick_and_place_detect_object
  1.type= pr2_pick_and_place_service/DetectObjects
  1.desc= Detects objects in robot's workspace
  2.name= pick_and_place_detect_table
  2.type= pr2_pick_and_place_service/DetectTable
  2.desc= Detects the table
  3.name= pick_and_place_pickup_object
  3.type= pr2_pick_and_place_service/PickUpObject
  3.desc= Picks up a specified object with the specified arm
  4.name= pick_and_place_point_head
  4.type= pr2_pick_and_place_service/PointHead
  4.desc= Points the head at the current place rectangle and also can direct heads in small increments 
  5.name= pick_and_place_take_collisionmap
  5.type= pr2_pick_and_place_service/TakeCollisionMap
  5.desc= Description: Takes a collision map
  6.name= pick_and_place_place_object
  6.type= pr2_pick_and_place_service/PlaceObject
  6.desc= Places object in the indicated hand at either the place rectangle or where it came from
  7.name= pick_and_place_move_arm_to_side
  7.type= pr2_pick_and_place_service/MoveArmToSide
  7.desc= Moves arm to the side
}
```


