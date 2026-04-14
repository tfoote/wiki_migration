## The Basics

This package forms the heart of the
[behavior engine stack](behavior_engine). It includes a node that, when
run, creates the Lua environment for skill development, execution, and
monitoring. It implements a reactive behavior layer, in which arbitrary
execution schemes can be implemented. It provides specific tool support
to employ the approach of extended hybrid state machines.

You can find the newest version at <http://github.com/timn/ros-skiller>.

It is part of the [behavior engine stack](behavior_engine).

## Requirements

It builds on utility packages from the
[behavior engine stack](behavior_engine). Additionally, it uses
[actionlib](actionlib) via [actionlib_lua](actionlib_lua) to make use of
functionality provided by the base system and other ROS nodes.

## Documentation

Guides and howtos are currently work in progress. For now we would like
to refer to the example set of skills provided in the
[herb_skills](herb_skills) package.
