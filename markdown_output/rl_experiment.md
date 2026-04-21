## Documentation

Please take a look at the
[tutorial](reinforcement_learning/Tutorials/Reinforcement Learning Tutorial)
on how to install, compile, and use this package.

Check out the code at:
<https://github.com/toddhester/rl-texplore-ros-pkg>

This package provides a way of running reinforcement learning
experiments with the agents from the [rl_agent](rl_agent) package and
environments from the [rl_env](rl_env) package without using the
[rl_msgs](rl_msgs) interface. Instead, the code instantiates agent and
environment objects and calls their methods directly. It can be set to
run for a particular number of episodes and trials, and prints out the
sum of rewards for each episode to cerr.

### Running an experiment

To run an RL experiment, you can call rl_experiment like so:



```
rosrun rl_experiment experiment --agent type --env type [options]
```

 where the agent type is one of the following:



```
qlearner sarsa modelbased rmax texplore dyna savedpolicy
```

 and the environment type is one of the
following:



```
taxi tworooms fourrooms energy fuelworld mcar cartpole car2to7 car7to2 carrandom stocks lightworld
```

 There are a number of options available to set
parameters of both the agent and environment used. More details on the
agent options are available in the [rl_agent](rl_agent) documentation,
and more details on the env options are available in the
[rl_env](rl_env) documentation.

. Agent Options:

-   \--gamma value (discount factor between 0 and 1)
-   \--epsilon value (epsilon for epsilon-greedy exploration)
-   \--alpha value (learning rate alpha)
-   \--initialvalue value (initial q values)
-   \--actrate value (action selection rate (Hz))
-   \--lamba value (lamba for eligibility traces)
-   \--m value (parameter for R-Max)
-   \--k value (For Dyna: \# of model based updates to do between each
    real world update)
-   \--history value (# steps of history to use for planning with delay)
-   \--filename file (file to load saved policy from for savedpolicy
    agent)
-   \--model type (tabular,tree,m5tree)
-   \--planner type
    (vi,pi,sweeping,uct,parallel-uct,delayed-uct,delayed-parallel-uct)
-   \--explore type (unknowns,greedy,epsilongreedy)
-   \--combo type (average,best,separate)
-   \--nmodels value (# of models)
-   \--nstates value (optionally discretize domain into value \# of
    states on each feature)
-   \--reltrans (learn relative transitions)
-   \--abstrans (learn absolute transitions)
-   \--v (For TEXPLORE: coefficient for variance bonus intrinsic
    rewards)
-   \--n (For TEXPLORE: coefficient for novelty bonus intrinsic rewards)

Env Options:

-   \--deterministic (deterministic version of domain)
-   \--stochastic (stochastic version of domain)
-   \--delay value (# steps of action delay (for mcar and tworooms)
-   \--lag (turn on brake lag for car driving domain)
-   \--highvar (have variation fuel costs in Fuel World)
-   \--nsectors value (# sectors for stocks domain)
-   \--nstocks value (# stocks for stocks domain)

General Options:

-   \--prints (turn on debug printing of actions/rewards)
-   \--seed value (integer seed for random number generator)
-   \--nepisodes value (# of episodes to run for this task or \# of
    steps for non-episodic tasks)

In addition to these options, there a few variables that can be changed
in the code, in the
[rl.cc file](http://www.ros.org/doc/indigo/api/rl_experiment/html/rl_8cc.html).
Near the top of the file are two variables: MAXSTEPS and NUMTRIALS.
MAXSTEPS determines the maximum number of steps for an episode. A new
episode will be started after this many steps even if the agent has not
reached a terminal state.

#### Example

As an example, here is how you would run Q-Learning
([Watkins 1989](rl-texplore-ros-pkg/rl_references)) on the stochastic
Taxi task ([Dietterich 1998](rl-texplore-ros-pkg/rl_references)):



```
rosrun rl_experiment experiment --agent qlearner --env taxi --stochastic
```

 Or to run real-time TEXPLORE
([Hester and Stone 2010](rl-texplore-ros-pkg/rl_references),
[Hester et al 2012](rl-texplore-ros-pkg/rl_references)) at 10 Hz on the
deterministic Fuel World task
([Hester and Stone 2010](rl-texplore-ros-pkg/rl_references)) with 8
discrete trees:



```
rosrun rl_experiment experiment --agent texplore --nmodels 8 --planner parallel-uct --actrate 10 --env fuelworld --deterministic
```

 While you should find that the qlearner, sarsa,
dyna, and rmax agents work fine on the easier tasks (tworooms, taxi,
etc), they will not converge within the default 1000 episodes on more
complex tasks like Fuel World. As an example, here is how to run
Q-Learning ([Watkins 1989](rl-texplore-ros-pkg/rl_references)) on the
Fuel World task
([Hester and Stone 2010](rl-texplore-ros-pkg/rl_references)) using the
\--nepisodes flag to run it for 1,000,000 episodes, which should be
enough time for it to converge.



```
rosrun rl_experiment experiment --agent qlearner --env fuelworld --nepisodes 1000000
```

 Another problem you may run into is when
running these methods on the continuous domains (mcar, cartpole,
car2to7, car7to2, and carrrandom). For these domains, the tabular RL
methods (Q-Learning, SARSA, Dyna, R-Max) will need the state to be
discretized. The following command will run Q-Learning
([Watkins 1989](rl-texplore-ros-pkg/rl_references)) on the Mountain Car
task ([Sutton and Barto 1998](rl-texplore-ros-pkg/rl_references)) while
discretizing each of the state features into 10 discrete values using
the \--nstates option.



```
rosrun rl_experiment experiment --agent qlearner --env mcar --nstates 10
```

 [References](rl-texplore-ros-pkg/rl_references)
