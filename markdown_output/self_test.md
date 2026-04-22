## Running a Self-Test

You can get a list of the available subtests with the rosservice
command:

```
$ rosservice list | grep "/self_test$"
/hokuyo_node/self_test
```



You can then run the self test using rosservice:

```
$ rosservice call /hokuyo_node/self_test
```



You can get different output with the *deprecated* `run_selftest`
node: 

```
$ rosrun self_test run_selftest /hokuyo_node/self_test
```



## C++ API

The
[self_test::TestRunner](http://www.ros.org/doc/api/self_test/html/classself__test_1_1TestRunner.html)
class will advertise a service "self_test". When called, it will
perform a check on the node's connection status, and any other checks a
developer wants to perform on a node or device.

An example use of the self_test package's API can be found in
[self_test/src/selftest_example.cpp](https://github.com/ros/diagnostics/blob/hydro-devel/self_test/src/selftest_example.cpp).

### Stability and Status

The documented C++ and ROS API should be considered stable.

### self_test::TestRunner

self_test contains the
[self_test::TestRunner](http://www.ros.org/doc/api/self_test/html/classself__test_1_1TestRunner.html)
class that can be used to sequence a set of tests to be run in order to
test a device. It advertises a self_test service. When the service is
called, the `self_test::TestRunner` calls the tests that have been
defined in order, and combines the results into a
[diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)
array (see the service definition
[diagnostic_msgs/srv/SelfTest](https://docs.ros.org/en/rolling/p/diagnostic_msgs/srv/SelfTest.html)).
A detailed example can be found in
[self_test/src/selftest_example.cpp](https://github.com/ros/diagnostics/blob/hydro-devel/self_test/src/selftest_example.cpp).

## Nodes



```clearsilver
node {
 0{
 name = selftest_rostest
 desc = A rostest that runs a self-test and reports success if the self-test passed.
 param {
  0{
  name= ~node_to_test
  type= string
  default= ""
  desc= Name of the node to run the self-test on.
  }
  1{
  name= ~max_delay
  type= string
  default= 60
  desc= Maximum amount of time to wait for the `self_test` service to show up.
  }
 }
```


