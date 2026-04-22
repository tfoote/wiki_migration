## Overview

This package provides an interface and basic utilities for monitor
hardware systems on the PR2 during production testing. This package does
not contain a stable or supported API, but it is used internally by
Willow Garage production team members to monitor hardware.

The node `pr2_hw_test_monitor` is can be run as a "monitor" to check
a robot of device under test. The monitor loads "listeners" to observe
look for specific events or conditions. The monitor polls the listeners
for status, and resets or halts listeners as necessary. Using different
listener configurations, the monitor can check almost any PR2 system or
sub-system.

The monitor node publishes
[pr2_self_test_msgs/msg/TestStatus](https://docs.ros.org/en/rolling/p/pr2_self_test_msgs/msg/TestStatus.html)
on the `test_status` topic with data it collects from listeners. It
also publishes
[diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)
on `diagnostics` that it collects from the listeners.

## Configuring a Monitor

### Listeners

Listeners should be subclasses of `pr2_hw_listener/PR2HWListenerBase`.

The `halt` and `reset` methods should halt or reset the device under
test. This could mean, for example, calling the
`pr2_etherCAT/reset_motors` service.

### Loading Listeners

Listeners are loaded by parameters in the private namespace of the
`pr2_hw_test_monitor` node. This example loads a `CameraListener`
and an `EthercatListener`: 

```
ethercat:
  type: EthercatListener
  file: ethercat_listener
camera:
  type: CameraListener
  file: camera_listener
```

 The parameters
`type` and `file` are mandatory, and specify the class name and
filename/submodule of the listener, respectively. The `file` is
assumed to be in the package `pr2_hardware_test_monitor`.

## Monitor Behavior

At the simplest level, the test monitor polls each listener at 1Hz to
check status. The listener returns a tuple of: 

```
level (int) : 0 - OK, 1 - WARN, 2 - ERROR, 3 - STALE
message (str) : Status message
diags ([ diagnostic_msgs/DiagnosticStatus ]) : Diagnostics to publish
```



The monitor collects the status level and message and publishes it to
the output topic `test_status` as a
[pr2_self_test_msg/msg/TestStatus](https://docs.ros.org/en/rolling/p/pr2_self_test_msg/msg/TestStatus.html).

### Output Level + Message

The output level is set to the maximum of the level of the listeners.

The message is assembled from a string of errors and warning messages.
If the status is "0", the message is "OK".

In order to detect transient errors, the monitor will "latch" errors
until it is reset. This latching happens after a grace period ends.

### Halt/Reset

The monitor advertises the services `halt_test` and `reset_test`
(both of type
[std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)).

When halted, the monitor calls the `halt` method on all listeners and
likewise on `reset`. Listeners must start or stop hardware, for
example by calling `pr2_etherCAT/reset_motors`.

After a reset, any latched errors are cleared and a 30 second grace
period begins. Any errors that occur in the 30 second grace period are
not latched.

### Exceptions and Error Conditions

The monitor node listens to a `/heartbeat` topic of type
[std_msgs/msg/Empty](https://docs.ros.org/en/rolling/p/std_msgs/msg/Empty.html).
If the there is not traffic on this topic for 300 seconds, the monitor
node will halt all listeners and report an error.

If any listener fails to load, the monitor will report an error with a
message of "Listener Startup Error". This can happen if either the
`type` or `file` parameters are not specified, a listener doesn't
exist, or a listener returns false on `create`.

## Monitor Node ROS API



```clearsilver
name = pr2_hw_test_monitor
desc = Monitors PR2 hardware testing
pub {
  0.name = /diagnostics
  0.type = diagnostics_msgs/DiagnosticArray
  0.desc = Diagnostics output from listeners

  1.name = test_status
  1.type = pr2_self_test_msgs/TestStatus
  1.desc = Status of test or device
}
sub {
  0.name = /heartbeat
  0.type = std_msgs/Empty
  0.desc = Heartbeat from Test Manager.
}
param {
  0.name = ~
  0.type = {}
  0.desc = Listener parameters
}
srv{
0.name= halt_test
0.type= std_srvs/Empty
0.desc= Halt monitor and listeners
1.name= reset_test
1.type= std_srvs/Empty
1.desc= Reset monitor and listeners
}
```



## Listener Info

Each listener is initialized using the `create()` method with a given
set of parameters. The descriptions below explain what parameters, if
any, a listener needs, and the ROS API of each listener.

### EtherCAT Listener

Monitors `pr2_etherCAT/motors_halted` and `calibrated` topics.
Reports an error if motors halted, and a warning if uncalibrated.

`halt` method halts motors, `reset` method resets them.

The EtherCAT Listener allows at most 10 net dropped packets per hour
during tests. Net dropped packets are defined as dropped packets minus
late packets. If more dropped packets are reported by "EtherCAT
Master" in the diagnostics, the listener will halt motors and report
"Dropped Packets". See.

Encoder errors will cause the listener to report an error. This error
will be cleared on `reset`.

Parameters:

-   `drops_per_hour` ( `int` ) : Allows users to specify a maximum
    packet drop rate. Default: 10.

### Transmission Listener

Monitors `pr2_transmission_check/trans_status` for status of all robot
transmissions. The [pr2_transmission_check](pr2_transmission_check) node
must be running for this to work.

The transmission listener can also check for casters slipping.


```yaml
trans:
  type: TransmissionListener
  file: trans_listener
  caster_slip: fl
```



This makes sure the caster does not slip more than a prescribed amount
during the caster burn in. When the caster slip detection is enabled,
the `TransmissionListener` will subscribe to
`pr2_controller_manager/mechanism_statistics` and verify the caster's
rotation.

### CameraListener

The !CameraListener listens for diagnostics from any `wge100` camera
node.

It will report an error if the camera reports error values three times
(consecutively), or goes more than five second before it reports an
"OK" reading.

The listener will report a warning for transient error conditions, like
when the camera reports a one-off error.

Reports stale if camera doesn't respond for 10 seconds.

A regression test in this package checks for this behavior.

### Diagnostics Aggregated Listener

Listens to the `/diagnostics_agg`
([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html))
to check for any problems in the diagnostics.

Parameters:

-   `ignore_diags` ( \[ `str` \] ) - Diagnostic categories to ignore
-   `whitelist` ( \[ `str` \] ) - Focus only on these categories of
    diagnostics.

### Hokuyo Listener

Monitors diagnostics from a [hokuyo_node](hokuyo_node) with the given
namespace. Reports a warning/error for any warning or error in the
diagnostics.

Parameters:

-   `name` ( `str` ) - Name of hokuyo node. Ex: `hokuyo_node`

### ECStats Listener

Listens to dropped packets and/or links from an `ecstats` node in the
`ectools` package.

### DriveListener

Listens to `base_driving`
([std_msgs/msg/Bool](https://docs.ros.org/en/rolling/p/std_msgs/msg/Bool.html)
topic and reports if PR2 is driving during burn in test.

-   Halt - Calls `pr2_base/halt_drive` service to stop driving.
-   Reset - Calls `pr2_base/reset_drive` service to start driving.
