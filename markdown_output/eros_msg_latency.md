## Overview

This package includes three separate tests benchmarking the speed of msg
passing in various contexts.

-   Passing a copy of float64 between two processes.
-   Passing a copy of float64 between two threads.
-   Passing a pointer to a float64 between two threads.

all of course, via topics. It is also worth perusing this code just to
make sure you're clear on the syntax which separates the above passing
methods, it can be subtle if you're new to it.

## Usage

For all of these, make sure you have pre-run `roscore`.

### InterProcessCopy

```
./talker
./listener
```

It will output latencies and finally when terminated (ctrl-c) will
output the average latency to standard output.

### InterThreadCopy

```
./thread_passing_copies
```

### InterThreadPointers

```
./thread_passing_pointers
```

Note this one is almost functionally identical to the previous one - you
just pass a boost shared pointer when publishing instead of an actual
object.

## Notes

Passing inter-thread with pointers is fast. There is no tcp/ip layer and
no copying. Also, you may find on very low spec boards, the latencies
drastically increase - there are many polling loops in the ros and this
seems to play havoc with the msg passing latencies. Also make sure you
have everything optimised (release modes) and the floating point
settings correctly set.
