## Overview

Designed as an upgrade to the 2011 app manager used on turtlebots and
pr2's.

## Current Implementation

### Features

The current version is a 0.7 version . It has the following features:

-   Advertises handles for `/platform_info`, `/list_rapps`,
    `/status` and `/invite` to external, gateway based ros systems.
-   When invited, it will flip `/start_rapp` and `/stop_rapp`
    services across to the ros system doing the inviting (the *remote
    controller*).
-   Launches and manages a single rapp (robot/rocon app) at a single
    time.
-   Flips the rapp specified connections to the *remote controller*.

### Advertised Services

These services are freely shared to any ros subsystem that wants to
consume them via the [gateway's](rocon_gateway) advertise/pull
mechanisms. The purpose is to provide introspection to the robot (i.e.
the system that runs the app manager) to make a decision as to whether
it wishes to assume control of the robot. Assuming control is managed by
making a request to invite the robot.

```clearsilver
srv{
  no_header=True
  1{
  name = platform_info
  type = rocon_app_manager_msgs/GetPlatformInfo
  desc = Provide a description of the robot via a platform tuple.
  }
  2{
  name = list_rapps
  type = rocon_app_manager_msgs/GetRappList
  desc = List apps that are available/installable on the robot.
  }
  3{
  name = status
  type = rocon_app_manager_msgs/Status
  desc = Status of the app manager (busy, idle, running an app or not).
  }
  4{
  name = invite
  type = rocon_app_manager_msgs/Invite
  desc = Request to assume control of the app manager (start_rapp, stop_rapp).
  }
```

### Controller Services

These services are only flipped after an invitation has been made.

```clearsilver
srv{
  no_header=True
  1{
  name = start_rapp
  type = rocon_app_manager_msgs/StartRapp
  desc = Start the requested rapp.
  }
  2{
  name = stop_rapp
  type = rocon_app_manager_msgs/StopRapp
  desc = Stop the requested rapp.
  }
```

## Standalone Mode Launcher parameters

The list of arguments to use for standalone mode robot launcher.
[rocon_app_manager/standalone.launch](https://github.com/robotics-in-concert/rocon_app_platform/blob/indigo/rocon_app_manager/launch/standalone.launch)

```
Required Arguments:
  auto_start_rapp: autostart a rapp, e.g. rocon_apps/talker
Optional Arguments:
  auto_rapp_installation (default "false"): http://wiki.ros.org/rocon_app_manager/Tutorials/indigo/Automatic Rapp Installation
  capabilities (default "false"): enable/disable a capability server
  capabilities_blacklist (default "[]"): blacklist specific capabilities
  capabilities_nodelet_manager_name (default "capability_server_nodelet_manager")
  capabilities_package_whitelist (default "[std_capabilities]"): get capabilities from these packages only
  capabilities_parameters (default "/opt/ros/indigo/share/rocon_app_manager/param/capabilities.yaml"): detailed parameter configuration for the providers
  capabilities_server_name (default "capability_server") 
  interactions (default "false")
  interactions_list (default "[]")
  rapp_package_blacklist (default "[]")
  rapp_package_whitelist (default "[rocon_apps]"): comma separated list of package names
  rapp_preferred_configuration_file (default "/opt/ros/indigo/share/rocon_app_manager/param/preferred_default.yaml")
  robot_description (default "To err is human, to 'arr is pirate.")
  robot_icon (default "rocon_icons/cybernetic_pirate.png") 
  robot_name (default "Cybernetic Pirate") 
  robot_type (default "pc")
  rosbridge_address (default "localhost")
  rosbridge_port (default "9090")
  screen (default "true"): verbose output from running apps
  simulation (default "false"): if simulated robot
  zeroconf (default "false")
  zeroconf_name (default "Cybernetic Pirate")
  zeroconf_port (default "11311")
```

## Concert Mode Launcher parameters

The list of arguments to use for concert mode robot launcher.
[rocon_app_manager/concert_client.launch](https://github.com/robotics-in-concert/rocon_app_platform/blob/indigo/rocon_app_manager/launch/standalone.launch)

```
Required Arguments:
  concert_uri: configure concert hub uri for direct connection.
Optional Arguments:
  capabilities (default "false"): enables/disables a default capability server in this concert client
  capabilities_blacklist (default "[]"): blacklist specific capabilities
  capabilities_package_whitelist (default "[]"): get capabilities from these packages only (e.g. std_capabilities)
  capabilities_parameters (default "/opt/ros/indigo/share/rocon_app_manager/param/capabilities.yaml"): detailed parameter configuration for the providers
  concert_watch_period (default "10"): the period used by gateways for watching concert connections
  concert_whitelist (default "[]"): list of concert names this robot will work with
  disable_zeroconf (default "false"): disable zeroconfiguration
  firewall (default "false"): typically false (don't let anything in), only for simulation clients
  interactions (default "false")
  interactions_list (default "[]")
  local_machine_only (default "false"): only work with local concerts (testing, simulations)
  rapp_auto_installation (default "false"): http://wiki.ros.org/rocon_app_manager/Tutorials/indigo/Automatic Rapp Installation
  rapp_package_blacklist (default "[]")
  rapp_package_whitelist (default "[rocon_apps]"): comma separated list of package names
  rapp_preferred_configuration_file (default "/opt/ros/indigo/share/rocon_app_manager/param/preferred_default.yaml")
  robot_description (default "To err is human, to 'arr is pirate.")
  robot_icon (default "rocon_icons/cybernetic_pirate.png")
  robot_name (default "Cybernetic Pirate")
  robot_type (default "turtlebot")
  robot_unique_name (default "true"): postfix a uuid to the robot name for uniqueness
  screen (default "false"): verbose output from running apps
  simulation (default "false"): if simulated robot
```
