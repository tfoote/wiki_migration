## Features

- `Mutex` - multi-thread variable protection.
- `Thread` - raii style one-shot thread class.
- `Threadable` - an inheritable thread interface.

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

- [Thread](#thread) : threading
  functionality via composition.
- [Threadable](#threadable) :
  threading functionality via inheritance.
- [Thread Locks](#thread-locks)
  : locking threads to protect shared data.
- [Priorities](#priorities) :
  setting thread or process scheduling priorities.

## Thread

- **Description:** Threading functionality via composition.
- **Keywords:** ecl threads
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Threadable](#threadable)
  [Thread Locks](#thread-locks)
  [Priorities](#priorities)

The ecl `Thread` class adds threadable functionality via composition
(i.e. via objects) rather than via inheritance. The default mode is raii
style, that is, it initialises and automatically starts a thread when
constructed and manages the thread cleanly when the thread object goes
out of scope.

It does have an alternative delayed mode which will instantiate a thread
object and only begin threading work when loading the `start()` method
with a worker function.

### Construction

Construction can be done directly through free and member function
handles or via function objects. Refer to the documentation on
`Function Objects` and `Reference Wrappers` in
[ecl_utilities](https://index.ros.org/p/ecl_utilities) for more details
about creating and using function objects/reference wrappers (note, use
a reference wrapper if you want to pass a 'heavy' function object!).



```cplusplus
using ecl::utilities::generateFunctionObject;

int f() {}
int g(int i) {}
class A { 
    void f() {}
    void g(int i) {}
};
class FunctionObject {
public:
    typedef void result_type;
    void operator()() { 
        //
    }
};

// ...

A a;
FunctionObject function_object;

Thread thread1(f));                                   // Thread a nullary global function.
Thread thread2(generateFunctionObject(g, 3));         // Thread a bound unary global function.
Thread thread3(&A::f, a);                             // Thread a nullary member function.
Thread thread4(generateFunctionObject(&A::g, a, 2));  // Thread a bound unary member function.
Thread thread5(function_object);                      // Thread a nullary function object.
Thread thread6(ref(function_object));                 // Thread a reference to a nullary function object.
```



### Scope

Also, this object is permitted to go out of scope without affecting the
thread that it started (it may very well still be running!). When it
goes out of scope, it simply detaches it and lets it clean itself up. At
this point you only lose control of administration of the thread
(joining, checking if it is running, cancelling etc).



```cplusplus
void g() {
    for (int i = 0; i < 10; ++i ) {
        sleep(1);
        cout << i << endl;
    }
}

void create_out_of_scope_thread() {
    Thread thread(g);
} // thread will go out of scope here.

// ...

create_out_of_scope_thread();
// Cannot manage the thread from here, but it will continue running.
sleep(10); // Note that we have no way of joining with it.
```



### Stack Size

On embedded systems with no swap its important to watch how much stack
memory you supply to the thread. This can be manually specified in the
thread constructor.



```cplusplus
Thread thread(g,1024*1024); // allocates 1M to the thread instead of the system default which is usually 8M.
```



### Priority

Thread priorities can be specified at the point where the function is
loaded and designated to start (i.e. either when loading the constructor
or the `start()` function).

If you wish to configure the thread's priority dynamically, you'll
have to fall back to using the `ecl::set_priority()` function directly
from inside the worker function.

Refer to the tutorial on
[priorities](#priorities) for more
information.

### Other

Other member functions include

- `cancel()` : instructs a running thread to abort at the next
  permitted interruption point (read the man pages for pthreads for more
  info).
- `join()` : wait for the running thread to finish.
- `isRunning()` : check to see if the thread is still running.

Error handling is done in debug mode (i.e. -DNDEBUG is not set) via
exceptions. These will throw and report any information on the resulting
posix errors should they occur.

## Threadable

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Thread](#thread).
- **Description:** Threading functionality via inheritance.
- **Keywords:** ecl threadable
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Thread Locks](#thread-locks)
  [Priorities](#priorities)

The threadable class implements a concept for worker threads that want
to retain state information (possibly for use by other parts of the
program) in a class. Think of it as a threaded function object rather
than a regular c-style threaded function.

Implementation wise, it provides an inheritable interface for your
threading class. All the class needs to do is:

- inherit the `Threadable` class.
- implement the `runnable()` method.
- call the `start()` method to begin running in a sepearate thread.

Note that it will not spawn multiple threads - it has a check that
ensures it will only execute one thread at any point in time. It is
designed to be something more akin to a thread function object rather
than a thread factory.



```cplusplus
class A : Threadable {
    void runnable() {
    // thread work here
    }
}

int main() {
    A a;
    a.start();
    return 0;
}
```

## Thread Locks

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Thread](#thread),
  [Threadable](#threadable).
- **Description:** Locking threads to protect shared data
- **Keywords:** ecl threads mutex
- **Tutorial Level:** INTERMEDIATE

### Overview

The mutex is fairly standard, and on some systems can be more complex,
but here the wrapper simply acts as a closed door with the usual lock,
trylock and unlock features. The behaviour is also somewhat different
depending on the platform.

On posix, the class is set up to run in two modes. When NDEBUG is not
defined, it will do exception handling (via ecl's
[StandardException](https://index.ros.org/p/ecl_exceptions)) for posix
errors as well as configuring the mutexes for deadlock checking (see
below for example code). Exception handling and deadlock checking are
disabled when NDEBUG is defined.



```cplusplus
Mutex mutex;

mutex.lock();     // Locks
// do work here
mutex.unlock();
mutex.trylock();  // Locks
mutex.trylock();  // Fails to lock and returns immediately.
mutex.unlock();


mutex.lock();
// mutex.lock();     // The DEADLOCK! Like this, the program will usually halt forever.

// If NDEBUG is not defined, then on posix systems, you can catch deadlocks like this.
try {
    mutex.lock();
} catch ( StandardException &e ) { 
    std::cout << e.what() << std::endl;
}   

// Typical output from a caught deadlock:
// Location : /mnt/froody/work/code/cpp/projects/ecl/modules/core/src/lib/threads/mutex_pos.cpp:57
        // Flag     : The object was used incorrectly.
        // Detail   : DEADLOCK! The mutex has already been locked by this thread, it now has to wait on itself.
```

## Priorities

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Thread](#thread),
  [Threadable](#threadable).
- **Description:** Setting thread or process scheduling priorities.
- **Keywords:** ecl threads priorities
- **Tutorial Level:** INTERMEDIATE

### Levels

The ecl defines abstract levels to standardise the priority api across
platforms. These are defined in the `Priority` enum which has values
for:



```cplusplus
using ecl::BackgroundPriority;
using ecl::LowPriority;
using ecl::NormalPriority;
using ecl::HighPriority;
using ecl::CriticalPriority;
// Posix real time scheduling priorities only (not available on windows).
using ecl::RealTimePriority4;
using ecl::RealTimePriority3;
using ecl::RealTimePriority2;
using ecl::RealTimePriority1; // highest priority
```



### Setting

The threading classes typically allow configuration from their methods,
however you can set/reset the priority for the current thread at any
point by calling `set_priority`.



```cplusplus
ecl::set_priority(ecl::BackgroundPriority);
```



### Process Priority

Calling the `set_priority` function in the main thread will configure
your process' priority (this setting should get passed on to its
children by default on most systems).

### Higher Level Priorities

Typically linux systems do not come pre-configured for higher level
priorities - typically anything higher than `NormalPriority` requires
special permissions. If these are not set, the `set_priority` function
will either throw an exception (in debug mode) or return false when not
granted permission to do so.



```cplusplus
try {
    set_priority(RealTimePriority4);
} catch ( const StandardException &e ) { 
    std::cout << "Do not have permission for the higher level priorities." << std::endl;
}
```



To configure your system to do so, edit `/etc/security/limits.conf`.
An example of editing this file for a user *snorri* to enable both
realtime priorities to level 95 and the maximum niceness setting on a
typical linux box:



```cplusplus
snorri          -       nice            -20
snorri          -       rtprio           95
```



### Real Time Scheduling

This is just some notes (for curiosity) with reagards to priorities
corresponding to `RealTimePriority4` or above.

Posix systems will often have various real time priority scheduling
capabilities. Note that this is *not real time linux*. Rather, threads
working under this sort of scheduling are pulled from the usual userland
scheduling manager where they are typically assigned a *niceness* value.

A single thread pulled into real time scheduling is guaranteed to get
cpu time *whenever it needs it*. There is no weighting, or favours done
for threads who've waited a long time. It's a guarantee. The rest of
the threads on the system will then be spliced time when the real time
thread is sleeping or idle.

/!\\ Be careful with this! We've found it can greatly enhance control
loops for motors to ensure that they work sufficiently in most systems
without the need to go to real time linux. However you must take care
that these threads don't start starving the remaining threads on your
system.

In addition, a thread working at `RealTimePriority2` is guaranteed to
get cpu time over a thread working at `RealTimePriority1`. Two threads
at the same real time priority level will go into a round robin.

You can check that your threads are running at realtime priority by
running the following command:



```
> ps -C <process_name> -m -o pid,rtprio,ni,pri,vsize,rssize,pmem,pcpu,comm
```

## Tutorials

- [Priorities](#priorities):
  Setting thread or process scheduling priorities.
- [Thread](#thread): Threading
  functionality via composition.
- [Thread Locks](#thread-locks):
  Locking threads to protect shared data
- [Threadable](#threadable):
  Threading functionality via inheritance.
