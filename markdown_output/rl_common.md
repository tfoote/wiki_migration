## Documentation

This package defines interfaces for agents, environments, models, and
plannersin the file
[core.hh](http://www.ros.org/doc/indigo/api/rl_common/html/core_8hh.html).
All agents, environments, models, and planners should inherit from their
appropriate base class.

Please take a look at the
[tutorial](reinforcement_learning/Tutorials/Reinforcement Learning Tutorial)
on how to install, compile, and use this package.

Check out the code at:
<https://github.com/toddhester/rl-texplore-ros-pkg>

### Experience

First, an experience \<s,a,r,s\'\> tuple is defined, which is used to
update the model. The state s the agent came from is a vector of floats,
the action it took is an int, the reward it received is a float, and the
next state s\' it transitioned to is a vector of floats. In addition,
there\'s a bool indicating if the transition was terminal or not. Full
documentation for the experience struct is available
[here](http://www.ros.org/doc/indigo/api/rl_common/html/structexperience.html).

### StateActionInfo

!StateActionInfo is the struct that the model must return when quering
the model for its predictions for a given state action. It has a
confidence (a float), a boolean telling if it is a \'known\' transition
or not, a float predicting the reward, a float predicting the
termination probability, and a map of states (vectors of floats) to
floats that gives the probabilities of next states. Full documentation
for the !StateActionInfo struct is available
[here](http://www.ros.org/doc/indigo/api/rl_common/html/structStateActionInfo.html).

### Agent

Agent is defined with a number of methods. Mainly it has
first_action(state) which is called for the first action in an episode
and returns an action. After that next_action(reward, state) should be
called, which returns an action. Finally upon reaching a terminal state,
last_action(reward) can be called. In addition to these methods,
seedExp(vector of experiences) can be used to seed the agent with a set
of experiences. Full documentation for the Agent class is available
[here](http://www.ros.org/doc/indigo/api/rl_common/html/classAgent.html).

### Environment

The environment has a sensation() method which returns the current state
vector and a terminal() method tells if the agent is in a terminal state
or not. The agent can act upon the environment by calling apply(action)
which returns a reward. A set of experience seeds to initialize agents
is available using the getSeedings() method. There are also a number of
methods to get information about the environment such as getNumActions,
getMinMaxFeatures, getMinMaxReward, and isEpisodic. Full documentation
for the Environment class is available
[here](http://www.ros.org/doc/indigo/api/rl_common/html/classEnvironment.html).

### MDPModel

The Markov Decision Process model only has four methods that it must
implement:

-   updateWithExperiences(vector of experience) updates the model with a
    vector of additional experiences.
-   updateWithExperience(experience) updates the model on single new
    experience.
-   getStateActionInfo(state, action, !StateActionInfo&) returns the
    model\'s prediction (!StateActionInfo) for the queried state and
    action.
-   getCopy() returns a copy of the model.

Full documentation for the MDPModelclass is available
[here](http://www.ros.org/doc/indigo/api/rl_common/html/classMDPModel.html).

### Planner

A planner must implement a few methods. Here are the key ones:

-   updateModelWithExperience(state, action, next state, reward,
    terminal) updates the agent\'s model with the new experience.
-   planOnNewModel() is called when the model has changed. It runs the
    planner on the model to compute a new policy.
-   getBestAction(state) returns the best action for the given state.

Full documentation for the Planner class is available
[here](http://www.ros.org/doc/indigo/api/rl_common/html/classPlanner.html).
