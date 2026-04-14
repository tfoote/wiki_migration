## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/ipc.hpp>

using ecl::Semaphore;
using ecl::SharedMemory;
```

If outside of ros, you will also need to link to \`ecl_ipc\`.

## Cross Platform Support

Currently there is only the posix structures. There is win32 code lying
around from an earlier version of the ecl, but since we\'re not using
windows these days, it is largely untested against more recent updates.
When we have a need, it will be reintroduced.

## Tutorials

-   [Semaphores](ecl_ipc/Tutorials/Semaphores) - inter-process locks for
    use with shared memory.
-   [Shared Memory](ecl_ipc/Tutorials/Shared Memory) - fast, typesafe,
    interprocess communication.
