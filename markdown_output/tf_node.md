## Overview

Provides a ROS node interface for tf::TransformListener and
tf::TransformBroadcaster.

This package exposes the methods of tf::TransformListener and
tf::TransformBroadcaster as a set of ROS services. This functionality
may be useful for accessing transforms from ROS nodes written in
programming languages other than C++ or Python. Service call overhead
may render this package unsuitable for heavy users of transforms,
however. Node also supports additional functionality, such as setting up
and cancelling static transforms (which are published at some specified
frequency), and setting up standing transforms of messages from a source
to target topic.
