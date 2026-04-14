## Motion Capture

Motion capture is an excellent tool for examining and analyzing human
and robot movement. It tracks the locations of specific points through
time. To represent such data, we present the
\<\<MsgLink(mocap_point_cloud/MotionCapture)\>\> message.

### Message Details

!MotionCapture messages have four primary features. 1. \'\'\'id\'\'\' -
An optional string describing the motion capture 2. \'\'\'labels\'\'\' -
An optional array of strings labeling each of the points in the cloud 3.
\'\'\'frames\'\'\' - An array of PointClouds representing the locations
of the markers through time. 4. \'\'\'rate\'\'\' - A float specifying
the number of frames per second.

The labels should correspond to the points in the pointclouds such that
label\[i\] is the label for the point stored at frames\[t\].points\[i\].
Missing data is demarcated with the point (0,0,0).

### Mocap Storage

Reading motion capture data from their original compressed formats (i.e.
[c3d](c3d)) can often be a slow process. Instead, we have started
storing the data as [rosbag](rosbag) files, containing
\<\<MsgLink(mocap_point_cloud/MotionCapture)\>\> messages.

## Library

This package can be used either in library format in Python, or by using
the four nodes described below.

### mcpc_helper

This library contains basic operations for reading in and converting
mocap files.

-   \`load(filename)\` - reads in mocap data from a file. If the
    filename contains \"c3d\", it reads in the c3d file. Otherwise, it
    reads in the bag file. It returns an array of !MotionCapture
    messages.
-   \`read_from_c3d(filename)\` - reads in c3d file, returns as a
    !MotionCapture
-   \`read_from_bag(filename)\` - reads in bag file, returns array of
    !MotionCaptures
-   \`write_to_bag(filename, mocaps)\` - writes the array of
    !MotionCaptures to a bag file
-   There are also a number of helper functions (\`center\`, \`rotate\`,
    etc.)

### mcpc_player

This library allows you to create a player object, which broadcasts the
PointClouds over time, using specified topics. Example usage:
```
#python
player = MocapPlayer(scale=100.0)
player.add(mocap, "/mocap0")
player.play()
``` You can also send the messages for a particular
frame using \`play_frame(t)\`.

The MocapPlayer will broadcast the data points as !PointClouds, with the
labels sent out in Markers. It is also possible to create an additional
set of Markers that draw a skeleton for the given points.

## Nodes

This package provides four different nodes for reading/examining mocap
data.

### C3d Converter

This node uses the [c3d](c3d) package to convert c3d motion capture
files to \<\<MsgLink(mocap_point_cloud/MotionCapture)\>\> messages,
stored in bag files.

```
rosrun mocap_point_cloud convert.py file1.c3d file2.c3d ...
```

This will convert the c3d files into the bag files file1.c3d

### Play

This node will load a single c3d/bag file, and play its contents using
the mcpc_player library. It will keep looping through all timepoints
according to the frame rate, until manually killed.

```
rosrun mocap_point_cloud play.py file1.bag
```

### Play using a GUI

This node is similar to Play, but allows the user to control which
timepoint is displayed using a GUI slider.

```
rosrun mocap_point_cloud play_gui.py file1.bag
```

### Statistics

The final node is a statistics utility that we\'ve found useful in our
own work. Given a list of c3d/bag files as parameters, it will print out
the following statistics for each individual !MotionCapture contained in
the files.

-   filename
-   id
-   Number of frames
-   Number of points per frame (\"tracks\")
-   Number of non-zero points in first time frame (\"initial\")
-   Minimum/Maximum/Average number of non-zero points in any time frame
    (\"minTrks\"/\"maxTrks\"/\"avgTrks\")
-   Minimum/Maximum/Average coverage of a given track over all time
    frames (\"minCov\"/\"maxCov\"/\"avgCov\")
-   Number of tracks that are non-zero in all time frames (\"full\")
-   Number of tracks that are non-zero in 90% of time frames
