## Summary

Planning algorithms for doing human in the loop manipulation. Contains
an implementation of HPN (Hierarchical Planning in the Now) planner by
Leslie Pack Kaelbling and Tomás Lozano-Pérez has been implemented. Also
has implements a goal regression planner for doing flat task planning.

## How to Get the Code

To get the code directly from version control, add the following to your
.rosinstall: ```
- svn: {local-name: electric_sandbox, uri: 'https://code.ros.org/svn/wg-ros-pkg/branches/trunk_electric/electric_sandbox'}
```

## How to Run the Example

```
roscd hierarchical_interactive_planning
``` ```
python examples/set_table/set_table.py plan_tree.dot
```
```
dot plan_tree.dot -Tpng -o plan_tree.png
``` ```
display plan_tree.png
```
