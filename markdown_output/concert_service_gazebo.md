This package contains all the robot-agnostic code for running simulated
robots in Gazebo with the concert framework.

## Workflow

Given a set of robots with their locations, this package provides a
service that spawns Gazebo locally, spawns those robots in Gazebo,
create a concert client for each robot, and flip connections to each
concert allowing them to behave as independent robot clients.

## Using this package with a new robot

In order to use this package, you'll have to do the following.

<<TutorialChain(concert_service_gazebo/Tutorials/indigo/How to add a
new robot type)>>

```wiki
 1. You'll need to prepare your robot launch file such that multiple robots can be spawned without a topic or tf name clash. This is typically achieved by prefixing both your topic names and tf frames with a robot-specific prefix. If you can run a single launch file with two or more simulated robots in Gazebo, you should be able to use this module to spawn multiple concert clients, one for each robot.
 2. Next, you'll need to write a new package that extends the `RobotManager` module in this package, specifying the following pieces of information:
  * How to spawn the robot in Gazebo.
  * How to delete the robot in Gazebo.
  * How each concert client for a simulated robot should be launched.
  * Which connections need to flipped over from gazebo to each robot.
```

## Example

An example is available in the [gazebo_concert](gazebo_concert) package.

## Other useful notes

1\. When spawning the robots in Gazebo, make sure that you spawn the
robots in the global ROS namespace, and not the namespace of the service
from which you'll be spawning Gazebo (typically
`/services/<service-name>/`). 2. Do not flip connections to a
robot's concert if you eventually plan to use them locally (by pulling
it through a rapp). This will cause infinite copies of the topic to be
flipped around between the concert master and the concert clients.
Additionally subscribers misbehave when subscribed against 2 ROS masters
([#127](https://github.com/robotics-in-concert/rocon_multimaster/issues/127))
3. Make sure that you set `/use_sim_time` to `true` when launching
the concert master as well as each concert client.
