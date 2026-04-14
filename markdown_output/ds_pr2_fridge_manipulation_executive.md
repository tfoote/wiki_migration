The pr2_fridge_manipulation_executive serves as an intermediate layer
between the master_executive and all action_servers provided in the
ds_pr2\_\* packages. It contains a statemachine that responds to two
types of action requests for the PR2:

-   retrieving a drink from the fridge given the ID of the shelf rail.
    (PR2GetDrinkAction)
-   placing the drink on the busbot.(PR2PlaceDrinkOnTBotAction)

# Usage:

All nodes required for the state machine to complete the action requests
are launched by ```
roslaunch ds_pr2_fridge_manipulation_executive fridge_pr2.launch
```
