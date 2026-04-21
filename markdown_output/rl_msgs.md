## Documentation

This package defines a standard way for agents and environments to
communicate through ROS messages. In ROS computation is done by nodes
that perform different tasks that communicate through a set of ROS
messages. ROS provides the framework to publish, subscribe to and
receive these messages, in addition to tools for logging, displaying,
plotting, and playing back ROS messages. This package defines a set of
ROS messages for a reinforcement learning agent and environment to
communicate. These messages are similar to the messages used by RL-Glue
([Tanner and White 2009](rl-texplore-ros-pkg/rl_references)), but are
simplified and defined in the ROS format.

Please take a look at the
[tutorial](reinforcement_learning/Tutorials/Reinforcement Learning Tutorial)
on how to install, compile, and use this package

Check out the code at:
<https://github.com/toddhester/rl-texplore-ros-pkg>

![\|width="480"](attachment:reinforcement_stack_overview.png)

Agents from the [rl_agent](rl_agent) package can communicate with
environments from the [rl_env](rl_env) package through this interface.
In addition, you can write your own agents and environments that will
work with the ones in those packages by passing the same messages
defined here.

The framework is being designed to be as flexible as possible. While our
algorithms and environments will mostly follow a certain style, we
understand that every robot and every experiment differs. Our hope is to
not force our philosophy onto other people, as long as you adhere to
[rl_msgs](rl_msgs) you can design and implement your algorithms and
environments in your own style.

### Messages passed from Agent to Environment

-   **RLAction**: This message sends the environment the action (an
    integer) that the agent has selected.
    [rl_msgs/RLAction](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLAction.html)
-   **RLExperimentInfo**: This message provides information on the
    results of the latest episode of the experiment, namely an episode
    number, the sum of rewards for that episode, and the number of
    actions the agent took in that episode. The episode_reward can be
    plotted to look at rewards per episode.
    [rl_msgs/RLExperimentInfo](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLExperimentInfo.html)

### Messages passed from Environment to Agent

-   **RLEnvDescription**: This message describes the environment with a
    title, the number of actions, the number of states, the range of
    each state feature, the maximum one-step reward, the range of
    rewards, if the task is episodic or not, and if the task is
    deterministic or stochastic.
    [rl_msgs/RLEnvDescription](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLEnvDescription.html)

```{=html}
<!-- -->
```
-   **RLEnvSeedExperience**: This message provides a full experience
    <s, a, s', r> seed for the agent to use for learning. In addition
    to the state, action, next state, and reward, it also includes a
    boolean indicating if it is a terminal transition or not.
    [rl_msgs/RLEnvSeedExperience](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLEnvSeedExperience.html)
-   **RLStateReward**: This is a message from the environment with the
    agent's new state, the reward received on this time step, and
    whether this transition is terminal or not.
    [rl_msgs/RLStateReward](http://www.ros.org/doc/indigo/api/rl_msgs/html/msg/RLStateReward.html)

[References](rl-texplore-ros-pkg/rl_references)
