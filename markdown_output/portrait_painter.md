## Overview

The portrait_painter stage is the last stage of the
[portrait_bot](portrait_bot) project. It is responsible for converting
the images created in [face_contour_detector](face_contour_detector) to
instructions for the robots arm. For this we use the
[ee_cart_imped](ee_cart_imped) controller. Furthermore portrait_painter
is responsible for defining the canvas the image will be drawn on.

The package consists of three nodes:

-   **LineExtractor** Accepts images and converts them into lists of
    2D-Points
-   **PainterMain** Translates 2D-Point lists to 3D arm movement
    commands
-   **ManualCanvasSetting** Used to tell the robot where the canvas is

## Tutorial

portrait_painter is part of the [portrait_bot](portrait_bot) stack. To
learn how it is used please refer to the
[portrait_bot/Tutorials/Running the portrait bot](portrait_bot/Tutorials/Running the portrait bot)
Tutorial.

## How does it work?

### LineExtractor

LineExtractor receives the contour images from contour_detector. It uses
potrace to create a plot file representing the contours of the edges in
the image. Then it converts that plot file into a list of lines, whereat
each line consists of an absolute start point and following relative
points.

Since potrace returns contours / polygons each line will result in at
least two parallel edges. LineExtractor tries to revert that effect, so
only one line will be drawn. Afterwards it calls for each line the
*job_submission* service of the PainterMain node. After the last line is
drawn the Gripper is moved away from the picture to a position right of
the head.

### PainterMain

PainterMain provides the services *canvas_setting* and *job_submission*.
It holds three Vector3 objects representing the upper left, upper right
and lower left corner of the canvas. These Vector3 objects have to be
set by ManualCanvasSetting using the *canvas_setting* service call
before the robot can draw.

PainterMain accepts jobs from LineExtractor using the *job_submission*
service. Each job represents one line of the image as a list of
2D-Points with values between 0 and 1. Using the 3D coordinates of the
canvas these points are translated into points in 3D space.

PainterMain creates a Trajectory object - as described
[ee_cart_imped_action/Tutorials/Writing a Stiffness Controller](here) -
that navigates the arm to a point 10 cm above the first point of the
line, to the actual point and then to every other point of the line.

### ManualCanvasSetting

Before you can begin drawing, the robot must know where in the 3D space
the canvas is. To do this we have chosen that the user must move the arm
to the upper left, upper right and lower left corner of the canvas
manually. There is a *Set Corners* button in the gui that will call a
*alubsc/node_instr/manual_canvas_setting* server provided by
ManualCanvasSetting. After the button is clicked the GUI will display
instructions like "move Gripper to upper left corner of the canvas and
press button".

Once the last point is set the node will call the *canvas_setting*
server of PainterMain to report the canvas coordinates.
