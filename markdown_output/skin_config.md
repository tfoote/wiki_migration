## The Skin Configuration Interface

The skin_config node starts the Skin Configuration Interface as
displayed below.

![](attachment:skin_config.png)

It communicates with the skin_serv Service of the
[skin_driver](skin_driver) node and can be used to reconfigure the
following settings of the skin driver:

1\. **Number of sensor elements:** Enter the number of connected sensor
elements and press set to save. 1. **Static Threshold:** Enter the
static threshold. Default: 10. (relevant only for \"Go\"/\"NoGo\"
detection). If a new threshold is entered also enter range of sensor ids
to which the new threshold should be applied to. 1. **Dynamic
Threshold:** Enter the dynamic threshold. Default: 64. (relevant only
for \"Go\"/\"NoGo\" detection).

The two command buttons on the bottom of the window have the following
functionality:

1\. **Ram to Flash:** Save the config to the Ram of the Skin\'s hardware
interface. This config will be loaded when the skin is reset at power
up. 1. **Init Skin:** Initialize skin and set \"Ini\" values to current
\"X\" values. This is needed to calibrate the skin.

## Nodes

```clearsilver
node.0{
name=skin_config_interface
desc= The `skin_config_interface` node provides a graphical user interface to configure the Bosch skin. It communicates with the [[skin_driver]] node via the skin_serv service. 

param {
}
pub {
}
sub {
  0.name= skin_driver/skin_data
  0.type= skin_driver/skin_meas
  0.desc= Raw skin measurement with configuration data
}
srv {
  0.name= skin_driver/skin_serv
  0.type= skin_driver/skin_serv
  0.desc= Service to reconfigure skin
}
```
