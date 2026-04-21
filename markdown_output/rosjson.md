## Stability

This package is for internal use only.

## Usage

The JSON (!JavaScript Object Notation) format is useful when building
Web-based interfaces that need access to ROS data. rosjson is meant to
be coupled with a Python Web server so that the JSON objects can be
served over a Web connection. [rosweb](rosweb) is one example Web server
implementation, but it is currently in high design flux.

## Roadmap

No further features are planned for the ROS JSON library as JSON itself
is just a data representation. Python 2.6 has a json module that would
simplify the existing code and make it more robust, but as the current
package is < 50 lines of Python, there's not much to improve upon.
