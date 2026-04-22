## Overview

This package provides the two nodes, that enable to run and interact
with different non-ros-programs. `rosshell` can be used to start a
program or any kind of shell-command. If some kind of interaction with
the programs is required, use `rosshellX` to receive and send messages
from stdin, stdout, and stderr.

## Usage

The required commands are always defined as a string:



```
$ rosrun rosshell rosshell.py "command"
```





```
$ rosrun rosshell rosshellX.py "command"
```



have a look at the examples or at the included launch-files.

## Examples

### rosshell

This command is just used to generate some random noise \...


```
$ rosrun rosshell rosshell.py "aplay -c 2 -f S16_LE -r 44100 /dev/urandom"
```



Pipe the results of /dev/random into a text file \...


```
$ rosrun rosshell rosshell.py "cat /dev/random > test.txt"
```



or the some information about the current directory \...


```
$ rosrun rosshell rosshell.py "ls -Shal > test.txt"
```



### rosshellX

This node is used if you require some interaction with stdin, stdout,
and stderr.

`rosshellX` is by default subscribed to /rosshellX/stdin and publishes
at topic /rosshellX/stdout and /rosshellX/stderr, all of type
[std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html).

#### Some basic calculations

`bc` is just a simple commandline-calculator

1\. open three shells 2. start `bc` with the following command:


```
$ rosrun rosshell rosshellX.py "bc"
```

 3. print the the results of `bc` stdout by
running: 

```
$ rostopic echo /rosshellX/stdout
```

 4. and now, send some inputs like:


```shell
$ rostopic pub /rosshellX/stdin std_msgs/String "99*99\n"
$ rostopic pub /rosshellX/stdin std_msgs/String "sqrt(2.0)\n"
$ rostopic pub /rosshellX/stdin std_msgs/String "33^3\n"
$ rostopic pub /rosshellX/stdin std_msgs/String "quit\n"
```

 5. to interact a bit with stderr, simply
subscribe for: 

```
$ rostopic echo /rosshellX/stderr
```

 and publish some nonsense like


```shell
$ rostopic pub /rosshellX/stdin std_msgs/String "öjaki\n"
```



#### Additional functionality

To get some filesystem-information try: 

```
$ rosrun rosshell rosshellX.py "command"
```

0

or



```
$ rosrun rosshell rosshellX.py "command"
```

1

both are the same but you also have the possibility to change the
command and topics, also within the launch-file, have a look at
`rosshellX.launch` \...



```
$ rosrun rosshell rosshellX.py "command"
```

2

## Nodes



```
$ rosrun rosshell rosshellX.py "command"
```

3

## Bug Reports & Feature Requests ==/
