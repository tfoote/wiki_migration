## Stability

This package is still unstable, and does not have a released API.

## Scripts

These scripts below have not been released and are still unstable, but
we we\'re still documenting them since they\'re being used as a part of
calibrating the PR2.

### propagate_config2.py

This script generates a calibrated URDF by combining an exisiting URDF
with the results of
[pr2_calibration_estimation](pr2_calibration_estimation).

\'\'\'\`./propagate_config\`\'\'\'\` \[initial.yaml\]
\[calibrated.yaml\] \[cal_measurements.bag\] \[cal_output.xml\]\`

-   \`\[initial.yaml\]\` - The system definition before running
    calibration
-   \`\[calibrated.yaml\]\` - The system definition after running
    calibration
-   \`\[cal_measurements.bag\]\` - Bagfile that contains the original
    URDF. The URDF must be availabe on the topic \`/robot_description\`
    as a \<\<MsgLink(std_msgs/String)\>\>
-   \`\[cal_output.xml\]\` - File to which to write the updated URDF

### propagate_baseline.py

This script should be run on a running robot in order to update a
stereocamera\'s baseline parameter.

\'\'\'\`./propagae_baseline.py\`\'\'\'\` camera:=\[camera_namespace\]
\[calibration_bagfile\] \[system_filename\] \[config_camera_name\]\`

-   \`\[camera_namespace\]\` - Ros name to prepend onto the call to
    set_calibration\"
-   \`\[config_filename\]\` - yaml file that stores the baseline shift\"
-   \`\[config_camera_name\]\` - Name of the camera in the system
    definition file. Tells script which baseline shift to use\"
