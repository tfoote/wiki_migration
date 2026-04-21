This package provides a node with the following action servers:

-   Spawning of a collision model for the fridge given the fridge's x,y
    position and angle in the PR2's local frame, as provided by
    ds_pr2_fridge_drink perception (spawnFridgeAction).
-   Collision-free planning and execution for grasping a can from three
    predefined locations on the fridge shelf. (grabAction)

![\| height=640 ](attachment:fridge.png )

# Usage:



```
roslaunch pr2_drink_fetching_planner pr2_drink_fetching_planner.launch
```


