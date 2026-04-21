## Overview

The **vigir_step_control** provides a step queue management system and a
state machine to keep track of current step plan execution. It is able
to feed the low-level motion layer with the proper number of steps
required for seamless execution while continuously merging incoming step
plans provided by the [footstep planner](vigir_footstep_planning). This
allows even for continuous walking using our
[footstep planning](vigir_footstep_planning) stack. This package
provides following features:

-   Step Queue Management:
-   Seamless updates, merges, and stitches of multiple step plans
-   Convenient step spooler
-   Easy integration:
-   Pre-implemented state machine simplifies deployment
-   Comprehensive interface plugin as conveyor between footstep planning
    and motion execution layer

For detailed information about the system please take a look at the
[tutorial page](vigir_step_control/Tutorials/SystemOverview).

## Getting Started

### Installation

The **vigir_step_control** packages can be downloaded from Git``Hub:

-   <https://github.com/team-vigir/vigir_step_control.git> Furthermore
    you may need to download the dependencies as well (if not already
    done):
-   <https://github.com/team-vigir/vigir_pluginlib.git>
-   <https://github.com/team-vigir/vigir_footstep_planning_msgs.git>
-   <https://github.com/team-vigir/vigir_footstep_planning_basics.git>
    After a recompile of you workspace everything should be ready to
    use.

### Example Startup

In order to run this example. you will need to install the
[vigir_footstep_planning](vigir_footstep_planning) stack as well. An
install instruction can be found
[here](vigir_footstep_planning#installation).

After compiled your workspace you start up the system (each line in a
seperate terminal): ```
roscore
roslaunch vigir_footstep_planning footstep_planner_test.launch
roslaunch vigir_step_control step_controller_test.launch
roslaunch vigir_footstep_planning step_interface_rqt.launch
```

In the *step_interface_widget* you have first to select a footstep
planner parameter set. Afterwards the direction commands become
available which allows to generate simple pattern of footsteps. As soon
a footstep plan has been generated the *Execute* button becomes active
as well. When you click on this button the previously generated
footsteps will be executed virtually by the `StepControllerTestPlugin`
which fakes an footstep execution. During the fake execution, you will
be able to follow the fake execution in the *step_interface_widget* by
the progress bar.

**Note:** If you would like to see the system running with a real robot,
then you can get in touch with it using the THORMANG3 in simulation. The
full install instruction can be found
[here](vigir_footstep_planning#thormang3_demo).

## Tutorial

**A Tutorial will be added step by step
[here](vigir_step_control/Tutorials) soon. In the meantime feel free to
contact us, if you have further questions!**

## Sample Applications

### THORMANG3

The THORMANG3 provides a nice real world example how to migrate the
software into an exisiting setup
[here](https://github.com/thor-mang/ROBOTIS-THORMANG-MPC/tree/indigo-devel/thormang3_step_control_module).

During the Humanoids@Robo``Cup Demo 2016 at Leipzig, the step
controller was used.
[Youtube](https://www.youtube.com/watch?v=uoyYznea0Pk)

#### THORMANG3 Demo

If you would like to try it out in simulation by yourself, then just
follow the instructions [here](vigir_footstep_planning#thormang3_demo).
