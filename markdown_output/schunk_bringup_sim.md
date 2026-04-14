## Usage

The following simulated Schunk components are available

-   standalone 7-DOF lwa, `lwa.launch`
-   standalone 6-DOF powerball arm, `powerball.launch`
-   standalone sdh, `sdh.launch`
-   7-DOF lwa with sdh, `lwa_sdh.launch`

You can spawn the components in an empty gazebo world using the
corresponding launch files, e.g. ```
roslaunch schunk_bringup_sim lwa_sdh.launch
```
