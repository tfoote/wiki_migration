## Overview

This package contains api extracted from 2.4.x/3.y.z versions of opencv
that are not included in the system opencv released for indigo
platforms.

-   parallelised thread support for qt imshows (i.e. call imshow related
    api safely from any thread)
-   zoomable imshow windows

![Zoomable Imshows\|width=600](attachment:zoomable_imshows.png)

## Usage

The api has been namespaced in a separate namespace, `cv_backports` so
as to avoid conflicts with the regular opencv api.

A full listing of the api can be found in each header. Only the commonly
used ones are shown here.

**cv_backports/imshow.hpp**

```cplusplus
void imshow(const std::string& winname, cv::InputArray mat);
void namedWindow(const std::string& winname, int flags = cv::WINDOW_AUTOSIZE);
void destroyWindow(const std::string& winname);
void destroyAllWindows();
int waitKey(int delay = 0);
void imshow(const std::string& winname, cv::InputArray mat);
int startWindowThread();
void resizeWindow(const std::string& winname, int width, int height);
void moveWindow(const std::string& winname, int x, int y);
void setWindowProperty(const std::string& winname, int prop_id, double prop_value);//YV
double getWindowProperty(const std::string& winname, int prop_id);//YV
typedef void (*MouseCallback)(int event, int x, int y, int flags, void* userdata);
void setMouseCallback(const std::string& winname, MouseCallback onMouse, void* userdata = 0);
CvFont fontQt(const std::string& nameFont, int pointSize=-1,
                         cv::Scalar color=cv::Scalar::all(0), int weight=CV_FONT_NORMAL,
                         int style=CV_STYLE_NORMAL, int spacing=0);
void addText( const cv::Mat& img, const std::string& text, cv::Point org, CvFont font);
```

## Examples

**imshow**

```cplusplus
#include <cv_backports/imshow.hpp>

cv::Mat image;
// ...load the image
std::string name = "Depth Image";
cv_backports::namedWindow(name, CV_WINDOW_KEEPRATIO);
cv_backports::imshow(name, image);
// eventually
cv_backports::destroyWindow(name);
```
