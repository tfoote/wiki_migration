Process modules control different robot actuators. Every robot needs a
special set of process modules matching its own actuator types. We use
process modules to write high-level plans that are robot independent, by
creating a process module API. Plans thus just need to know the API of
process modules, and can run on different kinds of robots by invoking
different process modules.

This means plans will assume a set of process modules, and if the robot
has suitable process modules, the plan will run. More specifically, a
high-level plan parameterizes a process module symbolically, by using a
designator. The process module then resolves the designator, depending
on the robot's capabilities and the current context and creates a
low-level parameterization that can be used to execute an action. For
instance, to move the robot to a location where it can see a specific
object, we state in the plan:

```
(with-designators ((loc (location `((to see) (obj ,obj)))))
  (pm-execute :navigation loc))
```

This part of a plan would call the navigation process module by its
alias :navigation and pass to it a designator. The actual action that is
executed can be very different on a robot with differential drive, a
biped robot, or a robotic car.
