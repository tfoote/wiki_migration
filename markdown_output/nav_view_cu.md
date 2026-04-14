\'\'\'Note that the prairiedog platform uses the more advanced
\`visualization_cu\` for user interaction.\'\'\'

\`nav_view_cu\` is a minimalistic `OpenGl` based substitute for an early
release of \`nav_view\` (circa ROS V0.8) . It can be used to interact
with a basic robot in a limited number of ways, including setting pose
and goal positions. We initially wrote nav_view_cu because the netbooks
used on the prairidog robotic platform do not have graphics cards, and
therefore cannot run the Ogre graphics library, or any code that depends
on it.

\`nav_view_cu\` does not currently use the tf package, and may therefore
not be advanced enough for many newer ROS applications. Future updates
may include this functionality (especially if we find that it is in
demand).
