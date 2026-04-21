1.  keywords State, Machine, Statemachine, Executive

  -- ------------------ -- -- -- ---------------------- --
     [English](smach)            [简体中文](cn/smach)   
  -- ------------------ -- -- -- ---------------------- --

[Youtube](https://www.youtube.com/watch?v=F3slROzVNbc)

## About SMACH

**When should I use SMACH?**

SMACH is useful when you want a robot to execute some complex plan,
where all possible states and state transitions can be described
explicitly. This basically takes the hacking out of hacking together
different modules to make systems like mobile robotic manipulators do
interesting things.

-   Fast prototyping: The straightforward Python-based SMACH syntax
    makes it easy to quickly prototype a state machine and start running
    it.

```{=html}
<!-- -->
```
-   Complex state machines: SMACH allows you to design, maintain and
    debug large, complex hierarchical state machines. You can find an
    example of a complex hierarchical state machine
    [here](pr2_plugs_executive).

```{=html}
<!-- -->
```
-   Introspection: SMACH gives you full introspection in your state
    machines, state transitions, data flow, etc. See the
    [smach_viewer](smach_viewer) for more details.

**When should I NOT use SMACH?**

-   Unstructured tasks: SMACH will fall short as the scheduling of your
    task becomes less structured.
-   Low-level systems: SMACH is not meant to be used as a state machine
    for *low-level* systems that require high efficiency, SMACH is a
    *task-level* architecture.
-   Smash: Do not use SMACH when you want to smash something, for that
    use
    [ smash](https://en.wikipedia.org/wiki/Hulk_and_the_Agents_of_S.M.A.S.H.).

**Is SMACH only a finite state machine library?**

You can build a finite state machine using SMACH, but SMACH can do much
more. SMACH is a library for task-level execution and coordination, and
provides several types of "state containers". One such container, is a
finite state machine, but this container can also be a state in another
container. See the [tutorials page](smach/Tutorials) for a list of
containers and states built into SMACH.

## Documentation

The [documentation page](smach/Documentation) provides an overview of
the concepts used in SMACH.

The [tutorials page](smach/Tutorials) contains an extensive set of
tutorials to get you up to speed building and running your own state
machines.
