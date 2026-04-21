The continuous operation executive is a [smach](smach) state machine
that starts/stops tasks, and monitors the battery level.

### Low battery

When the battery level drops below 30%, the executive sends a preempt
signal to the currently running task. This task gets 5 minutes time to
quit and leave the robot in a state where it can navigate. This means
that after the task quits, the robot should not be holding anything, not
be too close to any obstacle, not be behind a closed door, etc. When a
task does not quit within the allocated 5 minutes, it will get killed.

When the robot does not have any scheduled tasks, it will go charge
itself once the battery level drops below 70%.

![\|width="750"](attachment:executive.png)

### High battery

The robot remains plugged in until the battery level reaches 90%. At
this time, the robot will unplug itself if there are any scheduled
tasks. If any task got interrupted when the robot was low on battery,
this task will get started again. So a task will only get removed from
the task queue when it is completed.
