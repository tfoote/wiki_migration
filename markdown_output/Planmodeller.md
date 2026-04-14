The Planmodeller is used to design ALICA plans. Binaries are provided.
It can simply be started by ```
rosrun Planmodeller start.sh
```

## Setup

In order to work in a domain, the Planmodeller needs four projects to be
defined. All of them can be created by clicking the button \"Create
Projects\". Specifically these are:

-   Plans: Holds all the executable plans
-   Roles: Holds information about the roles available to the robots.
-   Misc: A special project holding files relating the two above.
-   Expressions: This is were the Planmodeller will put all generated
    source files. Domain specific parts, such as conditions guarding
    transitions in state machines need to be edited in these files.
