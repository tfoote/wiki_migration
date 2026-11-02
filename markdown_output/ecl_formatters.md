## Overview

Typically c/c++ libraries bundle streaming and formatting within the
same tool (printf, iostream, \...). This tends to make them cumbersome
for simple tasks. The formatter classes in this package externalise the
formatting task from the io manipulation (which is usually just (u)char
manipulation), This increases the efficiency of low level operations
whilst also maintaining type safety. They typically do this by making
use of the lower level functionality provided by
[ecl_converters](https://index.ros.org/p/ecl_converters).

The formatter classes can be used standalone, with stl streams or with
[ecl_streams](https://index.ros.org/p/ecl_streams).

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

- [Using Ecl Formatters](#using-ecl-formatters)
- [Writing a Custom Formatter](#writing-a-custom-formatter)

## Available Formatters

Each standard formatter is a template specialisation of the form
`Format<inputType>` where the available input types are:

- integral types (char, short, int, long, long long and unsigned
  equivalents)
- float types (float, double)
- string
- arrays and stencils in
  [ecl_containers](https://index.ros.org/p/ecl_containers)

## Using Ecl Formatters

- **Description:** Introduction to the usage of ecl formatters.
- **Keywords:** ecl formatters
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Custom Formatters](#writing-a-custom-formatter)

### Instantiation & Configuration

#### Construction

Formatters are functors - functions with state. You instantiate a
formatter type and then make use of it as if it were a function call.
Each formatter typically comes with a few format parameters that can be
used to modify the format of the output (e.g. text width, no. of decimal
points etc). These can be supplied at instantiation if the default set
is not suitable.



```cplusplus
Format<int> format(); // Default format initialisation
Format<int> format(8,RightAlign,Hex); // Custom format initialisation
```



#### Modifying Format Configuration

The format parameters can be changed singly with appropriately named
setters, or collectively via:: a bundled `operator ()` call. Sometimes
common combinations are also provided with a convenient setter via the
`operator ()`.



```cplusplus
format.base(Hex);
format(8,RightAlign,Dec);
```



Changing the format parameters in this way will set the default
formatting for any input values given to the formatter in the future.

### Streaming

The formatters are primarily intended to be used with streams. For
convenience they have been designed to be used with any stream that
implemenents the `<<` operator. Subsequently they are useful with
either `TextStreams` from
[ecl_streams](https://index.ros.org/p/ecl_streams) or the usual c++
streams. When used in conjunction with `TextStreams` they provide a
very fast streaming interface.

#### Permanent Formatting

To format with the parameters stored in the formatter, you simply
provide the formatter with the input value. Note that the formatter will
only accept a value of the type specified in the formatter's template
argument.



```cplusplus
ostream << format(i) << " " << format(9);
```



For convenience, you can also change the format parameter on the fly
(this is recorded permanently).



```cplusplus
ostream << format.base(Hex)(i) << " " << format(10,LeftAlign,Dec)(9);
```



#### Temporary Formatting

Occasionally you will only need to change the format for one instance.
To effect a temporary change in this way, supply the input value along
with the specified formatting options.



```cplusplus
ostream << format(i,6,CentreAlign,Hex);
```



### Issues

{OK} - use one format call per line when streaming



```cplusplus
ostream << "[" << format(q.x());
ostream << ", " << format(q.y());
ostream << ", " << format(q.z()) << "]";
```



{X} - do not make several calls per line when streaming



```cplusplus
ostream << "[" << format(q.x()) << ", " << format(q.y()) ostream << ", " << format(q.z()) << "]";
```



The ecl in debug mode (`-DNDEBUG` is not defined) will utilise an
exception throwing assert to check that multiple formatters aren't used
in one line when streaming.

The why - there are some awkward aspects of streaming that make it
difficult for the formatters to function perfectly. Without going into
the details, this means it is impossible to format several objects on
the same line differently, and expect the result to come back in the
correct order. I haven't currently got a solution for this, so there
are two options:

1\. Leave the formatters as they are and ensure that only one formatter
is used on each line (abort/throw if this occurs) 2. Push the formatters
back into TextStream.

The second option is no good - it just turns TextStream into a
heavyweight iostream. A priority for us is fast logging, so we must keep
TextStream lightweight and since the first option is merely a coding
style issue, that's easy to handle so long as we are aware of it.

## Writing a Custom Formatter

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Using Ecl Formatters](#using-ecl-formatters).
- **Description:** Writing your own custom formatters.
- **Keywords:** ecl formatters
- **Tutorial Level:** INTERMEDIATE

Formatters must implement

- Formatting setters
- Input value operator
- Temporary formatting operators
- Streaming friend function



```cplusplus
class MatrixFormatter {
public:
    MatrixFormatter& precision(int p);     // Setter
    MatrixFormatter& operator()(Matrix M); // Input Operator
    MatrixFormatter& operator(int p, int w ... ); // Combination setter
    MatrixFormatter& operator(Matrix M, int p, int w ...); //Temporary formatting operator
    template <typename OutputStream, typename N> friend OutputStream& operator << (OutputStream& ostream, MatrixFormatter& formatter);
}
```



Note that the setters and operators must return the formatter so that
the friend function can implement the formatting.

For the `Format<Type>` class to automagically find this formatter,
you can implement one of two methods. If you have access to the class's
internals, simply typedef it as "Formatter" inside the class,
otherwise simply specialise the `Format<>` class for your type and
inherit the formatter.



```cplusplus
// Method one, if you have access to the classes internals
class Matrix {
public:
    typedef MatrixFormatter Formatter;
};

// Method two
template <>
class Format<Matrix> : public MatrixFormatter {};
```



### Example

See `include/ecl/containers/array\$ vim formatters.hpp` in
[ecl_containers](https://index.ros.org/p/ecl_containers) for a concrete
example.

## Tutorials

- [Using Ecl Formatters](#using-ecl-formatters):
  Introduction to the usage of ecl formatters.
- [Writing a Custom Formatter](#writing-a-custom-formatter):
  Writing your own custom formatters.
