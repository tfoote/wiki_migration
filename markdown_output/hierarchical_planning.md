```wiki
'''WARNING:''' This documentation refers to an outdated version of rosjava and is probably incorrect. Use at your own risk.
```

## Task Planning Problems

Currently, this package is set up to solve problems involving a set of
surfaces (i.e., tables) and objects (i.e., Odwalla bottles) whose
positions are known in advance, with at most one goal per movable object
of the form: get bottle a to (a partiular region/point on) table b.

The current functionality is fairly brittle and limited, but could
relatively easily be extended, by adding to the world representation (in
\'\'src_clj/ros/planning/world.clj\'\') and extending/replacing the
action hierarchy (in \'\'src_clj/ros/planning/actions.clj\'\').

These instructions will briefly show a simple use of the task planning
code; many more details are provided in comments and function docstrings
in the code itself.

## Setup

To use the package, you will first have to follow the setup instructions
for [rosjava](rosjava) and [rosclj](rosclj), then \"rosmake
hierarchical_planning\".

Then, to bring up the ROS nodes required for planning/execution:

-   First, bring up the robot/simulator and nav stack
-   For a robot, bring up \'\'prx.launch\'\' and
    2dnav_pr2/\'\'move_base/2dnav_pr2.launch\'\'
-   For the simulator, use \'\'launch/sim1.launch\'\' or
    \'\'launch/sim2.launch\'\', or modify these as desired.
-   Second, roslaunch \'\'launch/both_arms.launch\'\' or
    \'\'launch/right_arm.launch\'\', depending on the arm configuration
    of your (possibly simulated) robot.

Finally, run \'\'bin/clj\'\' to bring up a REPL with all of the
necessary code on the classpath, and type

```clojure
(use '[ros.planning actions world sahtn])
```

to load the relevant code. Follow the instructions in [rosclj](rosclj)
to set up a NodeHandle, or (load \"ros/teleop\") from [clj_pr2](clj_pr2)
(should automatically be on the classpath) to do this automatically and
also load teleoperation code.

## Planning and Executing

First, you will need to set up the planning environment and goals. For
details on how to do this, see \'\'src_clj/ros/planning/world.clj\'\'.
Or, to use a preset demo environment for Willow Garage green room, you
can use (get-demo-env nh).

Then, to construct a (hopefully) good plan that solves this problem, use
\"sahtn\".

```clojure
(def *result* 
  (sahtn nh [[(make-setup-hla [true]) (make-act-hla true)]] 
         (get-demo-env nh) 
         {:ros.planning.actions/BaseRegionAction 5  
          :ros.planning.actions/ArmGraspHLA 1  
          :ros.planning.actions/ArmDropHLA 1  
          :ros.planning.actions/ArmPoseAction 1 
          :ros.planning.actions/GoDropRegionHLA 
            (fn [a] (let [[[ax bx] [ay by]] (get-xy-region-extent (:drop-region a))]
                      (if (or (= ax bx) (= ay by)) 
                          1 
                       (min 5 (int (* 5 (+ (- bx ax) (- by ay))))))))})
``` This tries to find a good solution to the demo
environment, with the single initial plan \[get robot to known state,
then solve the problem by moving things\], with a fairly low sampling
resolution for most actions, and adaptive sampling for object drop
regions based on the region perimeter. The robot will look around at
various points relevant to the plan as it thinks, and will output a
solution plus reward or nil for failure. Increasing the sampling
resolutions will decrease failure probability and increase plan quality,
but also increase planning time.

If a solution is found, it can be executed using execute-plan (which
will just fail if any actions fail), or execute-plan-robustly (which
will keep retrying failed actions until they succeed).

```clojure
(execute-plan nh (first *result))
(execute-plan-robustly nh (first *result))
```

## Video

[Youtube](https://www.youtube.com/watch?v=HBZjmsrJbEY)
