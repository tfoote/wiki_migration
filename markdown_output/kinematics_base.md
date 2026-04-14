Note this wiki is for the deprecated Arm Navigation version of
KinematicsBase. For the much newer MoveIt Kinematics Base, see
[this page](https://moveit.ros.org/documentation/plugins/#kinematicsbase).

This package provides a base class for implementing a kinematics plugin.
As such, it only contains a single header file. Examples of plugin
implementations for kinematics can be found in two packages: 1.
[pr2_arm_kinematics](pr2_arm_kinematics) contains a plugin
implementation of kinematics for the PR2 robot. 1.
[arm_kinematics_constraint_aware](arm_kinematics_constraint_aware)
contains a more generic plugin implementation that can be configured for
any serial manipulator.

Have a look at the documentation in the individual packages for more
information on how to configure and use them.

## Creating your own plugin implementation of kinematics

### The code

You can create your own plugin implementation of kinematics -
essentially a wrapper that wraps your custom kinematics solver by
inheriting from the base class defined in this package. The typical
procedure for this would be to create your own package (named
example_kinematics) and have a dependency on both the
\'\'kinematics_base\'\' and \'\'pluginlib\'\' packages.

Then, have a look at the
[Code API](http://www.ros.org/doc/api/kinematics_base/html/classkinematics_1_1KinematicsBase.html#_details).
You will need to implement all the pure virtual functions after
inheriting from the base class.

### Setting up the plugin

In addition to writing the code, you will also have to register the
plugin to make sure it can be accessed from other packages. This
involves several steps outlined below.

#### Setup the correct dependencies

Make sure you add the following lines to the manifest.xml file in
\'\'example_kinematics\'\'.

```
<depend package="pluginlib"/>
 <depend package="kinematics_base"/>
```

#### Setup the plugins file

In a file named \'\'example_plugins.xml\'\' in your example_kinematics
package, add the following lines and modify them to match the names you
have chosen for your components.

```
<library path="lib/libarm_kinematics_constraint_aware_lib">
  <class name="arm_kinematics_constraint_aware/KDLArmKinematicsPlugin" type="arm_kinematics_constraint_aware::KDLArmKinematicsPlugin" base_class_type="kinematics::KinematicsBase">
    <description>
      A generic implementation of kinematics as a plugin based on KDL.
    </description>
  </class>
</library>
```

1\. Replace \'\'arm_kinematics_constraint_aware_lib\'\' with the name of
the library object that contains your implementation of the kinematics.
E.g. if you named your library \'\'example_kinematics\'\', the first
line above should read: ```
<library path="lib/libexample_kinematics">
``` 1. Rename the class
name to be \'\'namespace/class_name\'\'. E.g. if your code is in the
namespace \'\'example_kinematics\'\' and you named your class
!ExampleKinematics, replace the class name with
\'\'example_kinematics/ExampleKinematicsPlugin\'\'. 1. Rename the type
to be \'\'namespace::class_name\'\'. E.g.
\'\'example_kinematics::ExampleKinematicsPlugin\'\'.

#### Export the plugins file

In the manifest.xml file for example_kinematics, make sure the following
lines are present in the \'\'export\'\' tag:

```
<kinematics_base plugin="${prefix}/example_plugins.xml" />
```

#### Register the plugin in your code

In your .cpp file, make sure you have the following line at the top:

```
PLUGINLIB_DECLARE_CLASS(example_kinematics,ExampleKinematicsPlugin, example_kinematics::ExampleKinematicsPlugin, kinematics::KinematicsBase)
```
