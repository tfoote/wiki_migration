## Overview

### Node APIs



```clearsilver
name = 
desc = 
pub {
  0.name = ~list
  0.type = concert_msgs/Services
  0.desc = shows all services' status and profile.
}
srv {
  0.name = ~enable
  0.type = concert_srvs/EnableService
  0.desc = enables a requested service
  1.name = ~update_service_config
  1.type = concert_srvs/UpdateServiceConfig
  1.desc = updates a service profile
}
param {
  0.name = ~disable_cache
  0.default = "false"
  0.type = bool
  0.desc = flag whether reading solution configuration and service profile from cache or default
  1.name = ~concert_name
  1.default = ""
  1.type = string
  1.desc = concert name, e.g. Pirate Concert, demo_concert, etc.
  2.name = ~services
  2.default = ""
  2.type = string
  2.desc = service list resource location
  3.name = ~default_auto_enable_services
  3.default = []
  3.type = list
  3.desc = autoenable services, e.g. [admin, initialisation] services which auto enabled on start up or "all" to enable all services
}
```


