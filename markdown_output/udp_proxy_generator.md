udp_proxy_generator generates ros to multicast proxies.

# Generating Proxies

In order to generate a proxy follow these steps:

-   Create a new package,
-   Add a dependency to udp_proxy_generator,
-   Include the cmake file: `rosbuild_include(udp_proxy_generator udp)`
-   Call `rosbuild_make_udpProxy()` from within your cmake file.
-   Add a file named `relayMsgs.conf` into the root directory of your
    package. An example is provided in the example directory.
-   Compile your package.

# Using Proxies

The generated proxy uses [Castor](Castor) to read multicast address and
port from a configuration file called UdpProxy.conf. An example can be
found in the package example directory.

It looks for this file in ES_ROOT/etc/hostname/, ES_ROOT/etc/ROBOT/, and
ES_ROOT/etc/ in this sequence.
