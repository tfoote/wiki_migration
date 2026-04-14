## Nodes

```clearsilver
node.0 {
  name = ir_node
  desc = Node for transmitting IR codes.
  sub {
  
    0.name = ir_code_name
    0.type = std_msgs/String
    0.desc = Name of IR code, stored in ~code_dir.
  }
  param {
  
    0.name = ~code_dir
    0.type = string
    0.desc = Directory where pickled IR code data is stored.
  }
}
```
