## Overview

This package is a ROS release of
[Swift Navigation](http://swiftnav.com/)'s libswiftnav. It offers a
variety of functionality related to linear algebra and spacial
processing.

  -- ---------------------------- -- -------------------------------------------- --
     **Official Documentation**      <http://docs.swift-nav.com/libswiftnav>      
     **Upstream Source**             <https://github.com/swift-nav/libswiftnav>   
                                                                                  
  -- ---------------------------- -- -------------------------------------------- --

The versions released to ROS are:

  -- ---------------- -- ------- --
     **ROS Hydro**       v0.8    
     **ROS Indigo**      v0.13   
                                 
  -- ---------------- -- ------- --

All libswiftnav releases are here:
<https://github.com/swift-nav/libswiftnav/releases>

## Building From Source

Note that because libswiftnav is a plain CMake project and not a
[catkin](catkin) one, you can't use it in a regular catkin workspace---
you must build and install using `catkin_make_isolated`, and then
overlay the resulting workspace with a regular catkin one.
