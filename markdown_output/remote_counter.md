In the remote_counter package contains an implementation of a counter
that can be remotely and atomically be incremented and/or decremented.
The implementation also includes a sample limited counter.

## Using the Limited Counter

The counter can be used either as a stand-alone node or by using it in
another node. Each counter has a unique name, initialized at the
constructor.

### Starting a stand-alone counter

To use the standalone node you can run



```
rosrun remote_counter RemoteCounter name_of_counter
```



### Using the counter inside your node

To use the counter inside a node is simple. You should first set as a
dependency the remote_counter package and include the RemoteCounter.h

Note that if you are using more than one thread (or many callback
queues) then the counter will not be atomically incremented

### Remotely incrementing the counter

To remotely increment/ decrement the counter you have to call the
remote_counter::countingSrv service. The only argument this service
accepts in the number by which to increment the counter. Note that if
you would like to decrement the counter you can try incrementing it by a
negative number.
