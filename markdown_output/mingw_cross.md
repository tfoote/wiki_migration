```wiki
Mingw is not likely to be re-enabled for groovy. If you're interested in committing time to re-enable it, please let us known - we can assist.
```

## Overview

-   [Status](mingw_cross/Status) - a list of currently compiling ros
    packages via mingw_cross.

## Installation

### Mingw Cross

You can of course install the mingw cross environment directly yourself
following the instructions at the
[mingw cross home page](http://mingw-cross-env.nongnu.org/).
Alternatively:

```
> roscd mingw_cross
> make install       # downloads, installs into ~/mingw 
                     # compiles gcc, apr, apr-util, log4cxx, boost, qt
                     # adds mingw_cross binary path to PATH in ~/.bashrc
> make uninstall     # remove ~/mingw and delete modifications in ~/.bashrc
```

Installation location can be moved if the `MINGW_INSTALL_PREFIX`
environment variable is set before running `make install`.

Further build recipes can be compiled into the toolchain by simply
switching to the mingw root and making the appropriate target. A list of
packages that can be installed can be found
[here](http://mingw-cross-env.nongnu.org/#packages). To build wxwidgets
for example,

```
cd ~/mingw
make wxwidgets
```

## Usage

See the [Tutorials](mingw_cross/Tutorials) for usage patterns.
