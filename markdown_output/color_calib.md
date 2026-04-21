Color_calib library contains a node and other color calibration
utilities for working with a macbeth chart.

At the moment, color-calibration node only runs on image_array topics.
To run the color calibration run, for instance: ```
rosrun color_calib calib_node images:=videre/images
```
Then click on the 4 corners in **clockwise** order, beginning with the
upper left corner of the dark-skin colored square.

It will compute the 3x3 color calibration and place it in the parameter:
` topic_name/image_label/color_calib`. For example, if the topic name is
"videre/images" and the image label is "left", the color calibration
will be placed in the parameter: `videre/images/left/color_calib`.

The following code snippet can be used to retrieve the color calibration
matrix from the parameter server as a CvMat. ```
CvMat* color_cal = cvCreateMat(3, 3, CV_32FC1);
cvSetIdentity(color_cal, cvScalar(1.0));

std::string color_cal_str = map_name("images") + std::string("/") + image_msg.images[i].label + std::string("/color_cal");

if (has_param(color_cal_str))
{
  XmlRpc::XmlRpcValue xml_color_cal;
  get_param(color_cal_str, xml_color_cal);
  for (int i = 0; i < 3; i++)
     for (int j = 0; j < 3; j++)
         cvmSet(color_cal, i, j, (double)(xml_color_cal[3*i + j]));
}
```

Another example in context can be found in the source for cv_view_array:
cv_view/src/cv_view_array.cpp

Once you have the color calibration matrix, you can use it to transform
an existing opencv image. Note, for the videre cameras, you will very
likely want to decompand the image first. Decompand is a function
contained in libcolorcalib. To use it, make your package depend on
color_calib, and then include the header: "colorcalib.h"

The following snippet will decompand an image and then transform it
according to the color calibration: ```
decompand(cv_image, cv_image);

if (cv_image->nChannels == 3)
   cvTransform(cv_image, cv_image, color_cal);
```
