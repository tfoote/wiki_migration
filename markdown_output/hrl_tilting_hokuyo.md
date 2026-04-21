## Making the Rig

Servo part number, CAD models for mounting adaptors, instructions for
constructing the rig can be found here:

-   <http://www.hsi.gatech.edu/hrl-wiki/index.php/Tilting_Hokuyo>

## Getting a Point Cloud

**Before using this code to obtain point clouds, you need to:**

1\. have made a rig consisting of a Hokuyo mounted on a Robotis
servo. 1. be able use [robotis](robotis) to operate a Robotis servo. 1.
be able to use [hrl_hokuyo](hrl_hokuyo) to get scans from a Hokuyo.

**Once you have the rig set up:**

1\. `roscd hrl_hokuyo; roslaunch acm0_utm.launch`

1\. `roscd hrl_tilting_hokuyo/src/hrl_tilting_hokuyo`

1\. `python tilt_hokuyo_servo.py -h`

1\. Run it with appropriate parameters. For example:

-   `python tilt_hokuyo_servo.py -d /dev/ttyUSB0 -n0 \--save_scan
    \--speed=10 \--id=<servo id> \--l2=0.035`

1\. You should see the servo tilt the UTM between the two angles that
you specified.

1\. Once the code runs, it will save the scans in a pkl. (e.g.
`2009Oct05_203107_dict.pkl`)

1\. To view the point cloud, use `display_3d_mayavi.py` (`python
display_3d_mayavi.py -h`)

## Using the Code

Brief description of the different files in this package:

1\. **tilt_hokuyo_servo.py** - defines the class to obtain point clouds.

1\. **display_3d_mayavi.py** - Uses
[mayavi2](http://code.enthought.com/projects/mayavi/#Mayavi2) to display
point clouds.

1\. **processing_3d.py** - some functions for working with point clouds.
Includes segmenting doors, door handles, horizontal surfaces (tabletops,
countertops etc.), objects on a horizontal surface etc.

1\. **occupancy_grid_3d.py** - 3D occupancy grid implementation in
python.

## Troubleshooting

1\. Can you get scans from a Hokuyo using [hrl_hokuyo](hrl_hokuyo)? 1.
Can you use [robotis](robotis) to operate a servo? 1. Walls are not
vertical or walls and the ceiling do not seem to be at right angles in
the point cloud:

1\. `roscd hrl_tilting_hokuyo/doc`

1\. look at the file `servo_transforms.jpg`

1\. Ensure that l1 and l2 that you are specifying when you run
`tilt_hokuyo_servo.py` are correct.

1\. **Note:** l2 can be negative depending on how the UTM is mounted.
