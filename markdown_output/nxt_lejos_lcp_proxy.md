## Overview

This package provides a controller for NXT robots running leJOS. It uses
the LEGO Communications Protocol (LCP) to connect to the NXT Robot,
which should be running the leJOS menu, or an LCP Responder program. It
works over USB or Bluetooth.

LCP is the protocol used by the standard LEGO Mindstorms firmware, so
this package should also work with NXT robots running the standard
firmware.

LCP is not a very efficient protocol for use with ROS, as too many
messages are sent back and forth to the NXT robot in order to navigate
the robot and report its sensor readings etc.

A more optimized controller will be developed to replace this package.
It will use an optimized protocol to reduce message traffic to the
robot, and will therefore be able to publish and respond to messages at
a higher frequency.
