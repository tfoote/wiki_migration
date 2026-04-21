The AlicaEngine is an execution layer for cooperative execution of Alica
plans, which can be designed using the [Planmodeller](Planmodeller). It
is written C# and runs under mono. It comes as library, meant to be
integrated into an executable with additional features, such as a
representation of the environment.

For installation and setup, best follow the example provided in the
package [alica_turtle](alica_turtle).

## API Details

-   The main namespace is
    [Alica](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/index.html)
-   Typical interactions take place through the singleton class
    [AlicaEngine](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/AlicaEngine.html).
-   Action programs, called *Behaviours* inherit from
    [BasicBehaviour](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/BasicBehaviour.html)
-   Domain specific components such as conditions and behaviours
    interact with specific parts of the internal state, encapsulated by
    a
    [RunningPlan](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/RunningPlan.html)

```{=html}
<!-- -->
```
-   The
    [AutoDiff](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AutoDiff/index.html)
    namespace provides primitives to formulate complex non-linear
    constraints, by writing to a
    [ConstraintDescriptor](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/ConstraintDescriptor.html)
    from within a generated
    [GetConstraint](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/GetConstraint.html)
    method. This version of AutoDiff is an adaptation of
    [Alex Shtof\'s AutoDiff](http://autodiff.codeplex.com/).
-   The currently preferred solver for these constraints is
    [CGSolver](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/CGSolver/Alica.Reasoner/CGSolver.html),
    however, direct interaction with the solver is never necessary.
    Instead, components query the engine using a
    [ConstraintQuery](http://cn-alica-ros-pkg.googlecode.com/git/AlicaEngine/doc/AlicaEngine/Alica/ConstraintQuery.html).
