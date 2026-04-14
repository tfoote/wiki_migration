## About

Confidence-Based Autonomy (CBA) is a classification based Learning from
Demonstration algorithm that allows the human user and robotic agent to
jointly construct the training set. The agent autonomously decides when
the it feels uncertain about an action policy decision and requests a
demonstration from its human user. This ROS package contains the core
components of the the algorithm. In addition to running the main CBA
node, the following components must be implemented in a manner that
suits the agent\'s needs:

-   State Publisher \-- a node to constantly publish the state of the
    agent via the \`state_listener\` topic.
-   Confidence Based Classifier \-- a classifier node that is able to
    provide a confidence measurement. This node will receive data points
    via the \`add_point\` and \`change_point\` topics and queried via
    the \`classify\` service.
-   Action Execution \-- a node to listen for execution requests via the
    \`execute\` topic and notify the CBA node that it has finished the
    action execution and provide any correction information via the
    \`a_complete\` service.
-   Demonstration Request \-- a node that is able to ask the human user
    to provide demonstration information via the \`demonstration\`
    service.

For additional details on CBA, please refer to the following
publication:

\`Sonia Chernova and Manuela Veloso. Interactive Policy Learning
through\` \` Confidence-Based Autonomy. Journal of Artificial
Intelligence Research.\` \` Vol. 34, 2009.\`
[PDF](http://web.cs.wpi.edu/~rail/files/ChernovaVelosoJAIR09.pdf)

## Nodes

```clearsilver
node.0 {
  name = cba
  desc = The main implementation of CBA. This node listens to a state publisher and attempts to produce an action label to execute. If the agent instead feels uncertain about its decisions, a demonstration request is given.
  sub {
    0.name = state_listener
    0.type = lfd_common/state
    0.desc = The latest state vector of the agent for CBA to predict an action for. All published state vectors must be of the same length.
  }
  srv_called {
    0.name = classify
    0.type = lfd_common/conf_classification
    0.desc = Classify the given state returning the confidence, classification label, and decision boundary label.
    1.name = demonstration
    1.type = lfd_common/demonstration
    1.desc = Request a demonstration for the given state returning the action label for the demonstrated action (if one was given) and a boolean value indicating if the demonstration was given. This request will block until a response is given. Therefore, if no demonstration is given by the user within a reasonable amount of time, the request should be returned with the valid flag set to `false`.
  }
  pub {
    0.name = add_point
    0.type = lfd_common/classification_point
    0.desc = A data point to be added to the classifier with its given label.
    1.name = change_point
    1.type = lfd_common/classification_point
    1.desc = A data point that already exists in the classifier that needs its label changed.
    2.name = execute
    2.type = std_msgs/Int32
    2.desc = The label for the action CBA has determined to be executed. This may be either the same action the user just demonstrated or be due to a confident decision.
  }
  srv {
    0.name = a_complete
    0.type = lfd_common/action_complete
    0.desc = Used to notify CBA that the agent has finished executing an action. This service should be called by the agent as soon as it has finished executing any action that resulted from the `execute` topic. Furthermore, if the action was autonomous, it is possible that the human user provided a corrective demonstration. If so, the correction information can be added to this service request with the valid flag set to `true`. If no correction was given, the valid flag should be set to `false`.
  }
  param {
    0.name = ~max_data_points
    0.type = `integer`
    0.desc = The maximum number of data points to allocate space for. Once `max_data_points` have been seen by the algorithm, all others will be ignored.
    0.default = 1024
    1.name = ~dist_thresh_mult
    1.type = `double`
    1.desc = The distance threshold multiplier. This is the value by which the average nearest neighbor distance is multiplied by when calculating the distance threshold.
    1.default = 1.5
  }
}
```

### Launching CBA

The CBA assumes the the above topics/services are already running. Once
it receives its first state via the \`state_listener\` topic, it will
continuously iterate through the algorithm. To launch the node, the
following commands can be used:

```
rosrun cba cba
```

Since this node requires additional topics/services to be running, it
may make sense to create a launch file for your application.

## CBA Test Nodes

The \`cba\` package includes a set of test nodes used to test the
functionality of the the CBA implementation. These nodes rely on
semi-random data and a highly-simplified classifier. They are included
only to serve as point of reference when implementing the nodes required
to interact with the \`cba\` node. ```clearsilver
node.0 {
  name = mock_state_publisher
  desc = The mock state publisher will continuously publish a random 3 dimensional state vector. The values are integers bounded in the range [0,25).
  pub {
    0.name = state_listener
    0.type = lfd_common/state
    0.desc = The latest state vector of the agent
  }
}
node.1 {
  name = mock_agent
  desc = The mock agent is responsible for handling action execution and demonstration requests. These services are handled autonomously for the purposes of this test implementation.
  srv_called {
    0.name = a_complete
    0.type = lfd_common/action_complete
    0.desc = Sent to indicate the current action has finished executing. 10% of the time a correction is given.
  }
  sub {
    0.name = execute
    0.type = std_msgs/Int32
    0.desc = Executes the action. This is simulated by sleeping for a small amount of time based on the action label. Once finished, the `a_complete` service is called.
  }
  srv {
    0.name = demonstration
    0.type = lfd_common/demonstration
    0.desc = Give the user demonstration information. A demonstration will be given for every other request. The demonstration label will be the exact value that the mock classifier will assign.
  }
}
node.2 {
  name = mock_classify
  desc = The mock classifier is a highly simplified classifier. This classifier splits up the data into 5 labels based solely on the third-dimensional value of the state. The confidence value is simply the number of unique data points observed divided by the total state size. Noise is randomly added to give incorrect classifications.
  srv {
    0.name = classify
    0.type = lfd_common/conf_classification
    0.desc = Classifies the given state vector and gives a confidence value.
  }
  sub {
    0.name = add_point
    0.type = lfd_common/classification_point
    0.desc = Add the given state vector and label to the data set.
    1.name = change_point
    1.type = lfd_common/classification_point
    1.desc = Change the label for the given state vector in the data set. For the mock classifier, this will simply verify that the state vector exists in the data set.
  }
}
```

## Running the CBA Tests

If you would like to run the CBA test nodes, this can be done via the
included \`cba_test.launch\` file. This file launches an instance of the
\`cba\`, \`mock_agent\`, \`mock_classify\`, and \`mock_state_publisher\`
nodes. To launch these nodes, the following commands can be used:

```
roslaunch cba_ctrl cba_test.launch
```

## Installation

To install the \`lfd\` stack, you can choose to either install from
source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/lfd.git
roscd lfd
rosdep install lfd
rosmake lfd
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-fuerte-lfd
```

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/lfd/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     \<tablewidth=\"100%\"\> ![](attachment:wpi.png)      \<:99%\>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
