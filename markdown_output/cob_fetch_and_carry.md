## Usage

Start bringup.

```
roslaunch cob_fetch_and_carry fetch_and_carry.launch
```

Including base movements ```
rosrun cob_fetch_and_carry fetch_and_carry.py
``` Without base movements
```
rosrun cob_fetch_and_carry only_grasping.py
```

Trigger new task ```
rosrun cob_fetch_and_carry trigger_new_task.py
``` press \"1\" to serve a drink

Select object ```
rosrun cob_fetch_and_carry order_client.py milk
```
