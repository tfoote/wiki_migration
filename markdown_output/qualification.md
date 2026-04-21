## Overview

The qualification system is the core of the
[wg_hardware_test](wg_hardware_test) stack. This system allows Willow
Garage production team members to test, evaluate and debug hardware
components of the PR2 or Texai.

**Note:** The qualification system is only designed to run on specific
machines at Willow Garage. This package has no external ROS or code API.
Tools in this package will not work without proper configuration and/or
authorization into Willow Garage systems.

### Run GUI

To run the qualification GUI, go to the \"Applications\" menu on a test
system, select \"WG Hardware Applications\" and run \"PR2
Qualification\".

To run from the command-line, run: ```
rosrun qualification qualify.py
``` A
\`\--debug\` option will enable debug mode. This is for developers only.

## Qualification System Overview

The qualification system takes any serialized part, tests it, and logs
the data.

### Invent Logs

Parts that pass qualification are marked with in Invent with their
\"Test Status\" key set to \"PASS\". Failed components are marked with
\"Test Status\" set to \"FAIL\".

Test data in the form of tarfile attachments are loaded to Invent. Test
parameters and measurements are also loaded to Invent so they can be
[analyzed](wgtest_data_analysis) later. The log files are stored in the
\"/wg_hardware_test/qualification\" directory before they are sent to
Invent.

### ROS Structure of Qualification

#### roslaunch_caller

Subtests, pre-startup scripts and shutdown scripts are run as separate
processes and launched using [roslaunch_caller](roslaunch_caller).

#### Service Calls

The Qualification Manager advertises services to communicate with
different subprocesses.

-   \`prestartup_done\`
    (\<\<SrvLink(pr2_self_test_msgs/ScriptDone)\>\>) - When pre-startup
    scripts terminate.
-   \`test_result\` (\<\<SrvLink(pr2_self_test_msgs/TestResult)\>\>) -
    For subtests that complete.
-   \`shutdown_done\` (\<\<SrvLink(pr2_self_test_msgs/ScriptDone)\>\>) -
    When shutdown scripts terminate.

These services are only advertised when it there is a corresponding
test, pre-startup script or shutdown script running.

#### Parameters

The qualification system sets parameters to configure different scripts.
All parameters outside the following namespaces are wiped after each
qualification test.

-   \`/invent\` - Inventory username and password are stored on
    parameter server.
-   \`/qualification\` - Parameters used for the qualification system
    itself. Includes:
-   \`power_board\` - \"serial\", \"breaker0\", etc of power board.
    \"serial\" is XXXX, \"breaker0\" is True/False.
-   \`serial\` - Serial number of device-under-test.
-   \`test_name\` - Test name

### Flow of Qualification Tests

The qualification start page shows a prompt for a serial number and a
\"Continue\" button. When an operator scans a part and presses
\"Continue\", they are asked to select the correct test to run.

The following parts are launch files that are launched during the
qualification system. Each launch file is specified in the \"test.xml\"
file for a particular test.

#### Instructions

Instructions are loaded after a test is selected. The instructions page
is an HTML document. Any images specified in the document are given
relative to their local path. If \"Cancel\" is pressed while the
instructions are displayed, the qualification system will return to the
start screen and the device-under-test will **not** be marked as a
failure. Pressing \"Cancel\" at any other time will fail the component.

#### Pre-startup Scripts

These launch files run after \"Continue\" is pressed from the
instructions. Each prestartup script is designed to prepare the
device-under-test and the fixture for testing. Prestartup scripts call a
ROS service when they are complete. The service response can be:

-   **OK**
-   **FAIL** - The component is unable to be tested.
-   **ERROR** - The fixture is not ready or improperly set up. Note: Any
    \"errors\" at the pretest level will not mark the component as
    \"FAIL\".

Pre-startup scripts are torn down when the ROS service is called, the
operator presses cancel, or a timeout is hit.

#### Startup Script

The startup script runs after the pre-startup scripts and before the
subtests are launched. It generally loads any drivers or controllers
needed to operate the device. It is only torn down when the test is
complete.

#### Subtests

Subtests are launched sequentially. They terminate with a ROS service
call, when \"Cancel\" is pressed, or after a timeout.

#### Shutdown Scripts

These scripts deactivate the test fixture after a test is complete. A
shutdown script will always be called when the test is terminated, no
matter what stage it was terminated in. The most common shutdown script
disables power to the device under test.

### Qualification Manager

The \`qualify.py\` script runs the qualification manager (GUI). Here is
an overview of the relevant components of the qualification manager.

#### Configuration Loading

Modules \`result_dir.py\`, \`test.py\`, \`test_loader.py\` and
\`wg_station.py\` load the configuration files to run the qualification
station, and set up the environment. These modules are well covered by a
unit test.

#### Manager / GUI

The core of the GUI is in \`qual_frame.py\` and \`component_qual.py\`.
These modules have no software tests. The module \`cont_frame.py\` is
for continuous operation of the qual system, an experimental feature.

#### Logging and Invent

The \`result.py\` module processes qualification results and submits
them to Invent. This module has software tests in
[test_pr2_self_test](test_pr2_self_test).

There is a script in \`test_pr2_self_test/test/test_invent\` that tests
that valid qualification data can be loaded to Invent. Any changes to
Invent submitting should be checked with that script.

### More Info

See also:

-   [Scripts](/Scripts) - Scripts that the qualification system uses to
    run tests.
-   [wg_invent_client](wg_invent_client) - Client API for WG inventory
    system.
-   [roslaunch_caller](roslaunch_caller) - Utility for launching nodes
    programmatically.

## Writing Qualification Tests

See [Writing Qualification Tests](/WritingQualificationTests) info page.
For configuration scripts, see
[Component Configuration](/ComponentConfiguration).

### Component Qualification

The component qualification system run tests like hysteresis tests on
different sub-assemblies of the robot. To qualify hardware, technicians
scan components into the system. Each serial number corresponds to one
or more tests to qualify different types of components. Each test is
described in an XML file (ex: \"tests.xml\") that has pretests, startup
scripts, subtests and shutdown tests. Most tests include:

-   Programming MCB\'s (using fwprog)
-   Configuring MCB\'s for different components (using motorconf)
-   Startup script to launch pr2_etherCAT
-   \"Checkout\" test to make sure all component plugged in
-   Hysteresis tests for each joint Each subtest calls a
    \<\<SrvLink(pr2_self_test_msgs/TestResult)\>\> service call, which
    gives the text of the result, a pass/fail indicator, and any plots
    from the tests. Subtests can pass automatically, which starts the
    next test automatically, or can request a human pass/fail input. The
    different subtests give the mechanical state of each component, and
    careful analysis of the data can show wear and failure modes. The
    system stores data automatically into the inventory system.

### Component Configuration

The configuration system is used to reconfigure components (casters,
grippers, cameras, etc) for installation on a robot. It can program a
component as a left or right unit.

## Test Machine Configuration

In order for the qualification system to run on a new machine, the
following conditions must be me.

### Accounts

You will need an account in the WG Inventory System or \"Invent\". You
may set up the default Invent username and password by using the
environment variables \`INVENT_USERNAME\` and \`INVENT_PASSWORD\`.

### Permissions

The \`/hwlog\` directory must be read/writable to the user. The
qualification system will write bag files of diagnostics to that
directory.

The user home directory must be read/writable to the user. Temporary log
files are written in \`/wg_hardware_test\`.

### Configuration Files

The file \`wg_map.xml\` contains the entries for each computer or
(\"station\") that the qualification system can run on. Any new machine
must be added to this file.

```
<station gui="qual2.willowgarage.com" host="qual2" 
	   powerboard="1009" breaker0="True"
           breaker1="True" breaker2="True" >
    <env name="ECAT_PORT" value="ecat0" />
  </station>
```

Parameters in the \"station\" tag:

-   \`gui\` - GUI host for qual system. Should be complete hostname
-   \`host\` - Test host. Tests can run on separate machine..
-   \`powerboard\` \[ optional \] - Power board serial number (ex:
    \"1002\"). Default: None
-   \`breaker##\` \[ optional \] - Breaker \[0-2\]. Whether that breaker
    is enabled by the power system. Default: False
-   \`env\` \[ optional \] - Any environment variables specific to this
    machine. Set by the qualification system when the machine is loaded.

When the qualification system starts up, it determines which station the
GUI is running on, and sets the power board and environment parameters
as necessary.
