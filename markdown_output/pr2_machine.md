## Machine files

This package provides 2 files:

-   `pr2.machine` : defines the machines `c1` and `c2` to have the
    addresses `c1` and `c2`, respectively, which maps them to the
    PR2's computers.
-   `sim.machine` : defines the machines `c1` and `c2` to both
    have the address `localhost`. These files are intended to be
    included by [roslaunch](roslaunch) files. The intended usage is:
    ```
<include file="$(find pr2_machine)/$(env ROBOT).machine" />
``` The user sets the `ROBOT` environment
    variable to `pr2` when working with a physical PR2, and `sim`
    when working in simulation. In this way, [roslaunch](roslaunch)
    files that refer to machines `c1` and `c2` will distribute
    computation appropriately on the robot, but still work on a single
    machine in simulation (assuming that the single machine can support
    the processing requirements).
