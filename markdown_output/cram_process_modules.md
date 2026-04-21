## Introduction

One goal of CRAM is to execute the same high-level plan on various
different robots. For that, we need to find an abstraction to separate
robot specific components and the high-level parts that specify the
actual behavior. For that purpose, we introduce process modules. Process
modules are basically the parts of a CRAM system that directly
communicate with the outer world, i.e. that trigger the navigation
process (e.g. [move_base](move_base)), manipulation or perception. For
the high-level components of the system, these process modules must be
black boxes in order to keep them general. The process modules for
controlling a robot are started up at the beginning of plan execution
and shut down when the robot finished its actions. Their input is always
an action designator provided by the
[cram_designators](cram_designators) package.

## API

Process modules are defined with the macro `def-process-module`. The
definition looks similar to a function definition in Common Lisp with
the difference that only one parameter can be declared, the name of the
variable the input designator is bound to. Whenever input is received,
the body of the process module is executed. Basically, action execution
in process modules has to perform the following steps:

1\. Resolve the action designator to get the actual commands to send to
the robot's hardware.

2\. Execute these parameters.

3\. Either throw an error if the execution failed or optionally return a
result value that is passed to the caller.

The following code illustrates how a simple navigation process module
could be defined:



```
(def-process-module navigation (input-designator)
  (let ((goal-pose (reference input-designator)))
    (or (execute-navigation-action goal-pose)
        (fail 'navigation-failed))))
```



We assume that the input designator (an action designator) resolves to a
3d pose that we can send to the function `execute-navigation-action`.
The function returns NIL if navigation failed. In that case we throw an
error.

To send a command to a process module, the package provides the API
method `pm-execute`. The following example shows how to send a
navigation action to the process module defined above:



```
(top-level
  (with-process-modules-running (navigation)
    (pm-execute navigation (make-designator 'action `((type navigation) (goal ,some-pose)))))
```



We assume that the variable `some-pose` is already bound to a 3d pose.
The macro `with-process-modules-running` is used to start up the
specified process modules and to shut them down after the code finished.
Normally, the macro is used at top-level and the process modules keep
running over the complete runtime of the robot. The surrounding
`top-level` form is necessary because `with-process-modules-running`
needs to be executed in a [cram_language](cram_language) environment.
