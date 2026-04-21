<<MsgSrvDoc(std_srvs)>>

## Overview

`std_srvs` contains two service types called `Empty` and
`Trigger`, which are common service patterns for sending a signal to a
ROS node. For the `Empty` service, no actual data is exchanged between
the service and the client. The `Trigger` service adds the possibility
to check if triggering was successful or not.

For common message definitions, please see the [std_msgs](std_msgs)
package.
