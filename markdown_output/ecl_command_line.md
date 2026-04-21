## Overview

Provides a templatised c++ parser for handling command line arguments.
The templates provide a very flexible manner for handling any type of
input argument.

The code for the command line parser is a simple wrapper around another
template header library called [TCLAP](http://tclap.sourceforge.net/).
Since it is relatively small, its bundled here in the command_line
subdirectory and namespaced in a convenient manner.

### Alternatives

A more complicated, but more flexible alternative (it allows argument
parsing from both command line and configuration file simultaneously) is
the `boost::program_options` library.

## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/command_line.hpp>

// Interface classes
using ecl::CmdLine;
using ecl::ArgException
// Argument classes
using ecl::SwitchArg;
using ecl::ValueArg;
using ecl::MultiArg;
using ecl::UnlabeledValueArg;
using ecl::UnlabeledMultiArg; // there are more - see tclap docs
```

## Tutorials

-   [Command Line Parsing with TCLAP](ecl_command_line/Tutorials/Command Line Parsing with TCLAP)

## Examples

-   `src/examples/command_line.cpp`.
