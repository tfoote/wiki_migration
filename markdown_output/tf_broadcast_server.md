This server broadcasts static transforms and is used in conjunction with
built-in RCommander tools to define persistent frames that motions can
be defined with respect to. See
[ Face Detection and Understanding Reference Frames](rcommander_pr2/tutorials/Face Detection and Understanding Reference Frames)
for an example.

## ROS API



```clearsilver
node.0 {
srv{
0.name= broadcast_transform
0.type= tf_broadcast_server/BroadcastTransform
0.desc= Instructs the server to broadcast the given transform with its associated name.
}
srv{
1.name= stop_broadcast_transform
1.type= tf_broadcast_server/RemoveTransform
1.desc= Given a transform name, will remove it from the list of transforms being actively broadcasted.
}
srv{
2.name= clear_all_transforms
2.type= tf_broadcast_server/ClearTransforms
2.desc= Clears all transforms being broadcasted.
}
}
```


