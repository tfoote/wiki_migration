## Overview

This is used to generate everything required for the msvc ros runtime
(i.e. roscore, rosmaster, roslaunch, rostopic etc). It does this by
ensuring there are executables for the python scripts (ugh, windoze) and
also by creating dummy targets so that this can act as a meta-package
for getting the runtime built in one shot.

## Tutorials

Fuerte only:

-   [Msvc Runtime Environment](win_ros/Msvc Runtime Environment - Fuerte)

## Python Executables

These scripts can\'t be run without a \`.py\` extension on windows and
even then, can\'t be run in the shell without directly calling python
first. Alot of the ros architecture expects these to be directly
executable, so rather than modifying the whole ros architecture, we sub
in executables that indirectly execute the python scripts.

### Adding

Simply copy one of the existing .exe\'s and rename it (they are
self-calling). More permanently, modify \`CMakeLists.txt\` in the src
folder.
