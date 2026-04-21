`rosping` is the tool to send ICMP ECHO_REQUEST to network hosts and
send back to you as rostopic message

## rosping Usage

`rosping <host>`

send ICMP ECHO_REQUEST to <host>

-   `host`: network address or hostname to ping

## Examples

```
$ rosrun rosping rosping 8.8.8.8
32 bytes from 8.8.8.8: icmp_seq=131, ttl=45, time=40.958 ms
32 bytes from 8.8.8.8: icmp_seq=132, ttl=45, time=40.856 ms
$ rostopic echo ping/delay
data: 40.903
---
data: 40.961
```

## ROS API

```clearsilver
node.0 {
  name=rosping
  desc=`rosping` is a node that publish ping result of hostaname
  sub{
  }
  pub{
    0.name=~delay
    0.type=std_msgs/Float
    0.desc=Network Delay(sec) between current machine and hostnamae
  }
  srv{
  }
  param {
    1.name= ~rate
    1.default=10
    1.type= float
    1.desc= duration between sending ping, 10.0 means 0.1 [hz]
}
```
