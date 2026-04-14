This a top-level package containing launch files for cart pushing on the
robot. See the [tutorials](cart_pushing/Tutorials) for instructions on
how to do this. See individual package pages for more on the specific
planners used. Here we provide instructions for common sorts of
customizations you might want to make.

## Customizing the cart geometry

See the
[tutorial](http://www.ros.org/wiki/cart_pushing/Tutorials/Configuring%20a%20new%20cart)
for how to do this. The files
\`launch/move_base/wg_holonomic_cart_params.yaml\` and
\`launch/move_base/wg_holonomic_cart_filter_params.yaml\` are the ones
that need to be edited.

## Using a different map

Edit the parameter to \`map_server\` in
\`launch/cart_pushing_robot.launch\`.

## Changing the initial robot pose

Edit the parameter to \`set_initial_robot_pose\` in
\`launch/cart_pushing_robot.launch\`.

## Modifying general navigation and costmap parameters

The files in \`launch/move_base\` correspond to those in the standard
[PR2 nav stack](pr2_2dnav).

## Making the planning faster

See the parameters in [sbpl_cart_planner](sbpl_cart_planner).
