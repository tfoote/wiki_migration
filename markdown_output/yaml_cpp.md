```wiki
As of ROS Electric, the Yamlcpp package has been replaced with a system dependency.  [[/diamondback|Old documentation]]
```

```wiki
From version 0.5, yaml-cpp started using boost as a dependency. If you'd like to continue using the non-boost variant (useful on embedded boards), pull in the ''yaml-cpp-0-3'' ros third party dependency. Note that ubuntu does provide a 0.3 variant, but it cannot be used in parallel. The ros third party dependency namespaces so that you can - see the [[https://github.com/stonier/yaml_cpp_0_3/blob/devel/Readme.md|README]].
```

Starting in ROS Electric, Yamlcpp is installed as a [rosdep](rosdep)
system dependency. This means that you compile against Yamlcpp without
requiring any ROS-specific build tools.

## ROS Electric: using the system install

### CMakeLists.txt

You need to explicitly link against against the yaml-cpp library:

```
target_link_libraries(${PROJECT_NAME} yaml-cpp)
```

### Package/stack dependencies

*If you have previously used yaml_cpp with ROS, make sure you remove
`<depend package="yaml_cpp" />` from your manifest.*

The `yaml-cpp` [rosdep](rosdep) is defined in the ROS
[common_rosdeps](common_rosdeps) stack/package. In order to get this
rule, you need to edit your `manifest.xml` and `stack.xml` as
follows:

1\. `manifest.xml`

```
<depend package="common_rosdeps" />

  <rosdep name="yaml-cpp" />
```

2\. `stack.xml`

```
<depend stack="common_rosdeps" />
```

## External Documentation

Please see the [yaml-cpp homepage](http://code.google.com/p/yaml-cpp/)
for documentation.
