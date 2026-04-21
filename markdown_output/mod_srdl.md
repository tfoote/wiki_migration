## New version available

A complete re-implementation of SRDL, srdl2, is available and contained
in the same ROS package mod_srdl. Please have a look at the tutorial and
documentation here: <http://www.knowrob.org/doc/srdl2_tutorial>

## Old version

### Getting Started

The SRDL functionality is packaged in the ROS package mod_srdl. In order
to use it follow these steps:

1\. Make sure to have a working copy of package mod_srdl on your
computer and run 

```
rosmake mod_srdl
```

 1.#2 Start srdl with the
command 

```
rosrun rosprolog rosprolog mod_srdl
```



### Some basic queries

Here are examples for some basic queries to get started:

All subactions of an action: 

```
subActions(srdl_action:'TableSetting', L).
```



All components of a robot: 

```
hasComponent(rosie:'TUM_Rosie_RobotInstance1', C).
```



Match based on robot components 

```
matchRobotAndAction(rosie:'TUM_Rosie_RobotInstance1', srdl_action:'TableSetting').
 matchRobotAndAction(rosie:'TUM_Rosie_RobotInstance1', srdl_action:'ChocolateCakeBaking').
```



All missing capabilities for an unfeasible action:


```
returnMissingCapsForAction(srdl_action:'ChocolateCakeBaking',  rosie:'TUM_Rosie_RobotInstance1', Caps).
```



Print all components that are missing for an unfeasible action (order
via capability and capability provision alternative):


```
printMissingComponents(srdl_action:'ChocolateCakeBaking', rosie:'TUM_Rosie_RobotInstance1').
```



Compute success probability (based on experience) for an action:


```
computeSuccessProbability(srdl_action:'TableSetting', P).
```



Show technical specification/ attributes of components (as far as
specified/ contained in KB): 

```
printAttributesOfComponent(pr2:'PR2_l_ArmComposition').
```



Check if a capability can be learned: 

```
verifyCapAvailability(srdl_cap:'RedCupRecognitionCapability', rosie:'TUM_Rosie_RobotInstance1').
 isLearnableCapability(srdl_cap:'RedCupRecognitionCapability', rosie:'TUM_Rosie_RobotInstance1').
```



### Actions in which TUM Rosie and PR2 differ

Example 1 - Driving backwards (possible for Rosie but not for PR2):


```
rosrun rosprolog rosprolog mod_srdl
```

0

Example 2 - Crushing a can of coke using strong grip (possible for PR2
but not for Rosie): 

```
rosrun rosprolog rosprolog mod_srdl
```

1
