## Nodes

API below is for information purposes only. pr2_computer_monitor is only
supported to monitor PR2 computers and systems.

```clearsilver
node.0 {
  name=cpu_monitor.py
  desc=The CPU Monitor, `cpu_monitor.py`, monitors the temperature, usage, and NFS status of the host computers. It is launch when a robot launches as part of pr2_core. It publishes to /diagnostics on three status names: "<hostname> CPU Temperatures", "<hostname> CPU Usage", and "<hostname> NFS I/O".
  pub{
    0.name= /diagnostics
    0.type= diagnostic_msgs/DiagnosticArray
    0.desc= Diagnostics about the status of the CPU(s).
  }
  param{Knowing
    0.name=~check_core_temps
    0.type=boolean
    0.default=False
    0.desc=Whether to check core temparatures. Deprecated.
    1.name=~check_impi_tool
    1.type=boolean
    1.default=True
    1.desc=Whether to use ipmi_tool, which only works on some machines
    2.name=~enforce_clock_speed
    2.type=boolean
    2.default=True
    2.desc=If clock speed below 2240 MHz and this is engaged, gives warning. Error if speed below 2150 MHz
    3.name=~load1_threshold
    3.type=float
    3.default=5.0
    3.desc=Warn if 1 minute load average goes above this threshold.
    4.name=~load5_threshold
    4.type=float
    4.default=3.0
    4.desc=Warn if 5 minute load average goes above this threshold.
    5.name=~check_nfs
    5.type=boolean
    5.default=False
    5.desc=Give statistics on NFS (network filesystem). Deprecated.    
    6.name=~num_cores
    6.type=int
    6.default=8
    6.desc=Check that we have correct number of cores. If set to <0, disables the check.
  }
```

#### Usage

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
``` To try it locally: ```
roslaunch pr2_computer_monitor cpu_monitor.launch
```

#### Implementation details

\`cpumonitor.py\` uses command line tools to monitor the CPU. These
commands are called in timer threads every 10 seconds or so to keep load
down.

  -- ----------------------------------------- ------------ ------------------------------------------------------- -------------------------------------------------------------------------------------- --
     Command                                                Result                                                                                                                                         
     \`sudo ipmitool sdr\`                                  Temperature, fan speed, temperature alarms                                                                                                     
     \`cat /proc/cpuinfo                       grep MHz\`                                                           Clock speed of the computers, which shows them throttling if temperature is too high   
     \`uptime\`                                             Give load average, number of users                                                                                                             
     \`free -m\`                                            Free memory                                                                                                                                    
     \`mpstat -P ALL 1 1\`                                  CPU usage                                                                                                                                      
     \`find /sys/devices -name temp1_input\`                Gives names of CPU core temps, only called at startup                                                                                          
  -- ----------------------------------------- ------------ ------------------------------------------------------- -------------------------------------------------------------------------------------- --

```clearsilver
node.0 {
  name=hd_monitor.py
  desc=The HD Monitor, `hd_monitor.py`, monitors temperature and disk usage of the host's hard drive. It is launch on the PR2 as part of pr2_core. It publishes to /diagnostics on two status names: "<hostname> HD Temperature" and "<hostname> HD Usage" (optional).
  pub{
    0.name= /diagnostics
    0.type= diagnostic_msgs/DiagnosticArray
    0.desc= Diagnostics about the status of the HD(s).
  }
  param{
    0.name=~no_hd_temp_warn
    0.type=boolean
    0.default=False
    0.desc=If True, then don't warn if hard drive temp is too hot. Deprecated.
  }
```

#### Usage

Since many robots use a network filesystem and have the same files on
all machines, it doesn\'t make sense to monitor drive space on all
drives. ```
Usage: hd_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
``` If the HOME_DIR directory above isn\'t
specified, the monitor will not check disk space remaining.

To try it locally: ```
roslaunch pr2_computer_monitor hd_monitor.launch
```

#### Implementation details

\`hd_monitor.py\` uses command line tools to monitor the HD.

  -- ------------------------------------- -- ---------------------------------------------------- --
     Command                                  Result                                               
     \`df -P \--block-size=1G HOME_DIR\`      Disk space remaining on the user\'s home directory   
  -- ------------------------------------- -- ---------------------------------------------------- --

\`hd_monitor.py\` will only check the disk usage if the home directory
argument is set from the command line.

To check hard drive temperature, it opens a socket to hddtemp, a daemon
program running on most Linux machines. You can check if hddtemp is
working by running: ```
$ netcat localhost 7634
|/dev/sda|Hitachi HDT725032VLA360|43|C|
```

```clearsilver
node.0 {
  name=ntp_monitor.py
  desc=The NTP Monitor, `ntp_monitor.py`, monitors the offset between computer clocks on a robot, if the robot uses Network Time Protocol (NTP). It uses `ntpdate` to check the offset. It publishes to /diagnostics  with the names "NTP offset from <hostname> to <server>" and "NTP self-offset for <hostname>".
  pub{
    0.name= /diagnostics
    0.type= diagnostic_msgs/DiagnosticArray
    0.desc= Diagnostics about the status of NTP.
  }
```

#### Usage

```
Usage: ntp_monitor ntp-hostname []

Options:
  -h, --help            show this help message and exit
  --offset-tolerance=OFFSET-TOL
                        Offset from NTP host
  --self_offset-tolerance=SELF_OFFSET-TOL
                        Offset from self
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```

To try it locally: ```
roslaunch pr2_computer_monitor ntp_monitor.launch
```

#### Implementation Details

\`ntp_monitor.py\` uses ntpdate to check the offset in clocks, using the
NTP protocol. ```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```0 Give the offset from the NTP
server, and the computer\'s self offset.

#### Computer Clocks and Self-Offset

Each computer has two times: the time \`chrony\` thinks it is, and the
system time. When they disagree, \`chrony\` slowly slews the system time
until they match again. When you do \`ntpdate -q \<server\>\` you
compare host\'s chrony time with the local system time. Doing \`ntpdate
-q \<hostname\>\` allows you to verify that the chrony time and the
system time match.

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```1

#### Usage

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```2 (No command-line arguments).

#### Implementation Details

The \`nvidia_temp.py\` script uses the command:
```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```3 to check the status of the GPU. This command
must work without a password. Configure your sudoers file accordingly.

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```4

#### Usage

Here is a typical launch file entry for running it:

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```5

## Installation and setup

With proper system dependencies, \`pr2_computer_monitor\` can work on
almost any linux system. Use [rosdep](rosdep) to install required
packages from the operating system: ```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```6

### Verifying hddtemp Daemon

It\'s a good idea to verify the installation of \`hddtemp\`. To contact
\`hddtemp\` (which measures hard drive temperature),
pr2_computer_monitor opens a socket to the \`hddtemp\` daemon.

First, verify that the \`hddtemp\` daemon is running.

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```7 This opens a socket to the daemon, which by
default runs on port 7634. You should see something like:

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```8 If \`hddtemp\` isn\'t up and running, start it
by typing:

```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```9 This will start it in daemon mode. Replace
\"/dev/sda\" above with the name of your hard drive if it\'s different.

### Configuring ipmitool

Now, check if you have \`ipmitool\` installed correctly. If you choose
not to use ipmitool to monitor CPU temperature and fan speed, disable it
with \`check_ipmi_tool\` parameter to False. ```
roslaunch pr2_computer_monitor cpu_monitor.launch
```0
If this command returns with an error (below), then you will need to
disable the ipmitool checks using the \`check_ipmi_tool\` parameter.
```
roslaunch pr2_computer_monitor cpu_monitor.launch
```1

The \`ipmitool\` command needs to work properly without a password. If
the above command asks for a \"sudo\" password, you\'ll need to edit the
sudoers file: ```
roslaunch pr2_computer_monitor cpu_monitor.launch
```2 Add the following line to use
\`ipmitool\` without typing your password: ```
roslaunch pr2_computer_monitor cpu_monitor.launch
```3

### Other Configuration

If your computers uses NFS, then you should enable the \`check_nfs\`
parameter for CPU monitor. The NFS status messages will have no data if
not enabled.

CPU monitor will warn if the CPU cores start throttling below 2240 MHz.
This is appropriate for the PR2, but if your computer is different,
disable the \`enforce_clock_speed\` parameter.

------------------------------------------------------------------------
