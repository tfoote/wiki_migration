## Overview

This package is still under development. The goal is to have an
automatic way of tuning the PID parameters on our controllers. We're
using [eodev](eodev) to implement our evolutionary algorithm.

Here is an overview of the early results obtained with the automatic pid
tuning. The algorithm was run on the simulated version of the hand in
Gazebo. The middle "wave" of the third plot shows an excellent tuning
in term of error minimization, but it's slightly unstable so we won't
use it.

![ Before tuning](attachment:rfj3_gazebo_hand_tuning.png )

![ After tuning](attachment:ffj3_gazebo_automatic_tuning.png )

![ Excellent tuning, but a bit unstable](attachment:amazing_tuning.png )

Finally we obtained a very well tuned joint using this optimization
algorithm, after a **35min** cycle. Here is the plot for the same
movement at different speed (please note that no targets is being
published for a short time when changing the movement speed, which
explains the difference between the (interpolated) target line and the
position line):

![ Excellent tuning\|width=600](attachment:very_good.png )

## Running the tuning

You should edit the starting seed of the algorithm (it is recommended to
use some working values) in the **seed.yaml** file. The
**max_variations** parameter in this file defines the range which will
be explored by the algorithm.

You can run the algorithm with the following command line:
```
$ rosparam load `rospack find sr_automatic_pid_tuning`/seed.yaml ; rosrun sr_automatic_pid_tuning sr_automatic_pid_tuning /sr_automatic_pid_tuning/targets:=/sh_ffj3_effort_controller/command --popSize=10 --weakElitism=2 --pCross=0.9 --maxGen=10 --joint="ffj3" _image_path:="`rospack find sr_movements`/movements/test.png" _min:=-200.0 _max:=200. _publish_rate:=500 _controler:="motor"
```

Other useful parameters:

-   **\--targetFitness=0** set a target for the fitness: if the target
    is reached, then stop.
-   **\--plotSRAutomaticPidTuningStat \--plotHisto**: generate a .xg
    file which you can plot with gnuplot.

### More options

To see all the options, you can run: ```
$ rosrun sr_automatic_pid_tuning sr_automatic_pid_tuning --help
```
