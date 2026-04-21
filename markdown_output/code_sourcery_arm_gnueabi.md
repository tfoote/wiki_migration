## Installation

```
roscd code_sourcery_arm_gnueabi  
make                             # downloads the toolchain binary.
make install                     # installs into the /usr/___ directories.
make uninstall                   # removes the toolchain from your system.
```

### Toolchain Bridge

Once you have the toolchain installed, you may need to make it ros-ready
(i.e. install apr, apr-util, log4cxx, boost) using the instructions for
a [toolchain bridge](eros/Tutorials/Toolchain Bridge).

## Usage

### Toolchain Module

Eros provides a ready made [toolchain module](eros_toolchains) you can
select to globally configure your ros environment. To globally configure
your ros environment to use this toolchain:

```
rostoolchain select code_sourcery/arm-none-linux-gnueabi
```

### Development Patterns

Depending on what kind of development you wish to do:

-   [Partial cross](eros/Tutorials/Partial Cross) : embedded development
    without linking to the core ros libraries.
-   [Full cross](eros/Tutorials/Full Cross) : cross-compile both ros and
    your packages.

## See Also

### Platform (Cpu) Configuration

You'll probably want to also globally configure your
[platform module](eros_platforms) as well (i.e. the
\$ROS_ROOT/rosconfig.cmake file). A useful example file for arm cores
can be found in 'eros_platforms/library/arm/arm1176jzf-s.cmake'.

### Other Sourcery Toolchains

If you use a 64 bit build platform or want a ulibc based toolchain,
you'll have to download yourself from
[code sourcery](http://www.codesourcery.com/sgpp/lite%5Fedition.html).
Then make your own [custom toolchain module](eros_toolchains).
