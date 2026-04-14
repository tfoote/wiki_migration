![ launch top window \| width=600](attachment:sna_rqt_moveit_1.png )

## Install

Follow \`rqt\`\'s general installation guide
[rqt/UserGuide/Install](rqt/UserGuide/Install).

On \`Ubuntu\`, \`rqt_moveit\` is available as binary pkg that comes
within [rqt_robot_plugins](rqt_robot_plugins) meta package.

## Issues

If you happened to find any problem, follow the usual steps (defined at
[Support](Support)), namely, Google search it,
[open a question](http://answers.ros.org/questions/) if you haven\'t
found a solution/workaround, and possiblly open a issue report or
enhancement request ticket on Issue/Bug tracker listed above.

### Known issues

Other than those opened tickets, here are something worth noted:

-   /!\\ Note that the refresh rate feature only works for monitoring
    nodes & parameters \-- it doesn\'t work for topic monitoring, which
    is done in external component ([rqt_topic](rqt_topic)) so that
    \`rqt_moveit\` doesn\'t have control for it.
