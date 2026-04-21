```wiki
Assimp ROS package deprecated (ROS Electric)
```

Starting in ROS Electric, Assimp is installed as a [rosdep](rosdep)
system dependency. This means that you compile against Assimp without
requiring any ROS-specific build tools. At the same time, Assimp 1 has
been replaced by Assimp 2.

## Electric: Porting to system dependency

Starting in ROS Electric, Assimp 2 is installed as a system dependency.
This means that you compile against Assimp 2 without requiring any
ROS-specific build tools.

### CMakeLists.txt

You need to explicitly link against against the Assimp library:

```
target_link_libraries(${PROJECT_NAME} assimp)
```

### Package/stack dependencies

Assimp is defined in the [common_rosdeps](common_rosdeps) stack/package.
You will need to update

1\. `manifest.xml` ```
<depend package="common_rosdeps" />
  <rosdep name="assimp" />
```

1\. `stack.xml` ```
<depend stack="common_rosdeps" />
```

## Documentation

Please see the [Assimp homepage](http://assimp.sourceforge.net/) for
documentation on the Assimp library. See also the
[Assimp API Documentation](http://assimp.sourceforge.net/lib_html/index.html).
