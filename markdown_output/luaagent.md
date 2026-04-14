## The Basics

The [behavior engine](behavior_engine) assumes a three layer separation
of the robot behavior control software. This package provides an
environment to formulate high-level agent programs using hybrid state
machines in Lua.

Essentially this environment lifts the approach of the
[skiller](skiller) to the higher level program. It communicates with the
skiller and uses it as the sole way of executing actions with the robot
hardware.

You can find the newest version at
<http://github.com/timn/ros-luaagent>.

It is part of the [behavior engine stack](behavior_engine).

## Requirements

It builds on utility packages from the behavior_engine stack.
Additionally, it uses [actionlib](actionlib) via
[actionlib_lua](actionlib_lua) to instruct and monitor the skiller.

## Documentation

Guides and howtos are currently work in progress. For now we would like
to refer to the example set of agents provided in the
[herb_agents](herb_agents) package.
