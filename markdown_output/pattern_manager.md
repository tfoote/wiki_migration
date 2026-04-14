## What is pattern_manager?

Simply put, pattern_manager is a tool for describing, arranging, and
managing transforms. This package allows you to create a tree of
transforms and to iterate through selected transforms within that tree.
This is done by manually \'activating\' transforms for iteration and
specifying the order in which they should be iterated.

An obvious example of an application of such a tool is in palletizing
processes, where there is possibly multiple pallets with various layers
that need to be picked or placed in a certain order. The pattern_manager
node streamlines batch processing of structured parts by affording tools
to easily set up and manage the iteration of such processes.

The package additionally features methods for easily generating a number
of predefined (but extendable) patterns of transforms such as: linear,
rectangular, circular etc.

Patterns of transforms can be grouped with other patterns. Additionally,
these groupings can also be sub-grouped. This enables the user to
combine multiple (groups of) patterns, which in turn allows seamless
iteration through multiple patterns, as if it was one pattern.

The following is an example of such a structure:

```
root [tf0]                      # <transform-name> [<transform-number>]
    ├── grp1 [tf1]                  # transform as pattern group/container
    │   ├── lin1 [tf2]              # ex. linear pattern of transforms
    │   │   ├── lin1_1 [tf3]           
    │   │   ├── lin1_2 [tf4]
    │   │   ├── lin1_3 [tf5]
    │   │   └── ...
    │   └── lin2 [tf11]
    │       ├── lin2_1 [tf12]           
    │       ├── lin2_2 [tf13]
    │       └── lin2_3 [tf14]
    ├── grp2 [tf6]
    │   ├── grp3 [tf7]
    │   │   ├── rect1 [tf8]         # ex. rectangular pattern of transforms
    │   │   │   ├── rect1_1 [tf9]
    │   │   │   ├── rect1_2 [tf10]
    │   │   │   └── ...
    │   │   └── ...
    │   └── ...
    └── ...
```

For information on how to specifically perform these operations, please
check out the tutorials for getting started with pattern_manager below.

## Tutorials

A list of tutorials for getting started with pattern_manager can be
found on the tutorials page [here](pattern_manager/Tutorials). These
tutorials cover interaction with the pattern_manager node via ROS
service calls using CLI.

An RQt-plugin has also been created as a GUI for pattern_manager. It can
be found
[here](https://github.com/teknologisk-institut/rqt_pattern_manager.git).

![\|height=\"558px\",width=\"334px\"](attachment:rqt_pattern_manager.png)
![\|height=\"380px\",width=\"275px\"](attachment:rqt_pattern_manager2.png)

Currently,
[rqt_pattern_manager](https://github.com/teknologisk-institut/rqt_pattern_manager.git)
only exists as source files on [github.com](https://github.com/),
although an official release is planned for sometime in the future.
