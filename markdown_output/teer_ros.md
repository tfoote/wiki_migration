This package uses *git submodule* to fetch teer and patches it to add
support for ROS\' time and protect condition variables when being
accessed from other threads. This is transparent, and to use teer with
ros you just have to add \`teer_ros\` as a dependency in your manifest
and do an \`import teer_ros\` in your script.
