## Overview

APPL is a C++ implementation of the SARSOP algorithm for solving
discrete POMDPs. Details of this algorithm can be found at
[appl homepage](http://bigbird.comp.nus.edu.sg/pmwiki/farm/appl/). This
package is a C++ ROS wrapper of the appl software。The package works as
a ROS server to give feedback to the ROS client about the current
optimal action according to the generated POMDP policy. In this way the
ROS user can develop independently instead of compiling together with
the APPL code and also can avoid potential library conflicts between
them.

## Before compiling the node

In this simple guide, we assume you have background knowledge of POMDP
planning.

1\. At the very first stage, you need to write a POMDPX model
description file. Information can be found at the above website.

2\. After you have the POMDPX file, you need to solve it with APPL to
generate the corresponding PolicyX file. The basic way of doing it is to
go to /appl/src folder and type: ./pomdpsol
../examples/POMDPX/Tiger.pomdpx (we have an example pomdpx file in the
above indicated position). The generated policy is written to out.policy
by default. The pomdpsol executable has already been compiled and placed
in the src folder. You don't need to recompile again.

3\. After you have the PolicyX file, you can use rosmake to compile the
node.

## Node

### Service

appl_request

Call this service to send the observation and get the action

### Parameters

appl_problem_name(string)

the position of the PomdpX file

appl_policy_name(string)

the position of the PolicyX file

## Service Description

A typical POMDP control cycle is : robot executes an action and receives
an observation. Here the robot controller needs to send the received
observation the service node to get the feedback action. The message
format is: ```
int64 cmd   --> command type

string obs  --> observation

string xstate  -->fully observable states

---

int64 action  -->the action you should execute given by the service node
```

1\. cmd=0 test command.

2.cmd=1 initialization. You need to specify the initial fully observable
states in xstate(if you have) you are in

3\. cmd=2 actual communication. You need to specify the obs and
xstate(if you have).

For obs , if there's only one observable variable, you just copy the
enumerable value of the variable as specified in the PomdpX file. If
there are more than one variable, you need to first concatenate those
values together in the ascending order of the variable names.

The rule of xstate is the same as obs.

For example, in the below PomdpX variable declaration script, it has 3
fully observable variables: RobPos,RobVel,PedPose.It has only one
observation variable oPed. A valid assignment to xstate can be
"sx00y00sR00sV0". And a valid assignment to obs can be "ox00y00".
```
<Variable>
<StateVar vnamePrev="RobPose_0" vnameCurr="RobPose_1" fullyObs="true">
<ValueEnum>
  sR00    sR01    sR02    sR03    sR04    sR05    sR06    sR07    sR08    sR09    strRob  	 	
</ValueEnum>
</StateVar>
<StateVar vnamePrev="RobVel_0" vnameCurr="RobVel_1" fullyObs="true">
<ValueEnum>
  sV0    sV1    sV2  	 
</ValueEnum>
</StateVar>
<StateVar vnamePrev="PedPose_0" vnameCurr="PedPose_1" fullyObs="true">
<ValueEnum>  
sx00y00    sx00y01    sx00y02    sx00y03    sx00y04    sx00y05    sx00y06    sx00y07    sx00y08    sx00y09    sx01y00    sx01y01    sx01y02    sx01y03    sx01y04    sx01y05    sx01y06    sx01y07    sx01y08    sx01y09    sx02y00    sx02y01    sx02y02    sx02y03    sx02y04    sx02y05    sx02y06    sx02y07    sx02y08    sx02y09    sx03y00    sx03y01    sx03y02    sx03y03    sx03y04    sx03y05    sx03y06    sx03y07    sx03y08    sx03y09   str 	 
</ValueEnum>
</StateVar>
<StateVar vnamePrev="PedGoal_0" vnameCurr="PedGoal_1" fullyObs="false">
<ValueEnum>
  G0    G1    G2    G3  	 
</ValueEnum>
</StateVar>
<ObsVar vname="oPed">
<ValueEnum>  
ox00y00    ox00y01    ox00y02    ox00y03    ox00y04    ox00y05    ox00y06    ox00y07    ox00y08    ox00y09    ox01y00    ox01y01    ox01y02    ox01y03    ox01y04    ox01y05    ox01y06    ox01y07    ox01y08    ox01y09    ox02y00    ox02y01    ox02y02    ox02y03    ox02y04    ox02y05    ox02y06    ox02y07    ox02y08    ox02y09    ox03y00    ox03y01    ox03y02    ox03y03    ox03y04    ox03y05    ox03y06    ox03y07    ox03y08    ox03y09   ostr 	 	
</ValueEnum>
</ObsVar>
<ActionVar vname="action_robot">
<ValueEnum> 
aCru  aAcc  aDec 	 	
</ValueEnum>
</ActionVar>
<RewardVar vname="reward_robot"/>
</Variable>
```

## Example

We provided a tigertest.cpp file in the root of the package, but you
need to copy it to a seperate node to run it as a client. Also you need
the Tiger.pomdpx and Tiger.policy in the examples/POMDPX folder.
