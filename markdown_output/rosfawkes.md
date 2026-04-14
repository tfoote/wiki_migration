## Integrating Fawkes and ROS

[Fawkes](http://www.fawkesrobotics.org) is a robot software framework
and employs a component-based approach providing a massively
multi-threaded and closely integrated environment for real-time robotic
applications. It has some unique features like blackboard a
communication infrastructure, framework feature distribution inspired by
aspect-oriented programming and comes with a lot of useful libraries and
tools to aid robot software development. That makes it worthwhile to
consider employing Fawkes even in an existing ROS ecosystem.

The given package integrates Fawkes into ROS as a package which includes
all of Fawkes and provides a ROS node that runs the Fawkes main
application. Within that main application, run-time loadable plugins
provide functionality. Plugins are like ROS nodelets on steroids. They
are the primary development target and therefore benefit from a lot of
infrastructure to easily and efficiently use framework features,
interact with other components, or communicate with other ROS nodes.

There are
[two ways to integrate Fawkes and ROS](http://www.fawkesrobotics.org/documentation/rosfawkes)
depending from which framework the integration is approached. So it does
not matter which framework is the primarily used one, for both scenarios
there is an easy way to integrate the two. Fawkes plugins can
participate in ROS communication by getting access to a central node
handle within the Fawkes application. In this case ROS nodes have no
notion that the node they interact with is written in Fawkes. But ROS
nodes can also make use of Fawkes libraries to directly access the
blackboard, the central data exchange hub.

This is still work in progress and further steps to integrate the two
frameworks more closely are required. As an integration example the
Fawkes
[ros-webview](http://trac.fawkesrobotics.org/wiki/Plugins/ros-webview)
plugin is provided to allow ROS nodes to extend the Fawkes
[webview](http://trac.fawkesrobotics.org/wiki/Plugins/webview) web
interface.

## Documentation

Preliminary instructions how to use rosfawkes are provided in the
[rosfawkes documentation](http://www.fawkesrobotics.org/documentation/rosfawkes).
This is still work in progress and constantly extended. An
[introductory paper](http://www.fawkesrobotics.org/publications/2010/simpar2010-fawkes-design-principles/)
describes the main features of Fawkes and its benefits.
