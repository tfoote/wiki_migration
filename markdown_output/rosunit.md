## Overview

`rosunit` is an internal tool for running unit tests within ROS. While
it can be run by a regular user, most users will generally use
`rosunit` indirectly via [rosbuild](rosbuild) test macros. The main
feature that `rosunit` provides is terminating a unit test based on a
timeout and generating an appropriate test failure. The rosbuild system
uses this feature to ensure that unit tests properly terminate.

`rosunit` currently supports:

-   gtest
-   Python `unittest` (via [rostest](rostest) wrappers)

The library that comes with `rosunit` can be used as described at
[unittest#Code-level_Python_Unit_Tests](unittest#Code-level_Python_Unit_Tests)

## Usage



```
$ rosrun rosunit rosunit -h

Usage: rosunit [options] <file> [test args...]

Options:
  -h, --help            show this help message and exit
  -t, --text            Run with stdout output instead of XML output
  --time-limit=TIME_LIMIT
                        Set time limit for test
  --name=TEST_NAME      Test name
```

 . `-t`, `\--text` . Runs a gtest-compatible
executable inside of a process monitor. If the test does not succeed
within the time limit (default 1 minute), the test is killed and marked
as a failure. Executable is not run within a ROS graph. `\--name` .
Set test name. Test name defaults to name of executable. This option
should be set when running wrapped tests, e.g. with `python`.
`\--time-limit` . Time limit for test.

## Helper Scripts

These helper scripts are intended for use only by the
[rosbuild](rosbuild) and test reporting infrastructure.

`clean_junit_xml.py`

. Aggregate test results in `test_results/_hudson`, stripping any
characters that cause Hudson trouble.

`check_test_ran.py <test-file.xml>`

`check_test_ran.py \--rostest <pkg-name> <test-file.xml>`

. Look for test results file. If none exists, write new test results
file that indicates test failure. If the `\--rostest` option is passed
in, it will use rostest's filename-generation scheme to look or the
correct test file.

`summarize_results.py <package>`

. Summarize test results for a single package.

`test_results_dir.py`

. Print the directory that test results are written to.

`pycoverage_to_html.py`

. Generate HTML versions of `coverage.py` test results.

## Roadmap

Historically, rosunit is based on a refactoring of [rostest](rostest).
It provides the unit-test infrastructure and rostest provides the
integration test infrastructure. rostest is also allowed to interact
with a running ROS graph.

The initial separation was not perfect. There is more room to migrate
more code from rostest into rosunit. Similarly, there is code within
rosunit that would be better supported by a graph-less version of
[roslaunch](roslaunch), i.e. a process monitor unattached to a ROS
master. Until that happens, rosunit contains code that is a copy of
internal libraries within roslaunch.
