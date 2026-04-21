STOMP (Stochastic Trajectory Optimization for Motion Planning) is an
optimization-based motion planner based on the PI\^2 (Policy Improvement
with Path Integrals, Theodorou et al, 2010) algorithm. It can plan
smooth trajectories for a robot arm, avoiding obstacles, and optimizing
constraints. The algorithm does not require gradients, and can thus
optimize arbitrary terms in the cost function like motor efforts.

To use this planner, simply launch
`launch/stomp_motion_planner.launch` in place of the motion planner
you normally use, and send motion planning requests to the service name
`/stomp_motion_planner/plan_path`. The motion planner uses the same
ROS interface that move_arm expects, and acts as a drop-in replacement
for OMPL or CHOMP.

## Paper

For more technical details, check out the
[ICRA 2011 paper](Papers/ICRA2011_Kalakrishnan#Instructions_for_reproducing_experiments).

## Video

[Youtube](https://www.youtube.com/watch?v=KZqi8wAcC4k)

## Demos

Please follow the instructions on the
[ICRA 2011 paper page](Papers/ICRA2011_Kalakrishnan#Instructions_for_reproducing_experiments)
for instructions on how to run demos of stomp_motion_planner.

## Results

### Planning with and without constraints

We conducted systematic experiments in a simulated world containing a
shelf with 15 cabinets, shown in the images below.

  -- ---------------------------------------------- -- -------------------------------------------------------------- -- --------------------------------------------------------------------------------------------------------------------------------- --
     ![shelf\|width=210](attachment:shelf_sm.png)      ![shelf_collide\|width=210](attachment:shelf_collide_sm.png)      ![shelf_good\|width=210](attachment:shelf_good_sm.png)                                                                            
     Simulation setup used to evaluate STOMP           Initial straight-line trajectory between two shelves              Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of the gripper   
  -- ---------------------------------------------- -- -------------------------------------------------------------- -- --------------------------------------------------------------------------------------------------------------------------------- --

Iterative evolution of trajectory costs for 10 trials of STOMP on a
constrained planning task between shelves:

![curves](attachment:curves.png)

We conducted tests of STOMP between all pairs of shelves reachable by
the PR2 arm, both with and without gripper orientation constraints. We
also compared the performance with that of
[chomp_motion_planner](chomp_motion_planner). The results are summarized
in the table below:

  -- ------------------------------------- -- --------------------- -- --------------------- -- ------------------- --
     Scenario                                 STOMP Unconstrained      CHOMP Unconstrained      STOMP Constrained   
     Number of successful plans               210/210                  149/210                  196/210             
     Avg. planning time to success (sec)      0.88 +- 0.40             0.71 +- 0.25             1.86 +- 1.25        
     Avg. iterations to success               52.1 +- 26.6             167.1 +- 113.8           110.1 +- 78.0       
  -- ------------------------------------- -- --------------------- -- --------------------- -- ------------------- --

### Planning while optimizing torques

We tested the ability of STOMP in optimizing arbitrary cost functions by
attempting to minimize the torques used in a motion. The images below
show plans obtained with and without torque optimization:

  -- ------------------------------------------------------------------ -- ----------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------- --
     ![pole_no_torque\|width=210](attachment:pole_no_torque_1_sm.png)      ![pole_torque_1\|width=210](attachment:pole_torque_1_sm.png)               ![pole_torque_2\|width=210](attachment:pole_torque_2_sm.png)                                                                 
     Plan obtained without torque minimization: arm is stretched.          Plan (a) obtained with torque minimization: entire arm is pulled down      Plan (b) obtained with torque minimization: elbow is folded in. Both solutions require lower gravity compensation torques.   
  -- ------------------------------------------------------------------ -- ----------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------------------------------------------- --

Feed-forward torques used in the above planning problem, with and
without torque optimization, averaged over 10 trials.

![torques](attachment:torques.png)
