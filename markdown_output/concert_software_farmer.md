## Overview

### APIs



```clearsilver
name = 
desc = 
pub {
  0.name = ~list
  0.type = concert_msgs/SoftwareProfiles
  0.desc = a list of available software in the system, latched
  1.name = ~status
  1.type = concert_msgs/SoftwareInstances
  1.desc = informs the current status of software farm like which software are running and who users are, and the paramter configuration. latched.
}
srv {
  0.name = ~allocate
  0.type = concert_srvs/AllocateSoftware
  0.desc = used by client to allocate software to user.
}
param {
  0.name = ~release_timeout
  0.type = double
  0.default = 15
  0.desc = timeout configuration for graceful system shutdown
}
```


