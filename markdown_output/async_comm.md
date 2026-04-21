This is a release of the `async_comm` library, following the
guidelines in [REP 136](http://www.ros.org/reps/rep-0136.html).

This C++ library gives a simple interface for asynchronous serial
communications over a serial port or UDP socket. It uses the
[Boost.Asio](http://www.boost.org/doc/libs/master/doc/html/boost_asio.html)
library under the hood, but hides from the user the details of
interfacing with the ports or sockets and managing send/receive buffers.

For more details, refer to the
[README](https://github.com/dpkoch/async_comm/blob/master/README.md) or
the [API documentation](https://codedocs.xyz/dpkoch/async_comm/).
