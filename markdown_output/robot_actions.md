# DEPRECATED

The robot_actions package has been deprecated in favor of the
[actionlib](actionlib) package. Please see the
[documentation](actionlib) for the [actionlib](actionlib) package
instead for information about using actions with ROS.

------------------------------------------------------------------------

## Package Summary

The robot_actions package provides a construct for goal achieving,
modular behavior primitives that are non-blocking for the client, and
preemptable. This is in contrast to a service which is not preemptable
and blocks the client. The proposed package will define core components
to enforce action semantics. Such actions will be primitives available
for aggregation into higher level tasks. Specific action implementations
will not be part of this package. However, I propose that the message
based interface common for invocation and monitoring of actions will be
included in the package, much as robot_srvs are done now. Abstract base
class actions will be provided to support common action patterns. The
genesis of this idea is the work done in developing the
highlevel_controllers, and this is effectively a factoring of that work.

A strawman indicating the relationships between a supervisory executive,
actions, and low-level controllers (real time controllers operating very
fast, with very limited lookahead) is shown below.

![](attachment:actions.png)

### ROS Message Interface

The states for an action are:

-   ACTIVE - the action has an active goal it is working towards.
-   UNDEFINED - the action is inactive, with no information regarding
    the outcome of a prior goal.
-   SUCCESS - the action is inactive, and on becoming inactive it
    successfully achieved its goal.
-   PREEMPTED - the action is inactive, but was commanded to deactivate
    by an external client.
-   ABORTED - the action is inactive, but did not complete its goal and
    gave up.

The states and their transitions are shown below.

![](attachment:action.std.png)

### Implementation Requirements

Whenever an actions is in an inactive state (i.e. UNDEFINED, SUCCESS,
PREEMPTED, ABORTED) it should be operating in a low-duty cycle. An
implementation of an action must also support:

-   Handling goal requests - a request to be enabled, with parameters
    for goal achievement specific to each type of action. It should
    respond with a message indicating it is in an ACTIVE state, and
    including necessary goal parameters to describe the goal it is
    pursuing. Note that if an action is already active, a new goal
    request has the semantics of preempting the current goal before the
    new goal can be active.
-   Handling goal preemption - a request to disable the action. It
    should respond with a message to indicate a PREEMPTED state.
-   Publishing a SUCCESS state message on successful completion of its
    goal, after which it should operate in a low-duty cycle.
-   Publishing an ABORTED state message when it has given up on a goal,
    after which it should operate in a low-duty cycle.
-   Publishing an UNDEFINED state on initialization, or whenever it must
    indicate that it is not active without any implication about the
    success or failure of a prior goal.

### Implementation Support

A small C++ framework has been put in place to allow easy implementation
of an action by sub-classing robot_actions::Action. The example below is
from a test action in test_robot_actions. It illustrates the primary
function an action implementer must provide - execute. This function
will block until the action has become deactivated. Note the use of the
function to test for preemption. if developers do not have such tests
then in practice their action will not be pre-emptable since preemption
must be signaled by the action implementer.



```cplusplus
class MyAction: public robot_actions::Action<Float32, Float32> {
public:

  MyAction(): robot_actions::Action<Float32, Float32>("my_action") {}

  const static int FAIL_IF = 30;

private:

  // This method will run for the number of ms given by the goal.
  virtual ResultStatus execute(const Float32& goal, Float32& feedback) {

    // Variable for accumulated running time
    double count = 0.0;
    ros::Duration d; d.fromSec(0.001);

    while (!isPreemptRequested() && count <= goal.data) {
      count += 1.0;
      feedback.data = count;
      update(feedback);
      d.sleep();
    }

    if (isPreemptRequested()) {
      return PREEMPTED;
    } else if(goal.data >= FAIL_IF){
      return ABORTED;
    }
    else {
      return SUCCESS;
    }
  }
};
```



We also provide a function to waitForDeactivation so that action
implementations based on callbacks can signal the execute method to
complete.

Finally, an ActionRunner class is provided to implement the ROS message
bindings, making the action callable over ROS.



```cplusplus
  MyAction action;

  // Now run it.
  robot_actions::ActionRunner runner(10.0);
  runner.connect<Float32, TestState, Float32>(action);
  runner.run();
```



### Test Support

An ActionClient has been provided to allow a test program in C++ to call
actions remotely, exercising the ROS message integration model. Simple
test executives can thus be built.

Here is a simple test executive.



```cplusplus
  // Use a client to test the action
  robot_actions::ActionClient<Float32, TestState, Float32> client("my_action");
  ros::Duration duration(5);
  duration.sleep();

  // Start the action; it must finish in 1 second
  Float32 g, f;
  g.data = 5;
  robot_actions::ResultStatus result = client.execute(g, f, ros::Duration(1));
  ASSERT_EQ(result, robot_actions::SUCCESS);

  // Start the action; it must finish in 0.0001 second
  result = client.execute(g, f, ros::Duration().fromSec(0.0001));
  ASSERT_EQ(result, robot_actions::PREEMPTED);
```



## Tutorials

Links to relevant tutorials

------------------------------------------------------------------------

[Troubleshooting](/Troubleshooting)

[Review Process](/Reviews)
