## Overview

When you run make in this package, it simply copies the files from the
released directory to the include and compiled_firmware directories. The
protocol headers are then used in the
[sr_edc_ethercat_drivers](sr_edc_ethercat_drivers) and
[sr_robot_lib](sr_robot_lib) to interpret the incoming packets.

The compiled firmware can be used in the bootloader plugin of the
[sr_control_gui](sr_control_gui) to update the firmware of the motors.

## Development Use

\'\'\'\'NB: For internal use at Shadow only\'\'\'\'

If you set the \'\'\'INTERNAL_FIRMWARE\'\'\' environment variable to 1,
then we\'ll download the latest version of the protocol and also the
latest compiled firmware from our internal svn (this is only possible if
you\'re working for Shadow).

If you\'re ready to make a relased firmware, just run make release in
the package. This will copy the files to the released directory, write
the current versions of the different software in the
tested_version.yaml file, and tag the current bzr revision with the
revisions as well.
