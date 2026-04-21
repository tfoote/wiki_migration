**proxy** is a multi-topic, on-demand repeater for message streams.

## Usage

Start the proxy with your desired prefix:

```
$ rosrun proxy proxy _prefix:=/proxy
```

Subscribe to a repeated topic (suppose you have a topic /scan):

```
$ rostopic echo /proxy/scan
```

## Notes

If you do not need support for multiple topics or on-demand
subscription, you could use the [relay](topic_tools/relay) node from
[topic_tools](topic_tools).

`proxy` will only relay topics whose messages are defined on the
system where `proxy` runs. This limitation exists because publishers
are required to advertise some information that is not available through
the rosmaster API, such as the message hash and message definition.

If you run multiple proxy instances, the proxies will repeat each
other's topics, but they will not create a loop. You can use this to
create message chains like the following:

```
/proxy3/proxy2/proxy1/scan
```

When you first subscribe to that topic, proxy 3 will subscribe to proxy
2, which will subscribe to proxy 1, which will read in the original
message.
