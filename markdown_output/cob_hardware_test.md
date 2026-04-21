## Documentation

### Simple Testing

Connect to the Robot with `ssh -X ...` and start the tests with


```
rostest cob_hardware_test robot.test test_auto:=true
```

 Auto tests are mainly sensor tests and do not
require user interaction.



```
rostest cob_hardware_test robot.test test_manual:=true
```

 Manual tests will make the robot moving and
require user interaction.
