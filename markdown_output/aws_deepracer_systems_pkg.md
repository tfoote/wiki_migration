## Overview

The
[DeepRacer Systems ROS package](https://github.com/aws-deepracer/aws-deepracer-systems-pkg)
creates the software_update_node, model_loader_node, otg_control_node,
network_monitor_node which are part of the core AWS DeepRacer
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
name = software_update_node
sub {
  0{
   name = /usb_monitor_pkg/usb_file_system_notification
   type = msg/USBFileSystemNotificationMsg
   desc = This message holds the file/folder details that is broadcasted, whenever a watched file is identified in the USB connected.
   }
  1{
   name = /deepracer_systems_pkg/network_connection_status
   type = msg/NetworkConnectionStatus
   desc = This message with network connection status to indicate if the device is connected to the internet.
   }
}
pub {
  0{
   name = /deepracer_systems_pkg/software_update_pct
   type = msg/SoftwareUpdatePctMsg
   desc = Publish a message with current software update percentage and status.
   }
}

srv {
  1{
   name = software_update_check
   type = srv/SoftwareUpdateCheckSrv
   desc = A service that is called to check if a software update is available for aws-deepracer-* packages.
  }
  2{
   name = begin_update
   type = srv/BeginSoftwareUpdateSrv
   desc = A service that is called to execute the software update and install latest deepracer packages.
  }
  4{
   name = software_update_state
   type = srv/SoftwareUpdateStateSrv
   desc = A service that is called to get the current software update state on the vehicle. Values include [ UPDATE_UNKNOWN, UP_TO_DATE, UPDATE_AVAILABLE, UPDATE_PENDING, UPDATE_IN_PROGRESS ].
   }
}

srv_called {
  1{
   name = /status_led_pkg/led_blink
   type = srv/SetStatusLedBlinkSrv
   desc = Client to the status LED blink service that is called to indicate progress of software update operation.
  }
  2{
   name = /status_led_pkg/led_solid
   type = srv/SetStatusLedSolidSrv
   desc = Client to the status LED solid service that is called to indicate success/failure of software update operation.
  }
  3{
   name = /usb_monitor_pkg/usb_file_system_subscribe
   type = srv/USBFileSystemSubscribeSrv
   desc = Client to USB File system subscription service to add  "update" folder to watchlist and trigger notification if it finds it in the USB drive.
   }
  4{
   name = /usb_monitor_pkg/usb_mount_point_manager
   type = srv/USBMountPointManagerSrv
   desc = Client to USB Mount point manager service to indicate that the usb_monitor_node can safely decrement the counter for the mount point once the action function for the "update" folder file being watched by software_update_node is succesfully executed.
   }
}
```

```clearsilver

name = model_loader_node

pub {
  0{
   name = /usb_monitor_pkg/usb_file_system_notification
   type = msg/USBFileSystemNotificationMsg
   desc = This message holds the file/folder details that is broadcasted, whenever a watched file is identified in the USB connected.
   }
}

srv {
  1{
   name = verify_model_ready
   type = srv/VerifyModelReadySrv
   desc = A service that is called when a new model is loaded to verify if the model was extracted successfully.
  }
  2{
   name = console_model_action
   type = srv/ConsoleModelActionSrv
   desc = A service that is called with actions to upload/delete models from device console. It supports actions to extract and copy a tar.gz file with model that was uploaded from the console or delete a model that is present in the /opt/aws/deepracer/artifacts folder.
  }
}

srv_called {
  1{
   name = /status_led_pkg/led_blink
   type = srv/SetStatusLedBlinkSrv
   desc = Client to the status LED blink service that is called to indicate progress of load model operation
  }
  2{
   name = /status_led_pkg/led_solid
   type = srv/SetStatusLedSolidSrv
   desc = Client to the status LED solid service that is called to indicate success/failure of load model operation.
  }
  3{
   name = /usb_monitor_pkg/usb_file_system_subscribe
   type = srv/USBFileSystemSubscribeSrv
   desc = Client to USB File system subscription service to add  "models" folder to watchlist and trigger notification if it finds it in the USB drive.
   }
  4{
   name = /usb_monitor_pkg/usb_mount_point_manager
   type = srv/USBMountPointManagerSrv
   desc = Client to USB Mount point manager service to indicate that the usb_monitor_node can safely decrement the counter for the mount point once the action function for the "models" folder file being watched by model_loader_node is succesfully executed.
   }
   5{
   name = /model_optimizer_pkg/model_optimizer_server
   type = srv/ModelOptimizeSrv
   desc = Client to model optimizer service that is called to optimize the models that is loaded from the USB and create the intermediate representation of the models.
   }
}
```

```clearsilver

name = otg_control_node

srv {
  1{
   name = get_otg_link_state
   type = srv/OTGLinkStateSrv
   desc = A service that is called to return the flag if host is connected to the device via the micro-USB cable.
  }
}
```

```clearsilver

name = network_monitor_node

sub {
  0{
   name = /usb_monitor_pkg/usb_file_system_notification
   type = msg/USBFileSystemNotificationMsg
   desc = This message holds the file/folder details that is broadcasted, whenever a watched file is identified in the USB connected.
   }
}

pub {
  0{
   name = /deepracer_systems_pkg/network_connection_status
   type = msg/NetworkConnectionStatus
   desc = Publish a message with network connection status to indicate if the device is connected to the internet.
   }
}

srv_called {
  1{
   name = /status_led_pkg/led_blink
   type = srv/SetStatusLedBlinkSrv
   desc = Client to the status LED blink service that is called to indicate progress of WiFi connection operation.
  }
  2{
   name = /status_led_pkg/led_solid
   type = srv/SetStatusLedSolidSrv
   desc = Client to the status LED solid service that is called to indicate success/failure of WiFi connection operation.
  }
  3{
   name = /usb_monitor_pkg/usb_file_system_subscribe
   type = srv/USBFileSystemSubscribeSrv
   desc = Client to USB File system subscription service to add  wifi-creds.txt file to watchlist and trigger notification if it finds it in the USB drive.
   }
  4{
   name = /usb_monitor_pkg/usb_mount_point_manager
   type = srv/USBMountPointManagerSrv
   desc = Client to USB Mount point manager service to indicate that the usb_monitor_node can safely decrement the counter for the mount point once the action function for the for the WiFi configuration file being watched by network_monitor_node is succesfully executed.
   }
}
```
