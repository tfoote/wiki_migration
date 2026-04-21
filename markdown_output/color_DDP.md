## Overview

To move the head, we use [actionlib](actionlib)'s SimpleActionClient and
the action interface head_traj_controller/point_head_action. Given an
initial position, an obstacle, and a goal, DDP outputs the
locally-optimal trajectory T. Define T\[0\] to be the initial pixel of
the green ball, then, we would like that at the next time step the pixel
of the green ball is at T\[1\]. So, our goal is to move the head so that
the detected pixel of the green ball is equal to T\[1\]. Using the
Kinect topic camera/depth/points we project the pixel difference
(T\[1\]-T\[0\]) as a three dimensional point, p, in the frame
'openni_rgb_optical_frame'. We then transform p into the 'base_link'
frame and, using the aforementioned action interface, tell the PR2 to
move to the transformed point.

## Differential Dynamic Programming (DDP)

DDP is an algorithm that solves locally-optimal trajectories given a
cost function over some space. In essence it works by
locally-approximating the cost function at each point in the trajectory.
It uses this approximation to finds the optimal change to the trajectory
(via a set of actions) that minimizes some cost metric (e.g. cumulative
cost). In the limit it converges to the optimal trajectory.

## Dynamics & Cost

Our dynamics is simply linear in two-dimensions, without velocities:

  -- ----------------------------------------------------------------- --
     \<:99%\> \$\$ *x*,,t,, \`=\` *A* *x*,,t-1,, + *B* *u*,,t,, \$\$   
  -- ----------------------------------------------------------------- --

where \$\$A = B = I_2\$\$. Our cost function has a quadratic minimum and
Gaussian obstacles:

  -- ----------------------------------------------------------------------------------------------------- --
     \<:99%\> \$\$ *c*,,t,, = \$\$\\frac{1}{2}\$\$(*q*\^h\^ *u*,,t,,\^2\^ + *c*,,b,, *b*(*x*,,t,,)) \$\$   
  -- ----------------------------------------------------------------------------------------------------- --
