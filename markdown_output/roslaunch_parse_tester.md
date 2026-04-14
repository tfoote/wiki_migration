## Overview

{X} \'\'\'Warning:\'\'\' This package, and all tools within, are
deprecated. Use [CMakeLists](CMakeLists#rosbuild_add_roslaunch_check)
file to test all launch files.

\`roslaunch_parse_tester\` has tools that allow users to parse and check
launch files, or an entire package. It can be used with command line
tools, or as a library as part of a build test system.

Using various options, roslaunch_parse_tester can check:

-   XML syntax
-   Incomplete or poorly formed tags
-   Parameter file paths
-   Machine assignments
-   Node paths
-   Configuration errors

## Tools

### Launch Parser

\`launch_parser.py\` parses and checks a launch file.

```
Usage: ./launch_parser.py file [options]

Options:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output for roslaunch parsing
  -q, --quiet          Parser gives error explanations if not quiet
  --env=ENV,VAL        Environment variables,value for launch file
  -m, --machine        Check machine assignments for each node
  -n, --node_check     Check that node exists
  -c, --config_errors  Check configuration errors
```

### Package Parser

\`package_parse_test.py\` checks all the launch files in a package.
Users can choose to \"blacklist\" individual files or entire
directories.

```
Usage: ./package_parse_test.py PKG [options]

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output from roslaunch all launch files.
  -q, --quiet           Quiet output from for all results for all launch
files.
  -a, --check_all       Check all file, proceed anyway on failures
  --env=ENV,VAL         Environment variables,values for launch files
  -b BLACKLIST, --blacklist=BLACKLIST Known bad files. Give path from package
  --black_dir=BLACK_DIR Known bad directories, all files ignored.
  -m, --machine         Check that machines can be assigned
  -n, --node_check      Check that node exists
  -c, --config_errors   Check configuration errors
```

## RPT as a Python Library

\`roslaunch_parse_tester\` can be used as a library in a Python script,
and be added to an automated build test.

### Example

```python
from roslaunch_parse_tester.package_parse import ROSLaunchPackageParser

def check_pkg(pkg):
    env = { 'MY_ENV_VAR': 'my_val' }
    black_dirs = [ 'directories', 'that_shouldnt', 'be_checked' ]

    launch_file_parser = ROSLaunchPackageParser(pkg, environment = env, black_dirs = black_dirs,
                                                assign_machines = True, node_check = True,
                                                quiet = False, config_err_check = True)

    return launch_file_parser.check_package()
```
