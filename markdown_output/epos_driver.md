This package provides simple interface to control maxon motors via EPOS
controler.

## Documentation

Package includes C library
([libEPOS](http://sourceforge.net/projects/libepos/)) to control the
EPOS motor control from maxon motor
([www.maxonmotor.com](http://www.maxonmotor.com)) using a GNU/Linux
system and ROS wrapper.

## Nodes

This package provides one node - epos_driver_node.



```clearsilver
name = epos_driver_node
desc = communicates with EPOS driver
pub {
  0.name = /tf
  0.type = tf/tfMessage
  0.desc = publishes a transform from frame /maxon to /base
  1.name = /EPOSState
  1.type = epos_driver/EPOSState
  1.desc = publishes current possition and other informations about driver
}
srv {
  0.name = /MoveTo
  0.type = epos_driver/MoveTo
  0.desc = request to move motor to given position
  1.name = /MoveCycle
  1.type = epos_driver/MoveCycle
  1.desc = request to move motor between two given positions
}
```


