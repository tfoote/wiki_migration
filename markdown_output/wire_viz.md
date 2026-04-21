## Goal

The goal of the wire_viz package is to visualize the input and the
output send to and received from the [wire_core](wire_core) package of
the [wire](wire) stack in RViz.

## Tutorial

A tutorial explaining this package is part of the [wire](wire) tutorials
and can be found [here](wire/Tutorials/Visualizing the world model).

## Nodes

### Topics



```clearsilver
pub {
  0.name=visualization_markers/world_evidence
  0.type=visualization_msgs/MarkerArray
  0.desc= Marker array representing the world model input
  1.name=visualization_markers/world_state
  1.type=visualization_msgs/MarkerArray
  1.desc= Marker array representing the world model output
}
sub {
  0.name= world_evidence
  0.type= world_model_msgs/WorldEvidence
  0.desc= Listen to the evidence fed to the world model.
  1.name= world_state
  1.type= world_model_msgs/WorldState
  1.desc= Listen to the estimated world state provided by the world model.
}
```



### Parameters



```clearsilver
param {
  0.name = show_cov
  0.default = false
  0.type = bool
  0.desc = Let the marker size grow with increasing covariance
  1.name = show_text
  1.default = true
  1.type = bool
  1.desc = Add text label to the marker
  2.name = show_id
  2.default = true
  2.type = bool
  2.desc = Show the 
  3.name = r
  3.default = 1.0
  3.type = double
  3.desc = Default color markers r-channel
  4.name = g
  4.default = 1.0
  4.type = double
  4.desc = Default color markers g-channel
  5.name = b
  5.default = 1.0
  5.type = double
  5.desc = Default color markers b-channel
  6.name = alpha
  6.default = 1.0
  6.type = double
  6.desc = Default transparency color markers (alpha)
  7.name = scale_x
  7.default = 0.1
  7.type = double
  7.desc = Size of the marker in x-direction
  8.name = scale_y
  8.default = 0.1
  8.type = double
  8.desc = Size of the marker in y-direction
  9.name = scale_z
  9.default = 0.1
  9.type = double
  9.desc = Size of the marker in z-direction
  10.name = offset_x_pos
  10.default = 0
  10.type = double
  10.desc = Offset of the marker position in the x-direction
  11.name = offset_y_pos
  11.default = 0
  11.type = double
  11.desc = Offset of the marker position in the y-direction
  12.name = offset_z_pos
  12.default = 0
  12.type = double
  12.desc = Offset of the marker position in the z-direction
  13.name = offset_x_rot
  13.default = 0
  13.type = double
  13.desc = Offset of the marker orientation in the x-direction
  14.name = offset_y_rot
  14.default = 0
  14.type = double
  14.desc = Offset of the marker orientation in the y-direction
  15.name = offset_z_rot
  15.default = 0
  15.type = double
  15.desc = Offset of the marker orientation in the z-direction
  16.name = offset_w_rot
  16.default = 0
  16.type = double
  16.desc = Offset of the marker orientation in the w-direction
  17.name = mesh_resource
  17.default = ""
  17.type = string
  17.desc = Default mesh resource for the geometric markers (default is no mesh)
  18.name = marker_type
  18.default = sphere
  18.type = string
  18.desc = Geometric shape of the marker, e.g., sphere, cube, cylinder
  19.name = duration
  19.default = 1.0
  19.type = double
  19.desc = Lifetime of the marker
}
```


