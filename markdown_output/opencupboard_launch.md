## Overview

This package contains launch files for the opencupboard stack.

-   **opendoors_executive.launch** begins the detection and grasping
    servers and the force controller for the arms.

Launch files more specific to the action are located in those packages.
These include

-   [opencupboard_launch](opencupboard_launch)/yaml/(your cabinet's
    yaml).yaml: Loads the yaml file you write with the parameters for
    the cupboard you are opening.
-   [pr2_tabletop_manipulation_launch](pr2_tabletop_manipulation_launch)/launch/pr2_tabletop_manipulation.launch:
    Loads tabletop manipulation used in detection.
-   [ee_cart_imped_launch](ee_cart_imped_launch)/launch/load_ee_cart_imped.launch:
    Loads the force controller for the arms
-   [opencupboard_launch](opencupboard_launch)/launch/open_toaster.launch:
    specially made for the bakebot demo

```{=html}
<!-- -->
```
-   grasp_handle.py: Begins the action for the handle grasping
-   door_processing_server: Begins the server to detect the door
-   object_processing_server: Begins the server to detect the handle
-   open_cupboard.py: Begins the action to open the cupboard
