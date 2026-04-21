## Overview

The Amazon Kinesis Video Streams ROS package enables robots to stream
video to the cloud for analytics, playback, and archival use. Out of the
box, the nodes provided make it possible to encode & stream image data
(e.g. video feeds and LIDAR scans) from a ROS "Image" topic to the
cloud, enabling you to view the live video feed through the Kinesis
Video Console, consume the stream via other applications, or perform
intelligent analysis, face detection and face recognition using Amazon
Rekognition.

The node will transmit standard \`sensor_msgs/Image\` data from ROS
topics to Kinesis Video streams, optionally encoding the images as h264
video frames along the way (using the included h264_video_encoder), and
optionally fetches Amazon Rekognition results from corresponding Kinesis
Data Streams and publishing them to local ROS topics.

Note: h.264 hardware encoding is supported out of the box for OMX
encoders and has been tested to work on the Raspberry Pi 3. In all other
cases, software encoding would be used, which is significantly more
computing intensive and may affect overall system performance. If you
wish to use a custom ffmpeg/libav encoder, you may pass a \`codec\` ROS
parameter to the encoder node (the name provided must be discoverable by
[avcodec_find_encoder_by_name](https://ffmpeg.org/doxygen/2.7/group__lavc__encoding.html#gaa614ffc38511c104bdff4a3afa086d37).
Certain scenarios may require offline caching of video streams which is
not yet performed by this node.

**Amazon Kinesis Video Streams**: Amazon Kinesis Video Streams makes it
easy to securely stream video from connected devices to AWS for
analytics, machine learning (ML), playback, and other processing.
Kinesis Video Streams automatically provisions and elastically scales
all the infrastructure needed to ingest streaming video data from
millions of devices. It also durably stores, encrypts, and indexes video
data in your streams, and allows you to access your data through
easy-to-use APIs. Kinesis Video Streams enables you to playback video
for live and on-demand viewing, and quickly build applications that take
advantage of computer vision and video analytics through integration
with Amazon Recognition Video, and libraries for ML frameworks such as
Apache Mx\`\`Net, Tensor\`\`Flow, and Open\`\`CV.

**Amazon Rekognition**: The easy-to-use Rekognition API allows you to
automatically identify objects, people, text, scenes, and activities, as
well as detect any inappropriate content. Developers can quickly build a
searchable content library to optimize media workflows, enrich
recommendation engines by extracting text in images, or integrate
secondary authentication into existing applications to enhance end-user
security. With a wide variety of use cases, Amazon Rekognition enables
you to easily add the benefits of computer vision to your business.

\`\`\`Keywords\`\`\`: ROS, AWS, Kinesis Video Streams

### License

The source code is released under
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Kinetic
-   Lunar
-   Melodic
