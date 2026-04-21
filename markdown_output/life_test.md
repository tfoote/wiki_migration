## Overview

The Test Manager system starts, stops and monitors hardware tests on
robot components.

To start Test Manager: ```
rosrun life_test test_manager.py
``` You can enable a "debug
mode" by giving a "\--debug" option.

To use Test Manager, scan a component serial number into the starting
box. Select which test to run and proceed.

### Role of Test Manager

In the WG hardware testing system, Test Manager oversees the burn
in/life testing system.

-   Loading/launching life tests/burn in tests
-   Monitoring and displaying test output
-   Logging and reporting data to the WG inventory system

## Implementation Details

### Software Modules

Modules for the Test Manager application.

#### Configuration Loading

Modules `config_loader.py`, `test_bay.py`, `test_param.py` and
`result_dir.py` store configuration data for different tests and
"rooms". These modules are well covered by a unit test.

#### GUI

Modules `manager.py` and `test_monitor_panel.py` contain the GUI.
Test Manager is not a model-view-controller piece of software, and the
GUI isn't separated from the implementation. These modules have no test
coverage.

#### Logging / Invent

The module `test_record.py` contains the logger for processing the
status of each test. This modules is well-tested in
[test_pr2_self_test](test_pr2_self_test). A script in
`test_pr2_self_test/test/test_invent` tests that Test Manager logs can
be submitted to Invent properly.

### Configuration Files

#### Tests

The file `life_test/tests.xml` loads details about individual tests.
Each test is assigned to a serial number, and a serial number may have
more than one test.

```xml
<tests>
  <test serial="faketes" name="Simple Test" 
        id="fake-burn" debug="true"
	short="Fake" duration="40"
	desc="Test to test life GUI"
	script="simple_test/test.launch" 
        power="false" type="Life Test" >
</tests>
```

The fields under the "test" tag include:

-   **serial** - First 7 serial digits number of the device under test.
-   **name** - Full name of test
-   **id** - ID of test, used for creating test BoM
-   **short** - Short name of test, displayed on title
-   **desc** - Test decription. Displayed in the "instructions" panel
-   **script** - Launch file to load. Path is given relative to the
    `life_test` package.
-   **power** - Whether the test needs power board enabled/disabled
-   **type** - String for type of test. Generally "Life Test".
-   **duration** - Test duration in hours. Set "0" or leave empty for
    continuous. Default: 0
-   **debug** - Whether the test can run outside of debug mode (default:
    False)

#### Test Room Configuration

The file `life_test/wg_test_rooms.xml` loads the configuration files
for each room and test "bay". A "bay" is a place where a test can be
run. Only one test can run in a bay at a time. Each room has multiple
bays.

```xml
<rooms>
  <room hostname="ckb" >
    <bay name="ckb"   machine="ckb"   board="1002" breaker="2" />
    <bay name="testi" machine="testi" board="1001" breaker="1" />
  </room>
</rooms>
```

The "hostname" of a room is the complete hostname of the master
computer. All slaves are given in "bay" tags.

Fields for "bay" tag:

-   **name** - Name of bay.
-   **machine** - Hostname of bay
-   **board** - Power board serial (ex: 1000). Optional
-   **breaker** - 0, 1, 2. Optional If the power board and breaker
    aren't specified, tests that need power won't be able to run on
    that bay.

Note that a single machine can have multiple bays.

#### Modifying Configuration

Both files can be reloaded while Test Manager is running through the
menu at the top. If either file fails to load, the Test Manager will
warn the user and continue using the original configuration. These files
are checked by the regression test, and be tested by calling "make
test" in the package `life_test`.

### Launching Tests

Tests are launched in the ROS namespace of the bay they are running in.
For example, launching a gripper life test in bay "testq" puts the
entire test in the "testq" namespace.

Global topics, parameters and services will not work for any test
running in the Test Manager system. The only exception is the
`/diagnostics` and `/tf` topics, which are remapped to
`/BAY/diagnostics` and `/BAY/tf` by the Test Manager.

The test launch file is included into a main Test Manager launch file
and launched in the bay namespace. This additional main launch file
contains:

-   Remaps from /diagnostics to /BAY/diagnostics, /tf to /BAY/tf
-   Machine tags:
-   `localhost` : Test Manager machine
-   `test_host` : Remote machine to run test. Default.
-   [rosbag](rosbag) recorders for diagnostics and motor trace data.

A [power board node](pr2_power_board) is started by Test Manager when
any test that needs power is launched. The power is controlled through
the ROS service interface to the power board node.

### Monitoring Tests

Test Manager users
[pr2_hardware_test_monitor](pr2_hardware_test_monitor) to monitor the
status and progress of tests. It listens to the `/BAY/test_status`
topic for each bay and logs progress and updates. This monitor must be
included in the launch file of the test.

The monitor determines the status of the test as "OK", "Warning",
"Error" or "Stale". The "elapsed time" counter for a test will
only advance if the status is "OK". If Test Manager does not receive
data from the monitor for 180 seconds, it will shut down the test and
disable the power.

### Heartbeat Topic

The `/heartbeat` topic is published at 1Hz. This is used as a
"deadman" or "keepalive" by the monitors. Any monitor that does not
receive a heartbeat will report "No Heartbeat" and halt. The "Run"
button will reset this condition.

### Log Files

Test Manager generates CSV log files in the
`/wg_hardware_test/test_manager` directory. These files are tarred up
and loaded into the inventory system by Test Manager at the end of every
test (when the "Close" button on each panel is pressed).

A note is added to the inventory system during each test. The note
updates with the current status and progress of the test approximately
every 10 minutes.

### Bag Files

Diagnostics, and motor traces are recorded into bag files in the
`/hwlog` directory. Bags are stored with the serial number of the
device-under-test in the filename.

## Test Manager ROS API

```clearsilver
name = test_manager.py
desc = Starts, stops and logs all WG burn in tests
sub {
  0.name = /NAMESPACE/test_status
  0.type = pr2_self_test_msgs/TestStatus
  0.desc = Status for each device-under-test
  1.name = /NAMESPACE/diagnostics
  1.type = diagnostic_msgs/DiagnosticArray
  1.desc = Diagnostics for each device-under-test (displayed in runtime_monitor)
  2.name = /diagnostics
  2.type = diagnostic_msgs/DiagnosticArray
  2.desc = Diagnostics, for power board info
}
pub {
  0.name = /test_info
  0.type = pr2_self_test_msgs/TestInfoArray
  0.desc = Current status of all devices under test.
  1.name = /heartbeat
  1.type = std_msgs/Empty
  1.desc = Heartbeat or keepalive for any slaves.
}
```

## Additional Documentation

[PR2 Burn In Test Overview](/PR2 Burn In)

Links to relevant tutorials:

[Starting the Test Status Viewer](/Starting Test Viewer)
