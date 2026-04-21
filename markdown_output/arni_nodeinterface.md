```wiki
''' This Documentation is under Construction'''

It is currently in alpha state and will be completed when it's done.
```

## Overview

The arni_nodeinterface package provides functionality to measure
resource usage data of the hosts and the nodes running on the host.
[arni_processing](arni_processing) can use the collected data to
determine which host or node is not behaving as it should.

This package provides a Service to shut down or restart misbehaving
nodes.

## Documentation

### Parameter

  -- ------------------------------ -- ------------------------------------------------------------------------------- --
     **parameter**                     **description**                                                                 
     window_max_elements               The maximum number of data for one time window                                  
     publish_intervall                 The intervall in which statistics about the collected stats will be published   
     /arni/check_enabled_interval      Periodically checks if enable_statistics is true, no data will be collected     
     search_nodes                      Sets the interval in which host will look for new or dead nodes                 
  -- ------------------------------ -- ------------------------------------------------------------------------------- --

### Service

arni_nodeinterface provides an interface to shut down, restart nodes or
execute some other command. The service-type has these fields:

  -- --------------- -- ----------------------------------------------------------------- --
     **field**          **description**                                                   
     node               Name of the node, the action should be executed on                
     action             Type of action to execute, valid values:stop,restart,command      
     command            If action was \'command\' this gives the command to be executed   
     returnmessage      Return value, message about success of action                     
  -- --------------- -- ----------------------------------------------------------------- --

### Third Party Packages

#### psutil

Psutil is used to collect usage stats. Version musst be at least 2.1.1
psutil can be found [here](https://github.com/giampaolo/psutil).

#### PySensors

PySensors is used to gather the current temperature of the host, maybe.
It can be found [here](https://pypi.python.org/pypi/PySensors/).
