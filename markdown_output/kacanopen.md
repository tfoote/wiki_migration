## Documentation

For now please, please refer to
<https://github.com/KITmedical/kacanopen/blob/master/README.md>.

![\|width=480](attachment:KaCanOpen_architecture.png)

Excerpt from documentation on github:

!KaCanOpen is an easy-to-use CANopen stack, which consists of four
parts:

-   **Drivers**: A wide range of hardware is supported using different
    CAN drivers. They have been developed by the CanFestival project.
    Read this for details.
-   **Core**: This is a library which implements basic CANopen protocols
    like NMT, SDO and PDO. As an example, you can easily fetch a value
    from a device (uploading in CanOpen terminology) via
    `core.sdo.upload(node_id, index, subindex)`. It furthermore allows
    you to register callbacks on certain events or any incoming
    messages, so one can build arbitrary CANopen nodes (master or slave)
    using this library.
-   **Master**: This library is intended to be used for a master node.
    It detects all nodes in a network and allows to access them via
    standardized CiA® profiles. For example, on a motor device (profile
    CiA® 402) you can simply call
    `mymotor.set_entry("Target velocity", 500)`. A main feature of this
    library is transparent SDO/PDO access to dictionary entries: By
    default a value is fetched and set via SDO. But you can configure
    PDO mappings to instead keep the value up-to-date in background via
    (more lightweight) PDO messages. The call itself
    (`mymotor.set_entry("Target velocity", 500)`) keeps unchanged.
-   **ROS Bridge**: This library provides a bridge to a ROS network,
    which makes !KaCanOpen especially interesting for robotics. After
    setting up the CANopen network, the library can publish slave nodes
    so they are accessible through ROS messages. Special effort is put
    into the use of standardized message types which allows interaction
    with other software from the ROS universe. For example, motors can
    be operated using !JointState messages.

!KaCanOpen is designed to make use of modern C++11/14 features and to
avoid redundant code on the user side wherever possible. Reusing all the
available functionality in Core, Master and Bridge, a custom node for a
custom CANopen device can be written in less than 100 lines of code.

## Related publication

```
@inproceedings{kacanopen2016,
  title = {KaCanOpen: An Open Plug&Play CANopen Stack for ROS in Modern C++},
  author = {Thomas Keh, Andreas Bihlmaier, Julien Mintenbeck and Heinz W{\"o}rn},
  booktitle = {Proceedings of the 47th International Symposium on Robotics (ISR)},
  year = 2016
}
```
