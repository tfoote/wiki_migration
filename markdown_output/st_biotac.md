------------------------------------------------------------------------

***This page is currently under development, please check back in the
future for updates***

Welcome to !SynTouch\'s new ROS package **st_biotac**. !SynTouch is
currently developing this package to process !BioTac data collected from
supported hardware (such as [st_cheetah](st_cheetah)).

For more information visit:
[SynTouch Website](http://www.syntouchllc.com)

------------------------------------------------------------------------

# Package Summary (temp)

This package contains all messages specific to the SynTouch stack,
configuration of data acquisition hardware, as well as the *future home*
for other useful tools for programming with the !BioTacs (such as a GUI,
data saving utilities, and other functions relevant to the status of the
!BioTac).

-   Authors: Abhishek Pawar, Gary Lin, and Jeremy Fishel, contact:
    ros@syntouchllc.com
-   Maintained by: Abhishek Pawar / abhishek.pawar@syntouchllc.com
-   License: GPL
-   External Website: <http://www.syntouchllc.com>
-   Source: (software currently under development)

## Overview

This is the main package of the SynTouch stack for interfacing with the
BioTac tactile sensor. It provides the messages used by other packages
in the stack.

### Planned Development

-   *GUI for visualizing BioTac data*
-   *Data saving tools for exporting to CSV*

## ROS API

*** INSERT ROS API FIGURE ***

### Subscribed Topics

-   **biotacs/\<port_name\>**: the BioTac data coming from the specified
    port (i.e. a port named \"left_hand\" would have the topic name\"
    biotacs/left_hand). Each sample appears as a new message for
    compatibility across different hardware. The configuration
    properties of each port are described below.

### Published Topics

```html
<a name="msgs"></a>
```

### Messages Explained

-   **!BioTac_Port_Data**: data published from supported acquisition
    hardware port. It contains:
-   *float64 time_stamp* The time at which samples were taken in ROS
    time.
-   *std_msg/string channel_id* The name of the sample channel collected
    (can be \"Pac\", \"Pdc\", \"Tac\", \"Tdc\", or *En* where n
    represents the electrode number, see the BioTac wiki page for
    additional details)
-   *int16\[\] Biotac_Data* Contains an array of integers of BioTac
    measurements. The length of the array is equal to the number of
    !BioTacs supported by the hardware. Values range from 0 to 4095 for
    connected !BioTacs; -1 is passed for !BioTacs that are not connected
    or the data is corrupted during transmission (i.e. has bad parity).

## Installation Instructions

```
UPDATE WHEN COMPLETE
```

## Contributing

If you are interested in contributing to the development of this stack
or would like to add or help us add new function to a package please
contact us at ros@syntouchllc.com

## Support

If you encounter a problem or need support please contact us at
ros@syntouchllc.com

------------------------------------------------------------------------
