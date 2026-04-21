This package can be used to learn a value function for general problems
in which state information and a simple reward signal can be provided.
For example, given set of time series data from continuous navigation,
one can provide a 5 dimensional state input (2 dimensional robot
position, 2 dimensional goal position, and time of day in hours) and
learn a value function predicting the value of any given state at a
given time of day. That is, we hope to learn to avoid various areas at
certain times of day due to traffic etc.

## Video

[Youtube](https://www.youtube.com/watch?v=6VuFEGoZ-xQ)

### Services

`agent_env` (<<SrvLink(value_learner/agent_env)>>) This service
expects a variable length array of type Float64 called state, a Float64
called reward, and responds with the value as a Float64. This service
also takes in a bool called isStateTerminal which is used in episodic
tasks to flag the terminal state of an episode when set to true.
Otherwise leave false.

### Parameters



```clearsilver
param {
  group.0 {
    0.name = ~/value_learner_agent/discount_factor
    0.type = float64
    0.desc = The discount factor of the underlying MDP.
    0.default = 0.99
  }
  group.1 {
    1.name = ~/value_learner_agent/rbf_width
    1.type = float64
    1.desc = The width of the radial basis functions.
    1.default = 0.05
  }
  group.2 {
    2.name = ~/value_learner_agent/numRBFs
    2.type = int
    2.desc = Number of radial basis functions to use in LSTD. Not necessary for RKHS-SARSA.
    2.default = 5
  }
  group.3 {
    3.name = ~/value_learner_agent/state_dim
    3.type = int
    3.desc = Dimension of the state input.
  }
  group.4 {
    4.name = ~/value_learner_agent/feature_types
    4.type = string
    4.desc = Type of feature map to use. Always set to raw for RKHS-SARSA.
    4.default = raw
  }
  group.5 {
    5.name = ~/value_learner_agent/isLearning
    5.type = int
    5.desc = If 1 will perform value function updates. If 0 will simply evaluate the given states.
    5.default = 1
  }
  group.6 {
    6.name = ~/value_learner_agent/param_file
    6.type = string
    6.desc = The path and file name of a parameter file for LSTD. New parameters will also be written to this file.
  }
  group.7 {
    7.name = ~/value_learner_agent/param_path
    7.type = string
    7.desc = The path of the directory containing the parameters for RKHS-SARSA.
  }
  group.8 {
    8.name = ~/value_learner_agent/lambda
    8.type = float64
    8.desc = lambda - the back-propagation coefficient for RKHS-SARSA.
  }
  group.9 {
    9.name = ~/value_learner_agent/step_size
    9.type = float64
    9.desc = The step size parameter for the RKHS-SARSA gradient steps.
  }
  group.10 {
    10.name = ~/value_learner_agent/projectron_sensitivity
    10.type = float64
    10.desc = The sensitivity parameter for the RKHS-SARSA algorithm. The higher this number, the less RBFs will be added.
  }
```



## learn_RKHS_SARSA.launch

This launches value_learner in learning mode using the RKHS-SARSA
algorithm. This offers the agent_env service which awaits a state and
reward and returns a value for the given state. The value response is
obviously not necessary whilst learning takes place, however it can be
quite useful for monitoring the progress. RKHS-SARSA is very useful when
online learning is required.

## learn_LSTD.launch

This launches value_learner in learning mode using the LSTD algorithm.
This offers the agent_env service which awaits a state and reward and
returns a value for the given state. The value response is obviously not
necessary whilst learning takes place, however it can be quite useful
for monitoring the progress. LSTD only performs batch updates, however,
given a batch of data it is guaranteed to give exactly the corresponding
value function.

## predict_RKHS_SARSA.launch

This launches value_learner in predict mode, given a set of parameters
learned using the RKHS-SARSA algorithm. This offers the agent_env
service which awaits a state and reward and returns a value for the
given state.

## predict_LSTD.launch

This launches value_learner in predict mode, given a set of parameters
learned using the LSTD algorithm. This offers the agent_env service
which awaits a state and reward and returns a value for the given state.

## steal_nav_data.py

Python script which obtains the necessary data from either a simulated,
or real, navigation run. This script fills out the state and reward
information accordingly and makes service calls to agent_env.
