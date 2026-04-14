## Overview

Vapor_master is a drop in replacement for
[rosmaster](http://wiki.ros.org/rosmaster) enabling high availability
ROS service discovery. Vapor removes the single point of failure
fundamental to ROS1 enabling new options for achieving greater scale,
up-time and resiliency in ROS 1.x solutions.

Vapor applies to three use cases:

-   assembly lines
-   mobile robotics
-   cloud services

If you find yourself dissatisfied with the rosmaster\'s limitations:

-   single point of failure
-   no hot swap capabilities
-   inability to respond to system faults
-   incapable of fan out
-   in-memory only data storage

Then vapor_master is for you!

### Architecture

Vapor implements the
[ROS Master API](http://wiki.ros.org/ROS/Master_API) as well as the
[Parameter Server API](http://wiki.ros.org/ROS/Parameter%20Server%20API)
utilizing a modern micro services approach. Unlike rosmaster, which does
only supports an in-memory datastore, vapor persists data to a mongodb
database. This enables instances of vapor to come and go without the
need to stop all other ROS nodes left running on other computers.

![ vapor uses mongodb replication to work through failure \|width=50%](attachment:vapr-1-to-1-db.png )

In assembly lines and mobile robots utilizing 3 or more computers,
vapor_master can be deployed to all compute nodes. While mongodb can be
deployed to a minimum of 3 nodes. In this scenario the ROS_MASTER_URI
can be set to \`http:*localhost:11311\` as if each node were its own
rosmaster. In this way an given compute node can come and go as needed
without preventing ros parameter access or service discovery.*

![ scale up and fan out \| width=25%](attachment:vapor-scaling.jpg )

In cloud environments vapor_master can be deployed to all cloud
instances while a dedicated mongodb cluster is deployed along side. Thus
enabling coherent datacenter scale deployments of ROS 1.x work flows.

### Non-goals

Vapor does not:

-   Secure ROS 1.x for usage on untrusted networks
-   Replace ROS 2.0
-   Traverse NATs

Vapor\'s focus is on scaling ROS 1.x for applications which require high
availability but are unable to be ported to ROS 2.0. It does not address
the security short comings of ROS 1.
