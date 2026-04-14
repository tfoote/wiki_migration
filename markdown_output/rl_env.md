## Documentation

Please take a look at the
[tutorial](reinforcement_learning/Tutorials/Reinforcement Learning Tutorial)
on how to install, compile, and use this package.

Check out the code at:
<https://github.com/toddhester/rl-texplore-ros-pkg>

This package contains a variety of environments that can be used for
reinforcement learning experiments. These can be used with new RL agents
written to use the [rl_msgs](rl_msgs) framework, or with existing agents
from the [rl_agent](rl_agent) package. The package contains the
following environments:

-   Taxi ([Dietterich 1998](rl-texplore-ros-pkg/rl_references))
-   Two room grid world
-   Four room grid world
-   Four room grid world with energy levels
-   Fuel World
    ([Hester and Stone 2010](rl-texplore-ros-pkg/rl_references))
-   Mountain Car
    ([Sutton and Barto 1998](rl-texplore-ros-pkg/rl_references))
-   Cart Pole
    ([Sutton and Barto 1998](rl-texplore-ros-pkg/rl_references))
-   Robot Car Velocity Control simulation
    ([Beeson et al 2008](rl-texplore-ros-pkg/rl_references),
    [Hester et al 2012](rl-texplore-ros-pkg/rl_references))
-   Stock Trading
    ([Strehl et al 2007](rl-texplore-ros-pkg/rl_references))
-   Light World
    ([Konidaris and Barto 2007](rl-texplore-ros-pkg/rl_references))

All of these domains can be run in stochastic or deterministic mode by
passing the \--deterministic or \--stochastic options. The two room
gridworld and mountain car tasks can also be run with action delays by
passing \--delay n. The robot car velocity control simulation is a
simulation of controlling the pedals of UT\'s autonomous car to control
its velocity. This simulation simulates a single 20 Hz step when called,
but actions do not have to be specified at 20Hz (as they do on the
actual robot car or in the Stage simulation of it).

### Running an environment

The environment can be run with the following command:

```
rosrun rl_env env --env type [options]
``` where the environment type is one of the
following options:

```
taxi tworooms fourrooms energy fuelworld mcar cartpole car2to7 car7to2 carrandom stocks lightworld
``` There are a number of options to specify
particular parameters of options for the various domains:

-   \--seed value (integer seed for random number generator)
-   \--deterministic (deterministic version of domain)
-   \--stochastic (stochastic version of domain)
-   \--delay value (# steps of action delay (for mcar and tworooms)
-   \--lag (turn on brake lag for car driving domain)
-   \--highvar (have variation fuel costs in Fuel World)
-   \--nsectors value (# sectors for stocks domain)
-   \--nstocks value (# stocks for stocks domain)
-   \--prints (turn on debug printing of actions/rewards)

#### Example

As an example, to run the car velocity control task, with the car
learning to go between random starting and target velocities, with
stochastic actions, lag on the brake actuator, and debug print
statements on, you would call:

```
rosrun rl_env env --env carrandom --lag --stochastic --prints
```

### How the Environment interacts with the RL Agent

The environment can interact with an RL agent in two ways. It can use
the ROS messages defined in [rl_msgs](rl_msgs), or another method can
call the agent and environment methods directly, as done in the
[rl_experiment](rl_experiment) package.

#### Using rl_msgs

The rl_msgs package defines a set of ROS messages for the agent and
environment to communicate. These are similar to the messages used in
RL-Glue ([Tanner and White 2009](rl-texplore-ros-pkg/rl_references)),
but simplified and defined in the ROS message format. The environment
publishes three types of messages for the agent:

-   [rl_msgs/RLEnvDescription](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLEnvDescription.html):
    this message describes the environment, number of actions, number of
    features, if its episodic, etc.

```{=html}
<!-- -->
```
-   [rl_msgs/RLEnvSeedExperience](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLEnvSeedExperience.html):
    this message provides an experience seed for the agent to use for
    learning.
-   [rl_msgs/RLStateReward](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLStateReward.html):
    this is a message from the environment with the agent\'s new state
    and reward received on this time step.

The environment subscribes to one type of message from the agent:

-   [rl_msgs/RLAction](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLAction.html):
    this message sends the environment the action that the agent has
    selected.
-   [rl_msgs/RLExperimentInfo](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLExperimentInfo.html):
    this message provides information on the results of the latest
    episode of the experiment.

When the environment is created, it sends an RLEnvDescription message to
the agent. Then it will send any experience seeds for the agent in a
series of RLEnvSeedExperience messages. Then it will send the agent an
RLStateReward message with the agent\'s initial state in the domain. It
should then receive an RLAction message, which it can apply to the
domain and send a new RLStateReward message. When the episode has ended,
the environment will receive an RLExperimentInfo message from the agent,
and it will reset the domain and send the agent a new RLStateReward
message with its initial state in the new episode.

#### Calling methods directly

Experiments can also be run by calling the agent and environment methods
directly (as done in the [rl_experiment](rl_experiment) package).
Methods that all environments must implement are defined in the
Environment interface in the [rl_common](rl_common) package
([API](http://www.ros.org/doc/indigo/api/rl_common/html/classEnvironment.html)).
Seeds can be retrieved from the environment with the getSeedings()
method. An action is applied to the environment with a call to
apply(action). The current state can be retrieved by calling sensation()
and terminal() will indicate if the agent is in a terminal state or not.

[References](rl-texplore-ros-pkg/rl_references)
