<http://rtc-us-ros-pkg.svn.sourceforge.net/viewvc/rtc-us-ros-pkg/trunk/rtcus_mobile_robots/rtcus_motion_models/>

## General Description

This package provides a template library to design different motion
models making possible parametrize the type of the representations of
the state, actions and time.

For instance the state could consider dynamic variables or not. Moreover
the state, actions or time could be represented with a probabilistic
description following the Probabilistic Robotic Foundations.

From the simplest transition function x_\[t+1\]=F(x_t,u,Delta t) a set
of more complex functions are generated. Including: sample a trajectory,
obtain the final state after a set of asynchronous action history,
obtain the final state after a set of actions, etc.

```
template<typename StateType, typename ActionType, typename Duration = ros::Duration, typename TTime = ros::Time>
class MotionModel;
```

## Example

Non holonomic and Deterministic 2D(non probabilistic) motion model.

```
class DeterministicNonHolonomic2D: public MotionModel<Pose,Twist>
```
