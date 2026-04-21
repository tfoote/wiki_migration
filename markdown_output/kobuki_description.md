## Urdf Files

There are two xacro files of importance:

-   `kobuki.urdf.xacro` - defines the `<kobuki/>` tag that can be
    embedded in other xacro files (e.g. turtlebot)
-   `kobuki_standalone.urdf.xacro` - can be called as a standalone
    robot description (see `launch/view_model.launch` for an example).

## Viewing the Model

There is a simple launcher inside the package that will let you view the
kobuki model rviz.

```
> roslaunch kobuki_description view_model.launch
```
