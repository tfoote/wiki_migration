# Summary

This package provides a simple way of processing and extracting camera
images from a stored bag file. Many bags will store only the raw_image
and camera_info, either because the creators want to avoid the overhead
of running image_proc or to minimize the amount of redundant information
stored in the bag. `bag_to_images` runs on a bag file, performs the
same processing as an image_proc node, and saves the resulting images to
disk as separate files. One of the main advantages of bag_to_images is
that unlike setting up a full ROS graph to do the same processing there
is no worry of dropped images.

# Usage

Basic usage (dumps colorized rectified images from left wide stereo
camera): ```
bag_to_images --bag [filename].bag
```

To see the various options available: ```
bag_to_images
```

Dumping .png files: ```
bag_to_images --bag [filename].bag --extension png
```

To dump (rectified) images from the right narrow camera:
```
bag_to_images --bag [filename].bag --camera /narrow_stereo/right --color false
```

# Implementation Notes

This package depends on the rosrecord C++ API, which is likely to change
at some point. It also depends on the unreleased C++ API for image_proc,
which is relatively stable.

## Handling of camera_info

The camera model used for rectification is updated whenever a new
camera_info message is encountered in the bag file. Until at least one
such message has been encountered images will be dropped.

## Possible future extensions

-   A progress indicator would be useful and can be added when the
    rosrecord API provides some feedback about progress.
-   Stereo processing might be useful, and options could be added to
    process and produce point cloud files and/or disparity maps
