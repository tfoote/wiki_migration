## Abstract

This package enables controlling elements (currently only lights) in the
[vmi_cognitive_environment](vmi_cognitive_environment) directly from an
Android device by simply publishing some switches' states.\
It shows how to rapid prototype a Android ROS node, which is functional
and has o decent GUI.

## GUI

The GUI is realized through
[SL4A](http://code.google.com/p/android-scripting/)'s (Scripting Layer
for Android) UiFacade using a WebView. The interface itself is an HTML
page based on [jQuery mobile](http://jquerymobile.com/), which is still
in alpha stage but yet already very functional.\
The communication between the background Python script and the HTML in
WebView is realized with SL4A's event system.
