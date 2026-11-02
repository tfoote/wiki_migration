## Overview

This package contains methods for filtering robot trajectories. These
filters are focused on the needs of industrial robots and applications.

## Filters

### uniform_sample_filter

Re-samples a planned trajectory with a uniform time step in between
points. Re-sampling is done using a higher order spline smoother in
joint space. The filter expects fully defined trajectories (position,
velocity, acceleration).

#### Parameters

- `sample_duration` (`float`): step size in seconds between way-points.

### n_point_filter

Reduces trajectory to be <=N total points. This reduction process uses
existing points (re-sampling and interpolation are not done). This
filter works best with a uniformly sampled trajectory, but this is not
required. If the trajectory is less than N points, no filtering is
performed.

#### Parameters

- `n_points` (`float`): maximum number of waypoints (must be >=2)

## Applying Filters

{ }}}} {}

## Tutorials

For more detailed examples see the
[tutorials](#tutorials-1)
page.

## Contact us/Technical support

For questions about this package or ROS-Industrial in general, please
contact the developers by posting a message in the
[ROS-Industrial category](https://discourse.ros.org/c/ros-industrial) on
ROS Discourse.

## Reporting bugs

## Tutorials

The following are Industrial Trajectory Filter specific tutorials:

- [Converting arm navigation trajectory filters into MoveIt Planning Request Adapters](#converting-arm-navigation-trajectory-filters-into-moveit-planning-request-adapters):
  This tutorial describes how to convert an
  [Arm Navigation](arm_navigation) *Trajectory Filter Plugin* into a
  MoveIt *Planning Request Adapter* that can be compiled in a catkin
  package. **(<=Groovy)**
- [Developing a Planning Request Adapter](#developing-a-planning-request-adapter):
  This tutorial is a step by step development of a planning request
  adapter using a simple smoothing filter as an example
- [Using a planning adapter inside of MoveIt.](#using-a-planning-adapter-inside-of-moveit):
  This tutorial will show you how to use a planning request adapter with
  !MoveIt.

Tutorials for using trajectory filters with Arm Navigation (deprecated
in Groovy, unsupported in Hydro and later):

- [Utilizing Trajectory Filters with a Generated Arm Navigation Package](#utilizing-trajectory-filters-with-a-generated-arm-navigation-package):
  Gives an overview of the common industrial trajectory filters and
  shows how to apply them to an auto-generated arm navigation package



```wiki

```

## Converting arm navigation trajectory filters into MoveIt Planning Request Adapters

```wiki
Arm navigation has been deprecated in the ROS Groovy release and removed in ROS Hydro.
```



- **Description:** This tutorial describes how to convert an
  [Arm Navigation](arm_navigation) *Trajectory Filter Plugin* into a
  MoveIt *Planning Request Adapter* that can be compiled in a catkin
  package. **(<=Groovy)**
- **Keywords:** trajectory, filters, plugin, path, adapter
- **Tutorial Level:** ADVANCED
- **Next Tutorial:**
  [Developing a Planning Request Adapter in MoveIt!](#developing-a-planning-request-adapter)

This tutorial will guide you through the process of taking a legacy
[Arm Navigation](arm_navigation) *trajectory filter* and converting into
a *Planning Request Adapter* that can be used within MoveIt. These
filter's are usually used to check that a robot's path avoids some
sort of constraint.

The following instructions are based on the process of converting the
[Arm Navigation](arm_navigation) Filter Base interface (the interface
for an arm *trajectory filters*) into a *Planning Request Adapter* that
is used by MoveIt. The arm trajectory base filter class can be located
here:
`/industrial_trajectory_filters/include/industrial_trajectory_filters/filter_base.h`
Since this version of the Filter Base class only provides some degree of
backwards compatibility with the original
[Arm Navigation](arm_navigation) interface, some parts of the original
[Arm Navigation](arm_navigation) filter code must be modified in order
to accommodate the differences introduced by the new adapter interface
class.

Every arm trajectory filter implements two pure virtual methods called
`update()` and `configure()`. The update method is where the bulk of
the trajectory filter computation is completed and update is where
configuration changes to the filter are made. Our goal is to simply shim
these two methods into our new planning adapter for MoveIt. Each filter
also has a `type` and `name` getter method that simple return
descriptive strings that should alos remain in place.

All the `getParam()` methods for parameter lookup are not supported by
the new Filter Base interface and so the filter implementation must be
modified so that parameters are read using the regular roscpp parameter
API (either through the node handle or the bare version)

A `MessageAdapter` structure has been provided in order to replace the
[Arm Navigation](arm_navigation) message with which the original
template interface was specialized.

### Configuring the Package Configuration XML File

The following dependencies must be added to the `package.xml` file in
the catkin package that contains your filter implementation. Our new
planning request adapter will talk using trajectory messages so we will
need both to build against and run the package with trajectory messages.
To bring in the MoveIt planning request adapter templates we will need
MoveIt and core and planning. We also need to bring in the old
trajectory filters and finally the plugin library. Finally, at the end
of the package file we need insert an export directive to tell ROS to
roll our new adapter into a plugin.



```highlight
  <build_depend>trajectory_msgs</build_depend>
  <build_depend>pluginlib</build_depend>
  <build_depend>moveit_core</build_depend>
  <build_depend>moveit_ros_planning</build_depend>
  <build_depend>industrial_trajectory_filters</build_depend>

  <run_depend>trajectory_msgs</run_depend>
  <run_depend>pluginlib</run_depend>
  <run_depend>moveit_core</run_depend>
  <run_depend>moveit_ros_planning</run_depend>
  <run_depend>industrial_trajectory_filters</run_depend>

  <export>
    <moveit_core 
      plugin="${prefix}/planning_request_adapters_plugin_description.xml"/> 
  </export>
```



### Create description file for your plugin

Create a `planning_request_adapters_plugin_description.xml` file in
your package directory and fill it with the following information:


```highlight
<library path="libmyplugin_package">
  <class name="my_filter_package/MyFilter"
    type="my_filter_package::MyFilterAdapter"
    base_class_type="planning_request_adapter::PlanningRequestAdapter">
    <description>
      This is my trajectory filter plugin
    </description>
  </class>
</library>
```



### Configure CMakeLists.txt

a\. Add package dependencies 

```highlight
find_package(catkin REQUIRED COMPONENTS moveit_ros_planning trajectory_msgs industrial_trajectory_filters)
```



a\. Include location of your package's header files


```highlight
include_directories(include ${catkin_INCLUDE_DIRS})
```



a\. Build plugin library 

```highlight
add_library(moveit_trajectory_filter_plugins src/my_filter.cpp)
target_link_libraries( moveit_trajectory_filter_plugins ${catkin_LIBRARIES})
```



a\. Make plugin library available to other packages


```highlight
catkin_package(
  CATKIN_DEPENDS moveit_ros_planning trajectory_msgs
  INCLUDE_DIRS include
  LIBRARIES moveit_trajectory_filter_plugins
)
```



### Modifying trajectory filter into a Planning Request Adapter

These changes are to be applied to your filter code.

a\. Remove all [Arm Navigation](arm_navigation) header files from the
source and header files of your original Trajectory Filter
implementation. None of the [Arm Navigation](arm_navigation) files can
be included in a catkin package and so they must be removed.

a\. Remove all header files that belong to a rosbuild only packages.
Catkin packages can not link against dependencies that live in a
rosbuild packages.

a\. Include the `industrial_trajectory_filters/filter_base.h` header
file in your own filter's header file.

a\. In your filter implementation, replace the base class
`filters::FilterBase<T>` with
`industrial_trajectory_filters::FilterBase<T>`.

a\. Remove all calls to the `getParam()` methods from the old
[FilterBase](http://ros.org/doc/groovy/api/filters/html/classfilters_1_1FilterBase.html)
class and instead use the roscpp parameter interface for any parameter
lookup tasks.

a\. In your filter's header file, declare a `typedef` that
specializes your filter template implementation to a version that uses
the `MessageAdapter` structure. For instance, if we are converting a
`MyFilter` class then we would add the following after the class
declaration: 

```highlight
typedef MyFilter<MessageAdapter> MyFilterAdapter;
```



- NOTE: In case the `MessageAdapter` structure does not fit the
  expected template class, then the filter's implementation must
  provide its own adapter structure that resembles the necessary parts
  of the expected [Arm Navigation](arm_navigation) message type. The
  specialization of such filter would then pass the custom adapter
  structure in the template argument list as follows:



```highlight
typedef MyFilter<CustomMessageAdapter> MyFilterAdapter;
```



a\. In your filter's source file, remove the plugin declaration
`PLUGINLIB_DECLARE_CLASS` and add the class loader macro. In the case
of our `MyFilter` class, this would be done by placing the following
line outside your class: 

```highlight
CLASS_LOADER_REGISTER_CLASS(my_filter_package::MyFilterAdapter, planning_request_adapter::PlanningRequestAdapter);
```



At this point you may compile your code in order to create the plugin.

- NOTE: The `adaptAndPlan(\...)` method in the Filter Base already
  maps the trajectory data between the `MessageAdapter` structure and
  the MoveIt planning interface objects passed in the argument list. The
  filter's implementation should override this method whenever a custom
  adapter structure is used or when additional functionality is needed.

a\. In order to see an example look at the implementation of the
`industrial_trajectory_filters/src/n_point_filter.cpp` planning
request adapter.

Once your planning request adapter compiles you can test its
functionality inside of MoveIt.
[This tutorial](http://wiki.ros.org/industrial_trajectory_filters/Tutorials/filters_inside_moveit)
will guide you through the steps.

## Developing a Planning Request Adapter

- **Description:** This tutorial is a step by step development of a
  planning request adapter using a simple smoothing filter as an example
- **Tutorial Level:** ADVANCED
- **Next Tutorial:**
  [Using a planning adapter inside of MoveIt](#using-a-planning-adapter-inside-of-moveit)

### Overview

The industrial_trajectory_filters package in the industrial_core
repository generally contains filters which were adapted from the arm
navigation package which is a precursor to MoveIt!. Prior tutorials
explained how to convert these older packages into planning adapter
plugins. However this tutorial will explain the details of creating a
planning adapter plugin. The tutorial uses a simple smoothing filter as
an example to explain the concepts.

### Required Matrials

A checked out copy of the industrial_core repository within a catkin
work space such that it compiles. All the code is contained in the
"industrial_trajectory_filters" package. Two other files are necessary
to install the filter. First, the ompl_planning_pipeline.launch file
needs to be modified to include the plugin in the pipeline. Next, a yaml
file defining the filter coefficients needs to be created and loaded as
part of the launch.

### Files of Interest

. industrial_trajectory_filters . CMakeLists.txt .
include/industrial_trjectory_filters/smoothing_trajectory_filter.h .
src/smoothing_trajectory_filter.cpp . src/add_smoothing_filter.cpp .
planning_request_adapters_plugin_description.xml . Launch file usually
ompl_planning_pipeline.launch . Yaml file defining the filter
coefficients

### The Plugin

MoveIt! uses 6 different kinds of plugins to perform a variety of
functions. The specific plugin is determined by the launch file.
Typically a ROS parameter is set telling the ROS node which of the
available plugins to use. The 6 types are:

1\. planning_interface::PlannerManager 1. kinematics::KinematicsBase 1.
move_group::MoveGroupCapability 1.
occupancy_map_monitor::OccupancyMapUpdater 1. rviz::Display 1.
planning_request_adapter::PlanningRequestAdapter

Implementation of any one of these plugins requires the following steps

1\. Create a class which inherits from one of the above classes 1.
Implement all of the necessary functions of that class 1. Load and
Register your class at the bottom of the class.cpp file a.
CLASS_LOADER_REGISTER_CLASS(your_class_name,base_class_name) 1. Modify
the xml file which tells the plugin loader about your plugin 1. Modify
the CMakeLists.txt file so that your plugin is added to the library.

### Creation of the Plugin Class

In this example we created the file "add_smoothing_filter.cpp" which
inherits from "PlanningRequestAdapter." It therefore has to implement
the following functions:

1\. A constructor with no parameters 1. std::string getDescription()
which returns a string describing the plugin 1. bool adaptAndPlan()
which has very unique expectations 1. bool init() An Optional method

Our parameter-less constructor retrieves filter values from the ROS
parameter server. The smoothing filter simply replaces every point/state
in a robot trajectory with a weighted average of the surrounding points.
This type of smoothing filter has advantages over finite impulse or
infinite impulse response filters because it does not introduce phase
lag. Don't worry if you are not familiar with filter design. It is
enough to understand that it smooths out the trajectory while not
causing significant deviation from the path. OMPL planners are sample
based. They tend to produce trajectories which are not smooth,
especially as they attempt to negotiate obstacles. Typically a smoothing
filter for our application will have symmetric coefficients which are
large in the middle and decrease toward the ends. It is necessary to
have an odd number of coefficients. The default filter has 5
coefficients \[ 0.25 0.5 1.0 0.5 0.25\] which is both odd and symmetric.

#### Defining an arbitrary smoothing filter using ROS parameters

The constructor looks first for the following parameter:
"/move_group/smoothing_filter_name" It then uses this base name to
load the filter coefficients.

A valid smoothing_filter.yaml file looks like this



```
smoothing_filter_name: /move_group/smoothing_5_coef
smoothing_5_coef:
       - 0.25
       - 0.50
       - 1.00
       - 0.50
       - 0.25
```

 These coefficients are added to a vector of
doubles and define the filter. Changing the values changes the degree of
smoothing. Generally more coefficients with thicker tails increases the
degree to which the robot cuts corners of the original trajectory. One
must load the yaml file somewhere in your launch scripts. For example,
one might add the following lines to their ompl_planning_pipeline.launch
file.



```
<rosparam command="load" file="$(find moveit_config)/config/smoothing_filter_params.yaml"/>
```

 The constructor then initializes the filter
with these coefficients.



```
if(!smoothing_filter_->Init(filter_coef_))
```



#### getDescription()

This member function has an obvious purpose and simple implementation.

#### adaptAndPlan()

The adapt and plan function has very special requirements because of the
way in which it is used by the planning pipeline. Adpaters are chained
together so that calling the top of the chain calls all of the adapters
in the chain. In order for the calling chain to work, each adapter must
call the PlannerFn (planner function) provided in the signature. Some
planning adapter plugins perform work prior to executing the planner,
some perform work after, and some do both. Regardless, they must call
the planner function passing along all the necessary parameters. For
example, our plugin post-processes the trajectory, so it calls the
planner prior to doing anything as follows:



```
bool result = planner(planning_scene,req,res);
```

 If the results are good, it then post processes
the resulting trajectory using the filter object as follows:



```
smoothing_filter_->applyFilter(*res.trajectory_);
```

 Any planning request adapter that adds new
waypoints to the trajectory must also keep track of the indices of the
additional points. These are returned as the last parameter as a vector
of indices. Our filter does not add any new points.

#### The smoothing filter: the plugin's workhorse

The smoothing filter is quite simple, it's applyfilter() method goes
through the way points in the robot trajectory one by one, replacing
each one with the weighted average of the adjacent points. However, it
must do some special math at the beginning and end where no adjacent
points exists. To handle the end cases we artificially generate the
required adjacent points in such a way as to continue the slope.

One should also note that the trajectory of each joint is processed
independently. Therefore, the body of the code has two nested for loops:



```
1.  for(int i=0; i<num_states; i++){
 2.  for(int j=1; j<num_points-1; j++){
```

 Within these loops, a new trajectory is
computed using the coefficients as weights. Neither the first nor the
last point is adjusted since these were the start and goal. One should
also note how the original trajectory points are read into the vector
"xv" so that they may be modified in place. With each iteration, the
vector "xv" is shifted using the following lines of code:



```
for(int k=0; k<num_coef_-1; k++){
      xv[k] = xv[k+1];
}
```

 The modified value computed as the weighted sum
of adjacent values is stored using the command.

` rob_trajectory.getWayPointPtr(j)->setVariablePosition(i,sum/gain_); `

At the bottom of this file is call to a macro which must be called by
all plugins.



```
CLASS_LOADER_REGISTER_CLASS(industrial_trajectory_filters::AddSmoothingFilter,
                            planning_request_adapter::PlanningRequestAdapter);
```



### Adding the filter to the xml file which defines the available plugins

The file "planning_request_adapters_plugin_description.xml" should
contain an entry for your newly created plugin similar to the following:



```
<class   name="default_planner_request_adapters/AddFIRFilter“type="default_planner_request_adapters::AddFIRFilter" base_class_type="planning_request_adapter::PlanningRequestAdapter"> <description> </description> </class>
```

## Using a planning adapter inside of MoveIt.

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Converting Arm Navigation trajectory filters into MoveIt Planning Request Adapters](#converting-arm-navigation-trajectory-filters-into-moveit-planning-request-adapters).
- **Description:** This tutorial will show you how to use a planning
  request adapter with !MoveIt.
- **Keywords:** Trajectory Filter MoveIt Arm Planning
- **Tutorial Level:** ADVANCED

This tutorial will teach you how to use an industrial trajectory filter
that was converted into a planning adapter inside of MoveIt.

### Planning Request Adapter - General Use

In order to use your new Planning Request Adapter inside a MoveIt
generated package do the following:

1\. Open the `ompl_planning_pipeline.launch` file of the MoveIt
package for your robot and add your filter to the beginning of the
`planning_adapters` list as follows: 

```highlight
<arg name="planning_adapters" value="
    my_filter_package/MyFilter
    default_planner_request_adapters/AddTimeParameterization
    default_planner_request_adapters/FixWorkspaceBounds
    default_planner_request_adapters/FixStartStateBounds
    default_planner_request_adapters/FixStartStateCollision
    default_planner_request_adapters/FixStartStatePathConstraints" />
```



1\. In the same launch file, declare any ros parameters used by your
filter as shown below:



```highlight
<param name="my_filter_parameter" value="40" />
```



1\. At this point you can now use the filter. Run `demo.launch` from
your MoveIt generated package and create path plans using the
`MovePlanningPlugin` in RViz. If your filter prints to `stdout`,
then you should see the output from it right after you generate a path.

### Example

The following section illustrates a specific example of using the
uniform sample filter from the
industrial_trajectory_filters
package.

1\. Following the steps above `ompl_planning_pipeline.launch` file
should be modified to match the following (original taken from
motoman_sia20d_moveit_config package):



```highlight
<launch>

  <!-- OMPL Plugin for MoveIt! -->
  <arg name="planning_plugin" value="ompl_interface/OMPLPlanner" />

  <!-- The request adapters (plugins) used when planning with OMPL. 
       ORDER MATTERS -->
  <arg name="planning_adapters" value="industrial_trajectory_filters/UniformSampleFilter
default_planner_request_adapters/AddTimeParameterization
				       default_planner_request_adapters/FixWorkspaceBounds
				       default_planner_request_adapters/FixStartStateBounds
				       default_planner_request_adapters/FixStartStateCollision
				       default_planner_request_adapters/FixStartStatePathConstraints" />

  <arg name="start_state_max_bounds_error" value="0.1" />

  <param name="planning_plugin" value="$(arg planning_plugin)" />
  <param name="request_adapters" value="$(arg planning_adapters)" />
  <param name="start_state_max_bounds_error" value="$(arg start_state_max_bounds_error)" />
  <param name="sample_duration" value="0.2"/>

  <rosparam command="load" file="$(find motoman_sia20d_moveit_config)/config/ompl_planning.yaml"/>

</launch>
```



Two modifications were made to the file:

- Added `industrial_trajectory_filters/UniformSampleFilter` to the
  `planning_adapters` list parameter. By adding this filter to the
  **beginning** of the list, we ensure that it is the **last** filter to
  be applied. This happens because the list is used for pre-processing
  trajectories (before planning), in which case the list is executed in
  order, and post-processing (after planning), in which case the list is
  executed in reverse order.
- Added `<param name="sample_duration" value="0.2"/>` as a
  filter parameter. The parameter name is specific to each filter
  (documented
  [here](http://wiki.ros.org/industrial_trajectory_filters#Parameters)),
  in this case `sample_duration` controls the desired time between
  waypoints after the filter is applied.

## Utilizing Trajectory Filters with a Generated Arm Navigation Package

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Creating an Arm Navigation Package for an Industrial Robot](Tutorials/Create_a_Arm_Nav_Pkg_for_an_Industrial_Robot).
- **Description:** Gives an overview of the common industrial trajectory
  filters and shows how to apply them to an auto-generated arm
  navigation package
- **Tutorial Level:** INTERMEDIATE

In this tutorial we will give an overview of the more common industrial
trajectory filters. We will then show how to apply the filters to an
existing auto generated arm navigation package.

### Common Industrial Trajectory Filters

Most industrial interfaces work best with uniformly sampled (equally
space way-points) trajectories with as few points as possible. The
trajectories generated by most ROS planners and smoothers are neither
uniform nor sparse. The industrial trajectory filters correct ROS
trajectories by first uniformly sampling the
trajectory(uniform_sample_filter) and then reducing them to N
points(n_point_filter).

### Using Industrial Filters in an Arm Navigation Package

In the
[previous tutorial](Tutorials/Create_a_Arm_Nav_Pkg_for_an_Industrial_Robot),
an arm navigation package was generated to control your robot. The
generated package includes several launch files that are used for
launching a system. Be default the generic trajectory filter chain is
used, but as was discussed previously this can be problematic for real
industrial systems. The following procedure demonstrates how to use
custom filter chains: 1. Edit trajectory_filter_server.launch
(substitute <my_robot_pkg> with your robot package name:


```
change: <rosparam command="load" file="$(find trajectory_filter_server)/config/filters.yaml" />
  to: <rosparam command="load" file="$(find <my_robot_pkg>)/config/filters.yaml" />
```

 1. Verify the change has been correctly made by
launching the following (it should fail and complain about a missing
filters.yaml file): 

```
roslaunch <my_robot_pkg> <my_robot_pkg>_planning_environment
```

 1. Add the desired
trajectory filter file (see example below) to
<my_robot_pkg>/config/filters.yaml 

```
service_type: FilterJointTrajectoryWithConstraints
  filter_chain:
  # Use of the parabolic spline smoother is recommended
  # Cubic spline shortcutter would fail for fast moves (i.e. low number of points
    -
      name: parabolic_smoother
      type: IterativeParabolicSmootherFilterJointTrajectoryWithConstraints
  # Uniformly sample motion (creates smooth motion on controller)
    -
      name: uniform_sample_filter
      type: IndustrialUniformSampleFilterJointTrajectoryWithConstraints
      params: {sample_duration: 0.010}
  # Limit the number of points sent to the controller
    -
      name: n_point_filter
      type: IndustrialNPointFilterJointTrajectoryWithConstraints
      params: {n_points: 10}
```

 1. Launch
your robot using: 

```
roslaunch <my_robot_pkg> <my_robot_pkg>_planning_environment
```

 1. Use the arm warehouse
visualizer (in rviz) to plan and filters trajectories. The filtered
trajectories should be uniform and limited to <N points if the filters
are working correctly.
