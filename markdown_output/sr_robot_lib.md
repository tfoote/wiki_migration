## Overview

The sr_robot_lib package is where the incoming etherCAT packets are
interpreted and stored in the correct structured to be made available
for the controllers.

This package also contains a class which builds the etherCAT command we
want to send to the hand, based on the configuration file
[motor_data_polling.yaml](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config/motor_data_polling.yaml),
the data is updated at different rates.

## Config files

The
[config](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config)
folder contains most of the configuration for the hand driver (except
the controller configuration):

-   [calibration.yaml](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config/calibration.yaml)
    is the calibration table for the different joints. You can calibrate
    the hand using the hand_calibration plugin in
    [sr_control_gui](sr_control_gui)
-   [friction_compensation.yaml](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config/friction_compensation.yaml)
    contains the different [friction maps](sr_friction_compensation).
-   [joint_to_motor_mapping.yaml](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config/joint_to_motor_mapping.yaml)
    is where the mapping from a given joint to a motor index is defined.
-   [motor_data_polling.yaml](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config/motor_data_polling.yaml)
    contains the different update rates.
-   [sensor_to_joint.yaml](http://bazaar.launchpad.net/~shadowrobot/sr-ros-interface-ethercat/sr_hand_palm_edc/view/head:/sr_robot_lib/config/sensor_to_joint.yaml)
    contains the mapping between the joints and the sensors: for example
    FFJ0 is the sum of FFJ1 and FFJ2, while THJ5, which is a compound
    sensor is the sum of THJ5a+THJ5b.
