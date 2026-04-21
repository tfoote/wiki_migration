The SSM_core package is a SMACH overhaul including an interpretor of
SCXML files.([SCXML standard](https://www.w3.org/TR/scxml/)). It creates
a finite state machine (based on SMACH) using the data from the SCXML
file. It can be usefull if you want to create a state machine using a
GUI that generate a SCXML file like :

-   [QT SCXML Editor Plugin](https://doc.qt.io/qtcreator/creator-scxml.html)
-   [SCXMLGui](https://github.com/fmorbini/scxmlgui)

## Creation of SCXML file

Here is a example of a SCXML file : 

```
<?xml version="1.0" encoding="UTF-8"?>
<scxml initial="Input Number">
    <datamodel>
        <data id="skill_file" expr="${airbus_ssm_tutorial}/resources/skills.xml"/>
    </datamodel>
    <state id="Input Number">
        <datamodel>
            <data id="skill" expr="Input"/>
        </datamodel>
        <transition event="Out" target="Primes"/>
        <transition event="Test" target="IsPrime"/>
        <transition event="Retry" target="Input Number"/>
    </state>
    <state id="Primes">
        <datamodel>
            <data id="skill" expr="Primes"/>
        </datamodel>
        <transition event="Off" target="End"/>
        <transition event="Reset" target="Input Number"/>
        <transition event="Continue" target="Input Number"/>
    </state>
    <state id="IsPrime">
        <transition type="external" event="Return" target="Input Number"/>
        <datamodel>
            <data id="skill" expr="isPrime"/>
        </datamodel>
    </state>
    <final id="End"/>
</scxml>
```



This example SCXML file can be found in the airbus_ssm_tutorial package.
It will create a very litte state machine using some keyboard entry to
test if an input number is a prime number or not. This is a basic
example.

There is a few constrains in order to make the SCXML file work as a
SMACH state machine.

-   Set up a skill register xml file as data in the datamodel at the
    root level



```
<?xml version="1.0" encoding="UTF-8"?>
<scxml initial="Input Number">
     <datamodel>
        <data id="skill_file" expr="${airbus_ssm_tutorial}/resources/skills.xml"/>
    </datamodel>
    ...
</scxml>
```



This file contains the informations about the predefined States you are
gonna use (like importing a Module / Class in Python).

For example : 

```
<?xml version="1.0"?>
<skills>
  <skill name="Input"   pkg="airbus_ssm_tutorial" module="airbus_ssm_tutorial1.skills" class="Input"/>
  <skill name="isPrime"	pkg="airbus_ssm_tutorial" module="airbus_ssm_tutorial1.skills" class="isPrime"/>
  <skill name="Primes"	pkg="airbus_ssm_tutorial" module="airbus_ssm_tutorial1.skills" class="Primes"/>
</skills>
```



Explanation :

-   'name' : The name you want to use inside the SCXML. It can be
    different from the class name.
-   'pkg' : The python package where the python file containing the
    class is located.
-   'module' : The python path to the file containing the class.
-   'class' : The class name of the SSM State / SMACH State

**WARNING : If you use a SMACH state instead of a SSM state. The
onEntry, onExit and datamodel/userdata assignment will not be used.**

-   Assign a SMACH State or a SSM State to the SCXML state by using the
    datamodel of the state.



```
<state id="IsPrime">
  <datamodel>
     <data id="skill" expr="isPrime"/>
  </datamodel>
  ...
</state>
```



Using the 'id' "skill" and set the 'expr' value to ``the name of
the skill you want to use``. In order to maintain the consistency of
the StateMachine, you have to link every outcome of this State inside
the SCXML. If you forget to link one, them the StateMachine consistency
check will fail.

**To help you know every outcomes/userdata of each states link inside
the skill XML file, you can run the "ssm_descriptor"**

This will generate a text file with a small description of every states
and a list of outcomes and userdata. 

```
roslaunch airbus_ssm_core ssm_descriptor.launch skill_xml_file:=empty_register.xml output_file:=/tmp/descriptor.txt
```

 Parameters
are :

-   skill_xml_file: the skill.xml file you want to scan. It should be
    located in the airbus_ssm_core/resources folder. If you want to put
    the skill.xml file in a different folder/pkg, use this syntax
    *\${pkg_name}/directory/file.scxml*
-   output_file: the absolute path for the output text file.

*todo : generate a qt scxml file with a pre-generated states / datamodel
to ease the authoring*

-   Parents states (containing other states) can't have a skill assign.
    Only atomic states.

```{=html}
<!-- -->
```
-   Transitioning from parents states.

To transitioning from a parent state. You have to follow some specific
rules to allow the remapping of the outcomes. There is two kind of
parent states :

-   Simple parent states (like a SMACH State Machine)

The transition has to be done through a final state from inside the
parent and then be link to the targeted state.

**SCXML**



```
<state id="Parent">
  <initial>
    <transition type="external" target="foo"/>
  </initial>
  <state id="foo">
     <transition event="to_bar1" target="Final_5"/>
     <transition event="to_bar2" target="Final_7"/>
   </state>
   <final id="Final_5"/>
   <final id="Final_7"/>
   <transition event="to_bar1" target="bar1"/>
   <transition event="to_bar2" target="bar2"/>
</state>
```



**Qt Authoring**

![\|width=40%](attachment:SSM_parent_transition.png)

-   Parallel (like a SMACH Concurence)

The transition form a parallel state is a bit more complicated because
of the multiple possible outcomes. In order to use the one that you
want, they're is a syntax. The 3 following states are in a Parallel
state : State A has 2 possible outcomes outA1 and outA2. State B has 2
possible outcomes possible outB1 and outB2. State C has just outC.

If you want to have the following transitions

-   outA1 and outB1
-   outB2 or outC
-   outA2

Then you will have the following SCXML :



```
<parallel id="Parallel_1">
  <state id="A"/>
  <state id="B"/>
  <state id="C"/>
  <transition event="Transition1" target="bar1" cond="A.outA1 AND B.outB1"/>
  <transition event="Transition2" target="bar2" cond="B.outB2 OR C.outC"/>
  <transition event="Transition3" target="bar3" cond="A.outA2"/>
</parallel>
```



The syntax that conditioning the outcome is written in the "cond" part
of the transition. 

```
"/state/./outcome/" "AND/OR" "/state/./outcome/"
```

 **For now it only support 2
states in the conditions !!**

## Execution

To execute a SCXML file you can use : 

```
roslaunch airbus_ssm_core ssm.launch scxml_file:=default
```



Input parameter is:

-   scxml_file: the scxml file you want to execute. It should be located
    in the airbus_ssm_core/resources folder. If you want to put scxml
    files in a different folder, use this syntax
    *\${pkg_name}/directory/file.scxml* or you can give the pull path to
    the file.

For example : 

```
roslaunch airbus_ssm_core ssm.launch scxml_file:=${airbus_ssm_core}/resources/defaulf.scxml
```

 There is a service to 'load' a
new SCXML file :

-   server_name + '/srv/init' (default : '/ssm/srv/init')

You can also use topics :

-   server_name + '/start' (default : '/ssm/start'), std_msgs/Empty.
    Trigger the execution of the state machine.
-   server_name + '/preempt' (default : '/ssm/preempt'),
    std_msgs/Empty. Trigger the interruption (premption) of the state
    machine.
-   server_name + '/pause' (default : '/ssm/pause'), std_msgs/Bool.
    If True, pause the execution of the state machine. If False, resume
    the execution.

Or use the airbus_ssm_plugin (which can be use in the airbus_cobos_gui
framework or as a standalone).

To launch the SSM Simple Action Server you can use :


```
<?xml version="1.0" encoding="UTF-8"?>
<scxml initial="Input Number">
     <datamodel>
        <data id="skill_file" expr="${airbus_ssm_tutorial}/resources/skills.xml"/>
    </datamodel>
    ...
</scxml>
```

0

The goal are the SCXML file you want to execute using the same
restriction of the input parameter scxml_file. The result is the outcome
of the last executed state.

The following topics works as well during execution :

-   server_name + '/preempt' (default : '/ssm/preempt'),
    std_msgs/Empty. Trigger the interruption (premption) of the state
    machine.
-   server_name + '/pause' (default : '/ssm/pause'), std_msgs/Bool.
    If True, pause the execution of the state machine. If False, resume
    the execution.
