## Overview

The \`rosmaster\` package implements the ROS [Master](Master). Most
programs will not need to interact with this package directly. The
\`rosmaster\` is run automatically whenever [roscore](roscore) is run
and all communication with the Master happens over XMLRPC APIs.

## Advanced: XMLRPC API

The XMLRPC API of the ROS Master is documented on the
[Master API](ROS/Master_API) page. This API is for advanced users only
and backwards compatibility is not guaranteed.
