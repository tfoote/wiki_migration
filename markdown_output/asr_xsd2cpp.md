![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package is used to generate C++ classes (headers) mapped to the
components of an input XML Schema.

## Functionality

It uses the *xsd* command of the
[mono tools](http://www.mono-project.com/docs/tools+libraries/tools/) to
create the C++ files from an *.xsd* file located in the *xsd* directory
of your project.

## Usage

### Needed packages

This package does not need any additional packages.

### Needed software

-   mono-devel

## Tutorials

To automatically generate C++ files from your XSD-schema add this
package as a dependency to your project. In your project's
*CMakeLists.txt* add the following lines:



```
include(${asr_xsd2cpp_SOURCE_DIR}/catkin_make.cmake)
xsd2cpp()
```

 For this to work you need to store the XSD-file
(created according to the W3C specifications) you want to convert in a
directory called *xsd* in the base directory of your project. Now build
your project and the generated files will be located in the *xsd_gen*
directory in your project's base directory.
