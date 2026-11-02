## Nodes

API below is for information purposes only. pr2_computer_monitor is only
supported to monitor PR2 computers and systems.

### cpu_monitor.py

The CPU Monitor, `cpu_monitor.py`, monitors the temperature, usage,
and NFS status of the host computers. It is launch when a robot launches
as part of pr2_core. It publishes to /diagnostics on three status names:
"<hostname> CPU Temperatures", "<hostname> CPU Usage", and
"<hostname> NFS I/O".

#### Published Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Diagnostics about the status of the CPU(s).

#### Usage



```
Usage: cpu_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```

 To try it locally: 

```
roslaunch pr2_computer_monitor cpu_monitor.launch
```



#### Implementation details

`cpumonitor.py` uses command line tools to monitor the CPU. These
commands are called in timer threads every 10 seconds or so to keep load
down.

  -- ----------------------------------------- ------------ ------------------------------------------------------- -------------------------------------------------------------------------------------- --
     Command                                                Result                                                                                                                                         
     `sudo ipmitool sdr`                                  Temperature, fan speed, temperature alarms                                                                                                     
     `cat /proc/cpuinfo                       grep MHz`                                                           Clock speed of the computers, which shows them throttling if temperature is too high   
     `uptime`                                             Give load average, number of users                                                                                                             
     `free -m`                                            Free memory                                                                                                                                    
     `mpstat -P ALL 1 1`                                  CPU usage                                                                                                                                      
     `find /sys/devices -name temp1_input`                Gives names of CPU core temps, only called at startup                                                                                          
  -- ----------------------------------------- ------------ ------------------------------------------------------- -------------------------------------------------------------------------------------- --

### hd_monitor.py

The HD Monitor, `hd_monitor.py`, monitors temperature and disk usage
of the host's hard drive. It is launch on the PR2 as part of pr2_core.
It publishes to /diagnostics on two status names: "<hostname> HD
Temperature" and "<hostname> HD Usage" (optional).

#### Published Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Diagnostics about the status of the HD(s).

#### Parameters

- `~no_hd_temp_warn` (`boolean`, default: `False`): If True, then don't
  warn if hard drive temp is too hot. Deprecated.

#### Usage

Since many robots use a network filesystem and have the same files on
all machines, it doesn't make sense to monitor drive space on all
drives. 

```
Usage: hd_monitor.py [--diag-hostname=cX]

Options:
  -h, --help            show this help message and exit
  --diag-hostname=DIAG_HOSTNAME
                        Computer name in diagnostics output (ex: 'c1')
```

 If the HOME_DIR directory above isn't
specified, the monitor will not check disk space remaining.

To try it locally: 

```
roslaunch pr2_computer_monitor hd_monitor.launch
```



#### Implementation details

`hd_monitor.py` uses command line tools to monitor the HD.

  -- ------------------------------------- -- ---------------------------------------------------- --
     Command                                  Result                                               
     `df -P \--block-size=1G HOME_DIR`      Disk space remaining on the user's home directory   
  -- ------------------------------------- -- ---------------------------------------------------- --

`hd_monitor.py` will only check the disk usage if the home directory
argument is set from the command line.

To check hard drive temperature, it opens a socket to hddtemp, a daemon
program running on most Linux machines. You can check if hddtemp is
working by running: 

```
$ netcat localhost 7634
|/dev/sda|Hitachi HDT725032VLA360|43|C|
```



### ntp_monitor.py

The NTP Monitor, `ntp_monitor.py`, monitors the offset between
computer clocks on a robot, if the robot uses Network Time Protocol
(NTP). It uses `ntpdate` to check the offset. It publishes to
/diagnostics with the names "NTP offset from <hostname> to
<server>" and "NTP self-offset for <hostname>".

#### Published Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Diagnostics about the status of NTP.

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



To try it locally: 

```
roslaunch pr2_computer_monitor ntp_monitor.launch
```



#### Implementation Details

`ntp_monitor.py` uses ntpdate to check the offset in clocks, using the
NTP protocol. 

```
ntpdate -q <server>
ntpdate -q <hostname>
```

 Give the offset from the NTP
server, and the computer's self offset.

#### Computer Clocks and Self-Offset

Each computer has two times: the time `chrony` thinks it is, and the
system time. When they disagree, `chrony` slowly slews the system time
until they match again. When you do `ntpdate -q <server>` you
compare host's chrony time with the local system time. Doing `ntpdate
-q <hostname>` allows you to verify that the chrony time and the
system time match.

### nvidia_temp.py

This node monitors an NVIDIA GPU for temperature and usage statistics.

#### Published Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Diagnostics about the status of NTP.
- `gpu_status`
  ([pr2_msgs/msg/GPUStatus](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/GPUStatus.html)):
  Machine readable status of the GPU

#### Usage



```
Usage: nvidia_temp.py
```

 (No command-line arguments).

#### Implementation Details

The `nvidia_temp.py` script uses the command: 

```
sudo nvidia-smi -a
```


to check the status of the GPU. This command must work without a
password. Configure your sudoers file accordingly.

### network_detector

The network detector, `network_detector`, monitors a given network
interface (such as "eth0") and publishes whether it is up and running
(connected) or not. The purpose is to detect **wired** network
connections, so the robot can avoid driving and yanking out its network
cable. Finding which network interface (if any) really represents a
wired connection must be done by the person who configures the robot. On
the PR2, this is "wan0" on computer C1.

#### Published Topics

- `/network/connected`
  ([std_msgs/msg/Bool](https://docs.ros.org/en/rolling/p/std_msgs/msg/Bool.html)):
  True if the interface exists and is connected, false otherwise.

#### Parameters

- `~interface_name` (`string`, default: `none`): Name of the network
  interface to monitor, for example "eth0" or "wan0".

#### Usage

Here is a typical launch file entry for running it:



```
<node pkg="pr2_computer_monitor" type="network_detector" name="network_detector" output="screen">
    <param name="interface_name" value="wan0"/>
  </node>
```



## Installation and setup

With proper system dependencies, `pr2_computer_monitor` can work on
almost any linux system. Use [rosdep](rosdep) to install required
packages from the operating system: 

```
$ rosdep install pr2_computer_monitor
```



### Verifying hddtemp Daemon

It's a good idea to verify the installation of `hddtemp`. To contact
`hddtemp` (which measures hard drive temperature),
pr2_computer_monitor opens a socket to the `hddtemp` daemon.

First, verify that the `hddtemp` daemon is running.



```
$ netcat localhost 7634
```

 This opens a socket to the daemon, which by
default runs on port 7634. You should see something like:



```
|/dev/sda|Hitachi HDT725032VLA360|41|C|
```

 If `hddtemp` isn't up and running, start it
by typing:



```
sudo hddtemp -d /dev/sda
```

 This will start it in daemon mode. Replace
"/dev/sda" above with the name of your hard drive if it's different.

### Configuring ipmitool

Now, check if you have `ipmitool` installed correctly. If you choose
not to use ipmitool to monitor CPU temperature and fan speed, disable it
with `check_ipmi_tool` parameter to False. 

```
sudo ipmitool sdr
```


If this command returns with an error (below), then you will need to
disable the ipmitool checks using the `check_ipmi_tool` parameter.


```
$ sudo ipmitool sdr
Could not open device at /dev/ipmi0 or /dev/ipmi/0 or /dev/ipmidev/0: No such file or directory
Get Device ID command failed
Unable to open SDR for reading
```



The `ipmitool` command needs to work properly without a password. If
the above command asks for a "sudo" password, you'll need to edit the
sudoers file: 

```
sudo visudo
```

 Add the following line to use
`ipmitool` without typing your password: 

```
sudo ipmitool sdr ALL NOPASSWD
```



### Other Configuration

If your computers uses NFS, then you should enable the `check_nfs`
parameter for CPU monitor. The NFS status messages will have no data if
not enabled.

CPU monitor will warn if the CPU cores start throttling below 2240 MHz.
This is appropriate for the PR2, but if your computer is different,
disable the `enforce_clock_speed` parameter.

------------------------------------------------------------------------

## Troubleshooting

### Errors when using pr2_computer_monitor

#### Error: CPU Temperature Error/Bad Reading

**Errors from CPU Temperature:** The diagnostics show an error under the
"CPU Temperature" heading, and it says it has a bad reading. This is
probably because the commands that `cpu_monitor.py` use to check the
computer aren't working.

**Solution:**

- Check the pr2_computer_monitor
  page for the implementation details. You should be able to run all the
  commands without an error.

#### NTP Offset Error

If you see an error under "NTP offset from <hostname> to
<server>", check if the "<server>" is available using `ntpdate
-q`. 

```
ntpdate -q my_server.my_server.com
```

 If this command returns an error,
`ntp_monitor.py` will fail to update. Correct the server name and try
again.

`ntp_monitor.py` also checks the offset for a computer against itself.
Check that this command works: 

```
ntpdate -q MY_HOSTNAME
```



Restarting "chrony" may work: 

```
sudo service chrony restart
```



#### CPU monitor reports "CPU Fan Off"

In the diagnostics data, you will see the fan speeds listed for each
CPU, and the "MB Fan RPM" data. If any of these fans is off, then the
PR2 computers will overheat and loose performance. This is a serious
problem with the PR2.

#### CPU monitor reports "Restarting temperature check thread"

The CPU monitor checks core temperatures using `ipmitool`. On
occasion, these calls to `ipmitool` can fail, and hang the thread that
checks temperatures. The CPU monitor will restart the temperature
checking thread and publish a warning to the console:


```
Restarting temperature check thread in cpu_monitor. This should not happen
```

 This problem is explained in.
