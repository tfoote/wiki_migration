## State Format Description

Proposer: \'\'\'John Hsu\'\'\'

This format is intended to keep state information of a robot as
described by the [URDF](urdf) file.

## Description

### Example

```
<model name="model">
  <position xyz="0 0 0" rpy="0 0 0"/>
  <twist xyz="0 0 0" rpy="0 0 0"/>
  <link name="link1">
    <position xyz="0 0 0" rpy="0 0 0"/>
    <twist xyz="0 0 0" rpy="0 0 0"/>
    <wrench force="0 0 0" torque="0 0 0" >
      <reference_point xyz="0 0 0" rpy="0 0 0"/> <!-- relative to the link origin -->
    </wrench>
  </link>
</model>
```
