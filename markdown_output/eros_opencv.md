## Overview

Ros\' package for opencv basically builds the whole kitchen sink. We
don\'t want most of it on an embedded board. So we turn off alot of
flags. Currently this pulls the latest bugfix release from opencv\'s svn
2.1 tag.

Unlike the ros package, this one also incorporates all the cmake
configurations from a \`rostoolchain.cmake\` and \`rosconfig.cmake\`
(toolchain, compile flags, sse\'s etc).

## Tested

-   \'\'Native\'\': linux
-   \'\'Cross-Compile\'\': arm, mingw32

## Usage

This package can either be used within the ros tree (appropriate exports
are configured) or or installed in a sysroot (\'make install\') which is
useful for traditional embedded development with a partial cross.

## Configuration Issues

Might be useful to be aware of some aspects of the build - these are
noted here.

### OpenCV Version

This package will have to be revalidated every time ros updates the
opencv - we should always try and sync our opencv package with theirs.
At the moment (cturtle), this is using a vanilla version from opencv
directly, whereas the ros opencv2 uses a patched branch - \'\'this needs
to be updated\'\'.

### Build Flags Used

Opencv is compiled with all options turned off except JPEG and PNG. To
modify the build, simply edit the appropriate section in
\`cmake/OpenCvBuild.cmake\` file.
