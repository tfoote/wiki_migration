## Overview

This provides a build recipe for cross-compiling a gdb/gdbserver combo.
This pair of tools allows you to do remote debugging without having to
run the debugger itself (nor libs with debugging symbols) on the target.
Very useful for embedded boards with limited memory or oomph.

This package is a component of eros'
[toolchain bridge](eros/ToolchainBridge).

## Compiling

This actually absolutely needs an eros toolchain to enable it to extract
useful information from TOOLCHAIN_TUPLE and TOOLCHAIN_SYSROOT.

## Tested

-   Native:
-   Cross-Compile: arm

## Usage

### Running

Make sure you have copies of your binary both locally and on the
embedded board. The embedded board copy may even be stripped, but the
local one must absolutely be non-stripped and have debug symbols.

**Embedded Board**

```
gdbserver 192.168.0.66:5200 ./hello
```

Note that the ip is actually ignored, the port number is the only thing
that is important.

**Build Platform**

```
arm-samsung-linux-gnueabi-gdb ./hello
(gdb) target remote 192.168.0.15:5200
(gdb) break main
(gdb) continue
(gdb) continue
```

### Backtraces

The first continue will stop at main, the second continue starts it
running. After a segfault

```
(gdb) list
(gdb) bt
```

The first command shows the source location of the last frame before the
crash. The latter, the backtrace (f full) provides the last chain of
commands.

## Issues

If the backtrace doesn't provide any symbols (all you see is alot of
??'s), it means gdb isn't finding the debug symbols in the appropriate
code/libraries. I thought it was supposed to embed these in your build
when you enable the --with-build-sysroot command, but it seems that is
only for the build process. So, to point your cross debugger at the
right place, you can either set some variables while running, or (more
easily) create a config file to run with gdb on the build platform. The
following example `iclebo.gdb` sets directories in the sysroot to
parse standard libraries in:

```
set solib-absolute-prefix /usr/arm-samsung-linux-gnueabi
set solib-search-path /usr/arm-samsung-linux-gnueabi/lib:/usr/arm-samsung-linux-gnueabi/usr/lib
```

You can then run it on something like a hellow world program as follows:

```
arm-samsung-linux-gnueabi-gdb --command=iclebo.gdb ./hello
(gdb) target remote 192.168.0.15:5200
(gdb) break main
(gdb) continue
(gdb) continue
```

Push this into a bash script to make it more convenient.
