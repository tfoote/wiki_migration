## Overview

Markov Decision Making (MDM) is a library to support the deployment of
decision-making methodologies based on Markov Decision Processes (MDPs)
to teams of robots using ROS.

MDM helps you map between the abstract representations of
\'\'states\'\', \'\'actions\'\' and \'\'observations\'\' that are used
in decision-theoretic frameworks, and the actual actuators and sensors
of your robots. It also interprets your decision-making policies and
lets you configure an appropriate run-time execution strategy. Note that
\'\'\'MDM isn\'t a solver / planning algorithm for decision-theoretic
problems\'\'\'. For that you can use ROS-independent toolboxes such as
[MADP](http://www.fransoliehoek.net/index.php?fuseaction=software.madp).
But once you have a decision-theoretic policy, MDM helps you execute
that policy on your robot.

Notable features include:

-   Supports both single agent and multiagent systems;
-   Its generic callback-based action interpretation allows actions to
    be implemented through other ROS-based frameworks (e.g.
    [actionlib](actionlib) / [smach](smach));
-   The ability to easily implement hierarchical MDPs / POMDPs;
-   Supports synchronous (fixed-rate) and asynchronous (event-driven)
    execution strategies;
-   Relevant execution information can easily be logged through ROS
    (actions, states, rewards, transition rates, etc.);
-   Out-of-the-box, MDM supports discrete MDPs and POMDPs. However, it
    is designed to be easily extendable to account for your own MDP /
    POMDP variants, if necessary;
-   MDM can interact with the
    [Multiagent Decision Process (MADP) Toolbox](http://staff.science.uva.nl/~faolieho/madp).
    [MADP](http://staff.science.uva.nl/~faolieho/madp/) is a toolbox for
    decision-theoretic research, containing state-of-the-art solution
    algorithms for multiagent MDP-based models, and is actively
    maintained and extended by researchers in that field. MDM can
    potentially implement any model which can be defined through
    [MADP](http://staff.science.uva.nl/~faolieho/madp/).

MDM has been used (and is being used) in several international research
projects, including [MAIS+S](http://gaips.inesc-id.pt/mais-s/);
[SocRob](http://socrob.isr.ist.utl.pt); and
[TERESA](http://teresaproject.eu/).

## Documentation

In the following sections, you can find a light technical description of
MDM, and information on how to use the library for your own MDP-based
applications. For a more in-depth look into MDM, you can also refer to
[the following technical report](http://users.isr.ist.utl.pt/~jmessias/MDM/mdm_report.pdf).

For an overview of the concepts underlying MDM, please see the page
[MDM Concepts](markov_decision_making/Tutorials/MDM Concepts).

You can find examples of how to implement each MDM layer in the
[Tutorials](markov_decision_making/Tutorials).

MDM is modular and meant to be flexible and easy to adapt to your own
applications. You can find more information on various specialized
use-cases of MDM in the page:
[Deploying MDM: Considerations for Specialized Scenarios.](markov_decision_making/Tutorials/OtherUseCases)

## FAQ

Q: \'\'Does MDM support \<My favorite framework\>-MDPs?\'\'\
A: There are so many generalizations and variants of the MDP framework
that it is virtually impossible to design a library that supports all of
them out-of-the-box. Rather than trying to explicitly support all MDP
variants, MDM gives you the building blocks that you can use (and adapt)
to put together a decision-theoretic controller for your robot(s). The
underlying motivation is much of the implementation work that goes into
deploying a decision-theoretic control policy can be re-used across
different robot applications, regardless of the particular MDP variant
that you\'re using. However, if you adapt MDM to your own application,
you\'re encouraged to contribute to the library with your own
modifications, since that may help other users in the future. Feel free
to contact us, in that case!

Q: \'\'What\'s with the predicates? I want a grid world!\'\'\
A: Without going into a discussion as to why regular discretizations
aren\'t a particularly good idea, note that as long as your state space
is discrete and finite, then your states can be indexed by a
fixed-length string of logical values (i.e. in binary). In other words,
as long as you have enough predicates, you can represent any (finite)
discrete state space. The [predicate_manager](predicate_manager) package
is lightweight and designed to handle a very large number of predicates,
if needed. If you really want a \"grid world\"-like representation of
your state space, you can either write a generic \'\'IsInCellX\'\'
predicate and instantiate it for each your cells, or use the
pose_labeler package (included in topological_tools) together with a map
of the environment in which each cell is uniquely colored.

Q: \'\'That\'s nice, but my state / action space is continuous.. How can
I implement those?\'\'\
A: Although the default MDM State and Action Layers implicitly describe
discrete state and action spaces, you can potentially use the same node
layout, and implement a State Layer that outputs real-valued scalars or
vectors; a Control Layer that maps that into a real-valued action, and
an Action Layer that just maps those into actuator controls. We don\'t
have any plans at this time to extend MDM by ourselves to
continuously-valued domains, but if you\'re interested in doing so,
please feel free to contact us.

Q: \'\'I see that by default, the control layer accepts a pre-computed
policy. Does MDM support Reinforcement Learning?\'\'\
A: Yes, there is a (currently experimental) branch in the Git repository
that already supports some of the most basic RL algorithms for MDPs
(Q-learning, SARSA).
