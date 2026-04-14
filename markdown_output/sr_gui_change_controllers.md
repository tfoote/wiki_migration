Use the change controllers plugin to either change the control type
PWM - Torque or load different types of controllers. Simply click on one
of the controller type buttons, and it will call a service from the
pr2_controller_manager to unload the currently running controllers if
necessary, and load the ones you selected. You can also stop the
currently running controller from this plugin. If you change the control
type (PWM - Torque) the controller type buttons will become unresponsive
for 3 seconds while waiting for the motor control hardware to complete
the change.

![Change controllers\|width=\"600\"](attachment:change_controllers.png)
