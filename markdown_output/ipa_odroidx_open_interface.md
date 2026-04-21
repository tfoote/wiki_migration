This package provides a specialized implementation of iRobot's Create
Protocol Specification on an Atmel AVR micro-controller. This package is
available from:
<https://github.com/ipa-josh/ipa_lcrob/tree/master/ipa_odroidx_open_interface>.

## Hardware Design

This implementation, while providing a framework for communication with
the master using a variant of iRobot's Create Open Protocol
Specification
(<http://www.irobot.com/filelibrary/pdfs/hrd/create/Create%20Open%20Interface_v2.pdf>),
has been focused to give its services as a:

-   Dual Motor Controller.
-   Motor Position Notifier.
-   Battery Voltage Monitor.

This design has three UART communication ports. Communication with the
master is done with the help of hardware UART port (using Peter
Fleury's UARTLibrary
<http://homepage.hispeed.ch/peterfleury/avr-software.html#libs>) where
as the communication with the motors is done using two soft UART ports
which have been implemented using a custom implementation of Thomas
Martin's SOFTUART
(<http://www.siwawi.arubi.uni-kl.de/avr_projects/#softuart>). Whereas
for the battery voltage notifier an external voltage divider circuit has
been connected to one of the ADC on the motor controller board.

## Software Design

The tasks performed by the motor controller board can be distributed
into:

-   Initialization.
-   Main Loop.

### Initialization

Before the software can enter the main loop, all of the connected
devices must be initialized. The baud rate between the controller board
and the master is set to 115200 bps where as the the baud rate between
the motor controller board and the motors is set to 9600 bps. Two timers
are exclusively set up for soft UART communication. Initialization
string "EN\\n" is sent to both the motors to enable them and the
message "HO\\n" is sent to move the motors to home position. This
ensures that the encoder values start from the initial position. In
addition to that, a timer of 15 milliseconds is set up for polling the
motor position from both the motors and also is used in case the
"STREAM" command is used by the master.

### Main Loop

The main loop is an infinite loop which actuates the parsing function
and the polls the motors to update their positions and in case the
"STREAM" command is enabled, it generates its response. It can be
extended to poll the voltage reading from the battery.

## Open Interface Protocol Implementation

### Interaction with "turtlebot_node"

Since the motor controller board is required to interact with the
**turtlebot_node** package (<https://bitbucket.org/ipa-josh/turtlebot>,
branch: ipa_create) it is expected of it to implement certain protocol
commands to ensure compatibility. The turtlebot_node first sets the the
motor controller board to its required state (Off, Passive, Safe and
Full) and expects the motor controller to save the state as specified as
it uses it as a check that the board is communicating properly. Since
currently there is no difference in any of the modes implemented on the
motor controller board, only a variable is being used to store the state
as requested by turtlebot_node. But for future work or if is required,
the code for the motor controller board can be extended to implement
this and also out in conditions for checking the current state of the
board before any action is taken.

After initialization, depending on which turtlebot driver is being used,
turtlebot_node repeatedly starts to send a "QUERY" command to the
controller board. In case of this package, it is preferred that the
**ipa_create** robot type be used since it introduces a custom query
field "100" which responds with the all the information from QUERY
command field "6" and also the encoder values from the motors
attached. In case, the turtlebot_node senses a change in the
"/cmd_vel" topic with respect to the velocity, it is required to
generate a "DRIVE DIRECT" command for the controller board. The
controller board should be able to handle this command.

### Motor Actuation and Position Monitoring

On receiving a "DRIVE DIRECT" command from the turtlebot_node, the
motor controller board forms a velocity message "VEL" for the motors.
This message also contains the desired velocity as requested by the
turtlebot_node. In addition to that, the motor controller board also
also sends a "POS" message to the motors to poll the current position
value. Its response is read and a position variable for each motor is
updated. Whenever the master requests for the position, the updated
position values are sent.
