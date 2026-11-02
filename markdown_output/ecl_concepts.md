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
doesn't have the specialised interface you want, but the compile time
error message is often very verbose and its difficult to find the error.
An idea which is merging into the c++ mainstream as well as that used by
the boost concept checking library is to characterise common behaviours
into _Concepts_. A simplified version of this is utilised here.

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

- [Implementing Concepts](#implementing-concepts)

## Concepts

Existing concepts in the ecl include:

\@section conceptsList Existing Concepts

- `BluePrints` - checks for blueprint functionality as defined in
  ecl_utilities.
- `Containers` - also bytecontainer, simple checks for basic
  prerequisite container methods.
- `NullaryFunctions` - function objects which require no arguments in
  execution.
- `Streams` - any class with basic char streaming capabilities.
- `Devices` - device functionalities compatible to those in
  ecl_devices.

## Implementing Concepts

- **Description:** Writing and using concept check tests.
- **Keywords:** ecl concepts
- **Tutorial Level:** INTERMEDIATE

### Overview

Usage is fairly simple. There are two steps:

- *Concept Test* : must be hand crafted to check all the characteristic
  behaviours of a concept.
- *Concept Check* : whenever required, call the concept check which runs
  the concept test to verify compliance.

### Concept Test

If you are using an existing concept (see below), skip through to the
concept check. Otherwise:

- Decide on a name for the concept.
- Create a templatised class of that name with a single arbitrary
  template argument (the class to be tested).
- Hand craft the testing function within that class using
  `compile_time_concept_test`().

The example here is the same as that used in `src/tests/concepts.cpp`:



```cplusplus
template <typename T>
class MyConcept {
    public:
        compile_time_concept_test(MyConcept) {
            T t;
            t.apply();  // This is the characteristic function required by this concept.
        }
};
```



Hand-crafting the concept testing function will often require a little
care to ensure the concept is appropriately covered.

### Concept Check

Once you have a test in place, you only need to insert
`compile_time_concept_check()` calls wherever you need them. Keep in
mind, the sole purpose of these is to provide convenient error logs when
something goes wrong.



```cplusplus
class A { // This class has the MyConcept functionality.
    public:
        // The following function characterises the MyConcept concept.
        // Comment this line and any MyConcept concept assertion
        // check will fail in compile time.
        void apply() {};
};

int main() {
    compile_time_concept_check(MyConcept<A>); // Checks A for compliance to the MyConcept concept.
    return 0;
}
```

## Tutorials

- [Implementing Concepts](#implementing-concepts):
  Writing and using concept check tests.
