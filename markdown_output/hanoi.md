This package allows a person to guide the PR2 through the Towers of
Hanoi puzzle. There can be only three discs, colored red, green, and
blue where the largest disc is red and the smallest blue.

There are three primary parts to this package:

1\. \'\'\'Webserver\'\'\': This is a python http server that connects a
javascript based GUI with ROS 1. \'\'\'Webgadgets\'\'\': These are the
javascript files that make up the GUI. These can hopefully be run on
many different platforms 1. \'\'\'Control code\'\'\': This part receives
commands from the webserver, controls the robot, and send back info to
the GUI via the webserver.

## Tutorials

Links to relevant tutorials
