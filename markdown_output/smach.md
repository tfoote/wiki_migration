1.  keywords State, Machine, Statemachine, Executive

  -- ------------------------------- -- -- -- ---------------------- --
     English            [简体中文](cn/smach)   
  -- ------------------------------- -- -- -- ---------------------- --

[Youtube](https://www.youtube.com/watch?v=F3slROzVNbc)

## About SMACH

**When should I use SMACH?**

SMACH is useful when you want a robot to execute some complex plan,
where all possible states and state transitions can be described
explicitly. This basically takes the hacking out of hacking together
different modules to make systems like mobile robotic manipulators do
interesting things.

- Fast prototyping: The straightforward Python-based SMACH syntax makes
  it easy to quickly prototype a state machine and start running it.

<!-- -->

- Complex state machines: SMACH allows you to design, maintain and debug
  large, complex hierarchical state machines. You can find an example of
  a complex hierarchical state machine [here](pr2_plugs_executive).

<!-- -->

- Introspection: SMACH gives you full introspection in your state
  machines, state transitions, data flow, etc. See the
  [smach_viewer](https://index.ros.org/p/smach_viewer) for more details.

**When should I NOT use SMACH?**

- Unstructured tasks: SMACH will fall short as the scheduling of your
  task becomes less structured.
- Low-level systems: SMACH is not meant to be used as a state machine
  for *low-level* systems that require high efficiency, SMACH is a
  *task-level* architecture.
- Smash: Do not use SMACH when you want to smash something, for that use
  [ smash](https://en.wikipedia.org/wiki/Hulk_and_the_Agents_of_S.M.A.S.H.).

**Is SMACH only a finite state machine library?**

You can build a finite state machine using SMACH, but SMACH can do much
more. SMACH is a library for task-level execution and coordination, and
provides several types of "state containers". One such container, is a
finite state machine, but this container can also be a state in another
container. See the [tutorials page](#tutorials) for
a list of containers and states built into SMACH.

## Documentation

The [documentation page](#documentation-1) provides an
overview of the concepts used in SMACH.

The [tutorials page](#tutorials) contains an
extensive set of tutorials to get you up to speed building and running
your own state machines.

## Tutorials

### SMACH Tutorials

#### Learning SMACH

If you just want to look at code, try out the learning by example. If
you rather follow a step-by-step guide, choose the step-by-step
tutorials.

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------ --
     <width="50%">**Learning Step-by-Step**                                                                                                                             <width="50%">**Learning by Example**   
     <\^> \* [Getting Started with smach](#getting-started-with-smach): This tutorial guides you through the very first steps of using smach.                                                 
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------ --

- [Passing User Data between States](#passing-user-data-between-states):
  This tutorial teaches you how to pass data from one state(machine) to
  the next state(machine).
- [Create a Hierarchical State Machine](#create-a-hierarchical-state-machine):
  This tutorial teaches you how to nest different state machines,
  creating a hierarchical state machine.
- [Calling Actions from a State Machine (ROS)](#calling-actions-from-a-state-machine-ros):
  This tutorial teaches you how to call action servers from within a
  SMACH state machine.
- [Viewing State Machines (ROS)](#viewing-state-machines-ros):
  This tutorial shows you how to use the smach viewer, a simple tool to
  monitor state machines and get introspection into the data flow
  between states.\|\|<\^> \*
  [Simple State Machine](#simple-state-machine):
  This tutorial shows how to put together a simple state machine with
  two states.
- [User Data Passing](#user-data-passing):
  This tutorial gives an example of two states passing user data to each
  other.
- [Nesting State Machines](#nesting-state-machines):
  This tutorial gives an example of nesting a state machine in another
  state machine, creating a hierarchical state machine.
- [Concurrent State Machine](#concurrent-state-machine):
  This tutorial shows an example of running two states in parallel.
- [Simple Action State (ROS)](#simple-action-state-ros):
  This tutorial shows an example of states that call directly into the
  actionlib interface.\|\|

#### SMACH Containers

- [StateMachine container](#statemachine-container):
  This tutorial teaches you how to use the !StateMachine container.
- [Concurrence container](#concurrence-container):
  This tutorial teaches you how to use the Concurrence container.
- [Sequence container](#sequence-container):
  This tutorial teaches you how to use the Sequence container.
- [Iterator container](#iterator-container):
  This tutorial teaches you how to use the Iterator container.
- [Wrapping a Container With actionlib](#wrapping-a-container-with-actionlib):
  This tutorial explains how to serve out a SMACH plan as an action over
  [actionlib](https://index.ros.org/p/actionlib).

#### SMACH States

- [Generic State](#generic-state):
  This tutorial show how to implement a generic SMACH State
- [CBState](#cbstate): This tutorial
  gives an example of how to use CBState, a state that simply executes a
  callback when it is active.
- [SimpleActionState (ROS)](#simpleactionstate-ros):
  This tutorial show how to use the !SimpleActionState to directly call
  an action interface using SMACH
- [ServiceState (ROS)](#servicestate-ros):
  This tutorial shows how to represent the execution of a service as a
  SMACH state.
- [MonitorState (ROS)](#monitorstate-ros):
  Monitor a state!

#### Advanced SMACH

- [StateMachinePreemption](#statemachinepreemption):
  Example of a state machine that implements preemption, using a
  concurrence container and monitor state.
- [State Preemption Implementation](#state-preemption-implementation):
  This tutorial shows how to implement simple flag-based preemption in
  SMACH states.
- [Writing Custom Container Classes](#writing-custom-container-classes):
  Most tasks can be performed without writing new types of container
  classes, but this tutorial explains how to write a new one.
- [Writing Custom State Classes with User-defined Callbacks](#writing-custom-state-classes-with-user-defined-callbacks):
  Sometimes you want to create a state class like
  smach.!SimpleActionState which receives user callbacks as arguments.
  If these callbacks change the SMACH interface of a state (outcomes,
  userdata keys), then the callbacks need to be annotated with this
  information.

### Test your SMACH knowledge

If you're interested in testing your SMACH knowledge,
[this page](#usecase) has a step-by-step
test/example to test your knowledge of different states and containers.

## Documentation

### SMACH Documentation

#### Concepts

##### Outcome Semantics

For all SMACH containers, the interface to contained states is defined
via **`'state outcomes`**'. A state's potential outcomes are a
property of the state instance, and must be declared before it is
executed. If a SMACH plan is written by hand, all potential outcomes are
declared on construction and the consistency of the state transitions
can easily be checked without executing it.

State outcomes may cause different things to happen in different types
of containers, but what happens after an outcome is emitted is
irrelevant from perspective of the state. In this sense, outcomes can be
considered "local" to a given state.

For example, a state might provide outcomes such as '`succeeded`',
'`aborted`', or '`preempted`' and as far as the state is concerned,
this is the way that it interacts with the task-level state flow. In the
context of a state machine, these outcomes would be associated with
other states, thus forming a transition. In the context of another
container, however, they might be treated differently. Outcomes simply
acts as a common interface between states and containers.

##### User Data

SMACH containers each have a flat database used to coordinate and pass
data between different states. This becomes useful when states compute
some result or return some sensor information. This allows such data to
be held at the execution level, and made available to other tasks or
procedures.

Similarly to outcomes, the userdata keys that are set and retrieved in
each state are described by the state's **`'input keys`**' and
**`'output keys`**'. These are also a property of the state instance,
and must be declared prior to execution. The declaration of all of these
interactions prevents errors and aides in debugging when the SMACH plans
become complex.

For information on the user data API see
[Manipulating Userdata in SMACH](#passing-user-data-between-states).

##### Preemption

Preemption propagation is built into SMACH. The `State` base class
includes an interface for coordinating preempt requests between
containers and contained states. Each container type has its own
well-defined behavior for responding to a preempt request. This allows
the system to both cleanly respond to termination signals from an end
user and be able to be canceled programmatically by a higher-level
executive.

##### Introspection

SMACH containers can provide a debugging interface which allows a
developer to (over ROS) set the full initial state of a SMACH tree. This
is visualized with the
[SMACH Viewer](https://index.ros.org/p/smach_viewer). This includes both
the initial state labels of each container as well as the contents of
the user data structures at each level.

#### States

"State" can mean different things in different contexts. In SMACH, a
"state" is a local state of execution, or equivalently a "state"
corresponds to the system performing some task. This is different from
formal state machines, where each state describes not what the system is
doing but rather describes a given configuration of the system. This
allows the user to focus on what the system is executing and the results
from said execution, as opposed to naming the points between execution.
States in SMACH correspond more to states in structured programming. For
more on this distinction, as well as how to visualize states in SMACH,
see
[State Diagrams VS Flow Charts](http://en.wikipedia.org/wiki/State_diagram#State_diagrams_versus_flowcharts).

##### Provided State Classes

  -- -------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------- -- ------------------------------------- --
     **Class**                                                                                                                                 **Description**                                                                 **Outcomes**                          
     State                                                                                                                                     State base interface.                                                           None                                  
     SPAState                                                                                                                                  A state which has three commonly used pre-defined outcomes.                     *succeeded*, *preempted*, *aborted*   
     [MonitorState](http://docs.ros.org/groovy/api/smach_ros/html/python/smach_ros.monitor_state.MonitorState-class.html)                      A state that subscribes to a ROS topic and blocks while a condition holds.      *valid*, *invalid*, *preempted*       
     [ConditionState](http://docs.ros.org/groovy/api/smach_ros/html/python/smach_ros.condition_state.ConditionState-class.html)                A state that executes a condition callback.                                     *true*, *false*                       
     [SimpleActionState](http://docs.ros.org/groovy/api/smach_ros/html/python/smach_ros.simple_action_state.SimpleActionState-class.html)      A state which acts as a proxy to a simple *actionlib* action.                   *succeeded*, *preempted*, *aborted*   
  -- -------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------- -- ------------------------------------- --

#### Containers

There are several container types that are provided by the SMACH
library. Different containers provide different execution semantics, but
they can all be treated like states in other containers. Containers may
have their own ways of specifying transitions for contained states,
since "transition" means different things in different contexts.

All SMACH containers have the following properties:

- They contain a dictionary of states where objects implementing the
  smach.State interface are keyed by string *labels*.
- They contain a userdata structure that all of their children can
  access.
- In order to modify the structure of a container, it must be *opened*
  (see below).

##### Opening Containers for Construction

This is done either by using Python's `with` keyword, or by calling
`open()` and `close()` on the container object. The `with` keyword can
be used either with the container object itself, or on the container's
`opened` method.

##### Adding States to Containers

SMACH containers provide static methods for adding children. These
methods access the currently open container and add the states
accordingly.

##### Provided Container Classes

  -- -------------------------------------------------------------------------------------------------------------- -- ----------------- --
     **Class**                                                                                                         **Description**   
     [StateMachine](http://docs.ros.org/groovy/api/smach/html/python/smach.state_machine.StateMachine-class.html)                        
     [Concurrence](http://docs.ros.org/groovy/api/smach/html/python/smach.concurrence.Concurrence-class.html)                            
     [Sequence](http://docs.ros.org/groovy/api/smach/html/python/smach.sequence.Sequence-class.html)                                     
     [Iterator](http://docs.ros.org/groovy/api/smach/html/python/smach.iterator.Iterator-class.html)                                     
  -- -------------------------------------------------------------------------------------------------------------- -- ----------------- --

## Troubleshooting

### Debugging SMACH state machines

SMACH comes with the
[smach_viewer](https://index.ros.org/p/smach_viewer), a GUI environment
to visualizes state machines. The smach viewer also gives introspection
into a running state machine. To learn more about the smach viewer, take
a look at
[this tutorial](#viewing-state-machines-ros).

### Report a Bug

## Getting Started with smach

### Why learn Smach?

Smach, which stands for "State Machine", is a powerful and scalable
Python-based library for hierarchical state machines. The Smach library
does not depend on ROS, and can be used in any Python project. The
[executive_smach](https://index.ros.org/p/executive_smach) stack however
provides very nice integration with ROS, including smooth
[actionlib](https://index.ros.org/p/actionlib) integration and a
powerful [Smach viewer](https://index.ros.org/p/smach_viewer) to
visualize and introspect state machines.

It is very easy to write a simple Smach state machine, while at the same
time Smach allows you to design, maintain and debug large, complex
hierarchical state machines. The image below shows an example state
machine used to coordinate
[actionlib](https://index.ros.org/p/actionlib) actions that allow the
PR2 robot to
[charge itself at a standard outlet](https://index.ros.org/p/pr2_plugs).

![width="750"](doc/smach.png)

### Installing Smach



```
$ sudo apt-get install ros-noetic-smach-ros
```



### Creating a State Machine

To create a Smach state machine, you first create a number of states,
and then add those states to a State Machine container.

#### Creating a state

To create a state, you simply inherit from the `State` base class, and
implement the `State.execute(userdata)` method:



```python
  class Foo(smach.State):
     def __init__(self, outcomes=['outcome1', 'outcome2']):
       # Your state initialization goes here

     def execute(self, userdata):
        # Your state execution goes here
        if xxxx:
            return 'outcome1'
        else:
            return 'outcome2'
```



- In the **init** method you initialize your state class. Make sure to
  never block in the init method! If you need to wait for other parts of
  your system to start up, do this from a separate thread.

<!-- -->

- In the **execute** method of a state the actual work is done. Here you
  can execute any code you want. It is okay to block in this method as
  long as you like. Once you return from this method, the current state
  is finished.

<!-- -->

- When a state finishes, it returns an **outcome**. Each state has a
  number of possible outcomes associated with it. An outcome is a
  user-defined string that describes how a state finishes. A set of
  possible outcomes could for example be \['succeeded', 'failed',
  'awesome'\]. The transition to the next state will be specified
  based on the outcome of the previous state.

#### Adding states to a state machine

A state machine is a container that holds a number of states. When
adding a state to a state machine container, you specify the transitions
between the states.



```python
  sm = smach.StateMachine(outcomes=['outcome4','outcome5'])
  with sm:
     smach.StateMachine.add('FOO', Foo(),
                            transitions={'outcome1':'BAR',
                                         'outcome2':'outcome4'})
     smach.StateMachine.add('BAR', Bar(),
                            transitions={'outcome2':'FOO'})
```

 The resulting state machine looks like this:

![width="350"](doc/simple.png)

- The red boxes show the possible **outcomes** of the state machine
  container: outcome4 and outcome5, as specified in line 1.
- In line 3-5 we **add** the first state to the container, and call it
  FOO. The convention is to name states with all caps. If the outcome of
  state FOO is 'outcome1', then we transition to state BAR. If the
  outcome of state FOO is 'outcome2', then the whole state machine
  will exit with 'outcome4'.
- Every state machine container is also a state. So you can **nest state
  machines** by adding a state machine container to another state
  machine container.

#### Example

This is a complete runnable example you can find in the
[executive_smach_tutorials](executive_smach_tutorials) package.



```wiki
<<GetCode(https://raw.githubusercontent.com/rhaschke/executive_smach_tutorials/indigo-devel/examples/state_machine_simple.py,#!python)>>
```

 Running the example:

For ROS Kinetic (and newer) versions just clone the git repository, cd
into the folder "executive_smach_tutorials" and run the example
(inside your ros environment) 

```
$ git clone https://github.com/eacousineau/executive_smach_tutorials.git
$ cd executive_smach_tutorials
$ ./examples/state_machine_simple.py
```



For older ROS-versions you can install the smach_tutorials package using
rosdep. 

```
$ roscd smach_tutorials
$ ./examples/state_machine_simple.py
```



This should give you the following output:



```
[INFO] 1279835117.234563: Executing state FOO
[INFO] 1279835117.234849: State machine transitioning 'FOO':'outcome1'-->'BAR'
[INFO] 1279835117.235114: Executing state BAR
[INFO] 1279835117.235360: State machine transitioning 'BAR':'outcome2'-->'FOO'
[INFO] 1279835117.235633: Executing state FOO
[INFO] 1279835117.235884: State machine transitioning 'FOO':'outcome1'-->'BAR'
[INFO] 1279835117.236143: Executing state BAR
[INFO] 1279835117.236387: State machine transitioning 'BAR':'outcome2'-->'FOO'
[INFO] 1279835117.236644: Executing state FOO
[INFO] 1279835117.236891: State machine transitioning 'FOO':'outcome1'-->'BAR'
[INFO] 1279835117.237149: Executing state BAR
[INFO] 1279835117.237394: State machine transitioning 'BAR':'outcome2'-->'FOO'
[INFO] 1279835117.237652: Executing state FOO
[INFO] 1279835117.237898: State machine terminating 'FOO':'outcome2':'outcome4'
```



### Pre-defined States and Containers

#### State library

The example above shows how you can implement your own states. However,
Smach comes with a whole library of pre-implemented states that cover
many common usecases:

- **!SimpleActionState**: automatically call
  [actionlib](https://index.ros.org/p/actionlib) actions.
- **!ServiceState**: automatically call ROS services
- **!MonitorState**
- \...

The 'Smach States' section on the
[tutorials page](#tutorials) gives an overview of
all available states.

#### Container library

Similarly, Smach also comes with a set of useful containers:

- **!StateMachine**: the generic state machine container
- **Concurrence**: a state machine that can run multiple states in
  parallel.
- **Sequence**: a state machine that makes it easy to execute a set of
  states in sequence. The 'Smach Containers' section on the
  [tutorials page](#tutorials) gives an overview of
  all available containers.

![width="350"](doc/containers.png)

The [next tutorial](#passing-user-data-between-states) will
teach you how to pass user data between different states and state
machines.

## Passing User Data between States

### Specifying User Data

A state could require some input data to do its work, and/or it could
have some output data it wants to provide to other states. The input and
output data of a state is called **userdata** of the state. When you
construct a state, you can specify the names of the userdata fields it
needs/provides.



```python
  class Foo(smach.State):
     def __init__(self, outcomes=['outcome1', 'outcome2'],
                        input_keys=['foo_input'],
                        output_keys=['foo_output'])

     def execute(self, userdata):
        # Do something with userdata
        if userdata.foo_input == 1:
            return 'outcome1'
        else:
            userdata.foo_output = 3
            return 'outcome2'
```



- The **input_keys** list enumerates all the inputs that a state needs
  to run. A state declares that it expect these fields to exist in the
  userdata. The execute method is provided a copy of the userdata
  struct. The state can read from all userdata fields that it enumerates
  in the input_keys list, but it can't write to any of these fields.

<!-- -->

- The **output_keys** list enumerates all the outputs that a state
  provides. The state can write to all fields in the userdata struct
  that are enumerated in the output_keys list.

**/!\\ Note:** Objects obtained from userdata via input_keys are wrapped
for immutability, thus a state cannot call methods on these objects. If
you require a mutable input object, you must specify the same key in
both input_keys and output_keys. If you are not passing objects, or you
do not need to call methods on or modify them, you should use unique
names in input_keys and output_keys, to avoid confusion and potential
bugs.

![width="250"](doc/user_data_single.png)

The interface to a state is defined by its outcomes, its input keys and
its output keys.

### Connecting User Data

When adding states to a state machine, you also need to connect the user
data fields, to allow states to pass data to each other. For example, if
state FOO produces 'foo_output', and state BAR needs 'bar_input',
then you can attach these two user data ports together using name
remapping:



```python
  sm_top = smach.StateMachine(outcomes=['outcome4','outcome5'],
                          input_keys=['sm_input'],
                          output_keys=['sm_output'])
  with sm_top:
     smach.StateMachine.add('FOO', Foo(),
                            transitions={'outcome1':'BAR',
                                         'outcome2':'outcome4'},
                            remapping={'foo_input':'sm_input',
                                       'foo_output':'sm_data'})
     smach.StateMachine.add('BAR', Bar(),
                            transitions={'outcome2':'FOO'},
                            remapping={'bar_input':'sm_data',
                                       'bar_output1':'sm_output'})
```

 The remapping field maps the in/output_key of a
state to a userdata field of the state machine. So when you remap
'x':'y':

- x needs to be an input_key or an output_key of the state, and
- y will automatically become part of the userdata of the state machine.

/!\\ Note that remapping is *not required* when the user data names used
in your state are the same as the user data names used by the state
machine. However, remapping makes the connections very explicit, so it
is *recommended* to always specify remapping, even something like
"remapping={'a':'a'}".

#### Passing data between states

We can use the remapping mechanism to pass data from state FOO to state
BAR. To accomplish this, we need one remapping when adding FOO, and one
remapping when adding BAR:

- FOO: remapping={'foo_output':'sm_user_data'}
- BAR: remapping={'bar_input':'sm_user_data'}

#### Passing data between state machines and states

We can also use the remapping mechanism to pass data from a state BAR to
the state machine that contains BAR. If 'sm_output' is an output key
of the state machine:

- BAR: remapping={'bar_output':'sm_output'}

Or, the opposite, we can pass data from the state machine to a state
FOO. If 'sm_input' is an input key of the state machine:

- FOO: remapping={'foo_input':'sm_input'}

![width="650"](doc/user_data.png)

### Example

This is a complete runnable example you can find in the
[executive_smach_tutorials](executive_smach_tutorials) package.



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/user_data2.py,#!python)>>
```

 Running the example:



```
$ roscd smach_tutorials
 $ ./examples/user_data2.py
```

 The
[next tutorial](#create-a-hierarchical-state-machine)
teaches you how to nest different state machines, creating a
hierarchical state machine.

## Create a Hierarchical State Machine

### Creating some states

For this example, we create a number of states, each with a number of
outcomes, input keys and output keys specified.



```python

  # State Foo
  class Foo(smach.State):
     def __init__(self, outcomes=['outcome1', 'outcome2'])
     
     def execute(self, userdata):
        return 'outcome1'


  # State Bar
  class Bar(smach.State):
     def __init__(self, outcomes=['outcome1'])
     
     def execute(self, userdata):
        return 'outcome4'


  # State Bas
  class Bas(smach.State):
     def __init__(self, outcomes=['outcome3'])
     
     def execute(self, userdata):
        return 'outcome3'
```



### Creating a hierarchical state machine

We create a top level state machine, and start adding states to it. One
of the states we add is another state machine:



```python
   # Create the top level SMACH state machine
    sm_top = smach.StateMachine(outcomes=['outcome5'])

    # Open the container
    with sm_top:

        smach.StateMachine.add('BAS', Bas(),
                               transitions={'outcome3':'SUB'})

        # Create the sub SMACH state machine 
        sm_sub = smach.StateMachine(outcomes=['outcome4'])

        # Open the container 
        with sm_sub:

            # Add states to the container 
            smach.StateMachine.add('FOO', Foo(),
                                   transitions={'outcome1':'BAR', 
                                                'outcome2':'outcome4'})
            smach.StateMachine.add('BAR', Bar(),
                                   transitions={'outcome1':'FOO'})

        smach.StateMachine.add('SUB', sm_sub,
                               transitions={'outcome4':'outcome5'})
```



The result looks like this. The only point to take away from this is
that every state machine is also a normal state. So you can add a state
machine to another state machine in the same way you add a state to a
state machine. So dealing with userdata is not any different when you
deal with hierarchical state machines: the sub state machine specifies
input and output keys, and they get remapped when you add the sub state
machine to the top level state machine.

![width="750"](doc/sm_expanded.png)

### Example

This is a complete runnable example from the
[executive_smach_tutorials](executive_smach_tutorials) package.



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/state_machine_nesting2.py,#!python)>>
```



Running the example: 

```
$ roscd smach_tutorials
$ ./examples/state_machine_nesting2.py
```

 The
[next tutorial](#calling-actions-from-a-state-machine-ros)
teaches you how to call action servers from within a SMACH state
machine.

## Calling Actions from a State Machine (ROS)

```python
from smach_ros import SimpleActionState
```



You could simply call any action from a
[generic state](#generic-state), but
SMACH has specific support to call actions, saving you a lot of code!
SMACH provides a state class that acts as a proxy to an
[actionlib](https://index.ros.org/p/actionlib) action. The instantiation
of the state takes a topic name, action type, and some policy for
generating a goal. The possible outcomes of the simple action state are
'succeeded', 'preempted' and 'aborted'.

Depending on how you get your goal, there are simple and more complex
ways to use the simple action state.

### Goal Message

#### Empty goal message

This is the trivial case, which will call an action server without
filling out anything in the goal message.



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           SimpleActionState('action_server_namespace',
                                             GripperAction),
                           transitions={'succeeded':'APPROACH_PLUG'})
```



#### Fixed goal message

A slightly more advanced usage let's you specify a hard-coded fixed
goal that will get passed to the action server:



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    gripper_goal = Pr2GripperCommandGoal()
    gripper_goal.command.position = 0.07
    gripper_goal.command.max_effort = 99999
    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        goal=gripper_goal),
                      transitions={'succeeded':'APPROACH_PLUG'})
```



#### Goal from user data

Imagine you have a number of fields in the user data that already
contain all the structs you need for your goal message. Then you can
simply connect the userdata directly to the fields in the goal message.
So, from the example above we learn that the gripper action has two
fields in its goal: max_effort and position. Imagine our userdata
contains the corresponding fields user_data_max and user_data_position.
The code below connects the corresponding fields.


```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        goal_slots=['max_effort', 
                                                    'position']),
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'max_effort':'user_data_max',
                                 'position':'user_data_position'})
```



The same works for 'result_slots': the result fields of an action can
automatically get written to your userdata. Also note that all fields
you specify in 'goal_slots' and 'result_slots' are automatically put
in your 'input_keys' and 'output_keys'.

#### Goal callback

This is the ultimate power version: you can get a callback when the
action needs a goal, and you can create your own goal message on demand.



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    def gripper_goal_cb(userdata, goal):
       gripper_goal = GripperGoal()
       gripper_goal.position.x = 2.0
       gripper_goal.max_effort = userdata.gripper_input
       return gripper_goal

    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        goal_cb=gripper_goal_cb,
                                        input_keys=['gripper_input'])
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'gripper_input':'userdata_input'})
```



In your goal callback you can use userdata, as long as you list the
input_keys in the constructor. One of the arguments of the callback is
the default goal. If you specified the 'goal=\...' in the constructor,
that object would get passed into the callback.

For more advanced callback usage, see `@smach.cb_interface`
[(API from ROS Jade)](http://docs.ros.org/jade/api/smach/html/python/smach.util.CBInterface-class.html)
decorator.

### Result Message

#### Result to userdata

You can write the result of the action directly to the userdata of your
state. 

```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        result_slots=['max_effort', 
                                                      'position']),
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'max_effort':'user_data_max',
                                 'position':'user_data_position'})
```



#### Result callback

The result callback is very similar to the goal callback. It allows you
to read any data from the action result fields, and even return a
different outcome than the default 'succeeded', 'preempted',
'aborted'.



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    def gripper_result_cb(userdata, status, result):
       if status == GoalStatus.SUCCEEDED:
          userdata.gripper_output = result.num_iterations
          return 'my_outcome'

    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        result_cb=gripper_result_cb,
                                        output_keys=['gripper_output'])
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'gripper_output':'userdata_output'})
```



In the result callback you get the status of the action, which tells you
if the action succeeded, aborted or was preempted. Plus you get access
to the userdata, and the result of the action.

Optionally you can return a different outcome from the result callback.
If you don't return anything, the state will return with the
corresponding outcome of the action.

For more advanced callback usage, see
[\@smach.cb_interface](http://www.ros.org/doc/api/smach/html/python/smach.util.CBInterface-class.html)
decorator.

The [next tutorial](#viewing-state-machines-ros)
shows you how to use the smach viewer, a simple tool to monitor state
machines and get introspection into the data flow between states.

## Viewing State Machines (ROS)

This is what you want to debug a running SMACH state machine:

![width="750"](doc/smach_viewer.png)

The SMACH viewer shows a graphical representation of all the states in
your (sub) state machines, the possible transitions between states, the
currently active state, and the current values of the userdata. The
SMACH viewer even allows you to set the initial state of your state
machine. This tutorial teaches you how to start using the SMACH viewer.

### Creating an Introspection Server

SMACH containers can provide a debugging interface (over ROS) which
allows a developer to get full introspection into a state machine. The
SMACH viewer can use this debugging interface to visualize and interact
with your state machine. To add this debugging interface to a state
machine, add the following lines to your code:



```python
# First you create a state machine sm
# .....
# Creating of state machine sm finished

# Create and start the introspection server
sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
sis.start()

# Execute the state machine
outcome = sm.execute()

# Wait for ctrl-c to stop the application
rospy.spin()
sis.stop()
```



- **server_name**: this name is used to create a namespace for the ROS
  introspection topics. You can name this anything you like, as long as
  this name is unique in your system. This name is not shown in the
  smach viewer.

<!-- -->

- **SM_ROOT**: your state machine will show up under this name in the
  smach viewer. So you can pretty much choose any name you like. If you
  have sub-state machines that are **in different executables**, you can
  make them show up as hierarchical state machines by choosing this name
  in a clever way: if the top level state machine is called 'SM_TOP',
  you can call the sub state machine 'SM_TOP/SM_SUB', and the viewer
  will recognize the sub state machine as being part of the top state
  machine.

For more details on the introspection server, see the
[API documentation](http://www.ros.org/doc/api/smach_ros/html/python/smach_ros.introspection.IntrospectionServer-class.html).

The smach viewer will automatically traverse the child containers of
`sm`, if any exist, and add ros hooks to each of them. So you only need
to hook up one introspection server to the top level state machine, not
to the sub state machines. Once the introspection server has been
instantiated, it will advertise a set of topics with names constructed
by appending to the server name given to it on construction. In this
case three topics would be advertised:

- `/server_name/smach/container_structure`
- `/server_name/smach/container_status`
- `/server_name/smach/container_init`

The first two publish heartbeat and event info regarding the structure
and status of the SMACH containers served out by "server_name" The
third is a topic for setting the configuration of the SMACH tree over
ROS.

The "SM_ROOT" argument is simply used for visualization, and forced
nesting of different servers.

### Running SMACH viewer

Once you have one or more introspection servers running in your ROS
system, you can start the smach viewer using: 

```
rosrun smach_viewer smach_viewer.py
```



The viewer will automatically connect to all running introspection
servers.

## Simple State Machine

All of the following examples can be run without modification. They can
be found in the [smach_tutorials](smach_tutorials) package in the
`examples` directory. The comments at the head of each file show
roughly what the output from running the script should look like.

![width="300"](doc/state_machine2.png)



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/state_machine2.py,#!python)>>
```

## User Data Passing

All of the following examples can be run without modification. They can
be found in the [smach_tutorials](smach_tutorials) package in the
`examples` directory. The comments at the head of each file show
roughly what the output from running the script should look like.

![width="300"](doc/smach_Tutorials_User%20Data%20Passing_state_machine2.png)



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/user_data2.py,#!python)>>
```

## Nesting State Machines

All of the following examples can be run without modification. They can
be found in the [smach_tutorials](smach_tutorials) package in the
`examples` directory. The comments at the head of each file show
roughly what the output from running the script should look like.

![width="400"](doc/state_machine_nested2.png)



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/state_machine_nesting2.py,#!python)>>
```

## Concurrent State Machine

All of the following examples can be run without modification. They can
be found in the [smach_tutorials](smach_tutorials) package in the
`examples` directory. The comments at the head of each file show
roughly what the output from running the script should look like.

![width=390"](doc/concurrence2.png)



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/concurrence2.py,#!python)>>
```

## Simple Action State (ROS)

All of the following examples can be ran without modification. They can
be found in the [smach_tutorials](smach_tutorials) package in the
*examples* directory. The comments at the head of each file show roughly
what the output from running the script should look like.

![width="450"](doc/actionstate.png)



```wiki
<<GetCode(https://raw.githubusercontent.com/eacousineau/executive_smach_tutorials/hydro-devel/smach_tutorials/examples/actionlib2_test.py,#!python)>>
```

## StateMachine container

### Creating a State Machine

First import the state machine: 

```python
from smach import StateMachine
```



Since a SMACH !StateMachine also provides a State interface, its
outcomes and userdata interactions must be specified on construction.


```python
sm = StateMachine(outcomes = ['outcome1', 'outcome2'],
                  input_keys = ['input1', 'input2'],
                  output_keys = ['output1', 'output2'])
```



Similarly to the SMACH State interface, input keys and output keys are
optional. The constructor signature is: 

```python
__init__(self, outcomes, input_keys=[], output_keys=[])
```



### Adding States

When adding states to a state machine you first specify the state
machine you want to add states to. This can be done by using Python's
"with" statement. You can think of this like "opening" the container
for construction. It creates a context in which all subsequent add\*
calls will apply to the open container.

For example, to add two states to a state machine called "sm", you
could write the following:



```python
with sm:
    StateMachine.add('FOO',
                     FooState(),
                     {'outcome2':'FOO',
                      'outcome3':'BAR'})
    StateMachine.add('BAR',
                     BarState(),
                     {'outcome3':'FOO',
                      'outcome4':'outcome2'})
```



The above example adds the two states labeled "FOO" and "BAR", of
type "FooState" and "BarState", respectively. There are optional
arguments to the static add method. The signature of the add method is:


```python
add(label, state, transitions=None, remapping=None)
```



For more details on transitions, take a look at
[Getting Started](#getting-started-with-smach)

For more details on remapping, take a look at
[User Data](#passing-user-data-between-states)

## Concurrence container

```python
from smach import Concurrence
```



### Specify concurrence outcomes

#### Concurrence Outcome Map

The outcome map of a SMACH concurrence specifies the policy for
determining the outcome of the concurrence based on the outcomes of its
children. Specifically, the map is a dictionary where the keys are
potential outcomes of the concurrence, and the values are dictionaries
mapping child labels onto child outcomes. Once all the states in the
concurrence have terminated, if **one** of these child-outcome mappings
is satisfied, the concurrence will return its associated outcome. If
**none** of the mappings are satisfied, the concurrence will return its
default outcome.



```python
cc = Concurrence(outcomes = ['outcome1', 'outcome2'],
                 default_outcome = 'outcome1',
                 input_keys = ['sm_input'],
                 output_keys = ['sm_output'],
                 outcome_map = {'succeeded':{'FOO':'succeeded',
                                             'BAR':'outcome2'},
                                'outcome3':{'FOO':'outcome2'}})
with cc:
    Concurrence.add('FOO', Foo())
    Concurrence.add('BAR', Bar())
```



The example above specifies the following policy:

- When 'FOO' has outcome 'succeeded' and 'BAR' has outcome
  'outcome2', the state machine will exit with outcome 'succeeded'.
- When 'FOO' has outcome 'outcome2', the state machine will exit
  with outcome 'outcome3', independent of the outcome of state BAR.

#### Callbacks

If you want full control over a concurrence state machine, you can use
the callbacks it provides, the child_termination_cb and the outcome_cb:



```python
# gets called when ANY child state terminates
def child_term_cb(outcome_map):

  # terminate all running states if FOO finished with outcome 'outcome3'
  if outcome_map['FOO'] == 'outcome3':
    return True

  # terminate all running states if BAR finished
  if outcome_map['BAR']:
    return True

  # in all other case, just keep running, don't terminate anything
  return False


# gets called when ALL child states are terminated
def out_cb(outcome_map):
   if outcome_map['FOO'] == 'succeeded':
      return 'outcome1'
   else:
      return 'outcome2'


# creating the concurrence state machine
sm = Concurrence(outcomes=['outcome1', 'outcome2'],
                 default_outcome='outcome1',
                 input_keys=['sm_input'],
                 output_keys=['sm_output'],
                 child_termination_cb = child_term_cb,
                 outcome_cb = out_cb)
                 
with sm:
   Concurrence.add('FOO', Foo(),
                   remapping={'foo_in':'input'})

   Concurrence.add('BAR', Bar(),
                   remapping={'bar_out':'bar_out'})
```



- The child_termination_cb is called every time one of the child states
  terminates. In the callback function you can decide if the state
  machine should keep running (return False), or if it should preempt
  all remaining running states (return True).

<!-- -->

- The outcome_cb is called once when the last child state terminates.
  This callback returns the outcome of the concurrence state machine.

## Sequence container

The Sequence container is a
[StateMachine container](#statemachine-container),
extended with auto-generated transitions that create a sequence of
states from the order in which said states are added to the container.
Only the differences are noted here.

### Creating a Sequence Container

First import the sequence type: 

```python
from smach import Sequence
```



A container Sequence has its outcomes, specified on construction, along
with the 'connector_outcome' which is used for the automatic
transitions. The constructor signature is: 

```python
__init__(self, outcomes, connector_outcome):
```



### Adding States

Adding states to a sequence is the same as to a container.

But, each state added will receive an additional transition from it to
the state which is added after it. The transition will follow the
outcome specified at construction of this container.

If one of the transitions given in the dictionary mapping parameter to
'Sequence.add()' follows the connector outcome specified in the
constructor, the provided transition will override the automatically
generated connector transition.

### Example

For example, when creating a sequence of action states, no transition
mapping is needed. All action states have the usual outcome triple,
which the sequence needs to have as its outcomes, too:



```python

sq = Sequence(
        outcomes = ['succeeded','aborted','preempted'],
        connector_outcome = 'succeeded')
with sq:
    Sequence.add('MOVE_ARM_GRAB_PRE', MoveVerticalGripperPoseActionState())
    Sequence.add('MOVE_GRIPPER_OPEN', MoveGripperState(GRIPPER_MAX_WIDTH))
    Sequence.add('MOVE_ARM_GRAB',     MoveVerticalGripperPoseActionState())
    Sequence.add('MOVE_GRIPPER_CLOSE', MoveGripperState(grab_width))
    Sequence.add('MOVE_ARM_GRAB_POST', MoveVerticalGripperPoseActionState())
```

## Iterator container

### Overview

The iterator allows you to loop through a state or states until success
conditions are met. This tutorial demonstrates how to use an iterator to
sort a list of numbers into evens and odds.

### The Code

Below is the full state machine, create a file called
`iterator_tutorial.py` and copy the following code:

Source:
[iterator_tutorial.py](https://github.com/eacousineau/executive_smach_tutorials/blob/hydro-devel/smach_tutorials/examples/iterator_tutorial.py)



```python
#! /usr/bin/env python


import roslib; roslib.load_manifest('smach')
roslib.load_manifest('smach_ros')
import rospy

import smach
from smach import Iterator, StateMachine, CBState
from smach_ros import ConditionState, IntrospectionServer

def construct_sm():
    sm = StateMachine(outcomes = ['succeeded','aborted','preempted'])
    sm.userdata.nums = range(25, 88, 3)
    sm.userdata.even_nums = []
    sm.userdata.odd_nums = []
    with sm:
        tutorial_it = Iterator(outcomes = ['succeeded','preempted','aborted'],
                               input_keys = ['nums', 'even_nums', 'odd_nums'],
                               it = lambda: range(0, len(sm.userdata.nums)),
                               output_keys = ['even_nums', 'odd_nums'],
                               it_label = 'index',
                               exhausted_outcome = 'succeeded')
        with tutorial_it:
            container_sm = StateMachine(outcomes = ['succeeded','preempted','aborted','continue'],
                                        input_keys = ['nums', 'index', 'even_nums', 'odd_nums'],
                                        output_keys = ['even_nums', 'odd_nums'])
            with container_sm:
                #test wether even or odd
                StateMachine.add('EVEN_OR_ODD',
                                 ConditionState(cond_cb = lambda ud:ud.nums[ud.index]%2, 
                                                input_keys=['nums', 'index']),
                                 {'true':'ODD',
                                  'false':'EVEN' })
                #add even state
                @smach.cb_interface(input_keys=['nums', 'index', 'even_nums'],
                                    output_keys=['odd_nums'], 
                                    outcomes=['succeeded'])
                def even_cb(ud):
                    ud.even_nums.append(ud.nums[ud.index])
                    return 'succeeded'
                StateMachine.add('EVEN', CBState(even_cb), 
                                 {'succeeded':'continue'})
                #add odd state
                @smach.cb_interface(input_keys=['nums', 'index', 'odd_nums'], 
                                    output_keys=['odd_nums'], 
                                    outcomes=['succeeded'])
                def odd_cb(ud):
                    ud.odd_nums.append(ud.nums[ud.index])
                    return 'succeeded'
                StateMachine.add('ODD', CBState(odd_cb), 
                                 {'succeeded':'continue'})
            #close container_sm
            Iterator.set_contained_state('CONTAINER_STATE', 
                                         container_sm, 
                                         loop_outcomes=['continue'])
        #close the tutorial_it
        StateMachine.add('TUTORIAL_IT',tutorial_it,
                     {'succeeded':'succeeded',
                      'aborted':'aborted'})
    return sm

def main():
    rospy.init_node("iterator_tutorial")
    sm_iterator = construct_sm()

    # Run state machine introspection server for smach viewer
    intro_server = IntrospectionServer('iterator_tutorial',sm_iterator,'/ITERATOR_TUTORIAL')
    intro_server.start()


    outcome = sm_iterator.execute()

    rospy.spin()
    intro_server.stop()

if __name__ == "__main__":
    main()
```



### The Code Explained

Start by constructing the iterator, the constructor takes the following
arguments: 

```
__init__(self, outcomes, input_keys, output_keys, it=[], it_label='it_data', exhausted_outcome='exhausted')
```

 In this example, the `outcomes`
now include `preempted`, a default `outcome` of the iterator. The
`it` argument is the list of objects that will be iterated over and
the `it_label` is key that holds the current value of the of the item
in the `it` list. The `exhausted` argument should be set to the
preferred state machine outcome, in this example the iterator outcome is
`succeeded` when the iterator is done looping through the `it` list.



```python
        tutorial_it = Iterator(outcomes = ['succeeded','preempted','aborted'],
                               input_keys = ['nums', 'even_nums', 'odd_nums'],
                               it = lambda: range(0, len(sm.userdata.nums)),
                               output_keys = ['even_nums', 'odd_nums'],
                               it_label = 'index',
                               exhausted_outcome = 'succeeded')
```



Now add a container and create the states for sorting the list into even
and odd. 

```python
        with tutorial_it:
            container_sm = StateMachine(outcomes = ['succeeded','preempted','aborted','continue'],
                                        input_keys = ['nums', 'index', 'even_nums', 'odd_nums'],
                                        output_keys = ['even_nums', 'odd_nums'])
            with container_sm:
                #test wether even or odd
                StateMachine.add('EVEN_OR_ODD',
                                 ConditionState(cond_cb = lambda ud:ud.nums[ud.index]%2, 
                                                input_keys=['nums', 'index']),
                                 {'true':'ODD',
                                  'false':'EVEN' })
                #add even state
                @smach.cb_interface(input_keys=['nums', 'index', 'even_nums'],
                                    output_keys=['odd_nums'], 
                                    outcomes=['succeeded'])
                def even_cb(ud):
                    ud.even_nums.append(ud.nums[ud.index])
                    return 'succeeded'
                StateMachine.add('EVEN', CBState(even_cb), 
                                 {'succeeded':'continue'})
                #add odd state
                @smach.cb_interface(input_keys=['nums', 'index', 'odd_nums'], 
                                    output_keys=['odd_nums'], 
                                    outcomes=['succeeded'])
                def odd_cb(ud):
                    ud.odd_nums.append(ud.nums[ud.index])
                    return 'succeeded'
                StateMachine.add('ODD', CBState(odd_cb), 
                                 {'succeeded':'continue'})
```



Add the container to the iterator:



```python
            #close container_sm
            Iterator.set_contained_state('CONTAINER_STATE', 
                                         container_sm, 
                                         loop_outcomes=['continue'])
```



Finish by adding the iterator to the top level state machine:



```python
        #close the tutorial_it
        StateMachine.add('TUTORIAL_IT',tutorial_it,
                     {'succeeded':'succeeded',
                      'aborted':'aborted'})
```



### Running the Code

Make sure that a `roscore` is running: 

```
$ roscore
```

 Run
the `smach_viewer` so you can see the results:


```
$ rosrun smach_viewer smach_viewer.py
```

 Now run the state machine:


```
$ sudo chmod a+x iterator_tutorial.py
$ python ./iterator_tutorial.py
```



![attachment:smach_tutorial.png](doc/smach_tutorial.png)

## Wrapping a Container With actionlib

### Wrapping a SMACH State

SMACH provides the top-level container called !ActionServerWrapper. This
class advertises an [actionlib](https://index.ros.org/p/actionlib)
action server. Instead of being executed by a parent, its contained
state goes active when the action server receives a goal. Accordingly,
this container does not inherit from the smach.State base class and
cannot be put inside of another container.

The action server wrapper can inject the goal message received by the
action server into the contained state, as well as extract the result
message from that state when it terminates. When constructing the action
server wrapper, the user specifies which state machine outcomes
correspond to a succeeded, aborted, or preempted result.

Consider this example, which wraps a SMACH state machine as an action:



```python
import rospy

from smach import StateMachine
from smach_ros import ActionServerWrapper

# Construct state machine
sm = StateMachine(outcomes=['did_something',
                            'did_something_else',
                            'aborted',
                            'preempted'])
with sm:

# Construct action server wrapper
asw = ActionServerWrapper(
    'my_action_server_name', MyAction,
    wrapped_container = sm,
    succeeded_outcomes = ['did_something','did_something_else'],
    aborted_outcomes = ['aborted'],
    preempted_outcomes = ['preempted'] )

# Run the server in a background thread
asw.run_server()

# Wait for control-c
rospy.spin()
```



### Getting The Goal/Result Messages Into/Out Of The Contained State

The above code will call sm.execute(), but it will not load the goal
into the contained state machine, nor will it extract a result. In order
to do these things, you need to tell the action server wrapper what it
should call the goal and result messages in the context of SMACH. You
can replace the action server wrapper construction call with the
following:



```python
# Construct action server wrapper
asw = ActionServerWrapper(
    'my_action_server_name', MyAction, sm,
    ['did_something','did_something_else'], ['aborted'], ['preempted'],
    goal_key = 'my_awesome_goal',
    result_key = 'egad_its_a_result' )
```



The keyword arguments *goal_key* and *result_key* are the SMACH userdata
keys in the context of the ActionServerWrapper. Like any other
container, this means that the wrapper's contained state (in this case
the state machine *sm*) will receive a reference to this userdata
structure when its execute() method is called. Similarly to how userdata
is passed between scopes in nested state machines, in this case, you
need to set these key identifiers in the state machine *sm* as well.

In order to copy in the keys form the parent, you can replace the
construction call for the state machine *sm* with this:



```python
# Construct state machine
sm = StateMachine(
        outcomes=['did_something','did_something_else','aborted','preempted'],
        input_keys = ['my_awesome_goal'],
        output_keys = ['egad_its_a_result'])
```



Once you have done this, you can access these keys from any state added
to *sm*. For more goal/result policies, see the
[ActionServerWrapper API documentation](http://www.ros.org/doc/api/smach/html/python/smach.action_server_wrapper.ActionServerWrapper-class.html#__init__).

## Generic State

```python
from smach import State
```



The most general (but often least efficient) way to create a state is to
derive from the 'State' base class. You can pretty much do anything
you want in the execute method of a state. Know that SMACH comes with a
library of useful states that you can use, without having to write a
whole custom state.



```python
  class Foo(smach.State):
     def __init__(self, outcomes=['outcome1', 'outcome2']):
       # Your state initialization goes here
     
     def execute(self, userdata):
        # Your state execution goes here
        if xxxx:
            return 'outcome1'
        else:
            return 'outcome2'
```



Some good code practices:

- Do not block in your constructor. If your state needs to wait for
  another component to come up, do this in a separate thread

## CBState

```python
from smach import CBState
```



### Description

This state simply executes a single callback when the state is executed.
This is useful for executing arbitrary code in a state, without having
to declare a new state class. This class supports the use of the
`smach.cb_interface` decorator, and its API can be found
[here](http://www.ros.org/doc/api/smach/html/python/smach.state.CBState-class.html#__init__).

The CBState calls the callback with at least one argument: the
container's userdata. Additional arguments and keyword arguments can be
given to the CBState on construction. These args will be passed into the
callback when the CBState is executed.

### Example

The following example adds a CBState to a SMACH StateMachine that takes
in some arguments and variables from userdata, and stores their sum in
the userdata key 'xyz':



```python
@smach.cb_interface(input_keys=['q'],
                    output_keys=['xyz'],
                    outcomes=['foo'])
def my_cb(ud, x, y, z):
    ud.xyz = ud.q + x + y + z
    return 'foo'
...
with sm:
    ...
    StateMachine.add('MY_CB', CBState(my_cb,
                                      cb_args=[10],
                                      cb_kwargs={'z':2,'y':3}),
                              {'foo':'OTHER_STATE'})
    ...
```

## SimpleActionState (ROS)

```python
from smach_ros import SimpleActionState
```



You could simply call any action from a
[generic state](#generic-state), but
SMACH has specific support to call actions, saving you a lot of code!
SMACH provides a state class that acts as a proxy to an
[actionlib](https://index.ros.org/p/actionlib) action. The instantiation
of the state takes a topic name, action type, and some policy for
generating a goal. The possible outcomes of the simple action state are
'succeeded', 'preempted' and 'aborted'.

Depending on how you get your goal, there are simple and more complex
ways to use the simple action state.

### Goal Message

#### Empty goal message

This is the trivial case, which will call an action server without
filling out anything in the goal message.



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           SimpleActionState('action_server_namespace',
                                             GripperAction),
                           transitions={'succeeded':'APPROACH_PLUG'})
```



#### Fixed goal message

A slightly more advanced usage let's you specify a hard-coded fixed
goal that will get passed to the action server:



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    gripper_goal = Pr2GripperCommandGoal()
    gripper_goal.command.position = 0.07
    gripper_goal.command.max_effort = 99999
    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        goal=gripper_goal),
                      transitions={'succeeded':'APPROACH_PLUG'})
```



#### Goal from user data

Imagine you have a number of fields in the user data that already
contain all the structs you need for your goal message. Then you can
simply connect the userdata directly to the fields in the goal message.
So, from the example above we learn that the gripper action has two
fields in its goal: max_effort and position. Imagine our userdata
contains the corresponding fields user_data_max and user_data_position.
The code below connects the corresponding fields.


```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        goal_slots=['max_effort', 
                                                    'position']),
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'max_effort':'user_data_max',
                                 'position':'user_data_position'})
```



The same works for 'result_slots': the result fields of an action can
automatically get written to your userdata. Also note that all fields
you specify in 'goal_slots' and 'result_slots' are automatically put
in your 'input_keys' and 'output_keys'.

#### Goal callback

This is the ultimate power version: you can get a callback when the
action needs a goal, and you can create your own goal message on demand.



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    def gripper_goal_cb(userdata, goal):
       gripper_goal = GripperGoal()
       gripper_goal.position.x = 2.0
       gripper_goal.max_effort = userdata.gripper_input
       return gripper_goal

    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        goal_cb=gripper_goal_cb,
                                        input_keys=['gripper_input'])
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'gripper_input':'userdata_input'})
```



In your goal callback you can use userdata, as long as you list the
input_keys in the constructor. One of the arguments of the callback is
the default goal. If you specified the 'goal=\...' in the constructor,
that object would get passed into the callback.

For more advanced callback usage, see `@smach.cb_interface`
[(API from ROS Jade)](http://docs.ros.org/jade/api/smach/html/python/smach.util.CBInterface-class.html)
decorator.

### Result Message

#### Result to userdata

You can write the result of the action directly to the userdata of your
state. 

```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        result_slots=['max_effort', 
                                                      'position']),
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'max_effort':'user_data_max',
                                 'position':'user_data_position'})
```



#### Result callback

The result callback is very similar to the goal callback. It allows you
to read any data from the action result fields, and even return a
different outcome than the default 'succeeded', 'preempted',
'aborted'.



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    def gripper_result_cb(userdata, status, result):
       if status == GoalStatus.SUCCEEDED:
          userdata.gripper_output = result.num_iterations
          return 'my_outcome'

    StateMachine.add('TRIGGER_GRIPPER',
                      SimpleActionState('action_server_namespace',
                                        GripperAction,
                                        result_cb=gripper_result_cb,
                                        output_keys=['gripper_output'])
                      transitions={'succeeded':'APPROACH_PLUG'},
                      remapping={'gripper_output':'userdata_output'})
```



In the result callback you get the status of the action, which tells you
if the action succeeded, aborted or was preempted. Plus you get access
to the userdata, and the result of the action.

Optionally you can return a different outcome from the result callback.
If you don't return anything, the state will return with the
corresponding outcome of the action.

For more advanced callback usage, see
[\@smach.cb_interface](http://www.ros.org/doc/api/smach/html/python/smach.util.CBInterface-class.html)
decorator.

## ServiceState (ROS)

```python
from smach_ros import ServiceState
```

 You could simply call any service from a
[generic state](#generic-state), but
SMACH has specific support to call services, saving you a lot of code!
SMACH provides a state class that acts as a proxy to a
[ROS service](Services). The instantiation of the state takes a service
name, service type, and some policy for generating a service request.
The possible outcomes of the service state are 'succeeded',
'preempted' and 'aborted'.

/!\\ The service state is almost identical to the simple action state.
Just replace 'goal' with 'request', and 'result' with
'response'.

### Request

#### Empty request message



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv),
                           transitions={'succeeded':'APPROACH_PLUG'})
```



#### Fixed request message



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv,
                                        request = GripperSrv(9.0)),
                           transitions={'succeeded':'APPROACH_PLUG'})
```

 /!\\ You may need to use the actual request
type instead of the service type: ie. request = GripperSrvRequest(9.0)
instead of GripperSrv.

#### Request from user data



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv,
                                        request_slots = ['max_effort',
                                                         'position']),
                           transitions={'succeeded':'APPROACH_PLUG'})
```



#### Request callback



```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:

    @smach.cb_interface(input_keys=['gripper_input'])
    def gripper_request_cb(userdata, request):
       gripper_request = GripperSrv().Request
       gripper_request.position.x = 2.0
       gripper_request.max_effort = userdata.gripper_input
       return gripper_request

    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ServiceState('service_name',
                                        GripperSrv,
                                        request_cb = gripper_request_cb,
                                        input_keys = ['gripper_input']),
                           transitions={'succeeded':'APPROACH_PLUG'})
```



For more advanced callback usage, see
[\@smach.cb_interface](http://www.ros.org/doc/api/smach/html/python/smach.util.CBInterface-class.html)
decorator.

### Response

#### Response to user data

#### Response callback

This works similarly to the SimpleActionState
[result callback](#result-callback-1),
except instead of receiving both the result status and result data, the
second argument to the callback is simply the service response message.

For more advanced callback usage, see
[\@smach.cb_interface](http://www.ros.org/doc/api/smach/html/python/smach.util.CBInterface-class.html)
decorator.

## MonitorState (ROS)

```wiki
NB - This is just what I coded up while trying to understand the MonitorState. Please don't take it for best practices or anything, until JonBohren or somebody with more experience takes a look at it.
-LauraLindzey
```



### Setup

Here's an example of a simple state machine using MonitorState. In
order to transition from state Foo to state Bar, send a message to the
/sm_reset topic: 

```
rostopic pub -1 /sm_reset std_msgs/Empty
```



### The Code



```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('smach_MonitorState_example')
import rospy
import smach
import smach_ros

from std_msgs.msg import Empty

class bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['bar_succeeded'])
    def execute(self, userdata):
        rospy.sleep(3.0)
        return 'bar_succeeded'

def monitor_cb(ud, msg):
    return False

def main():
    rospy.init_node("monitor_example")

    sm = smach.StateMachine(outcomes=['DONE'])
    with sm:
        smach.StateMachine.add('FOO', smach_ros.MonitorState("/sm_reset", Empty, monitor_cb), transitions={'invalid':'BAR', 'valid':'FOO', 'preempted':'FOO'})
        smach.StateMachine.add('BAR',bar(), transitions={'bar_succeeded':'FOO'})

    sis = smach_ros.IntrospectionServer('smach_server', sm, '/SM_ROOT')
    sis.start()
    sm.execute()
    rospy.spin()
    sis.stop()

if __name__=="__main__":
    main()
```



### Code with Notes



```python
def monitor_cb(ud, msg):
    return False
```

 Arguments are the userdata and the message.
This needs to return False when we want the monitor state to terminate.
In this case, the monitor state will return 'invalid'



```python
    sm = smach.StateMachine(outcomes=['DONE'])
    with sm:
        smach.StateMachine.add('FOO', 
                               smach_ros.MonitorState("/sm_reset", 
                                                      Empty, 
                                                      monitor_cb), 
                               transitions={'invalid':'BAR', 
                                            'valid':'FOO', 
                                            'preempted':'FOO'})
```

 Note that your MonitorState needs to define
transitions for all three possible outcomes ('valid', 'invalid',
'preempted').

From the source code for MonitorState: 

```
def __init__(self, topic, msg_type, cond_cb, max_checks=-1)
```

 The
max_checks argument is a limit on how many times the monitor_cb can be
called before the MonitorState will return 'valid'.

## StateMachinePreemption

```wiki
NB - This is just what I coded up while trying to understand how to add preemption into a state machine. Please don't take it for best practices or anything, until JonBohren or somebody with more experience takes a look at it.
-LauraLindzey
```



### Setup

The goal here is to have a state within a state machine that terminates
either after a calculation has been finished OR after a particular
condition has been met. We use a
[ concurrence container](http://www.ros.org/wiki/smach/Tutorials/Concurrence%20container )
to join together a
[simple state that implements preemption](http://www.ros.org/wiki/smach/Tutorials/State%20Preemption%20Implementation)and
a [monitor state](http://ros.org/wiki/smach/Tutorials/MonitorState). The
monitor state checks if a message has been received to the /sm_reset
topic.

The sm starts in SETUP, transitions to FOO, and then loops between FOO
and BAR. FOO is a Concurrence Container containing FOO_RESET, a
MonitorState, and FOO_CALC, a simple state performing a long
calculation. If the machine is in state FOO and a message is sent to
/sm_reset, FOO_RESET will return, FOO_CALC will be preempted, and the
maachine transitions to SETUP. Otherwise, if FOO_CALC finishes,
FOO_RESET is preempted and the machine transitions to BAR.

### Code



```python
#!/usr/bin/env python
import roslib; roslib.load_manifest('smach_preemption_example')
import rospy
import smach
import smach_ros

from std_msgs.msg import Empty

class setup(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['setup_done'])
    def execute(self, userdata):
        rospy.sleep(3.5)
        return 'setup_done'

class foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['foo_succeeded', 'preempted'])
    def execute(self, userdata):
        for idx in range(5):
            if self.preempt_requested():
                print "state foo is being preempted!!!"
                self.service_preempt()
                return 'preempted'
            rospy.sleep(1.0)
        return 'foo_succeeded'

def child_term_cb(outcome_map):
    if outcome_map['FOO_CALC'] == 'foo_succeeded':
        return True
    elif outcome_map['FOO_RESET'] == 'invalid':
        return True
    else:
        return False

def out_cb(outcome_map):
    if outcome_map['FOO_RESET'] == 'invalid':
        return 'foo_reset'
    elif outcome_map['FOO_CALC'] == 'foo_succeeded':
        return 'foo_done'
    else:
        return 'foo_reset'

def monitor_cb(ud, msg):
    return False     

def main():
    rospy.init_node("preemption_example")

    foo_concurrence = smach.Concurrence(outcomes=['foo_done', 'foo_reset'],
                                        default_outcome='foo_done',
                                        child_termination_cb=child_term_cb,
                                        outcome_cb=out_cb)

    with foo_concurrence:
        smach.Concurrence.add('FOO_CALC', foo())
        smach.Concurrence.add('FOO_RESET', smach_ros.MonitorState("/sm_reset", Empty, monitor_cb))

    sm = smach.StateMachine(outcomes=['DONE'])
    with sm:
        smach.StateMachine.add('SETUP', setup(), transitions={'setup_done':'FOO'})
        smach.StateMachine.add('FOO', foo_concurrence, transitions={'foo_done':'BAR', 'foo_reset':'SETUP'}) 
        smach.StateMachine.add('BAR', foo(), transitions={'foo_succeeded':'FOO', 'preempted':'SETUP'})

    sis = smach_ros.IntrospectionServer('smach_server', sm, '/SM_ROOT')
    sis.start()
    sm.execute()
    rospy.spin()
    sis.stop()

if __name__=="__main__":
    main()
```



### Code with Notes

## State Preemption Implementation

Sometimes, no state or container type will not satisfy your needs.
Before you decide this, make sure you have examined all the provided
state and container types. There are three key features that need to be
considered when defining a new type of SMACH state:

- Interface declaration
- Execution implementation
- Preemption implementation

If you just want to copy and paste some code to modify for a state you
can start with this very simple state:



```python

import roslib; roslib.load_manifest('smach')
import rospy

from smach import State

class FibState(State):
    def __init__(self, n):
        """Constructor."""
        State.__init__(self,
                outcomes = ['done','preempted'],
                input_keys = [],
                output_keys = ['fib_result'])
        self.n = n

    def execute(self,ud):
        """Calculate the nth fibonacci number."""
        f = 0
        f1 = 0
        f2 = 1
        for i in range(self.n):
            # Check for preempt
            if self.preempt_requested():
                self.service_preempt()
                return 'preempted'
            # Calculate the next number
            f = f1 + f2
            f1 = f2
            f2 = f

        # Store a tuple containing the result in userdata
        ud.fib_result = (self.n, f)

        return 'done'

    def request_preempt(self):
        """Overload the preempt request method just to spew an error."""
        State.request_preempt(self)
        rospy.logwarn("Preempted!")
```



### SMACH Interface

SMACH containers interact with their contained states through state
outcomes and userdata keys. The outcomes need to be declared in order to
be able to be bound to targets in a container, and the userdata keys
need to be declared in order to trace the dataflow in the system. This
explicit declaration allows us to catch errors on construction of a
SMACH tree instead as well as while we're executing it.

### Execution Implementation

When a state is entered by the execution of some container, its
`execute()` method is called. This is a method that blocks and returns
some (registered) outcome identifier (string). Once this method exits,
the state should be considered dormant, or inactive.

If a certain state corresponds to a long-running task, it should be
brought up in a concurrence or some other parallel container, instead of
spinning off a thread and exiting quickly.

### Preemption Implementation

In simple cases like the example above, preemption can be done simply by
checking the method `preempt_requested()`. If this cannot be done, the
`request_preempt()` method can be overloaded in this new state class.
Preempts will usually come in on a separate thread, and this method
should not block longer than it takes to notify any child threads /
processes to preempt.

## Writing Custom Container Classes

## Writing Custom State Classes with User-defined Callbacks

SMACH provides a decorator which can attach a SMACH interface to a
function. This includes user data input keys, output keys, and state
outcomes. A common pattern for extensible state design is to use
callback functions that are called on various events. For example,
!SimpleActionState can call callbacks for generating goal messages or
processing result messages, and !MonitorState calls a callback each time
a message comes in on a specified topic.

If a state defines an interface that can take callback functions, it
should support this decorator model. Doing so is as simple as checking
for the existence of the SMACH interface methods. A single function is
provided bu the `smach.util` module.

### Single User Callback

The following code shows how to integrate the SMACH interface provided
by a callback function into the interface of a state. This state simply
receives a SINGLE callback function and calls it when the state is
executing. 

```python
class MyState(smach.State):
    def __init__(self, cb):
        smach.State.__init__(self, outcomes=['done'])

        self._cb = cb
        if cb and smach.has_smach_interface(cb):
            self.register_input_keys(cb.get_registered_input_keys())
            self.register_output_keys(cb.get_registered_output_keys())
            self.register_outcomes(cb.get_registered_outcomes())
    ...
    def execute(self, ud):
        # Call callback
        cb_outcome = self._cb(ud)

        # If callback returned an outcome, return it as the state outcome
        if cb_outcome:
            return cb_outcome 
        
        return 'done'
```



### Multiple User Callbacks

If more than one callback is supplied, the state class implementer
should ensure that no side-effects are caused by adding callbacks with
different interfaces. This is done by using a userdata remapper when
passing userdata to the callbacks.

The following state takes a list of callbacks as an argument, and stores
each callback's input and output keys. Then, when each callback is
called while this state is executing, they will receive access to only
their declared input and output keys. This prevents accidental access to
be granted to one callback by another callback.



```python
class MyState(smach.State):
    def __init__(self, cb_list):
        smach.State.__init__(self, outcomes=['done'])

        self._cbs = cb_list
        for cb in cb_list:
            if cb and smach.has_smach_interface(cb):
                self._cb_input_keys.append(cb.get_registered_input_keys())
                self._cb_output_keys.append(cb.get_registered_output_keys())
 
                self.register_input_keys(self._cb_input_keys[-1])
                self.register_output_keys(self._cb_output_keys[-1])
                self.register_outcomes(self._cb_input_keys[-1])
    ...
    def execute(self, ud):
        # Call callbacks
        for (cb, ik, ok) in zip(self._cbs,
                                self._cb_input_keys,
                                self._cb_output_keys):

            # Call callback with limited userdata
            cb_outcome = self._cb(smach.Remapper(ud,ik,ok,{}))

            # If callback returned an outcome, return it as the state outcome
            if cb_outcome:
                return cb_outcome 
        
        return 'done'
```

## UseCase

### SMACH Use Case

This use case will explore the usability and learning curve of SMACH.
This use case starts with a simple use of just the SMACH API, and
finishes with a concrete example that interfaces with other ROS systems:
an executive that will coordinate two turtles in
[turtlesim](https://index.ros.org/p/turtlesim).

This use case assumes a basic understanding of python, ROS,
[rospy](https://index.ros.org/p/rospy), and
[actionlib](https://index.ros.org/p/actionlib).

#### Create The Package

First, create the pacakge with a number of dependencies:


```
$ roscreate-pkg smach_usecase rospy std_srvs smach turtlesim
$ roscd smach_usecase
```



Create a launchfile to launch a
[turtlesim](https://index.ros.org/p/turtlesim) environment. Call it
"turtle_nodes.launch": 

```xml
<launch>
  <node pkg="turtlesim" name="turtlesim" type="turtlesim_node"/>
</launch>
```



You should now be able to run the following to launch a
[turtlesim](https://index.ros.org/p/turtlesim) environment:


```
$ roslaunch smach_usecase turtle_nodes.launch
```



#### Create The Executive

Create the directory "scripts" in the "smach_usecase" package. In
this directory, create a python script called "executive.py". This
script will be the primary focus of the rest of the use case.

In this script, create the backbone of the SMACH executive. This
involves, the necessary imports, the definition of a *main()* function,
and creation of an empty SMACH state machine.



```python
#!/usr/bin/env python

import roslib; roslib.load_manifest('smach_usecase')

import rospy
import smach

def main():
    rospy.init_node('smach_usecase_executive')

    sm_root = smach.StateMachine(outcomes=[])

    with sm_root:
        pass

    outcome = sm_root.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
```



#### Add Some Service Call States

Add two states to the (currently empty) state machine "sm_root." The
first state should call the ROS service provided by
[turtlesim](https://index.ros.org/p/turtlesim) to reset the simulation.
The second state should spawn a new turtle at (0,0) called "turtle2".

These two tasks are both executed with service calls and can be
implemented with SMACH
[smach.ServiceState](#servicestate-ros)s.
The !ServiceState represents the execution of a ROS service call. They
provide the potential outcomes "succeeded", "aborted", and
"preempted".

- The first service is called "reset" and its service type is
  `std_srvs.Empty`.
- The second service is called "spawn" and its service type is
  `turtlesim.srv.Spawn`. Its request type, `turtlesim.srv.SpawnRequest`,
  takes four arguments (x, y, theta, name)

Once you have added the two states, you should be able to launch your
turtlesim launchfile, and then run the executive. When running the
executive, you should see turtlesim get reset and then a new turtle
should appear in the corner at (0,0).

![width=300](doc/uc02_ts.png)

#### Attach SMACH Viewer For Introspection

It's possible to view the structure and state of a SMACH tree while
it's executing. This is done by attaching a `smach.IntrospectionServer`
to the root of a given SMACH tree. Then,
[smach_viewer](https://index.ros.org/p/smach_viewer) can be ran to
introspect on the tree.

The
[smach_viewer tutorial](#viewing-state-machines-ros)
shows how this is done. Once you have added the introspection server,
you can run SMACH Viewer like so:



```
$ rosrun smach_viewer smach_viewer.py
```



If you named your states "RESET" and "SPAWN" in the previous
section, you should see a structure like this:

![width=600](doc/uc03.png)

In the above image, states are represented by ovals, and their outcomes
are represented by directed edges. The outcomes of the container
"sm_root" are shown in red. It is a good convention to capitalize
state names, to write outcomes in lower case, and to use underscores
where multiple words are present in a name.

#### Add Interface To TurtleSim Shape Action

Next you will add some more tasks sequence of states. These tasks will
involve calling some more services, as well as a couple of
[actionlib](https://index.ros.org/p/actionlib) actions. Before adding
the code that calls the actions, we need to add the action servers to
our launchfile.

Adding the following lines to "turtle_nodes.launch" will bring up a
pair of action servers that can draw polygons with the two turtles:


```xml
  <node pkg="turtle_actionlib" name="turtle_shape1" type="shape_server"/>
  <node pkg="turtle_actionlib" name="turtle_shape2" type="shape_server">
    <remap from="/turtle1/pose" to="/turtle2/pose"/>
    <remap from="/turtle1/cmd_vel" to="/turtle2/cmd_vel"/>
  </node>
```



Before adding the action states, add two more service states. The first
should move "turtle1" to the coordinates (5.0,1.0), and the second
should move "turtle2" to the coordinates (9.0,5.0). These services are
called "turtle1/teleport_absolute" and "turtle2/teleport_absolute",
respectively. They use the service of type
`turtlesim.srv.TeleportAbsolute`, and the request type has three
arguments (x, y, theta).

Next add two states that will send goals to the action servers
"turtle_shape1" and "turtle_shape2", the two action servers that we
added to the launchfile above. This can be done trivially with
[smach.SimpleActionState](#simple-action-state-ros)s.

The first state should draw a big undecagon (11 sides) of radius 4.0,
with turtle1, and the second state should draw a small hexagon of radius
0.5 with turtle2. The action type is `turtle_actionlib.msg.ShapeAction`
and the goal type has two arguments (edges, radius).

Once you have added the four states described above, you should be able
to run the script and see the two turtles each draw a polygon.

![width=300](doc/uc04_ts.png)

If you run SMACH Viewer, and used the naming convention shown, you
should see the following graph while turtle1 is drawing the big polygon.

![width=600](doc/uc04.png)

#### Make Shapes Drawn in Parallel

In this next step, you will put the two shape-drawing states into a
concurrence. This will send the two action goals simultaneously, and
wait for them both to terminate.

Fist construct a concurrence, a tutorial for which is can be found
[here](#concurrent-state-machine). Add the
concurrence to the state machine, and then move the two states that send
shape goals from the root state machine into the concurrence.

When executing the code, you should now see both turtles move
simultaneously like so:

![width=300](doc/uc05_ts.png)

Additionally, if you followed the same naming conventions, SMACH Viewer
should now show a structure similar to the following:

![width=600](doc/uc05.png)

Note that this shows that the small polygon has finished being drawn,
but the big one is still active.

#### Make The Second Turtle Stop When the First Gets Too Close

In this next step, you will make turtle2 stop when turtle1 gets too
close. This involves implementing a *monitor* pattern. The idea behind
this pattern is to allow a state to preempt (or stop) a sibling when
some condition is no longer satisfied.

The SMACH ROS library has a monitor state which provides the mechanism
for associating a condition callback with a topic and message type. The
callback is called each time the state receives a message on the
specified topic. If the callback returns `True`, then it continues to
block, but if it returns `False`, it will terminate with the outcome
'invalid'. More on the monitor state can be found on the
[MonitorState Tutorial](#monitorstate-ros)
page.

Such a state can be placed in a concurrence with another state. Then the
only thing necessary to do to make it kill the sibling when the
condition no longer holds, is to give the concurrence a "child
termination callback". This callback (if specified) is called each time
a child in a SMACH Concurrence terminates, and determines whether or not
the other states should be sent preempt signals.

When using a concurrence and a monitor state to implement this pattern,
the child termination callback can simply be an anonymous function that
always returns `True`: 

```python
    ...
    child_termination_cb = lambda state_outcomes: True,
    ...
```



This way, the first state that terminates will cause the other states in
the concurrence to be preempted. If you follow the same naming
conventions, after making this modification to the SMACH tree in the
executive, the SMACH Viewer should now show a structure similar to the
following:

![width=600](doc/uc06.png)

#### Make The Second Turtle Start Over When the First Leaves

The final modification to the behavior of this executive, is to add some
simple recovery behavior to the small polygon drawing. In the previous
step, once turtle2 stopped drawing, it never started again. In this
step, you will need to add another monitor which holds while the turtles
are close.

In order to create the outcome loop-back, you will also need to put the
monitor concurrence along with this new monitor into a state machine.
See the graph in SMACH Viewer below to get a better idea of how this
will look.

![width=800](doc/uc07.png)

#### Wrap SMACH Executive Into An Action

- Remove execute call
- Add wrapping code
- Create a python script that calls the action
- Run
