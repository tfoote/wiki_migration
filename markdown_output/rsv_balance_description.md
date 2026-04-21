RoboSavvy's self-balance platform URDF model and meshes.

## Customization

This package provides easy to use URDF xacro files which you can include
to assemble your own robot model using the self-balance platform.

The platform macro is provided by the file:
*rsv_balance_description/urdf/urdf/balance.urdf.xacro* and can be
included in your URDF model as such: 

```
<robot name="you_awesome_robot" xmlns:xacro="http://www.ros.org/wiki/xacro">
  <xacro:include filename="$(find rsv_balance_description)/urdf/balance.urdf.xacro" />
  <xacro:balance/> 

  ..
  .. <your_awesome_robot_here>
  ..

</robot>
```



As an example you can look at
*rsv_balance_description/urdf/urdf/robot.urdf.xacro*, which puts on top
a rod and a dummy weight of 5kg.

![\|width=100%](attachment:simulation_tutorial3.png)
