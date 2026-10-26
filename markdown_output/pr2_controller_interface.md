## The controller interface

To implement a real time controller, your controller needs to inherit
from the `pr2_controller_interface::Controller` base class. The base
class contains

- four methods you need to implement: init, starting, update and
  stopping, and
- one method you can call: getController.

The base class looks like this:



```cplusplus
namespace pr2_controller_interface
{
  class Controller
  {
  public:
    virtual bool init(pr2_mechanism_model::RobotState *robot, 
                     ros::NodeHandle &n);
    virtual void starting();
    virtual void update();
    virtual void stopping();

    bool getController(const std::string& name, 
                       int sched, 
                       ControllerType*& c);
  };
}
```



The image below gives the flowchart that shows in what order these four
methods are called (more details in the text below).

![\|width=550](attachment:controllers.png)

### Initializing the controller

The `init` method is executed in **non-realtime**. The `init` method
is called when you load a controller, to initialize the controller. Note
that initializing a controller is independent of starting it: the
initialization can be done any amount of time before starting the
controller. The `init` method takes two arguments:

- **robot**: this is a `pr2_mechanism_model::RobotState` that
  describes the robot model (see
  [pr2_mechanism_model](pr2_mechanism_model)). The model provides access
  to the robot joints (actuators, encoders, etc.), and contains a
  kinematic/dynamic description of the robot mechanism.
- **n**: this `ros::NodeHandle` is the "namespace" of the
  controller. In the namespace of this node handle, the controller can
  read configuration from the parameter server, advertise topics, etc.

The `init` method returns if the initialization was successful or not.
If the initialization fails, the controller will get unloaded by
[pr2_controller_manager](pr2_controller_manager). Make sure to always
use `ROS_ERROR("explanation");` to inform the user why your
controller failed to initialize. A controller can only be initialized
once. If you want to re-initialize a controller, you first need to
unload it, and then load it again.

### Starting the controller

The `starting` method is executed in **hard realtime**. The starting
method is called once every time a controller is started, by the
[controller manager](pr2_controller_manager). Starting is executed in
the same cycle as the first update call, right before this update call.

The `starting` method initializes the controller right before the
first time update is called. The
[controller manager](pr2_controller_manager) is allowed to re-start a
controller at a later time, without having to unload/load the
controller.

### Updating the controller

The `update` method is executed in **hard realtime**. The `update`
method of every controller is called periodically by
[pr2_controller_manager](pr2_controller_manager) at a frequency of 1000
Hz. This means that the execution time of all controllers combined
cannot take more than 1 mili-second. In the update loop, the real
control work is done.

### Stopping the controller

The `stopping` method is executed in **hard realtime**. The
`stopping` method is called once every time a controller is stopped.
Stopping is executed in the same cycle as the last update call, right
after this update call.

The `stopping` method does not return anything, it is not allowed to
fail.

### Requesting a pointer to another controller

The `getController` method is executed in **non-realtime**. The
`getController` method allows a controller to get a pointer to another
controller. This is used to create a "chain" of controllers, where
each controller sends its output to the next controller, **in
realtime**. This system is a poor replacement of the non-realtime ROS
communication.

The `getController` method takes three arguments:

- **name**: a string with the name of the controller you would like to
  get a pointer to.
- **sched**: An int (ENUM) this specifies if the requested controller
  should be executed before or after your controller. Possible values
  are `pr2_controller_interface:BEFORE_ME` and
  `pr2_controller_interface::AFTER_ME`.
- **c** This is a pointer to the controller you requested, with the type
  matching the type of the requested controller. The type is also the
  template argument for the `getController` method.
