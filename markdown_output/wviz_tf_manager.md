## Overview

When observing or controlling a robot remotely over high latency
connections, it is important to compress and limit the amount of data
being sent without sacrificing the amount of information being provided
to the client. For many robots, tf topics are quite large and are
published frequently. wviz_tf_manager publishes a topic tf_changes that
publishes the tfs that have changed at a given polling frequency. A tf
is considered to have changed if the change is larger than either the
translational_update_distance or the angular_update_distance (parameters
that are bot set by default to 10). By default the polling_frequency is
set to 10 hz but can be set as a rosparam in the launch file.
Additionally the node provides a service, publish_all_transforms, that
allows a client to request all transforms.

## Running the wviz_tf_manager node



```
$ rosrun wviz_tf_manager wviz_tf_manager
```



## Nodes



```clearsilver
pub {
  0.name= tf_changes
  0.type= tf/tfMessage
  0.desc= tf messages which have recently been updated
}
srv{
  0.name= ~<name>/publish_all_transforms
  0.type= wviz_tf_manager/PublishAllTransforms
  0.desc= Allows a client to request that all available tfs be published 
}
param{
  0.name=~<name>/polling_frequency
  0.default= 10
  0.type= double
  0.desc= Frequency at which changed tfs are published
  1.name=~<name>/translational_update_distance
  1.default= 10
  1.type= double
  1.desc= Minimum amount of translational change required 
  2.name=~<name>/angular_update_distance
  2.default= 10
  2.type= double
  2.desc= Minimum amount of angular change required

}
```


