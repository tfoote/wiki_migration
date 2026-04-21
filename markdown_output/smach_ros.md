## ROS integration

For example, if you want to call an [actionlib](actionlib) action from
SMACH, you can of course write a
[generic state](smach/Tutorials/Generic State), which would look
something like this: 

```python
  class ManualActionState(smach.State):
     def __init__(self, outcomes=['succeeded', 
                                  'aborted',
                                  'preempted']):
       self.action_client = SimpleActionClient('action_name',
                                               ActionType)
       self.action_client.wait_for_server()

     
     def execute(self, userdata):
       goal = ActionGoal()
       ret = self.action_client.send_goal_and_wait
       if ret == ActionStatus.SUCCEEDED:
          return 'succeeded'
       elif ret == ActionStatus.PREEMPTED:
          return 'preempted'
       elif ret == ActionStatus.ABORTED:
          return 'aborted' 


sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           ManualActionState(),
                           rransitions={'succeeded':'APPROACH_PLUG'})
```

 But you can call that same
action with much less coding, using the !SimpleActionState:


```python
sm = StateMachine(['succeeded','aborted','preempted'])
with sm:
    smach.StateMachine.add('TRIGGER_GRIPPER',
                           SimpleActionState('action_server_namespace',
                                             ActionState),
                           transitions={'succeeded':'APPROACH_PLUG'})
```



SMACH ROS offers the same type of support for ROS services and ROS
topics. For more details take a look at the
[tutorials](smach/Tutorials).
