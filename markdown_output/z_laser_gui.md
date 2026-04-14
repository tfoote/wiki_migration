The interface has been developed with QtCreator tool and it makes use of
[PyQt5](https://pypi.org/project/PyQt5/) libraries to run the GUI.

. ![\|width=\"400px\"](attachment:gui_general.png)

This package aims to improve the user experience with the stack. For
that purpose, several functionalities that ease the interaction with the
ROS API are included in the GUI:

-   The general menu provides a fast view of projector status with LED
    indicators.
-   CoordinateSystem and ProjectionElement submenus wraps the definition
    and control operations of projection elements: set active coordinate
    system, add projection element, scan targets, etc.
-   Push buttons allow triggering the actions on projector.

The image below shows an example of projection element definition: user
selects the figure type, fills in the fields with necessary data and
press the add button. Next time the projection is started, this new
figure will be projected.

. ![\|width=\"400px\"](attachment:gui_line.png)

## Acknowledgement

\<\<Include(rosin/acknowledgement)\>\>
