## Vrep_ros_plugin

Vrep_ros_bridge is a meta-package. It contains the Vrep_ros_plugin and
all the handlers.

Vrep_ros_plugin contains the main code of the bridge. We wrote
Vrep_ros_plugin starting from a template called v_repExtPluginSkeleton,
available in the V-REP folder \"/programming\" with the porpoise to
create your own plugin. You can find more information about the plugins
in V-REP
[here](http://www.coppeliarobotics.com/helpFiles/en/plugins.htm/).

Ros V-Rep Plugin used the pluginlib package pluginlib package. Pluginlib
is a C++ library for loading and unloading plugins from within a ROS
package. Plugins (the handlers) are dynamically loadable classes that
are loaded from a runtime library (i.e. shared object, dynamically
linked library). In this way ours handler are actually plugins with some
dependencies.

GenericObjectHandler contains all the objects in the scene to which we
have added a custom data. The handlers are derived classes that
redefines the functions of the GenericObjectHandler in order to handle
the object.
