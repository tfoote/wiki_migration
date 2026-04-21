## rosnode command-line tool

The `rosnode` command-line tool displays information about ROS
[Nodes](Nodes). The currently supported commands are:



```
rosnode info	print information about node
rosnode kill	kill a running node
rosnode list	list active nodes
rosnode machine	list nodes running on a particular machine or list machines
rosnode ping	test connectivity to node
rosnode cleanup	purge registration information of unreachable nodes
```



### rosnode info

`info <node-name>` Display information about a node, including
publications and subscriptions. 

```
$ rosnode info /node_name
```



### rosnode kill

IMPORTANT: `rosnode kill` is not guaranteed to succeed. If a node is
hung or set to "respawn" in [roslaunch](roslaunch), it may either fail
to die or may quickly reappear.

`kill <node-name>\...` Kill one or more nodes by name.


```
$ rosnode kill rosout add_two_ints_server
```

 `kill` Interactive mode. This enables you to
select which node to kill from a numbered list, which is useful for
killing anonymous nodes.

```
$ rosnode kill
1. /rosout

Please enter the number of the node you wish to kill.
>
```

 `kill -a`, `kill
\--all` Kill all nodes.

### rosnode list

`list` Display a list of current nodes. 

```
$ rosnode list
```



`list <namespace>` Display a list of current nodes inside
`/namespace`. 

```
$ rosnode list /my_ns
```



`list -u` List XML-RPC URIs of current nodes. 

```
$ rosnode list -u
```


`list -a`, `list \--all` List name and XML-RPC URIs (all info) of
current nodes. 

```
$ rosnode list -a
```



### rosnode machine

`machine <machine-name>` List nodes running on a particular
machine.

```
$ rosnode machine ninja.local
/talker-ninja.local-72266-1257921234733
/rosout
/listener-ninja.local-72615-1257921238320
```



`machine` List all machines

### rosnode ping

`ping <node-name>` Ping a node repeatedly.

```
$ rosnode ping /node_name
```



`ping \--all` Ping all nodes. This option cannot be used with
`-c`.

```
$ rosnode info /node_name
```

0 ROS 0.11: `-a` may also be used.

`ping -c COUNT` Ping a node COUNT times. This option cannot be used
with `\--all`.

```
$ rosnode info /node_name
```

1

### rosnode cleanup

IMPORTANT: `rosnode cleanup` was meant as a temporary solution and its
use was not encouraged in normal operation. Its benefit is aesthetic and
it has the downside of potentially unregistering functioning nodes.
[Relevant discussion](http://answers.ros.org/question/9521/rosnode-zombies/).

`cleanup` Purge the registration of any node that cannot be contacted
immediately. Prints list of unreachable nodes which has to be confirmed.


```
$ rosnode info /node_name
```

2

## Roadmap

`rosnode` is a stable command-line tool within the ROS core toolchain.
No major feature development is currently scheduled for this tool.
