## Messages Explained

This package contains messages specific to our packages. They are
defined in a separate package to minimize the dependencies between
packages. If you develop a node to interact with ours, most of the time,
you only need to depend on this package (and not on [sr_hand](sr_hand)).

The main messages contained in this stack are:

-   **joint**: contains the important information regarding a joint:
    name, position, target, torque, motor temperature, motor current, as
    well as an error flag. This message is not used on its own, but is
    often the main components of the other messages.
-   **joints_data**: is being published , for example, on the
    shadowhand_data topic. It contains a table of all the joints in the
    robot.
-   **sendupdate**: is the message used to send a new target to the
    robot. It contains a table of joints. You can give any number of
    targets you want. Just specify the joint_name and joint_target in
    each **joint** you add (the other fields of the **joint** message
    are ignored). For more details, you can have a look at this
    [tutorial](sr_hand/Tutorials/Moving the Robot).
-   **contrlr**: is used to specify new controller parameters for the
    robot PID loop.
