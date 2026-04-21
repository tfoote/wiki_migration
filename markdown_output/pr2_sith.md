## Background

One of the great things about working on ROS is the ability to see
everyone else's code. So when Joe Romano create the pr2_props demo, I
was able to take it apart and see how it worked. The basic idea was to

-   Move the arm to a designated pose
-   Begin moving the arm to another pose
-   If an acceleration is detected in the wrist accelerometer, stop.
-   Repeat as necessary

This, along with
[Stanford's Demo](http://www.wired.com/gadgetlab/2011/07/light-saber-robot/)
gave me an idea. Essentially, what if you did the same exact demo, with
slightly different arm positions, and a plastic lightsaber in the robots
hand.

## Implementation

While the original pr2_props was written in C++, I converted the whole
thing to be Python in a slightly more modular way. All of the arm
positions are saved and loaded from yaml files.

## Usage

The launch file duel_with_setup will move the PR2's arm to its side,
and open the gripper. Place the lightsaber in the PR2's gripper
pointing up and press enter.

## Cute Video

[Youtube](https://www.youtube.com/watch?v=lg1u4iAPYZY)
