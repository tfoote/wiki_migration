## Overview

`rocon_launch` was originally a tool designed for spawning multimaster
test environments on a single pc. It did this by spawning multiple
terminals, inside each of which it would execute roslaunch on a specific
port.

This however turned out to also be useful in conveniently launching
different windows on a single ros system which is a surprisingly
repetitive pattern in testing. Instead of starting your main roslauch in
one terminal and then switching to a different terminal to launch, for
example rviz, you could bundle the procedure in a single
`rocon_launch`.

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <style="text-align: center;" tablewidth="100%">![\|width=100%](attachment:rocon_launch/Tutorials/indigo/Rocon Launch for Single Masters/rocon_launch.png)   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Specifications

## Tutorials
