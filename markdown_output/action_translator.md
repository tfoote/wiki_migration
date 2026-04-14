## Overview

Since we are only incrementally transitioning to the new action protocol
(defined in [actionlib](actionlib)), a running system could have both
actionlib actions and robot_actions actions running side-by-side. Since
TREX doesn\'t support the actionlib interface yet, you can use the
action_translator to wrap actionlib actions, allowing them to still
communicated over the robot_actions wire protocol.
