## Overview

## ROS API



```clearsilver

node.0 {
name = fmrp
desc = nic
sub {
0{
name = ~<name>/taskTopic
type = fmrp/task_msg
desc = Basic GPS Data
}
}
pub {
0{
name = ~<name>/planTopic
type = fmrp/plan_msg
desc = Basic GPS Data
}
}
param {
  0.name = ~<name>/simpleGraph
  0.type = string 
  0.desc = Filename of xml with simple graph specification
  1.name = ~<name>/fullGraph
  1.type = string 
  1.desc = Filename of xml with full graph specification. Used only if simpleGraph is not set.
  2.name = ~<name>/rootNode
  2.type = int
  2.desc = Root node of spanning tree. If isn't set, that is used root from GraphML (doesn't work well yet)
  3.name = ~<name>/saveFullGraph 
  3.type = string
  3.desc = Where save generated full graph into GraphML. Is saved only if parameter exist.
  4.name = ~<name>/taskTopic 
  4.type = string
  4.desc = Topic name for task subscribing.
  5.name = ~<name>/planTopic 
  5.type = string
  5.desc = Topic name for output plans.
```


