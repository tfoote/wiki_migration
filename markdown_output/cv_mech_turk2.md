# Command line usage

## session_results.py

Download image annotation results from the server and save them into
files locally

Usage: rosrun cv_mech_turk2 session_results.py \--session=SESSION
\[\--server=SERVER\] \[\--saveto=results/session\]
\[\--size=IMG_WIDTHxIMG_HEIGHT\] \[\--truesize\] \[\--naming\]

-   \--session - the name of the session to read results from
-   \--server - the URI or alias of the server
-   \--size=640x480 - will convert annotations to 640x480 frame. By
    default, the annotations are converted to the resolution of the
    downloaded image ("TRUESIZE"). "NONE" will force no conversion.
    Otherwise, the annotation will be converted to the specified width
    and height.
-   \--truesize - same as \--size="TRUESIZE"
-   \--naming - determines how to name the local filenames (image and
    annotations). By default (\--naming=original), the images and
    annotations use the original image name (e.g. frame0001.jpg) that as
    submitted for annotation. If \--naming=server_image, then the image
    names on the server (unique IDs) will be used for naming the local
    images and annotation. If \--naming=server_work_unit, the work unit
    ID will be used as the local name for the image and the submission.
-   \--filter whether to filter by the quality. By default the filter is
    good and only the submissions that have a good grade are downloaded.
    "\--filter=none" downloads all submissions.

## submit_image.py

The program submits images to mechanical turk annotation server.

Usage: rosrun cv_mech_turk2 \--session=SESSION \--server=SERVER
\[\--web_jpeg_quality=NN\] \[\--web_resolution=WIDTHxHEIGHT\] filenames1
\[(filename2)\*\]

-   session - session ID to submit images to (required).
-   server - server URI (e.g. <http://vm6.willowgarage.com/> or server
    alias e.g. "default" or "test")
-   web_jpeg_quality - 0-100 - what jpeg quality should be used for
    imgae display on the server. The server will keep and store the
    original, but the actual tasks would use the reduced quality images.
-   web_resolution - WIDTHxHEIGHT - what resolution should the images
    use for annotation purposes. E.g. \--web_resolution=640x480 or
    \--web_resulution=1024x768 . If the web_resolution is not provided,
    the actual image resolution is used.
-   filenameNNN - non-keyword arguments are treated as image names. All
    are submitted for annotation, 1 image per task. At least 1 image
    must be specified.

## convert_outlines_to_masks.py

Converts polygons to segmentation masks. Reads anntoations from
dir_to_annotations/annotations and images from
dir_to_annotations/images. Outputs dir_to_annotations/masks

Usage: rosrun cv_mech_turk2 convert_outlines_to_masks.py
\--annotations_dir=dir_to_annotations

-   \--annotations_dir - dir_to_annotations. Path where
    session_results.py saved session results.

e.g: ```
rosrun cv_mech_turk2 session_results.py --server=vm6 \
  --session=whiteboard-debug-4s --filter=none

rosrun cv_mech_turk2 convert_outlines_to_masks.py \
  --annotations_dir=./results/whiteboard-debug-4s/
```
