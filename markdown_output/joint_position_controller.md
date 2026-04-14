This package contains a simple joint position controller. The controller
follows PR2\'s controller structure and can be used in combination with
the [pr2_controller_manager](pr2_controller_manager). It creates a
KDL::Tree based on the robot\'s URDF model. All joints inside this tree
are then controlled independently of each other using a PD control
scheme.
