## Usage

From command line run:



```
rosrun muse_bldc_motor_drive muse_bldc_motor_drive
```

 Now *muse* node publishes a list with Muse
Drives that are visible on the network and is ready to listen to your
commands.

Node runs in default frequencies: 1KHz for both feedback and
control/state machine commands.

If you want to set another value for these frequencies, you can run:



```
rosrun muse_bldc_motor_drive muse_bldc_motor_drive <feedback_frequency(Hz)> <control_frequency(Hz)>
```

 Note: There is no point in setting higher value
for feedback frequency. However, you can decrease it, if you do not need
it to be so high, or your network cannot handle such a high frequency.

Now you can create your own node, that publishes commands to muse node
and subscribes to desirable topics.

## Nodes

### muse_bldc_motor_drive

#### Published Topics

muse/module_discovery (muse_bldc_motor_drive/module_list.msg)

. Provides a *list* with all active Muse Modules, that are visible
through current network and the *number* of them. The *list* provides
some information for each module: module name, module ip, module status.

<feedback_topic_name> (muse_bldc_motor_drive/feedback.msg)

. Provides the *name* of current Muse Module and also, feedback -
*current \[A\], speed \[krpm\], position \[revs\], bus voltage \[V\],
temperature \[C\]* - possible *erros/faults, control mode and fsm
state*.

#### Subscribed Topics

muse/communication (muse_bldc_motor_drive/communication_cmd.msg)

. A command to open or close the topics needed for communication with a
single Muse Module. You have to set the ip or name of desired Module and
you choose the names of topics needed to send commands and get feedback
from it. You can get Module's name or ip from *muse/communication*
publisher and see if it's connected to the network.

<control_commands_topic_name> (muse_bldc_motor_drive/control_cmd.msg)

. An interface to send control commands to Muse Module. Commands
provided: . *SET_CONTROL_LIMITS * . *SET_CURRENT_GAINS * .
*SET_SPEED_GAINS * . *SET_POSITION_GAINS* . *SET_CURRENT* . *SET_SPEED*
. *SET_POSITION*

<state_machine_commands_topic_name>
(muse_bldc_motor_drive/state_machine_cmd.msg)

. An interface to send state machine commands to Muse Module. Commands
provided: . *CONNECT\
* . *DISCONNECT\
* . *STARTUP\
* . *SHUTDOWN\
* . *ENABLE_SERVO\
* . *DISABLE_SERVO\
* . *CONTROL_ON\
* . *CONTROL_OFF\
* . *QUICK_ENABLE\
* . *CALIBRATE_ELEC_ANGLE_OFFSET\
* . *CALIBRATE_START\
* . *SET_NAME\
* . *CLEAR_FAULTS\
* . *CLEAR_ERRORS *

#### Parameters

control frequency(float64, default: 1000.0)

. This is the frequency that Muse Node can handle sent commands.

feedback frequency(float64, default: 1000.0)

. This is the frequency of published feedback from Muse Node.
