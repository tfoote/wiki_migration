(Now [pr2_ethercat](pr2_ethercat) in Hydro and later)

## Nodes

```clearsilver
node.0 {
  name=pr2_etherCAT
  desc=`pr2_etherCAT` is the node that executes the main loop for controlling the EtherCAT devices (including all motors) on the PR2.  It loads [[pr2_controller_manager]], which in turns loads and runs controllers that act directly on the robot's motors.  The ROS API detailed below is the interface for controlling `pr2_etherCAT` itself; as a result of loading the controllers, the `pr2_etherCAT` process offers a broader, and varying ROS API.  Superuser privileges are required to run `pr2_etherCAT`, to allow it to set its scheduling priority to run as a real-time process.  
  srv{
    0.name= pr2_etherCAT/reset_motors
    0.type= std_srvs/Empty
    0.desc= Reset the motors. This is required after a runstop is reset (by turning the red push-button on the back of the robot, or pressing the "Start" button on the wireless runstop), and after the motors have been halted via the `halt_motors` service.  Most often called from [[pr2_dashboard]].
    1.name= pr2_etherCAT/halt_motors
    1.type= std_srvs/Empty
    1.desc= Halt the motors.  To reset them, call `reset_motors`.  Most often called from [[pr2_dashboard]].
  }
```

#### Permissions

Running \`pr2_etherCAT\` requires the following \"capabilities\":

-   **CAP_IPC_LOCK** Lock memory (mlockall())
-   **CAP_SYS_NICE** Set real-time scheduling policies
-   **CAP_NET_RAW** Use raw sockets (for EtherCAT communications)
    Superuser has these capabilities, but they can also be granted to
    another executable by setting file system attributes on the
    executable file. The \`pr2_grant\` program is a setuid-root program
    which copies \`pr2_etherCAT\` to a part of the filesystem where
    attributes can be set (\`/var/tmp\`), and then grants the necessary
    capabilities to be able to run \`pr2_etherCAT\`.

#### Usage

```
Usage: ./pr2_etherCAT [options]
  Available options
    -i, --interface <interface> Connect to EtherCAT devices on this interface
    -x, --xml <file|param>      Load the robot description from this file or parameter name
    -u, --allow_unprogrammed    Allow control loop to run with unprogrammed devices
    -h, --help                  Print this message and exit
```

#### Example

\`pr2_etherCAT\` is usually executed from a launch file, such as
[pr2_bringup](pr2_bringup)/pr2.launch. Common configuration:
```
<node name="realtime_loop" machine="c1" launch-prefix="pr2_grant" pkg="pr2_etherCAT" type="pr2_etherCAT" args="-i ecat0 -x robot_description"/>
```

### pr2_grant

\`pr2_grant\` is a utility that allows a regular user to run
\`pr2_etherCAT\` with appropriate capabilities. See the section in
\`pr2_etherCAT\` on \"Permissions.\"

## reset_motors.py

\`reset_motors.py\` is a simple command-line script that calls the
\`pr2_ethercat/reset_motors\` service.

```
$ rosrun pr2_etherCAT reset_motors.py
```
