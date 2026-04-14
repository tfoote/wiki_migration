The node manages script addition, removal and execution. It also
provides an information retrieval interface for available scripts and
some useful details about each script.

# Example script

Suppose we have a node that publishes current CPU usage to the
\'\'\'/cpu\'\'\' topic. Each message contains an array named
\'\'\'cores\'\'\' with usage information for each core. We also have a
topic with configuration information: \'\'\'/config\'\'\'.

Now we will create a simple script which will warn about high cpu usage.

## Predicate

```python
#! type predicate
#! name cpu_monitor
#! interval 1
#! hardware_id lab_pc_1
#! fail warn
core1 = {/cpu/cores[0:1]}
core2 = {/cpu/cores[1:2]}
core3 = {/cpu/cores[2:3]}
core4 = {/cpu/cores[3:4]}
cpu_th = {/config/cpu_threshold}
core_th = {/config/core_threshold}
average = (core1 + core2 + core3 + core4) / 4.0
average < cpu_th
core1 < core_th
core2 < core_th
core3 < core_th
core4 < core_th
```

## Python

```python
#! name cpu_monitor
#! interval 1
#! hardware_id lab_pc_1
#! fail warn
core1 = topic("/cpu/cores[0:1]")
core2 = topic("/cpu/cores[1:2]")
core3 = topic("/cpu/cores[2:3]")
core4 = topic("/cpu/cores[3:4]")
cpu_th = topic("/config/cpu_threshold")
core_th = topic("/config/core_threshold")
average = (core1 + core2 + core3 + core4) / 4.0
validate.is_true(average < cpu_th, "Cpu usage too high")
validate.is_true(core1 < core_th, "core1 usage too high")
validate.is_true(core2 < core_th, "core2 usage too high")
validate.is_true(core3 < core_th, "core3 usage too high")
validate.is_true(core4 < core_th, "core4 usage too high")
```

You can activate the script using rqt plugin -
<http://wiki.ros.org/scriptable_monitor_rqt>

![Adding new script\|width=780](attachment:add_script.png)

# Documentation

## Scripts

### Configuration parameters

Parameters are preceded by \'#!\'. Syntax: ```parameter_name

```
There is one required parameter: \"name\" - the identification name of
the script, it must be unique.

Example: ```name

```
