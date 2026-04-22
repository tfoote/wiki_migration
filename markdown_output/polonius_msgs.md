For full information on how Polonius works, see the [polonius](polonius)
stack page.

## Cue

[polonius_msgs/msg/Cue](https://docs.ros.org/en/rolling/p/polonius_msgs/msg/Cue.html)

This message not only represents a simple log message, but also can
trigger Polonius to move from one state to another.

## Interface Update

[polonius_msgs/msg/InterfaceUpdate](https://docs.ros.org/en/rolling/p/polonius_msgs/msg/InterfaceUpdate.html)

This message is sent from the Polonius engine to the GUI to communicate
what elements of the graphical interface to display. It contains 4 main
pieces of information.

-   The name of the state
-   A descriptive label for that state
-   A status code (see below)
-   List of button texts to display

### Status Codes

The five status codes represent which state the Polonius engine is in.
0. Pausing - Waiting a set amount of time before proceeding to the next
state 1. Waiting for Cue - Waiting for the initial click to enter a
state 2. Executing - Status while an action is being executed 3. Waiting
for Outcome - Waiting for the terminal click to transition out of a
state 4. Done - Polonius has reached a terminal state and is finished
executing
