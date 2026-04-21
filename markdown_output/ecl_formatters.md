## Overview

Typically c/c++ libraries bundle streaming and formatting within the
same tool (printf, iostream, \...). This tends to make them cumbersome
for simple tasks. The formatter classes in this package externalise the
formatting task from the io manipulation (which is usually just (u)char
manipulation), This increases the efficiency of low level operations
whilst also maintaining type safety. They typically do this by making
use of the lower level functionality provided by
[ecl_converters](ecl_converters).

The formatter classes can be used standalone, with stl streams or with
[ecl_streams](ecl_streams).

## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/formatters.hpp>

// The formatter template family
using ecl::Format;

// Common formatter parameters
using ecl::NoAlign;
using ecl::LeftAlign;
using ecl::CentreAlign;
using ecl::RightAlign;

// Integral formatter parameters
using ecl::Bin;
using ecl::Dec;
using ecl::Hex;

// Float formatter parameters
using ecl::Fixed;
using ecl::Sci;
```



If outside of ros, you will also need to link to *ecl_formatters*.

## Tutorials

-   [Using Ecl Formatters](ecl_formatters/Tutorials/Using Ecl Formatters)
-   [Writing a Custom Formatter](ecl_formatters/Tutorials/Writing a Custom Formatter)

## Available Formatters

Each standard formatter is a template specialisation of the form
`Format<inputType>` where the available input types are:

-   integral types (char, short, int, long, long long and unsigned
    equivalents)
-   float types (float, double)
-   string
-   arrays and stencils in [ecl_containers](ecl_containers)
