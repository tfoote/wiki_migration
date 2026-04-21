![\|height="504px",width="519px"](attachment:estimation.png)

## External Documentation

This is a third party package with
[external documentation](http://orocos.org/bfl).

## Using BFL in ROS with Catkin Builds:

```highlight
find_package(PkgConfig)

pkg_check_modules(BFL REQUIRED bfl)

message("BFL include dirs:" ${BFL_INCLUDE_DIRS})
message("BFL library dirs:" ${BFL_LIBRARY_DIRS})

include_directories(${BFL_INCLUDE_DIRS})
link_directories(${BFL_LIBRARY_DIRS})

[..]

# for every target using BFL:
target_link_libraries(your_executable ${BFL_LIBRARIES})
```
