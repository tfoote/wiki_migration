## Features

-   `Mutex` - multi-thread variable protection.
-   `Thread` - raii style one-shot thread class.
-   `Threadable` - an inheritable thread interface.

There are also a few methods for setting thread/process priorities.

### Cross Platform Support

Currently the windows code is available, but not currently present (need
to port it from the old version of ecl) because it isn't getting
used/tested frequently. It can be added back in when and as needed
quickly as the framework is still in place.

## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/threads.hpp>

// The thread classes
using ecl::Mutex;
using ecl::Thread;
using ecl::Threadable;
    
// Priorities
using ecl::set_priority;
using ecl::get_priority;
using ecl::print_priority_diagnostics;
using ecl::BackgroundPriority;
using ecl::LowPriority;
using ecl::NormalPriority;  
using ecl::HighPriority;    
using ecl::CriticalPriority;
using ecl::RealTimePriority1;   
using ecl::RealTimePriority2;   
using ecl::RealTimePriority3;   
using ecl::RealTimePriority4;
```



If using catkin with ROS, you should make sure to declare a dependency
on ecl_threads in your package.xml and find_package ecl_threads in your
CMakeLists.txt:



```
find_package(catkin REQUIRED COMPONENTS
   ecl_threads
   # other dependencies ...
)
```



If outside ros, you will also need to link to *ecl_threads*.

## Tutorials

-   [Thread](ecl_threads/Tutorials/Thread) : threading functionality via
    composition.
-   [Threadable](ecl_threads/Tutorials/Threadable) : threading
    functionality via inheritance.
-   [Thread Locks](ecl_threads/Tutorials/Thread Locks) : locking threads
    to protect shared data.
-   [Priorities](ecl_threads/Tutorials/Priorities) : setting thread or
    process scheduling priorities.
