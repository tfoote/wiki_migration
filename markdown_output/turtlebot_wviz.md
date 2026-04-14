This package allows users to interact with their Turtlebot though a web
interface.

## Installation and Set Up

1\. Follow installation instructions for your version of the remote_lab
stack [remote_lab](remote_lab). 2. Set up a webserver and direct it so
that it can see turtlebot_viz.html 3. Edit turtlebot_viz.html lines 23
and 23 to point to the correct rosjs_server (where rosbridge is located)
and the correct mjpeg_server(where mjpeg_server is running). In our case
nob was the name of our turtlebot. 4. Start [rosbridge](rosbridge) 5.
Roslaunch ` turtlebot_wviz turtlebot_viz.launch` 6. Open the webpage
from the appropriate address in Chrome.

## Video

[Youtube](https://www.youtube.com/watch?v=7Y30FX1hgZM)
