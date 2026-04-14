This package provides high level manipulation of X11 widgets from
Python. In addition to various methods for identifying particular X11
windows that are being displayed, the following methods are available.
For details, consult the API:

-   `typeControlCharToActiveWindow()`: Type a given keystroke. Examples
    being \"alt+r\", \"Control_L+J\", \"ctrl+alt+n\", \"BackSpace\",
    \"Linefeed\".
-   `typeTextToActiveWindow()`: Type a given string, which must not
    contain control chars. For sending individual control chars, use
    `typeControlCharToActiveWindow()`.
-   `mouseClick()`: Effect a mouse button click as if the user had
    performed the action.
-   `mouseDown()`: Effect a mouse button press as if the user had
    performed the action.
-   `mouseUp()`: Effect a mouse button release as if the user had
    performed the action.
-   `getMouseGlobalPos()`: Return the current mouse position in global
    coordinates.
-   `moveMouseAbsolute()`: Move the mouse cursor as if the user had
    performed the action.
-   `moveMouseRelative()`: Move the mouse cursor relative to its current
    position.
-   `activateWindow()`: Activates a specified X11 window.
-   `getWindowGeometry()`: Provides geometry of a specified X11 window.
