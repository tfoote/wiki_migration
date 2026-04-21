## PREREQUISITES

It would be useful to familiarize yourself with the SMACH API before
attempting to write a RECOVERY SMACH state machine. A very well
documented set of tutorials on how to write state machines for the SMACH
can be found [here](smach/Tutorials).

## RECOVERY SMACH THEORY

The RECOVERY SMACH package introduces an ORACLE into regular SMACH state
machine. An ORACLE is a meta state which handles failure recovery by
transitioning the state machine from a failed state to any other state
in the state machine. The ORACLE handles these transitions based on
first order predicate logic. In the event of a failure the ORACLE
attempts to execute the preconditions for a given state (which might
include other states or independent preconditions). If satisfied the
ORACLE executes the current state or it transitions the state machine to
a state without preconditions in the current behavior execution chain.
In the event of unrecoverable failures or high failure states the ORACLE
can query the expert for assistance. Expert assistance can be provided
with user designed shared autonomy interfaces. More details on the
ORACLE behavior can be found in our
[ ICRA 2012](attachment:recovery_shared_autonomy/ICRA12.pdf) submission.

## ORACLE AND EXPERT INTERFACE

In the event of multiple failures at a certain state (above 75% failure
rate), the ORACLE can query the expert. The expert query is handled
through a shared autonomy interface shown below.

![\|width=100%](attachment:recovery_shared_autonomy/shared_auto_interface.png)

Through this GUI the expert can manually pick a state to transition the
state machine to or perform an expert recovery behavior using a shared
autonomy interface.

The expert GUI also shows the failure rate of the current states with a
simple color code where GREEN indicates a low failure state and RED
being a high failure state. The rate of failures of transitions is also
show in the GUI.

### SHARED AUTONOMY INTERFACE

A shared autonomy interface can be any independent process, that can be
launched as a node or launch file to replace the functionality of a
certain state in the state machine. Once the functionality of the
current state in the state machine has been superseded by the expert,
the expert can transition the state machine to a future state using the
expert GUI.

## HOW TO WRITE CODE

Now to the most important part of this tutorial. How does all this
work??

Initially you'll have to initialize the state machine by inheriting the
state machine base class and setting the oracle flag, this operation
would be very similar to SMACH state machines. Also specify a read/write
location for the failure and transition matrices.

```python
    sm = smach_recovery.StateMachine(outcomes=['succeeded','aborted','preempted'],oracle = 1)
    current_path =  path.join(path.dirname(__file__), 'data')
    sm._file_failure = current_path+'/failure_matrix_.pkl'
    sm._file_transition = current_path+'/transition_matrix_.pkl'
```

By setting oracle = 1 you are turning on the ORACLE recovery behavior.
If oracle is set to zero the state machine acts like a regular SMACH
state machine.

Now to specify preconditions for any state in the state machine, the
preconditions are specified with a identifier(string) which could either
be another state in the state machine or an independent class that is
not a part of the current execution cycle.

```python
with sm:
        # Add states to the container
        smach_recovery.StateMachine.add('FOO', Foo(),
                               transitions={'outcome1':'FOB',
                                            'outcome2':'succeeded',
                                            'aborted':'aborted'},
                               preconditions={'FIBONACCI':SimpleActionState('/fibonacci',
                               FibonacciAction,
                               result_cb = fibonacci_cb,
                               goal = sm.userdata.fibonacci)})
```

preconditions are specified similar to transitions except that the
dictionary maps a string to an object of a class.

These preconditions are the set of preconditions that need to be
satisfied for the current state to execute independently. In the
execution of the state machine these preconditions might be satisfied by
outcomes of some other state or series of states. For independent
execution of a state this precondition needs to first be satisfied to
successfully execute the state.

Finally to invoke the recovery you need to check if the oracle flag has
been invoked with the following snippet of code to follow the container
construction.

```python
if sm._oracle:
        sm = recovery.failure_free(sm)
```

Then the state machine is executed similar to a SMACH state machine.

## COMPATIBILITY

RECOVERY SMACH can handle any of the current (diamondback version)
containers that SMACH offers this includes: statemachine,concurrence,
iterator and sequence containers. It can also handle any type of state:
generic, simpleaction, cb,service and monitor. The API would be similar
to as demonstrated above

## RUNNING THE DEMO CODE

To run the demo run the following commands in the given order on
separate terminals after starting the roscore

```
rosrun smach_recovery_viewer smach_viewer.py
``` ```
rosrun recovery_tutorials fibonacci_server
```
```
rosrun recovery_tutorials simple_oracle.py
```
