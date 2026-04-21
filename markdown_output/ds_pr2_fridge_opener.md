The package provides an action server for opening and closing the fridge
with the PR2 robot as well as an action server for moving the base. In
the drink serving demo the closing of the fridge action was** not**
used. ![](attachment:openning_fridge.jpg)

# Usage:

## Start the action server:

```
roslaunch ds_pr2_fridge_opener open_close_fridge.launch
```

## OpenFridge Action Definition

```
#goal
float32 x
float32 y
float32 u
float32 z
---
#result
int32 SUCCESS=1
int32 FAILURE=0
int32 result
---
#feedback
```

## Calling OpenFridge Action

Please see example in
[ds_pr2_fridge_manipulation_executive](ds_pr2_fridge_manipulation_executive)
package.
