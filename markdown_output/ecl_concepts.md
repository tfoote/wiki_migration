## Overview

For templatised functions and classes, the input template arguments
usually have little or no restriction on the class that can be used,
e.g.

```cplusplus
template <typename T>
void f(T input) {
    // use some aspect of T's interface
}
```

Of course the compile will fail if you try to use an input type, T, that
doesn\'t have the specialised interface you want, but the compile time
error message is often very verbose and its difficult to find the error.
An idea which is merging into the c++ mainstream as well as that used by
the boost concept checking library is to characterise common behaviours
into \_Concepts\_. A simplified version of this is utilised here.

## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/concepts.hpp>

// The concept definition/validation classes.
using ecl::BluePrintConcept;
using ecl::ContainerConcept;
using ecl::SignedByteContainerConcept;
using ecl::UnsignedByteContainerConcept;
using ecl::NullaryFunctionConcept;
using ecl::StreamConcept;
using ecl::InputCharDeviceConcept;
using ecl::OutputCharDeviceConcept;
using ecl::InputOutputCharDeviceConcept;
using ecl::InputByteDeviceConcept;
using ecl::OutputByteDeviceConcept;
using ecl::InputOutputByteDeviceConcept;
```

## Usage

-   [Implementing Concepts](ecl_concepts/Tutorials/Implementing Concepts)

## Concepts

Existing concepts in the ecl include:

\@section conceptsList Existing Concepts

-   \`BluePrints\` - checks for blueprint functionality as defined in
    ecl_utilities.
-   \`Containers\` - also bytecontainer, simple checks for basic
    prerequisite container methods.
-   \`NullaryFunctions\` - function objects which require no arguments
    in execution.
-   \`Streams\` - any class with basic char streaming capabilities.
-   \`Devices\` - device functionalities compatible to those in
    ecl_devices.
