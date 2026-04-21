## Nodes



```clearsilver
node.0 {
  name = mouse
  desc = Uses a pose to control an on-screen mouse. After startup, press ''h'' for help with keyboard commands.
  sub {
  
    0.name = head_pose
    0.type = geometry_msgs/PoseStamped
    0.desc = The input pose
  }
  pub {
  
    0.name = mouse
    0.type = geometry_msgs/PointStamped
    0.desc = A 2D point containing the current cursor position
  }
  param {
  
    0.name = ~move_mouse
    0.type = bool
    0.desc = Sets whether mouse movement is enabled when the node launches. Mouse movement can also be enabled and disabled with keyboard commands.
  }
}
```


