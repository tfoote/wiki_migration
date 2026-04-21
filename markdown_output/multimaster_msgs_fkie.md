<<MsgSrvDoc(multimaster_msgs_fkie)>>

## Master Discovering

The <<MsgLink(multimaster_msgs_fkie/ROSMaster)>> describes a
discovered ROS Master by `name` and `uri`. It offers also additional
information about corresponding
[master_discovery](http://ros.org/wiki/master_discovery_fkie) node and
timestamps of last detected changes of the ROS Master. The
<<SrvLink(multimaster_msgs_fkie/DiscoverMasters)>> service returns
the list with current discovered ROS Masters. The changes of each ROS
Master are annonced by
<<MsgLink(multimaster_msgs_fkie/MasterState)>>.

The <<MsgLink(multimaster_msgs_fkie/LinkState)>> and
<<MsgLink(multimaster_msgs_fkie/LinkStatesStamped)>> messages offers
additional information about the link quality to discovered ROS Master
machines.

## Synchronization

The <<SrvLink(multimaster_msgs_fkie/GetSyncInfo)>> service uses
<<MsgLink(multimaster_msgs_fkie/SyncMasterInfo)>> respectively
<<MsgLink(multimaster_msgs_fkie/SyncTopicInfo)>> messages to return
the all currently synchronized `topics` and `services`.

## Default Configuration

The services <<SrvLink(multimaster_msgs_fkie/ListNodes)>> and
<<SrvLink(multimaster_msgs_fkie/ListDescription)>> returns the nodes
and their description. The <<SrvLink(multimaster_msgs_fkie/Task)>>
service can then be used to launch one of these nodes. See
[default_cfg](http://ros.org/wiki/default_cfg_fkie) for additional
information.
