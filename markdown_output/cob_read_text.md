## Detailed Documentation

### Overview

Cob_read_text detects and recognizes text in natural images. The system
was trained for indoors household environment with Care-O-bot's stereo
vision colour cameras. Text localisation and OCR occur separately and
can be evaluated using precision, recall. For locating text on images
Stroke Width Transformation is used. Text whose baseline was found is
transformed back into horizontal text using Bézier curves and given to
OCR software to recognize text.

To use read text clone the repository to your disc and build it.

### Usage

#### Single Image

To read text on a single image:
`roslaunch cob_read_text read_text.launch image:=path_to_image`

read_text.launch -> run_detection -> text_detect

#### Image Stream

To read text from a camera stream:
`roslaunch cob_read_text read_text_from_camera.launch`

read_text_from_camera.launch -> text_detect

Remap "image_color" to topic that publishes to be processed images.

#### Evaluation Database

To read text on images of database with ground truth data:
`roslaunch cob_read_text read_text_with_eval.launch xmlfile:=path_to_xmlfile`

read_text_with_eval.launch -> run_detection -> text_detect

### Parameters for read_text

Parameters are specified in launch/params.yaml.



```clearsilver
param {
    0.name = smoothImage
    0.type = bool
    0.desc = smoothing of whole input image before processing
    0.default = false

    1.name = maxStrokeWidthParameter
    1.type = int
    1.desc = maximal number pixels of recognized strokes, good for big text: <50, small test: >50
    1.default = 50

    2.name = useColorEdge
    2.type = bool
    2.desc = use rgb channels to compute edgeMap
    2.default = false

    3.name = cannyThreshold1
    3.type = int
    3.desc = upper threshold for canny algorithm
    3.default = 120

    4.name = cannyThreshold2
    4.type = int
    4.desc = lower threshold for canny algorithm
    4.default = 50

    5.name = compareGradientParameter
    5.type = double
    5.desc = parameter when comparing gradients of opposing edges, in paper: 3.14 / 6
    5.default = 1.57 

    6.name = swCompareParameter
    6.type = double
    6.desc = parameter when comparing stroke widths between pixels
    6.default = 3.0

    7.name = colorCompareParameter
    7.type = int
    7.desc = parameter when comparing color between pixels, set to 255 to deactivate
    7.default = 100

    8.name = maxLetterHeight_
    8.type = int
    8.desc = maximum height of component in pixels
    8.default = 100

    9.name = varianceParameter
    9.type = double
    9.desc = maximum variance of stroke width inside component
    9.default = 1.5

    10.name = diagonalParameter
    10.type = int
    10.desc = diagonal of component has to be smaller than diagonalParameter*medianStrokeWidth
    10.default = 10

    11.name = pixelCountParameter
    11.type = int 
    11.desc = number of pixels inside component belonging to letter has to be bigger than maxStrokeWidth * pixelCountParameter
    11.default = 5

    12.name = innerLetterCandidatesParameter
    12.type = int
    12.desc = maximum number of foreign components inside component
    12.default = 5

    13.name = heightParameter
    13.type = double
    13.desc = [turned off], width has to be smaller than heightParameter * height
    13.default = 2.5

    14.name = clrComponentParameter
    14.type = int
    14.desc = maximum color value difference 
    14.default = 20

    15.name = distanceRatioParameter
    15.type = double
    15.desc = maximum pythagorean distance between 2components
    15.default = 2.0

    16.name = medianSwParameter
    16.type = double
    16.desc = maximum quotient of median sw of 2 components
    16.default = 2.5

    17.name = diagonalRatioParameter
    17.type = double
    17.desc = maximum diagonal ratio between 2 components
    17.default = 2.0

    18.name = grayClrParameter
    18.type = double
    18.desc = maximum gray color value difference between components
    18.default = 10.0

    19.name = clrSingleParameter
    19.type = double
    19.desc = maximum single colour value difference between components
    19.default = 20.0

    20.name = areaParameter
    20.type = double
    20.desc = maximum area ratio between components
    20.default = 1.5

    21.name = pixelParameter
    21.type = double
    21.desc = [turned off] maximum pixel number ratio (pixels belonging to letter) 
    21.default = 0.3

    22.name = p
    22.type = double
    22.desc = probability p
    22.default = 0.99 

    23.name = maxE
    23.type = double
    23.desc = maximum percentage of outliers in dataset
    23.default = 0.7

    24.name = minE
    24.type = double
    24.desc = minimum percentage of outliers in dataset
    24.default = 0.4

    25.name = bendParameter
    25.type = int
    25.desc = maximum angle of bezier curve
    25.default = 30

    26.name = distaneParameter
    26.type = double
    26.desc = parameter, with which maximum distance between curve and point is calculated
    26.default = 0.8

    27.name = sigma_sharp
    27.type = double
    27.desc = how strong is blur when sharpening with unsharp mask
    27.default = 1.0

    28.name = threshold_sharp
    28.type = double
    28.desc = sets minimum brightness change that will be sharpened
    28.default = 3.0

    29.name = amount_sharp
    29.type = double
    29.desc = magnitude, how much contrast is added at the edges when sharpening
    29.default = 1.5

    30.name = result_
    30.type = int
    30.desc = which spell check method is used
    30.default = 2

    31.name = showEdge
    31.type = bool
    31.desc = show gray colored edgemap image
    31.default = false

    32.name = showSWT
    32.type = bool
    32.desc = show swt map
    32.default = false

    33.name = showLetterCandidates
    33.type = bool
    33.desc = show connected components
    33.default = false

    34.name = showLetters
    34.type = bool
    34.desc = show connected components recognized as letter
    34.default = false

    35.name = showPairs
    35.type = bool
    35.desc = show pairs (2 letters belonging together)
    35.default = false

    36.name = showChains
    36.type = bool
    36.desc = show all text segments after pairs were merged together
    36.default = false

    37.name = showBreakLines
    37.type = bool
    37.desc = show how text blocks are broken into several lines
    37.default = false

    38.name = showBezier
    38.type = bool
    38.desc = show all bezier models that are created within ransac
    38.default = false

    39.name = showRansac
    39.type = bool
    39.desc = show ransac result -> show best bezier model only
    39.default = false

    40.name = showNeighborMerging
    40.type = bool
    40.desc = show how neighbor texts are merged if they fit together and were accidentally separated before
    40.default = false

    41.name = showResult
    41.type = bool
    41.desc = show results after ocr
    41.default = false

    42.name = transformImages
    42.type = bool
    42.desc = use bezier-transformed images (true) or normal rectangles around bezier lines
    42.default = true
  }
```



## Additional Applications

### read_evaluation

To evaluate cob_read_text the application read_evaluation is used.
Usage: read_evaluation takes a .xml-file containing a list of images
with ground-truth bounding boxes enclosing every text that can be found.

Example input file: 

```
<?xml version="1.0" encoding="UTF-8"?>
<tagset>
 <image>
 <imageName>example_image2.png</imageName>
  <taggedRectangles>
   <taggedRectangle center_x="605.894" center_y="636.016" width="94" height="40" angle="-20" text="Sprite" />
   <taggedRectangle center_x="752.5" center_y="626.5" width="47" height="25" angle="0" text="Red" />
  </taggedRectangles>
 </image>
</tagset>
```



All rectangles are described via:

-   their center point
-   their width and height
-   their rotation angle (clockwise)
-   and the text written inside of them.

For every image referenced between <image> and </image> in the .xml
file, read_evaluation calls cob_read_text and compares the results with
the solution.

The evaluation is based on the ICDAR 2005 Robust Reading Competitions
system using recall and precision as measure: "Precision p is defined
as the number of correct estimates divided by the total number of
estimates. Recall r is defined as the number of correct estimates
divided by the total number of targets. We define the match m,,p,,
between two rectangles as the area of intersection divided by the area
of the minimum bounding box containing both rectangles. For each
rectangle in the set of estimates we find the closest match in the set
of targets, and vice versa. Hence, the best match m(r, R) for a
rectangle r in a set of Rectangles R is defined as: m(r, R) = max m,,p,,
(r, r') \| r' ∈ R Then, our new more forgiving definitions of
precision and recall, where T and E are the sets of ground-truth and
estimated rectangles respectively:

p = ( Σ,,r_e ∈ E,,m(r_e, T) ) / \|E\|

r = ( Σ,,r_t ∈ T,,m(r_t, E) ) / \|T\|

(S. M. Lucas. ICDAR 2005 text locating competition results. In Proc. 8th
Int'l Conf. Document Analysis and Recognition, volume 1, pages 80--84,
2005)

Results are saved in folder 'results' inside the image containing
folder.

Running the application:

`roslaunch cob_read_text read_text_with_eval.launch xmlfile:=path_to_xmlfile`

The .xml-file has to be specified in read_text_with_eval.launch.

### LabelBox

LabelBox can be used to generate a .xml-file for read_evaluation. Taking
an image or a folder with images inside, LabelBox produces a .xml-file
as seen above.

Running the application:

`$(rospack find cob_read_text)/bin/labelBox path_to_image`

`$(rospack find cob_read_text)/bin/labelBox path_to_folder/`

\- labelBox Help

-   Draw box with mouse.
-   Press direction keys to move/resize drawn box before entering text.
-   Press \[d\] for rotating clockwise.
-   Press \[a\] for rotating anticlockwise.
-   Press \[s\] for switching between moving and resizing with direction
    keys.
-   Press \[c\] for color change.
-   Press Return for entering text in drawn and resized box.
-   Press left mouse button on box to show text.
-   Press right mouse button to delete a box (after text was written
    inside).
-   Press \[z\] to show data of all drawn rects.
-   Press \[r\] to reset complete image.
-   Press \[ESC\] to quit/move on to next image. -\~

Allowed file types: 'png', 'PNG', 'jpg', 'JPG', 'jpeg',
'JPEG', 'bmp', 'BMP', 'tiff', 'TIFF', 'tif' or 'TIF'.

![example_image1\|width=300](attachment:tutorial3.png)

bases on literate_pr2 package from Menglong Zhu:
menglong(at)seas.upenn.edu
