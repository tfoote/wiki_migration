## Documentation

The RSM consists of various non-customizable and custom states that are
based on the Base State. The former non-customizable states and the Base
State are a part of this package containing the RSM\'s basics. To handle
state transitions the State Interface is used. Robot Control Mux
coordinates the actual control of the robot\'s movement while the
Service Provider contains services, publishers and subscribers for
communication between states and updating the GUI. To be able to handle
arbitrary robots, the RSM relies on Plugins that can be implemented
depending on the robot.

## Nodes

{ }}}}

{ }}}}
