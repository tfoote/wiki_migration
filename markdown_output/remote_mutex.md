This package contains an implementation of a remote_mutex to be used by
many different nodes. There are some rare cases when a common resource
needs to be shared but used with mutual exclusion. Each mutex has a
unique name through-out the system.

## Mutex Guard

The mutex guard is a single node and guards a single mutex. To start a
mutex guard run 

```
rosrun remote_mutex mutex nameOfMutex
```



## Use the mutex in your node

To use the mutex, you have to first add to manifest.xml a dependency to
this package and to the CMakeLists.txt to link the executable with the
RemoteMutex library.

In the code you should include 

```
#include "remote_mutex/RemoteMutex.h"
```



and then create an RemoteMutex object



```
RemoteMutex mutex("nameOfMutex");
```



the new object can now be used to lock, unlock or get the status of the
remote mutex using the object's methods.

For example by calling



```
mutex.lock();
```



The call blocks until it can locked. Note that you can set a maximum
amount of time to wait. For example,



```
bool locked = mutex.lock(ros::Duration(2));
```



will try to lock for 2 minutes. If it fails, then it will return false.

For the full documentation see API.

## Technical Information

The remote mutex implementation is based on a single service that the
mutex guard serves. The mutex clients lock and unlock the mutex by
calling a service (this is done by the RemoteMutex implementation).
