**NOTE:** Please see [pointgrey_camera_driver](pointgrey_camera_driver).

Home of the unofficial (incomplete) ROS driver for
[PointGrey](http://www.ptgrey.com/products/imaging.asp) *monocular*
cameras (Only tested with
[Chameleon](http://www.ptgrey.com/products/chameleon/chameleon_usb_camera.asp)
cameras both monochromatic and color).

This package was branched from Patrick Bouffard\'s
[ pgr_camera](https://github.com/pbouffard/ros.pgr_camera ) package.

## Third Party Requirement: FlyCapture2 SDK

The driver requires the
[ FlyCapture2 SDK ](http://www.ptgrey.com/products/pgrflycapture/flycapture_camera_software.asp ).

## TO DO

1\. *WARNING:* Images appear corrupted in ROS Fuerte. Needs to be
fixed! 1. Handle dynamic resizing of frames 1. Allow for more color
modes/encodings (for now using RGB8 encoding arbitrarily) 1.
Documentation
