## Overview

The parallel_quickstep library is a more or less port of
[physics_ode/ODE](physics_ode/ODE)\'s [quickstep](physics_ode/ODE)
method to the GPU, providing implementations in CUDA, OpenCL and OpenMP.

The approach operates by dividing the constraints into batches, where
each batch contains as few as possible redundant bodies. At each
iteration in the solver, constraints within a batch are operated on in
parallel, and batches are operated on serially. Several batching
strategies are provided, as well as several reduction strategies for
accumulating body accelerations for bodies involved with multiple
constraints in a given batch. The typical number of batches is 4 to 5,
though that is both configurable and dependent on the size of the
simulation.

## Usage

The package can be used either as a standalone library with ODE, or
directly with [Gazebo](gazebo)

The API is similar to that of ODE\'s quickstep, exposing the method
dWorldParallelQuickStep which can be used just as with dWorldQuickStep.

By default, the released version of parallel_quickstep is compiled with
CPU support only. To enable dWorldParallelQuickStep with CUDA, please
follow these steps: 1. Install CUDA on your system. 1. Checkout and
install [simulator_gazebo](simulator_gazebo) from source,

-   Easiest way is to use the [rosinstall tool](rosinstall), install it
    following instructions on the [rosinstall wiki](rosinstall).
-   Download
    [simulator rosinstall file](attachment:simulator.rosinstall) in your
    home directory, and run ```
rosinstall ~/diamondback_simulator ~/simulator.rosinstall
```
-   Rebuild simulator_gazebo stack, if you have previously checked out
    gazebo or parallel_quickstep locally, make sure to do a \`\`make
    clean\`\` first: ```
roscd gazebo
make clean
roscd parallel_quickstep
make clean
rosmake simulator_gazebo
``` During recompilation of
    [parallel_quickstep](parallel_quickstep), if CUDA is installed
    correctly on your system, cmake scripts in parallel_quickstep should
    detect it automatically. You should see cmake output on the console
    similar to: ```
...
-- CUDA Found, compiling with CUDA support
-- using sm_10 without DOUBLE_SUPPORT_ENABLED and ATOMIC_SUPPORT_ENABLED
-- CUDA Target Architecture: sm_10
...
```
-   Add the line (or modify as) \<stepType\>parallel_quick\</stepType\>
    to your Gazebo world file
-   Launch the world 1. Alternatively, you can configure the package for
    use with either CUDA, OpenCL or OpenMP directly in the base
    \`CMakeLists.txt\` file. Note that this will require the relevant
    libraries for each implementation, which at this time are not
    necessarily provided by ROS. For instance, for CUDA you will need
    NVIDIA\'s CUDA Toolkit, and for OpenCL you will need a supported
    driver.
