## Overview

A package that exports the [WebRTC](http://www.webrtc.org/) libraries
for use by other packages.

Some more information on some of the components of WebRTC can be found
here:

-   [SDP](https://webrtchacks.com/sdp-anatomy/)
-   [ICE](http://www.slideshare.net/saghul/ice-4414037)

## Building from Source

Make sure that all of the package dependencies have been installed. The
first time you build it may take significantly more time as it will
check out about 400MB of source from the internet. Subsequent builds
will be faster.

## Usage

The \`webrtc\` package does not export any include directories,
libraries, or compiler options directly. This is because there are a
substantial number of options and libraries that may cause issues with
other libraries. Instead \`webrtc\` exports a number of CMake variables
that can be used. See [webrtc_ros](webrtc_ros) for example usage.

-   webrtc_LIBRARIES - target_link_libraries(\<target\>
    \${webrtc_LIBRARIES})
-   webrtc_INCLUDE_DIRS - target_include_directories(\<target\> PUBLIC
    \${webrtc_INCLUDE_DIRS})
-   webrtc_DEFINITIONS - preprocessor macro definitions
