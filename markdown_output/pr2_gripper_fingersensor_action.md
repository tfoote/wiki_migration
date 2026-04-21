Ad-hoc structural review (08/03)

Replacemnt package for pr2_gripper_action which adds additional
functionality.

\--(- fingersensor -> _sensor - slipgrip_controller ->
pr2_gripper_sensor_controller - just call it controller and move actions
into controller directory)\--

\--(- all action definitions should go in pr2_gripper_sensor_msgs)\--

\--(- add in seperate zero SERVICE zero_fingertip_sensors. return
timestamp.)\--

\--(- force control action should return succeeded when the state of
force control is succesfully entered and force achieved. - need to
handle all states. such as not touching the tactile sensors)\--

\--(- change "place" to "gripper_sensor_event_detector")\--

\--(- need to ensure that each action monitors controller state and
handles changes appropriately.)\--

\- add in messages for state variables that define the different states

\- higher level action to just grab stuff. smash state machine to string
together

\--(- all finger forces should be something like
"fingertip_force".)\--

\--(- call motor effort something like "joint_effort" always)\--

\--(- slip servo should continue forver and give feedback)\--

\--(- add in "motors off" service and have all canceled actions fall
back to this)\--
