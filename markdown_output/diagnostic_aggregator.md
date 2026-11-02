## Overview

The `diagnostic_aggregator` contains a ROS node, `aggregator_node`,
that listens to
[diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)
messages on the `/diagnostics` topic, processes and categorizes the
data, and republishes on `/diagnostics_agg`. The `aggregator_node`
loads "Analyzer" plugins to perform the diagnostics processing and
categorization. The configuration and setup for each diagnostic
aggregator is specific to each robot and can be determined by users or
developers.

The two analyzers in this package, `GenericAnalyzer` and
`AnalyzerGroup`, hold and categorize diagnostic messages. They're
useful for categorizing components or systems. They can warn when an
item is stale, but do not do additional analysis of the diagnostics.
Other analyzers can be loaded as plugins by the `aggregator_node` on
startup.

The aggregated diagnostic output can be displayed in the
[robot_monitor](robot_monitor) tool. The `robot_monitor` displays
these messages in a hierarchical format. To determine the hierarchy, the
diagnostic aggregator prepends diagnostic status names with a path,
joined with "/". For example:

`prosilica: Frequency Status` \&rarr; `My
Robot/Sensors/Prosilica/prosilica: Frequency Status`

### Example

This shows how an `aggregator_node` might categorize and analyze
diagnostics data from a simple robot.

If a robot had diagnostics from the motor drivers, SICK laser scanner,
Videre camera and a few batteries, the diagnostic input might have
status names: 

```
Left Wheel
Right Wheel
SICK Frequency
SICK Temperature
SICK Connection Status
Stereo Left Camera
Stereo Right Camera
Stereo Analysis
Stereo Connection Status
Battery 1 Level
Battery 2 Level
Battery 3 Level
Battery 4 Level
Voltage Status
```



Using the diagnostic aggregator, we can move these diagnostic messages
into easy to understand categories to display in our `robot_monitor`.
To do this, just prepend the name of the category to the status names,
and separate them with "/". 

```
My Robot/Wheels/Left
My Robot/Wheels/Right
My Robot/SICK/Frequency
My Robot/SICK/Temperature
My Robot/SICK/Connection Status
My Robot/Stereo/Left Camera
My Robot/Stereo/Right Camera
My Robot/Stereo/Analysis
My Robot/Stereo/Connection Status
My Robot/Power System/Battery 1 Level
My Robot/Power System/Battery 2 Level
My Robot/Power System/Battery 3 Level
My Robot/Power System/Battery 4 Level
My Robot/Power System/Voltage Status
```



Using the above input, the Robot Monitor will categorize the data as
follows: 

```
My Robot
  -- Wheels
    -- Left
    -- Right
  -- SICK
    -- etc ...
  -- Stereo
  -- Power System
```



## Analyzers

The `aggregator_node` will load analyzers to store and process the
diagnostic data. Each analyzer inherits from the base class
`diagnostic_aggregator::Analyzer`. Analyzers must be in packages that
depend directly on [pluginlib](https://index.ros.org/p/pluginlib) and
diagnostic_aggregator.

The base analyzer class is the pure virtual
[diagnostic_aggregator::Analyzer](CodeAPI:diagnostic_aggregator/html/classdiagnostic__aggregator_1_1Analyzer.html)
class. All derived classes must implement these methods:

- `init()` - Loads parameters
- `match()` - Returns true/false if interested in viewing a status
  message
- `analyze()` - Analyze a new message
- `report()` - Report results or state
- `getPath()` - Get complete path (anything prepended onto status
  names)
- `getName()` - Get nice name, like "Motors" or "Sensors"

Analyzers can choose the error state for any
[diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)
message they analyze and report. Generally, the "parent" of an
analyzer has an error state of the maximum of its children, but some
analyzers may have more advanced methods.

The analyzers are responsible for correctly setting the names of each
item they analyze. The `aggregator_node` does not do any checking or
enforcement of the diagnostic status name hierarchy.

### Creating an Analyzer

Users can create Analyzers to load as plugins for different robots. See
the tutorial
[Creating a Diagnostic Analyzer](https://index.ros.org/p/diagnostics)
for details.

## Configuring an Aggregator

For a full tutorial, see the tutorial
[Configuring a Robot's Diagnostic Aggregator](https://index.ros.org/p/diagnostics).

To set up the diagnostic analyzer on a robot, the aggregator is given
parameters that will configure the analyzers. These parameters, below,
are in the private namespace of the aggregator node.


```
pub_rate: 1.0 # Optional, defaults to 1.0
base_path: 'PRE' # Optional, defaults to ""
analyzers:
  motors:
    type: PR2MotorsAnalyzer
  joints:
    type: GenericAnalyzer
    path: 'Joints'
    regex: 'Joint*'
```

 Under each sub namespace under `analyzers`, a
different analyzer is configured. Analyzers can be robot specific, or
they can be general purpose ones like the `GenericAnalyzer`.

Each analyzer needs a special parameter, `type`, in the namespace. The
`type` parameter gives the `aggregator_node` the class name of the
`Analyzer`.

Any diagnostic item that isn't analyzed is analyzed by an "Other"
analyzer, and will still appear in the Robot Monitor. "Other" items,
or remainders, are removed from the diagnostics output after going stale
for 5 seconds.

The `pub_rate` parameter (publish rate of `/diagnostics_agg`) is
optional, and defaults to 1.0. The `base_path` is prepended to all
`/diagnostics_agg` output, and defaults to "" (empty string).

### Launching a Diagnostic Aggregator

To look for an example of an aggregator in use, look in the
"diagnostic_aggregator/demo" directory. Users specify each
`Analyzer` in the private parameter space of the `aggregator_node`,
then start the node. 

```xml
<node pkg="diagnostic_aggregator" type="aggregator_node"
      name="diag_agg" >
  <rosparam command="load" 
            file="$(find diagnostic_aggregator)/demo/pr2_analyzers.yaml" />
</node>
```



## Basic Analyzer Types

In the `diagnostic_aggregator` package, the two analyzer types
provided: `GenericAnalyzer` and `AnalyzerGroup`. The
`GenericAnalyzer` can be used to categorize and track stale items. The
`AnalyzerGroup` categorizes analyzers themselves, allowing users to
"sub-categorize" analyzers.

### GenericAnalyzer

The `GenericAnalyzer` class is useful for categorizing diagnostics
data. It's mostly used for a particular device or category, like a
Hokuyo node or EtherCAT devices. It can be configured to analyze almost
any set of diagnostics data.

For a full tutorial on the `GenericAnalyzer`, see
[Using the GenericAnalyzer](https://index.ros.org/p/diagnostics)

### AnalyzerGroup

The
[AnalyzerGroup](CodeAPI:diagnostic_aggregator/html/classdiagnostic__aggregator_1_1AnalyzerGroup.html)
can load a group of analyzers as a sub group. This can be useful for
analyzing a group of similar items, like 4 different cameras. The
`AnalyzerGroup` can use any type of analyzer as one of the
sub-analyzers.



```
type: AnalyzerGroup
path: Sensors
analyzers:
  base_hk:
    type: GenericAnalyzer
    path: Base Hokuyo
    startswith: base_hokuyo_node
    num_items: 3
  tilt_hk:
    type: GenericAnalyzer
    path: Tilt Hokuyo
    startswith: tilt_hokuyo_node
    num_items: 3
  imu:
    type: GenericAnalyzer
    path: IMU
    startswith: imu_node
    num_items: 3
```



The above example can analyze the instruments on a PR2. The
`AnalyzerGroup` uses the parameter `path` to prepend to all output
names. In the above example,

`tilt_hokuyo_node: Frequency Status` \&rarr; `Sensors/Tilt
Hokuyo/tilt_hokuyo_node: Frequency Status`.

All sub-analyzers should go under the `analyzers` namespace of the
`AnalyzerGroup`. They should be specified in the same way that any
diagnostic analyzer would be specified.

Note: The diagnostic aggregator uses the `AnalyzerGroup` internally,
which is why this is very similar to setting up a diagnostic aggregator.

### DiscardAnalyzer

The `DiscardAnalyzer` is a subclass of the `GenericAnalyzer`. It
will "match" any item that the `GenericAnalyzer` matches, but will
discard the items and not report it.

This is useful for removing a device from a robot, or when setting up a
non-standard robot configuration.

### IgnoreAnalyzer

The `IgnoreAnalyzer` will simply ignore all parameters in its
namespace, and not match or report anything.

The difference between this and the `DiscardAnalyzer` above is that
since the `IgnoreAnalyzer` doesn't match anything, anything that it
is ignoring will be reported in "Other". The `DiscardAnalyzer` will
suppress any output from anything that it matches.

## ROS API

### aggregator_node

Collects diagnostics, loads diagnostic analyzer plugins

#### Subscribed Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Raw diagnostics input

#### Published Topics

- `/diagnostics_agg`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Processed diagnostics output, at 1.0 Hz (default)
- `/diagnostics_toplevel_state`
  ([diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)):
  **New in Fuerte:** The toplevel status of /diagnostics_agg published
  with the same rate

#### Parameters

- `~pub_rate` (`double`, default: `1.0`): Rate diagnostics output
  published
- `~base_path` (`string`, default: `" " (empty string)`): Prepended to
  all diagnostics output (ex: "Robot")
- `~analyzers` (`{}`): Load diagnostics analyzers according to these
  params. Each analyzer is initialized in separate namespace.

### analyzer_loader

Loads diagnostic analyzers, verifies initialization OK. Used as
regression test.

#### Parameters

- `~analyzers` (`{}`): Same format as aggregator_node

## Examples and Applications

PR2 robots use the `aggregator_node` and the `robot_monitor` for
diagnostic display. The launch files in "pr2_bringup/pr2.launch"
contain the configuration file for the `aggregator_node`.

The "diagnostic_aggregator/demo" directory has an example of an
`aggregator_node` used for testing and demonstrations.

## Tutorials

- [Adding Analyzers at Runtime](https://index.ros.org/p/diagnostics):
  Use launch files or bonds and a service to add a new set of analyzers
  to the aggregator.
- [Configuring a Robot's Diagnostic Aggregator](https://index.ros.org/p/diagnostics):
  This tutorial will help you set up and configure a diagnostic
  aggregator, using the PR2 as an example. The Aggregator can be
  configured for a robot or type of robot to perform basic analysis on
  the diagnostics.
- [Creating a Diagnostic Analyzer](https://index.ros.org/p/diagnostics):
  An example of how to write your own diagnostic analyzer plug-in for
  the diagnostic_aggregator.
- [Using the GenericAnalyzer](https://index.ros.org/p/diagnostics): Uses
  the `GenericAnalyzer` to analyze diagnostics from EtherCAT devices,
  hardware drivers and robot computers. Shows the complete feature set
  of the `GenericAnalyzer`.

## Troubleshooting

### Errors from diagnostic_aggregator

#### Error: Analyzer fails to load

The `aggregator_node` loads diagnostic analyzers to collect and
analyze diagnostics. These are loaded as plugins. If they fail to load,
you may see:

- An error in the `robot_monitor`, describing the initialization
  failure.
- An error in the ROS console, saying "Analyzer failed to load", or
  "Analyzer failed to initialize"

Analyzers are loaded at startup by the `aggregator_node`. Check your
robot's launch file for a node in package `diagnostic_aggregator`,
type `aggregator_node'. 

```
<node pkg="diagnostic_aggregator" type="aggregator_node"
      name="diagnostic_aggregator" >
  <rosparam command="load" 
            file="$(find some_pkg)/my_analyzers.yaml" />
</node>
```

 The first thing to do
is check the "some_pkg/my_analyzers.yaml" file and make sure it loads.
Make a new launch file "analyzer_load_test.launch"


```
<launch>
  <test pkg="diagnostic_aggregator" type="analyzer_loader"
        name="analyzer_load_test" >
    <rosparam command="load" test-name="load_test"
              file="$(find some_pkg)/my_analyzers.yaml" />
  </node>
</launch>
```

 Use [rostest](https://index.ros.org/p/rostest)
to launch it. 

```
rostest analyzer_load_test.launch
```

 If that passes, you should be OK,
and you may have discovered a bug in the `aggregator_node`.

If that doens't pass, use [rospack](https://index.ros.org/p/rospack) to
find all diagnostic analyzer plugins. 

```
$ rospack plugins --attrib=plugin diagnostic_aggregator
```

 Compare
the list from rospack with the YAML configuration file of the
aggregator. The YAML file should look like this:


```
analyzers:
  motors:
    type: GenericAnalyzer
    path: Motors
    startswith: EtherCAT
  power:
    type: GenericAnalyzer
    path: Power System
    contains: Battery
```

 Each parameter `type` gives a different class
of analyzer to load. Make sure every value for `type` is a valid
plugin. 

```
$ rospack plugins --attrib=plugin diagnostic_aggregator | grep GenericAnalyzer
```



Make sure that all the plugins are built. Check the packages and
dependencies and use [rosmake](https://index.ros.org/p/rosmake) to
rebuild if necessary.

Check the dependencies of the plugin packages. Each package containing
plugins should depend directly on
[pluginlib](https://index.ros.org/p/pluginlib) and
diagnostic_aggregator.
