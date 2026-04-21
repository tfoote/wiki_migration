## ROS API

To interact with controllers form another ROS node, the controller
manager provides five service calls:



```clearsilver
node.0 {
  name = pr2_controller_manager
  pub {
    0.name = task_manger/available_tasks
    0.type = continuous_ops_msgs/TaskList
    0.desc = The list of tasks that can be scheduled
    1.name = task_manger/scheduled_tasks
    1.type = continuous_ops_msgs/TaskList
    1.desc = The list of tasks that are already scheduled
  }
  srv {
    0.name = task_manager/add_task
    0.type = continuous_ops_msgs/AddTask
    0.desc = Add a new task to the task queue by providing the task_id
    1.name = task_manager/remove_task
    1.type = continuous_ops_msgs/ChangeTask
    1.desc = Remove a task from the task queue by providing the run_id
    2.name = task_manager/start_task
    2.type = continuous_ops_msgs/ChangeTask
    2.desc = Start a task from the task queue by providing the run_id
    3.name = task_manager/stop_task
    3.type = continuous_ops_msgs/ChangeTask
    3.desc = Stop a task from the task queue by providing the run_id
    4.name = task_manager/get_available_tasks
    4.type = continuous_ops_msgs/GetTaskList
    4.desc = Get the list of tasks that can be scheduled
    5.name = task_manager/get_scheduled_tasks
    5.type = continuous_ops_msgs/ReorderTaskList
    5.desc = Change the order of the scheduled task list
    6.name = task_manager/reorder_task
    6.type = continuous_ops_msgs/ChangeTask
    6.desc = Stop a task from the task queue by providing the run_id
  }
}
```


