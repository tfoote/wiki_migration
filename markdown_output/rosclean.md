## rosclean command-line tool

Usage: ```
Usage: rosclean <command>

Commands:
  rosclean check	Check usage of log files
  rosclean purge	Remove log files
```

### rosclean check

Report the disk usage of ROS log files.

```
$ rosclean check
348K ROS node logs
20K rosmake logs
```

### rosclean purge

**WARNING: use with care. This will delete files from disk!**

`rosclean purge` will remove directories associated with storing
ROS-related log files. You will be asked to confirm each deletion and it
is important that you verify the command that `rosclean purge`
executes is correct. Otherwise you *may lose important files.*

```
$ rosclean purge
Purging ROS node logs.
PLEASE BE CAREFUL TO VERIFY THE COMMAND BELOW!
Okay to execute:

rm -rf /u/username/.ros/log
(y/n)?
```
