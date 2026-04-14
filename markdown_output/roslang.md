## Overview

The \`roslang\` package is only of interest to those implementing a ROS
[client library](Client Libraries). Client libraries marks themselves as
such by depending on the \`roslang\` package, which allows
[rosbuild](rosbuild) and other tools to perform appropriate actions,
such as [msg](msg)- and [srv](srv)-based code generation. The
\`roslang\` package itself contains no actual code.
