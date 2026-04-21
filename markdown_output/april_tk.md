ROS package that downloads and build the April Toolkit
(<http://april.eecs.umich.edu/wiki/index.php/Download_and_Installation>)

## Running standalone tools

There is a convenience wrapper for running standalone tools with the
environment variables correctly setup. These instructions mirror the
instructions at <http://april.eecs.umich.edu/wiki/index.php/April_Tags>

### Camera Viewer

Since the [april_tags_node](april_tags_node) package subscribes to a ROS
image topic for the camera stream, it is *not essential* for this node
to work. However, if you intend to run the standalone tools in the
[april_tk](april_tk) package, you\'ll need this viewer to work.
```
rosrun april_tk execute april.jcam.JCamView
```

### Tag Generation

You can generate families of tags using the Tag Generator. This is
necessary if you wish to print out copies of the tags.
```
cd
mkdir ~/my_tags
rosrun april_tk execute april.tag.TagFamily april.tag.Tag36h11 ~/my_tags/tag36h11
```

### Tag Test

You can run the default Tag Test application to make sure your tag is
working. Note that the focal length of the camera as well as the tag
size is hard-coded into Tag Test, so the detection might be projected
incorrectly. ```
rosrun april_tk execute april.tag.TagTest --url <cam-url> [--tagfamily <tag-family>]
``` You can determine \`cam-url\`
through the Cam Viewer utility. Run Tag Test without any arguments to
see the help menu.

## Updating the April Toolkit version

This package wrapper downloads a specific revision of the April toolkit
for stability reasons (revision eafdf0739 from the april git
repository). If you find an upgraded version of the repository to work
better, feel free to submit a bug report.

## Report a Bug

This package just serves as a wrapper for the APRIL toolkit. If you
detect a bug in the wrapper, please report it on the repository
page(<http://code.google.com/p/utexas-ros-pkg/issues/list>). If you find
a bug in the APRIL toolkit, please contact the original developers.
