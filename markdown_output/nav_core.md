## Overview

The \`nav_core\` package contains key interfaces for the navigation
stack. All planners and recovery behaviors that wish to be used as
[ plugins](pluginlib ) in the [move_base](move_base) node must adhere to
these interfaces.

![](attachment:move_base_interfaces.png)

## BaseGlobalPlanner

The \`nav_core::BaseGlobalPlanner\` provides an interface for global
planners used in navigation. All global planners written as plugins for
the [move_base](move_base) node must adhere to this interface. Current
global planners using the \`nav_core::BaseGlobalPlanner\` interface are:

-   [global_planner](global_planner) - A fast, interpolated global
    planner built as a more flexible replacement to navfn. (pluginlib
    name: \"global_planner/GlobalPlanner\")
-   [navfn](navfn) - A grid-based global planner that uses a navigation
    function to compute a path for a robot. (pluginlib name:
    \"navfn/NavfnROS\")
-   [carrot_planner](carrot_planner) - A simple global planner that
    takes a user-specified goal point and attempts to move the robot as
    close to it as possible, even when that goal point is in an
    obstacle. (pluginlib name: \"carrot_planner/CarrotPlanner\")

### API Stability

-   The C++ API is stable.

### BaseGlobalPlanner C++ API

Documentation on the C++ API for the \`nav_core::BaseGlobalPlanner\` can
be found here:
[ BaseGlobalPlanner documentation](http://www.ros.org/doc/api/nav_core/html/classnav__core_1_1BaseGlobalPlanner.html ).

## BaseLocalPlanner

The \`nav_core::BaseLocalPlanner\` provides an interface for local
planners used in navigation. All local planners written as plugins for
the [move_base](move_base) node must adhere to this interface. Current
local planners using the \`nav_core::BaseLocalPlanner\` interface are:

-   [base_local_planner](base_local_planner) - Provides implementations
    of the Dynamic Window Approach(DWA)and Trajectory Rollout approaches
    to local control
-   [dwa_local_planner](dwa_local_planner) - Modular DWA implementation
    with a lot cleaner and easier interface to understand and more
    flexible y axis variables for holonomic robots than
    [base_local_planner](base_local_planner)\'s DWA
-   [eband_local_planner](eband_local_planner) - Implements the Elastic
    Band method on the SE2 manifold
-   [teb_local_planner](teb_local_planner) - Implements the
    Timed-Elastic-Band method for online trajectory optimization
-   [mpc_local_planner](mpc_local_planner) - Provides several model
    predictive control approaches embedded in the SE2 manifold

### API Stability

-   The C++ API is stable.

### BaseLocalPlanner C++ API

Documentation on the C++ API for the \`nav_core::BaseLocalPlanner\` can
be found here:
[ BaseLocalPlanner documentation](http://www.ros.org/doc/api/nav_core/html/classnav__core_1_1BaseLocalPlanner.html ).

## RecoveryBehavior

The \`nav_core::RecoveryBehavior\` provides an interface for recovery
behaviors used in navigation. All recovery behaviors written as plugins
for the [move_base](move_base) node must adhere to this interface.
Current recovery behaviors using the \`nav_core::RecoveryBehavior\`
interface are:

-   [clear_costmap_recovery](clear_costmap_recovery) - A recovery
    behavior that reverts the costmaps used by [move_base](move_base) to
    the static map outside of a user-specified range
-   [rotate_recovery](rotate_recovery) - A recovery behavior that
    perfroms a 360 degree rotation of the robot to attempt to clear out
    space.

### API Stability

-   The C++ API is stable.

### RecoveryBehavior C++ API

Documentation on the C++ API for the \`nav_core::RecoveryBehavior\` can
be found here:
[ RecoveryBehavior Documentation](http://www.ros.org/doc/api/nav_core/html/classnav__core_1_1RecoveryBehavior.html )
