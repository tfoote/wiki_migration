## Software Requirements

The implementation of a scenario needs some additional packages that are
not included in the bringup level, be sure that you have installed in
your system the following stacks:

-   [arm_navigation](arm_navigation)
-   [cob_manipulation](cob_manipulation)
-   [cob_navigation](cob_navigation)
-   [cob_object_perception](cob_object_perception)

If you want to run the scenario in simulation you need also
[cob_simulation](cob_simulation)

## Usage/Examples

The package contains the source code of some generic states divided
into:

-   Basic states
-   Manipulation states
-   Perception states
-   Navigation states

Also you can find some basic state machines already created, you can
take a look of these machines as example to create a new scenario.

In the package [cob_experimentation_days](cob_experimentation_days) you
can see a complete definition of a scenario script using
[cob_generic_states](cob_generic_states).
