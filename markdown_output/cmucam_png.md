# Step 1

There is a binary that must be downloaded to the cmucam3 camera. The
source, etc, for this is in the directory \`png-robin/\`. There is also
a precompiled hex file that you can use if you don\'t want to compile
the cmucam3-resident application yourself. But you\'ll still have to
download the hex file to the cmucam3 with lpc21isp.

If you want to make changes or recompile the cmucam3-resident
application, you should have a working installation of the cmucam3
development environment, and be able to compile the examples in the
cc3/projects directory and download the applications to the cmucam3.
Once you can do this, you can make a new directory in the \`projects/\`
directory of your cmucam3 distribution called \`png-robin/\` and copy
the contents of the \`png-robin/\` directory provided with this ROS node
into that one. The makefile should then work and provide the correct
paths and compile the application.

# Step 2

The \`cmucam_png\` node acquires a PNG file from the cmucam3 about once
every twenty seconds and publishes it as a compressed image. Acquisition
takes around 20 seconds per image because they come over a 115,200 bps
serial line. Each PNG image is 352x287 pixels in size. The topic used is
named \`cmucam\`.

The node is started as follows:

\`rosrun cmucam_png cmucam_png_server.py\`
