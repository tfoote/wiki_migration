## Overview

This is a light version of
[ecl_sigslots](https://index.ros.org/p/ecl_sigslots) and provides a very
ruthlessly simple signals and slots mechanisms useful for

- very\* embedded development. Differences from
  [ecl_sigslots](https://index.ros.org/p/ecl_sigslots):

<!-- -->

- Not thread safe\...

This is a bit of a vague statement on its own. In essence, its usually
important to make sure your signals and slots finish processing any
currently executing slots before they self destruct. Most sigslot
implementations dont do this,
[ecl_sigslots](https://index.ros.org/p/ecl_sigslots) does, but
ecl_sigslots_lite does not. If you
have a monolothic program with a single thread, this probably doesn't
matter, but if not, then you must take care to ensure signals and slots
close appropriately.

- No disconnects\...

Adding disconnect capability adds alot of complexity to the sigslots
implementation. Lite sigslots assume that signals and slots connections,
once fixed, stay until the signal goes out of scope.

- No dynamic storage (no heap storage with malloc/new)\...

This is often verboten with various embedded compilers and introduces
alot of system overhead. Lite sigslots allocates memory up front and
will not permit overuse thereafter.

- Self contained\...

While utilising things like standard error flag constructors (from
[ecl_errors](https://index.ros.org/p/ecl_errors)) might be convenient,
this package is and likely will often be used standalone in a firmware
project. As a result, its designed with its own internal mechanisms
(e.g. error class) so it's source can be simply copied to a firmware
project.

## Compiling & Linking



```cplusplus
#include <ecl/sigslots_lite.hpp>

// Signals
using ecl::lite::Signal;

// Functions
using ecl::lite::connect
using ecl::lite::global_slots_stored;
using ecl::lite::global_slots_capacity;
using ecl::lite::member_slots_stored;
using ecl::lite::member_slots_capacity;
```



## Examples

- `src/examples/sigslots.cpp`

## Tutorials

- [Debugging Sigslots Lite](#debugging-sigslots-lite):
  Utility functions for diagnosing lite sigslots.
- [Using Sigslots Lite](#using-sigslots-lite):
  Shows how to set up signals and slots with
  ecl_sigslots_lite.

## Debugging Sigslots Lite

### Utility Functions



```cplusplus
// statistics for global slots with arg type 'const char*'
std::cout << ecl::lite::global_slots_stored<const char*>() << std::endl;
std::cout << ecl::lite::global_slots_capacity<const char*>() << std::endl;

// statistics for global slots with no args
std::cout << ecl::lite::global_slots_stored<void>() << std::endl;
std::cout << ecl::lite::global_slots_capacity<void>() << std::endl;

// statistics for member slots of foo with no args
std::cout << ecl::lite::member_slots_stored<void>(foo) << std::endl;
std::cout << ecl::lite::member_slots_capacity<void>(foo) << std::endl;
```



Above, foo is an object of type Foo with member slots similar to the
class outlined in
[Using Sigslots Lite](#using-sigslots-lite).

## Using Sigslots Lite

### Slots in the Background

Users of lite sigslots don't actually directly use Slot classes (unlike
[ecl_sigslots](https://index.ros.org/p/ecl_sigslots)). Slots are still
there, but they are stored behind the scenes, either in a global slots
manager or member slots manager inherited by a class.

### Storage Capacities

Signals and slots need to reserve memory before usage. This identifies
how many connections each can handle. For global slots, you need to set
a static variable before making any connections to slots of that type.



```cplusplus
// allocate for global function slots with const char* and void arg footprints
template<> const unsigned int ecl::lite::GlobalSlots<const char*>::capacity = 4;
template<> const unsigned int ecl::lite::GlobalSlots<void>::capacity = 2;

int main() {
    // ...
```



For member slots, your class needs to inherit from the MemberSlots
interface and specify the capacity as a template parameter (default is
1).



```cplusplus
class Foo : public ecl::lite::MemberSlots<const char*,Foo>,
            public ecl::lite::MemberSlots<void,Foo,2>
{
public:
    Foo() {}

    void f(const char* str) { /* */ }
    void g() { /* */ }
    void h() { /* */ }
};
```



For signals, simply specify the capacity template parameter (again
default is 1) when instantiating the signal. This reflects the number of
connections it can handle.



```cplusplus
ecl::lite::Signal<const char*, 2> signal;
```



### Connections

Connections are made via the connect functions, linking directly to the
function pointers.



```cplusplus
connect(signal,f);            // connecting to a global slot
connect(signal,&Foo::f, foo); // connecting to a member slot
```
