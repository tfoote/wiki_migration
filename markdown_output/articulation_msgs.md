\<\<MsgSrvDoc(articulation_msgs)\>\>

## Model fitting/selection/evaluation using ROS message streams

Given a trajectory in form of a ROS
\<\<MsgLink(articulation_msgs/TrackMsg)\>\> message, the
\`model_learner_msg\` node of the
[articulation_models](articulation_models) package fits all available
template models, selects the one with the smallest BIC (Bayesian
Information Criterion), and publishes a ROS
\<\<MsgLink(articulation_msgs/ModelMsg)\>\> message. Note that this node
can then be used in real-time, as it skips trajectory messages if
necessary.

## Model fitting/selection/evaluation using ROS service calls

Alternatively, you might want to run model fitting, selection and/or
evaluation using ROS service calls. Corresponding services are provided
by the \`model_learner_srv\` node and the \`model_learner_prior\` node
in the [articulation_models](articulation_models) package.

## Visualization of trajectories and models

Trajectories \<\<MsgLink(articulation_msgs/TrackMsg)\>\> and models
\<\<MsgLink(articulation_msgs/TrackMsg)\>\> can be visualized in RVIZ
easily by using the Track and Model Display. See
[articulation_rviz_plugin](articulation_rviz_plugin) for how to set up
RVIZ to properly display them.
