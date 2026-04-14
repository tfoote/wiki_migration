## Overview

Diagnosis observers are that part of
[ tug_ist_model_based_diagnosis](tug_ist_model_based_diagnosis ) which
monitor the system behavior. These are general software entities
implemented as ROS nodes that monitor particular aspects of the system.
There are different kinds of observers supervising different aspects or
properties. The result of the observation is published on the
\'\'/observations\'\' topic as a first order logic (FOL) sentence. The
sentence is a representation of the observed property and its status.
Observations are published as a set of strings. Each string represents a
single FOL sentence like \'\'ok(topic)\'\', \'\'running(node)\'\',.etc.
There are different kinds of observers namely Diagnostic Observer
(DObs), General Observer (GObs), Node Observer (NObs), Qualitative
Observer (QObs), Binary Qualitative Observer (BiQObs), Multiple Observer
(MObs), Hardware Observer (HObs) and Property Observer (PObs).

## Nodes

```clearsilver
node.0 {
name= DObs
desc= DObs is Diagnostic Observer and it uses existing ''/diagnostics'' topic and publishes on ''/observations''.It is the connection between the existing ROS diagnostics system and the integrated diagnosis and repair system. ''DObs'' receives diagnostic messages and generate the output based on similar rules as the existing ROS diagnostic analyzers.
sub{
0.name= /diagnostics
0.type= diagnostic_msgs/DiagnosticArray
0.desc= diagnostics data from existing ROS diagnostics.
}
pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''ok(device_name),~ok(device_name)''.
}
}
node.1 {
name= HObs
desc= Hardware Observer subscribes to the measurements and status updates coming from the hardware diagnosis board to supervise the status of the different power supply channels. It provides the observation ''on(m)'' if the module ''m'' is powered, otherwise ''~on(m)''. Moreover, it provides all current measurements and power states in a special message on the topic ''/board_measurments''. This allows further observers to reuse the information.
pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''on(device),~on(device)''.
}
 param{
    0.name = ~topic
    0.type = string
    0.default = `"/board_measurments"`
    0.desc = It is the name of the topic published by the board controller.
}
}
node.2 {
name= GObs
desc= General Observer simply subscribes to a particular topic and uses the received messages as input. This is done by checking the frequency of messages. It submits ''ok(t)'' if it observes the right frequency of the topic ''t'' otherwise ''~ok(t)''.

pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''running(node_name),~running(node_name)''.
}
 param{
    0.name = ~topic
    0.type = string
    0.default = `"/Topic"`
    0.desc = It is the name of the topic whose frequency has to be observed.
    1.name = ~frq
    1.type = int
    1.default = 10
    1.desc = It is normal and required current frequency of the running topic.
    2.name = ~dev
    2.type = int
    2.default = 5
    2.desc = This deviation on both side of the frequency parameter.
    3.name = ~ws
    3.type = int
    3.default = 10
    3.desc = This is window size describing the number of times of occurrence of the topic output. The less is the window size the more strict is the observer.
}
}
node.3 {
name= NObs

desc= Node Observer observes the running state of software nodes. It submits ''running(n)'' if node ''n'' actually runs, ''~running(n)'' otherwise. It takes name of the node to be observed as parameter.

pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''running(node_name),~running(node_name)''.
}
 param{
    0.name = ~node
    0.type = string
    0.desc = It is the name of the node to be observed if its running or not.
}
}
node.4 {
name= QObs
desc= Qualitative Observer observes the abstract trend of a particular value in the message of a topic. It reports if value ''v'' actually increases ''inc(v)'', decreases ''dec(v)'' or stays constant ''const(v)''. The observer fits a linear regression for a given time window and compares it with a given slope.

pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''inc(val), dec(val)'' or ''cons(val)''.
}
 param{
    0.name = ~topic
    0.type = string
    0.default = `"/pose"`
    0.desc = It is the name of the topic whose message value has to be observed.
    1.name = ~field
    1.type = string
    1.default = `"pose.pose.position.x"`
    1.desc = This the field for value embedded inside the topic message.
    2.name = ~ws
    2.type = int
    2.default = 1000
    2.desc = This is window size describing the number of times of occurrence of the topic output. The less is the window size the more strict is the observer.
    3.name = ~b
    3.type = int
    3.default = 0.000005
    3.desc = It is the slop which is used for matching after linear regression.
}
}
node.5 {
name= BiQObs
desc= Binary Qualitative Observer observes match or mismatch between abstract trends of two particular values in the massage of one or two topic(s). It issues observation ''matched(val1,val2)'' if abstract trend of ''val1'' is similar to of ''val2'' otherwise ''~matched(val1,val2)''. BiQObs functions the same way as QObs except that it observes difference between two abstract trends.

pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''matched(topic1_val,topic2_val)'' or '~matched(topic1_val,topic2_val)''.
}
 param{
    0.name = ~topic1
    0.type = string
    0.default = `"/pose"`
    0.desc = It is the name of the first topic whose message value has to be matched.
    1.name = ~field1
    1.type = string
    1.default = `"pose.pose.position.x"`
    1.desc = This the field for value embedded inside the first topic message.
    2.name = ~ws1
    2.type = int
    2.default = 1000
    2.desc = This is window size describing the number of times of occurrence of the topic1 output. The less is the window size the more strict is the observer.
    3.name = ~b1
    3.type = int
    3.default = 0.000005
    3.desc = It is the slop which is used for matching after linear regression calculation for value of field1.
    4.name = ~topic2
    4.type = string
    4.default = `"/pose"`
    4.desc = It is the name of the second topic whose message value has to be matched.
    5.name = ~field2
    5.type = string
    5.default = `"pose.pose.position.y"`
    5.desc = This the field for value embedded inside the second topic message.
    6.name = ~ws2
    6.type = int
    6.default = 1000
    6.desc = This is window size describing the number of times of occurrence of the topic2 output. The less is the window size the more strict is the observer.
    7.name = ~b2
    7.type = int
    7.default = 0.000005
    7.desc = It is the slop which is used for matching after linear regression calculation for value of field2.
    8.name = ~mode
    8.type = string
    8.default = `"LIN"`
    8.desc = It is the mode of regression calculation and matching. It assumes one of two values ''"LIN"'' for simple linear regression, and ''"DRV1"'' for first calculating derivative of the values in the field1 of topic1.
    9.name = ~reg
    9.type = string
    9.default = yy
    9.desc = This is regression calculation code. ''"yy"'' represents that regression should be calculated for both the field1 and field2, ''"ny"'' means do not calculate regression for field1 but calculate regression for field2, similarly ''"yn"'' and ''"nn"'' values.
}
}
node.6 {
name= MObs
desc= Multiple Observer is similar to General Observer but subscribes to two topics. Therefore, more complex communication behaviors such as conditioned or triggered communication are observed between the topics.

pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''running(node_name),~running(node_name)''.
}
 param{
    0.name = ~in_topic
    0.type = string
    0.default = `"/Topic1"`
    0.desc = It is the name of the topic which acts like trigger for the other topic.
    1.name = ~out_topic
    1.type = string
    1.default = `"/Topic2"`
    1.desc = It is the name of the topic which is triggered from other topic.
    2.name = ~tim
    2.type = int
    2.default = 500
    2.desc = This is time(ms) providing delta time between triggering and triggered actions of the topic. If the conditioned topic is not triggered in specified time then observers reports ''~ok'' for the dependent topic.
}
}
node.7 {
name= PObs
desc= Property Observer supervises properties not directly related to a topic that may affect the robot performance like CPU or memory usage of a particular service used by a node. '''This observer is still under construction.''' 
pub{
0.name= /observations
0.type= tug_ist_diagnosis_msgs/Observations
0.desc= This topic gives information in the form of ''First Order Logic (FOL)'' sentences like ''ok(node,mem), ok(node,cpu)''.
}
 param{
    0.name = ~node
    0.type = string
    0.default = `"Node"`
    0.desc = It is the name of node which is observed against some system resource.
    1.name = ~property
    1.type = string
    1.default = `"MEM"`
    1.desc = This is the property being observed for the node. It assumes two properties "cpu" and "mem"     
    2.name = ~max_val
    2.type = float
    2.default = 0.2
    2.desc = It is maximum limit value for checking the system resource value. This value is percentage value. Means 0.2 means 0.2%.
    3.name = ~mismatch_thr
    3.type = int
    3.default = 5
    3.desc = This is threshold for counting how many times resource goes up to the maximum value. Until mismatch threshold system can tolerate but after mismatch threshold system will alarm for exceeding resource.
    4.name = ~ws
    4.type = int
    4.default = 10
    4.desc = This is window size describing the number of times of occurrence of the resource property measurment. The less is the window size the more strict is the observer.
}
}
```
