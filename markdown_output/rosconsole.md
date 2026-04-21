*For documentation on console output and logging APIs for
[roscpp](roscpp), please see the
[roscpp logging overview](roscpp/Overview/Logging).*

`rosconsole` is a C++ package that supports console output and logging
in [roscpp](roscpp). It provides a macro-based interface which allows
both `printf`- and stream-style output. It also wraps
[log4cxx](http://logging.apache.org/log4cxx/index.html), which supports
hierarchical loggers, verbosity levels and configuration-files.

The requirements for rosconsole are:

-   Simple basic interface
-   No required explicit initialization step
-   Multiple severity level support: info/error/warning/debug/etc\...
-   `printf`- and stream-style formatting
-   Ability to hook all output
-   Speed \-- With output turned off, it should have minimal impact on
    runtime performance, preferably without recompilation
-   File and line information available per output statement
-   External configuration (environment or file based) of what level of
    output we want
-   Thread-safe
-   Ability to compile out debugging/low severity messages

rosconsole provides most of this through log4cxx, and implements a few
of them through the macro wrappers.

rosconsole also provides an assertion/breakpoint library.

## Code API

[Included page rosconsole/CodeAPI not found](Included page rosconsole/CodeAPI not found)

### Assertions

rosconsole also provides assertions, in `ros/assert.h`:

-   `ROS_ASSERT(cond)`
-   `ROS_ASSERT_MSG(cond, \...)`
-   `ROS_BREAK()`

## Configuration

rosconsole will load a config file from
`\$ROS_ROOT/config/rosconsole.config` when it initializes.

rosconsole also lets you define your own configuration file that will be
used by log4cxx, defined by the ROSCONSOLE_CONFIG_FILE environment
variable. Anything defined in this config file will **override** the
default config file.

A simple example:



```
# Set the default ros output to warning and higher
log4j.logger.ros=WARN
# Override my package to output everything
log4j.logger.ros.my_package_name=DEBUG
```

 You may have noticed that the example says
"log4j" not "log4cxx". This is because log4cxx is directly
compatible with log4j's configuration files.

ROS output is set to **info** and higher by default.

For more detailed information on the config file, and log4cxx in
general, please see the
[official log4cxx documentation](http://logging.apache.org/log4cxx/index.html).

If you want to include a custom configuration into a specific launch
file, you can do so using the [<env>-tag](roslaunch/XML/env) of
roslaunch.

Example:



```
<launch>
  <env name="ROSCONSOLE_CONFIG_FILE"
       value="$(find mypackage)/custom_rosconsole.conf"/>
  <node pkg="mypackage" type="mynode" name="mynode" output="screen"/>
</launch>
```



## ROS Logger Hierarchy

Rosconsole uses the "ros" logger as its root-level logger. All unnamed
logging statements will be output to the "ros.<package_name>"
logger. The named variations will output to
"ros.<package_name>.<name>". There are a couple of defines that
expose this:

-   `ROSCONSOLE_ROOT_LOGGER_NAME` expands to "ros"
-   `ROSCONSOLE_DEFAULT_NAME` expands to "ros.<package_name>"

If you'd like to access one of your named loggers, you can get the name
by:



```cplusplus
const char* logger_name = ROSCONSOLE_DEFAULT_NAME ".<name>"
```



## Compile-time Logger Removal

rosconsole provides a way to remove logging at compile time, though this
should rarely be necessary. This is accomplished through the
`ROSCONSOLE_MIN_SEVERITY` define. Statements of a severity level lower
than `ROSCONSOLE_MIN_SEVERITY` will be compiled out. The options are:

-   `ROSCONSOLE_SEVERITY_DEBUG`
-   `ROSCONSOLE_SEVERITY_INFO`
-   `ROSCONSOLE_SEVERITY_WARN`
-   `ROSCONSOLE_SEVERITY_ERROR`
-   `ROSCONSOLE_SEVERITY_FATAL`
-   `ROSCONSOLE_SEVERITY_NONE` (no logging will be compiled in)

## Changing Logger Levels

If you want to change the logger levels via a configuration file, please
see the [Configuration](#Configuration) section.

To change the logger levels from C++, use
`ros::console::set_logger_level()`. Example:



```
#include <ros/console.h>
if( ros::console::set_logger_level(ROSCONSOLE_DEFAULT_NAME, ros::console::levels::Debug) ) {
   ros::console::notifyLoggerLevelsChanged();
}
```

 If you change one of the `Logger`'s
verbosity levels after any logging statements using that logger, you
**must** call `ros::console::notifyLoggerLevelsChanged()`. If you do
not, logging statements that have already been hit once (and therefore
initialized) may continue to print when they should not, and vice-versa.

For examples of this behavior, please see the `examples/example.cpp`
file.

## Console Output Formatting

rosconsole allows you to specify how you'd like its output to show up
in the console output through the `ROSCONSOLE_FORMAT` environment
variable. The default is equivalent to:



```
export ROSCONSOLE_FORMAT='[${severity}] [${time}]: ${message}'
```

 The full list of possible options follows.

  -- ----------------------------------------------------------------------------------------------------------------- ------------- ---------------------------------------------------------------------------- ---------------------- --
     **Token**                                                                                                                       **Sample Output**                                                                                   
     severity                                                                                                                        ERROR                                                                                               
     message                                                                                                                         hello world 0                                                                                       
     <style="text-align:left;vertical-align:top"                                                                    4>time                                                                                    1284058208.824620563   
     (if no sim time is available it only shows the wall time)                                                                                                                                                                           
     1284058208.824620563, 1234567890.123456789                                                                                                                                                                                          
     (if sim time is available it shows the wall time first and the sim time second)                                                                                                                                                     
     <style="text-align:left;vertical-align:top"                                                                    2>walltime                                                                                1284058208.824620563   
     (this feature was always available in Python, in C++ it is only available since `ros_console` version 1.12.6)                                                                                                                     
     thread                                                                                                                          0xcd63d0                                                                                            
     logger                                                                                                                          ros.roscpp_tutorials                                                                                
     file                                                                                                                            /wg/bvu/jfaust/ros/stacks/ros_tutorials/roscpp_tutorials/talker/talker.cpp                          
     line                                                                                                                            92                                                                                                  
     function                                                                                                                        main                                                                                                
     node                                                                                                                            /talker                                                                                             
  -- ----------------------------------------------------------------------------------------------------------------- ------------- ---------------------------------------------------------------------------- ---------------------- --

You can directly define the environment variable in a launch file (of
course, change the value depending on your needs):


```
<launch>
  <env name="ROSCONSOLE_FORMAT" value="[${severity}] [${time}] [${node}]: ${message}"/>
  <node pkg="mypackage" type="mynode" name="mynode" output="screen"/>
</launch>
```



### Change default time and walltime format

It gives the user control over how dates and times can be represented.

You need to finish **time** or **walltime** token with colon and then
specify **format string**, which can contain normal text together with
argument specifiers like **%M** and **%S**. It looks like:



```
export ROSCONSOLE_FORMAT='${time:format string}'
```

 or 

```
export ROSCONSOLE_FORMAT='${walltime:format string}'
```



It mostly supports
[strfime](https://en.cppreference.com/w/c/chrono/strftime) specification
for formatting dates/times.

The following table lists examples available for both C++ and Python.

  -- ------------------------- -- ---------------------- --
     **Format Specifier**         *Example*'            
     `%Y-%m-%d %H:%M:%S`        2020-04-29 20:02:1     
     `%y-%b-%d %I:%M:%S%p`      20-Apr-29 08:20:40PM   
     `%x %r`                    04/29/20 08:31:30 PM   
  -- ------------------------- -- ---------------------- --

### Changed default value in Python === the default format (if the environment variable is not set) for Python is now the same as for C++. If you want to keep the previous format for backward compatibility you can set the following:



```
export ROSCONSOLE_FORMAT='[${severity}] [WallTime: ${time}]: ${message}'
```



## Disable all logging

### With a configuration file

Create a custom rosconsole configuration file with the following content
and use it as described above:



```
log4j.threshold=OFF
```



### By calling a function

By invoking `ros::console::shutdown();` in C++ the logging subsystem
is shut down and therefore no more logging occurs.

## Force line buffering for ROS logger

When `stdout` of a ROS application is fully buffered, for example in
case when it is connected to a pipe, users may not see the output of the
application until the buffer fills up. The user can force line buffering
for ROS loggers that print to the console by setting the environment
variable `ROSCONSOLE_STDOUT_LINE_BUFFERED` to `1`.



```
<launch>
  <env name="ROSCONSOLE_CONFIG_FILE"
       value="$(find mypackage)/custom_rosconsole.conf"/>
  <node pkg="mypackage" type="mynode" name="mynode" output="screen"/>
</launch>
```

0 In this case the buffer will be flushed after
every line that is written to the logs.

Default value is `0`. When set to `0` the flush is not triggered on
every line and the default buffering scheme of `stdout` is used.

## See also

[Verbosity Level Best Practices](Verbosity Levels)
