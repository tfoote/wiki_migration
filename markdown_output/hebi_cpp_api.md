# Description

The HEBI CPP API package wraps the HEBI C++ API, allowing direct usage
of the API from a ROS node coded in C++.

## Using from your own project

To add this as a dependency in your package, add to your \`package.xml\`
file: \`\<depend\>hebi_cpp_api\</depend\>\`

and in your package\'s \`CMakeLists.txt\` file, add to the
\`find_package(catkin REQUIRED)\` statement: \`hebi_cpp_api\`

Also, in your \`catkin_package\` statement, ensure \`hebi_cpp_api\` is
listed in the \`CATKIN_DEPENDS\`.

## Examples

We have a set of examples of this C++ API wrapped into nodes, from
controlling a single actuator to prebuild arms and mobile bases, at:

<https://github.com/HebiRobotics/hebi_cpp_api_ros_examples>
