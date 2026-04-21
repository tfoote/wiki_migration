The task allocation uses a market-inspired approach by running a
single-round, single-item auction. The package offers two action servers
that perform the auction, one that acts as auctioneer and one that acts
as bidder. The auctioneer opens the auction for a specific duration in
which interested bidders can place a single bid. After the timeout the
winner, i.e., the bidder with the highest bid is announced.

## Dependencies

This package depends on the following message definitions:

-   [actionlib_msgs](actionlib_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The communication between CPSs is based on the
[CPSwarm Communication Library](https://github.com/cpswarm/swarmio).

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   \*_pos_provider

Further required packages are:

-   [actionlib](actionlib)

## Execution

To start the action servers, run the launch file


```
roslaunch task_allocation task_allocation.launch
```

 which launches both action servers which listen
for incoming requests.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`task_allocation.yaml` that allows to configure the behavior of the
auction process.

## Nodes



```clearsilver

node.0{
name=auction_action
desc=The `auction_action` node offers the `task_allocation_auction` action server that acts as auctioneer in the task allocation auction. When the action is called, it opens an auction and announces the task with ID and location. It then waits a specific time for the bids of other CPS. Once the auction timeout expires, it broadcasts the ID of the winning CPS, i.e., the one with the highest bid, to which the task is assigned. If no CPS participated in the auction, the action server aborts the auction goal.

goal{
0.name=cmd/task_allocation_auction/goal
0.type=cpswarm_msgs/TaskAllocationGoal
0.desc=A goal to start an auction containing the universally unique ID (UUID) of the auctioneer together with the ID and the position of the task that is auctioned.
}

result{
0.name=cmd/task_allocation_auction/result
0.type=cpswarm_msgs/TaskAllocationResult
0.desc=The result of the auction contains the UUID of the winning CPS, together with ID and position of the task that has been auctioned.
}

sub{
0.name=bridge/events/cps_selection
0.type=cpswarm_msgs/TaskAllocationEvent
0.desc=The the bids of the auction from other CPSs. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

pub{
0.name=cps_selected
0.type=cpswarm_msgs/TaskAllocatedEvent
0.desc=The UUID of the CPS that won the auction to the other CPSs. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

param{
0.name=~loop_rate
0.type=real
0.default=5.0
0.desc=The frequency in Hz at which to run the control loops.
1.name=~queue_size
1.type=integer
1.default=10
1.desc=The size of the message queue used for publishing and subscribing to topics.
2.name=~timeout
2.type=real
2.default=10.0
2.desc=The time in seconds to listen for incoming bids from other CPSs after the auction has been opened, i.e., auction duration.
}
}

node.1{
name=bid_action
desc=The `bid_action` node offers the `task_allocation_bid` action server that acts as bidder in the task allocation auction opened by another CPS. When the action is called, it computes a bid for the task based on its location. The bid value is inversely proportional to the distance between the CPS and the task. It publishes the bid and waits until the auction ends. If the CPS has won the auction, the action server goal succeeds, otherwise it is aborted.

goal{
0.name=cmd/task_allocation_bid/goal
0.type=cpswarm_msgs/TaskAllocationGoal
0.desc=A goal to compute a bid containing the universally unique ID (UUID) of the auctioneer together with the ID and the position of the task that is auctioned.
}

result{
0.name=cmd/task_allocation_bid/result
0.type=cpswarm_msgs/TaskAllocationResult
0.desc=The result of the auction contains ID and position of the task that has been auctioned.
}

sub{
0.name=pos_provider/pose
0.type=geometry_msgs/PoseStamped
0.desc=The current position of the CPS.
1.name=bridge/uuid
1.type=swarmros/String
1.desc=The UUID of this CPS. It is published by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
2.name=bridge/events/cps_selected
2.type=cpswarm_msgs/TaskAllocatedEvent
2.desc=The UUID of the CPS that won the auction. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

pub{
0.name=cps_selection
0.type=cpswarm_msgs/TaskAllocationEvent
0.desc=The auction bid submitted to the auctioneer CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

param{
0.name=~loop_rate
0.type=real
0.default=5.0
0.desc=The frequency in Hz at which to run the control loops.
1.name=~queue_size
1.type=integer
1.default=10
1.desc=The size of the message queue used for publishing and subscribing to topics.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
