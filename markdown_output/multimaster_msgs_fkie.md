## Master Discovering

The
[multimaster_msgs_fkie/msg/ROSMaster](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/msg/ROSMaster.html)
describes a discovered ROS Master by `name` and `uri`. It offers
also additional information about corresponding
[master_discovery](http://ros.org/wiki/master_discovery_fkie) node and
timestamps of last detected changes of the ROS Master. The
[multimaster_msgs_fkie/srv/DiscoverMasters](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/srv/DiscoverMasters.html)
service returns the list with current discovered ROS Masters. The
changes of each ROS Master are annonced by
[multimaster_msgs_fkie/msg/MasterState](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/msg/MasterState.html).

The
[multimaster_msgs_fkie/msg/LinkState](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/msg/LinkState.html)
and
[multimaster_msgs_fkie/msg/LinkStatesStamped](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/msg/LinkStatesStamped.html)
messages offers additional information about the link quality to
discovered ROS Master machines.

## Synchronization

The
[multimaster_msgs_fkie/srv/GetSyncInfo](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/srv/GetSyncInfo.html)
service uses
[multimaster_msgs_fkie/msg/SyncMasterInfo](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/msg/SyncMasterInfo.html)
respectively
[multimaster_msgs_fkie/msg/SyncTopicInfo](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/msg/SyncTopicInfo.html)
messages to return the all currently synchronized `topics` and
`services`.

## Default Configuration

The services
[multimaster_msgs_fkie/srv/ListNodes](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/srv/ListNodes.html)
and
[multimaster_msgs_fkie/srv/ListDescription](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/srv/ListDescription.html)
returns the nodes and their description. The
[multimaster_msgs_fkie/srv/Task](https://docs.ros.org/en/rolling/p/multimaster_msgs_fkie/srv/Task.html)
service can then be used to launch one of these nodes. See
[default_cfg](http://ros.org/wiki/default_cfg_fkie) for additional
information.
