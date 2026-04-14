## About

The \`rail_pick_and_place_tools\` package contains rviz plugins to aid
in the grasp demonstration collection and model generation process. This
package also contains launch files for easier running of this process.

## rviz Plugins

This package contains three rviz panels: Vision, Grasp Collection, and
Object Model Generation, shown and described below.

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------------------------------------- --
     \'\'\'Vision Panel\'\'\' - calls segmentation action and provides segmentation feedback.                                                                                                                                                                                                                                                                                           ![\| width=436](attachment:vision_panel.png )             
     \'\'\'Grasp Collection Panel\'\'\' - collects demonstration grasps and point cloud information, stored in a [graspdb](graspdb) database, and provides feedback on this process.                                                                                                                                                                                                    ![\| width=436](attachment:grasp_collection_panel.png )   
     \'\'\'Object Model Generation Panel\'\'\' - calls the model generation action on a selected subset of grasp demonstrations and object models read from a [graspdb](graspdb) database, stores new models in the database, and provides feedback on this process. The highlighted model in the list can also be displayed in the main rviz window or removed from the database.      ![\| width=487](attachment:model_generation.png )         
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------------------------------------- --

## Installation

To install the \`rail_pick_and_place\` package, you can install from
source with the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/rail_pick_and_place.git
cd ..
catkin_make
catkin_make install
```

## Startup

The \`rail_pick_and_place_tools\` package contains a launch file for
starting up the backend necessary for grasp demonstration collection and
object model generation, as well as a frontend that launches rviz with
the relevant panels and topics shown:

. ```
roslaunch rail_pick_and_place_tools model_generation_backend.launch
```

. ```
roslaunch rail_pick_and_place_tools model_generation_frontend.launch
```

The frontend should look something like this:

![\| width=800](attachment:interface_full.png )

See the tutorials section for detailed instructions on setting the
parameters necessary for the launch files and using the frontend to
collect data and generate models.
