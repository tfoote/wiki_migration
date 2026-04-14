## Overview

The
[DeepRacer USB Monitor ROS package](https://github.com/aws-deepracer/aws-deepracer-usb-monitor-pkg)
creates the usb_monitor_node which is part of the core AWS DeepRacer
application and will be launched from the
[deepracer_launcher](https://github.com/aws-deepracer/aws-deepracer-launcher).
More details about the application and the components can be found
[here](https://github.com/aws-deepracer/aws-deepracer-launcher).

### License

The source code is released under
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Foxy

## Node Details

```clearsilver
name = usb_monitor_node
pub {
  0{
   name = /usb_monitor_pkg/usb_file_system_notification
   type = msg/USBFileSystemNotificationMsg
   desc = Publisher to broadcast the notification messages when any of the files/folders that are in the watchlist are found in the USB drive.
   }
}

srv {
  1{
   name = usb_file_system_subscribe
   type = srv/USBFileSystemSubscribeSrv
   desc = Service that is called to add files/folders to the watchlist so that when they are found in the USB drive, a file system notification will be triggered.
  }
  2{
   name = usb_mount_point_manager
   type = srv/USBMountPointManagerSrv
   desc = Service exposing the functionality to safely increment/decrement the reference counter for the mount points.
  }
}
```
