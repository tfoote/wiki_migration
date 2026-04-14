## Overview

\`osc_bridge\` provides the core functionality of communicating with
both the OSC protocol and the ROS system.

[touchosc_bridge](touchosc_bridge) extends this node, so most users will
not need to interact with \`osc_bridge\`.

\`osc_bridge\` may be used to communicate with other OSC-compatible
hardware and software via both TCP and UDP, but these features remain
largely untested.

## Node API

```clearsilver
param {
0.name = ~osc_name
0.type = string
0.desc = Name of the node as it will appear in the Bonjour/Zeroconf system.
0.default = Test
1.name = ~port
1.type = int
1.desc = Port that the OSC server will listen on
1.default = 8000
2.name = ~regtype
2.type = string
2.desc = Bonjour registration type of the OSC server
2.default = _osc._udp
3.name = ~print_fallback
3.type = bool
3.desc = setting the parameter to "True" will cause unhandled incoming OSC messages to be printed to the console.
3.default = False
}
```
