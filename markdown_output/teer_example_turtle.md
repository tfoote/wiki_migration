## Content

This package provides three examples on how to use [teer](teer) with
ROS. They all use [turtlesim](turtlesim) and come with launch files. A
small library, `turtle_math.py`, implements the common code not
related to teer.

### lonely_turtle.py

A simple turtle moving in a square. This example employs two tasks
`turtle1_go` and `turtle1_task`. The first publishes
<<MsgLink(turtlesim/Velocity)>> commands every half second, while
the second task takes care of following the square path.

### turtle_dating.py

Two turtles moving in squares of opposite directions. When turtles meet,
they fall in love, forget about their doing, and dance for a while; then
they become bored and get back to business. Like in the previous
example, turtle move using two tasks each (`turtleN_go` and
`turtleN_wandering`). In addition, a fifth task, `cupidon`, waits
until turtles are close enough, pauses their tasks, makes them dance,
and resumes their tasks afterwards.

### turtle_coverage.py

One turtle does zigzag coverage and a second does situation awareness.
When the second meets the first, it takes control of it, moves it to a
certain position, and restarts its task. Like in the previous examples,
the zigzag behaviour is implemented using two tasks, `turtle1_go` and
`turtle1_coverage`. One novelty is the catching of the
`GeneratorExit` exception, which allows `turtle1_coverage` to kill
`turtle1_go` when killed. This provides a flexible mechanism to
implement parent/child relationship between tasks. The
situation-awareness behaviour is implemented using a pair of
`turtle2_orbit` and `turtle2_orbiting` tasks, the latter being the
task taking control of the coverage turtle (turtle 1).
