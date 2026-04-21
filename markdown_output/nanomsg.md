## About

This is a fairly naive cmake build of the nanomsg package. Usually
nanomsg builds with autotools and has many checks - the cmake
configuration assumes the result of many of these checks, but works
sufficiently for ubuntu indigo and some arm cross compiles\...at least
until ubuntu releases a system version of nanomsg.

[Nanomsg](http://nanomsg.org/) is a very lightweight (smaller brother of
zeromq) communications library accomodating various design patterns. It
can be useful for specialised instances where ros doesn't really fit.
e.g. Bridging connections to lightweight embedded boards or in grafting
your own custom messaging architecture for a specific use case.

## Examples

-   [nanomsg  examples](http://tim.dysinger.net/posts/2013-09-16-getting-started-with-nanomsg.html) -
    a tutorial code breakdown of some (uncompiled) example design
    patterns.
-   [message_multiplexing/mm_mux_demo/src/demos](https://github.com/stonier/message_multiplexing/tree/indigo/mm_mux_demux/src/demos) -
    compiled versions for some of the aforementioned nanomsg tutorials.
-   [message_multiplexing](https://github.com/stonier/message_multiplexing) -
    simple communication library built on top of this useful for certain
    embedded scenarios.
