Contains the Oculus Display for RViz.

# Usage

In RViz, add an !OculusDisplay. This will create an additional window
with a stereo rendering of the contents of the main RViz rendering area.
Check \"Render to Oculus\" to render in full screen mode on your Oculus
headset. Like with any Oculus application, it must be set up as
secondary screen for this to work.

By default, the Oculus view will be rendered from the same position as
the main RViz camera while following your head\'s orientation.
Alternatively, you can attach the camera to a tf frame.

The position of the virtual camera view is also published as the
\'/oculus\' tf frame.

This is how the Display should look like in windowed mode:

![\|width=760](attachment:screenshot.png)
