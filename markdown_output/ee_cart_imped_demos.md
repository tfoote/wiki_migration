This package contains demos for the ee_cart_imped_controller and its
wrapper action (ee_cart_imped_action).

# Running a Demo at MIT

To run a demo, you must first start the robot so that it acknowledges
the controller using the -e argument:

`sudo robot start -e`

Now make the package

`rosmake ee_cart_imped_demos`

and launch the [ee_cart_imped_action](ee_cart_imped_action). This stops
the default right arm controller, starts the
[ee_cart_imped_controller](ee_cart_imped_controller), and starts the
action server:

`roslaunch ee_cart_imped_action ee_cart_imped_action.launch`

Now you can run a demo. Since they are simply demos for the controller
package, they make very specific assumptions about the location of
things relative robot. Namely, to run the drawing demos (draw_square and
pr2_write_mit) at MIT, position the robot, table, and paper in
accordance with the red tape and lower the robot's torso all the way.
Then run

`rosrun ee_cart_imped_demos draw_square`

or

`rosrun ee_cart_imped_demos pr2_write_mit`
