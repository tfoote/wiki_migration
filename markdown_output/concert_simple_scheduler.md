  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"#ccccff style=\"border:1px solid black;text-align:center;vertical-align:top;\"\>This is part of the [Robotics in Concert](http://www.robotconcert.org/wiki/Main_Page) project.   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Overview

Because different systems require different scheduling policies, the
ROCON design allows for multiple scheduler implementations. The
scheduler runs as a ROS node on same master as the ROCON Conductor,
services and other Solution components.

This package supplies a simple fixed-priority scheduler using some
common infrastructure packages that other scheduler implementations can
use or modify.

## ROS Interface

```clearsilver
node.0 {
 name = simple_scheduler
 desc = This scheduler provides a relatively simple fixed-priority scheduler which allocates resources within each priority on a first-come, first-served basis.
 sub {
  0.name= rocon_scheduler
  0.type= scheduler_msgs/SchedulerRequests
  0.desc= Scheduler requests. Any ROCON service or application sending messages to this topic is called a '''requester'''.
  1.name= concert_client_changes
  1.type= concert_msgs/ConcertClients
  1.desc= ROCON clients known to the Conductor.
 }
 pub {
  0.name= rocon_scheduler_0123456789abcdef0123456789abcdef
  0.type= scheduler_msgs/SchedulerRequests
  0.desc= Per-requester scheduler feedback. Each '''requester''' assigns itself a universally unique identifier and subscribes to a feedback topic using the hexadecimal string representation of its UUID.
  1.name= resource_pool
  1.type= scheduler_msgs/KnownResources
  1.desc= The status of all ROCON clients currently managed by this scheduler.
 }
param {
  3.name= ~topic_name
  3.type= string
  3.default= rocon_scheduler
  3.desc= Name prefix to use for the request and feedback topics. Since the feedback topic is generated dynamically, it would otherwise be difficult to remap.
 }
}
```
