## Nodes



```clearsilver
node.0 {
  name=pr2_dashboard_aggregator
  desc=`pr2_dashboard_aggregator` is the node that collects and republishes data that is commonly visualized by [[pr2_dashboard]].  This node is launched when bringing up a robot, e.g., in [[pr2_robot]]/`pr2.launch`. `pr2_dashboard_aggregator` also keeps track of which messages are "stale". For each message it subscribes to (and subsequently re-publishes), it maintains a "valid" flag which indicates if the data is "new enough" to be used.
  pub{
    0.name= dashboard_agg
    0.type= pr2_msgs/DashboardState
    0.desc= Aggregated state information.
  }
  sub{
    0.name= power_board/state
    0.type= pr2_msgs/PowerBoardState
    0.desc= The state of the PR2 power board
    1.name= power_state
    1.type= pr2_msgs/PowerState
    1.desc= The state of the PR2 power system
    2.name= ddwrt/accesspoint
    2.type= pr2_msgs/AccessPoint
    2.desc= The state of the PR2 wireless access point
    3.name= pr2_etherCAT/motors_halted
    3.type= std_msgs/Bool
    3.desc= Whether the motors are halted
  }
```
