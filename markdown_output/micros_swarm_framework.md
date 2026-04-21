## Overview

micros_swarm_framework is a programming framework to facilitate
application development involving robot swarms. It makes coding for
swarms much easier by providing an adequate swarm-level abstraction, as
well as tools for swarm management, various communication mechanisms and
so on. Enlightened by the Buzz programming language for robot swarms,
micros_swarm_framework also provides essential data structures, such as
Neighbor, Swarm, and Virtual Stigmergy, to the user. Most importantly,
it is completely compatible with ROS Indigo and presented in the form of
a C++ library, which means that all resources in the ROS ecosystem are
still available to the user. It is currently compatible with ROS Indigo,
and is also extensible to Opensplice DDS.

## Compile

```
mkdir -p catkin_ws/src
cd catkin_ws/src
catkin_init_workspace
git clone https://github.com/xuefengchang/micros_swarm_framework.git
cd ..
catkin_make -j1
source devel/setup.bash
```

## Architecture

In order to make it modular and extensible, we chose to decompose the
framework into a layered structure, as shown in Fig. 1. The
Communication Interface layer is to implement an abstraction of the
underlying communication mechanisms, and provides a set of unified
interface to layer above. At the core of the framework is a runtime
platform, based on which APIs including abstract data structures, such
as Swarm, Neighbor, and Virtual Stigmergy, are provided to the user.
Upon this core part, we are also trying to build a library of typical
swarm algorithms to further facilitate the application development.

![](attachment:framework.png)

## Experiments

### experiment1: Motion and Spatial Coordination

![](attachment:app1.png)

### experiment2: Separation into Multiple Swarms

![](attachment:app2.png)

### experiment3: Flocking

![](attachment:app3.png)

## Instructions

### Swarm

#### create a swarm

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```

#### get swarm id

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```

#### get swarm members

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```

#### join in a swarm unconditionally

```
s.join();  //join in the swarm s
```

#### leave a swarm unconditionally

```
s.leave();  //leave the swarm s
```

#### join in a swarm according to a certain condition

```
bool checkID(unsigned int id)
{
    if(id%2==0)
        return true;
    return false;
}

/*
 *you might need to learn the bind and function in boost libarary.
 */
boost::function<bool()> bf=boost::bind(&checkID, self_id);

s.select(bf);  //the robot whose id is even join in the swarm s
```

#### leave a swarm according to a certain condition

```
bool checkID(unsigned int id)
{
    if(id%2==0)
        return true;
    return false;
}

boost::function<bool()> bf=boost::bind(&checkID, self_id);

s.unselect(bf);  //the robot whose id is even leave the swarm s
```

#### execute a swarm task

```
void printID(unsigned int id)
{
    std::cout<<"id="<<id<<std::endl;
}

boost::function<void()> f = boost::bind(&printID, self_id);

s.execute(f);  //the robot in the swarm s print the id of themselves
```

#### execute a swarm task

```
void printID(unsigned int id)
{
    std::cout<<"id="<<id<<std::endl;
}

boost::function<void()> f = boost::bind(&printID, self_id);

s.execute(f);  //the robot in the swarm s print the id of themselves
```

#### swarm break up operation

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```0

#### swarm intersection operation

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```1

#### swarm union operation

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```2

#### swarm difference operation

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```3

#### swarm negation operation

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```4

### Neighbors

#### create a default neighbors structure

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```5

#### create a user-defined data type neighbors structure

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```6

#### neighbors foreach function

foreach function perform a function that has no return value on each
robot's data

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```7

#### neighbors map function

map function perform a function that has a return value on each robot's
data. generating a new Neighbors structure. Key is robot's id and value
is the new data after transforming.

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```8

#### neighbors reduce function

reduce function perform a function on the whole neighbors data structure
and get a single return value.

```
Swarm s = Swarm(1);  //create a swarm s with id 1
```9

#### neighbors filter function

filter function perform the filtering operation according to
user-defined judging method on each tuple. generating a new neighbors
structure.

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```0

#### neighbors kin function

neighborsFilter function is a special filter essentially. generating a
new neighbors structure. every robot in the new neighbors structure is
in a specified swarm.

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```1

#### neighbors nonkin function

opposite of the kin

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```2

### VirtualStigmergy

#### create a VirtualStigmergy

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```3

#### virtualStigmergyPut

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```4

#### virtualStigmergyGet

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```5

#### get the size of a VirtualStigmergy

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```6 note: we could define VirtualStigmergy
structure using the simple type, for example int, float, string. For the
user-defined data-type, we need to use the Macro definition defined in
the micros_swarm_framework to serialize in order to store and transport
data of this type. We provided two Macro definition:BOOST_SERIALIZE,
MEMBER:

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```7

### NeighborCommunication

#### create a Neighbor Communication

#### broadcast a <key, value> tuple

#### listen to a key, execute the corresponding callback

## Simulation

### Motion and Spatial Coordination

start the Stage with 20 robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```8 start the daemon nodes of all the robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
int id=s.id();
```9 wait a minute, in order that all the daemon
nodes are started successfully, then start the App1 of all the robots.

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```0

### Separation into Multiple Swarms

start the Stage with 20 robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```1 start the daemon nodes of all the robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```2 wait a minute, in order that all the daemon
nodes are started successfully, then start the App2 of all the robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```3

### Flocking

start the Stage with 20 robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```4 start the daemon nodes of all the robots

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```5 wait a minute, in order that all the daemon
nodes are started successfully, then start the App3 of all the robots.

```
Swarm s = Swarm(1);  //create a swarm s with id 1
std::set<int> m=s.members();
```6
