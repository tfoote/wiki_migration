### Overview

This package contains text detection and recognition algorithm. It is
for general use: given any image input, output detection and recognition
results.

The implementation of text detection is based on:
```
Boris Epshtein, Eyal Ofek, Yonatan Wexler, "Detecting text in natural scenes with stroke width transform," Computer Vision and Pattern Recognition (CVPR) 2010.
```

### Workflow

1\. Given an input image, detecting the text region based on the
algorithm described in the paper above.

2\. After the text region detected, cropped out region will be fed into
tesseract ocr engine.

3\. Instead of directly output ocr result, another dictionary search
step is performed. Using letter appearance correlation, the closest word
in dictionary is found as the final output.

### Tutorials

#### run test script

After compiling the code, to test the code: ```
roscd read_text
cd scripts
sh test.sh
```

Which will read in a test image, a letter correlation matrix and a
dictionary, output an image named **\*\_detection.jpg under the same
directory, showing detected region with acceptable ocr results and final
output text in the right side of the image.**

#### command line usage

The following is just the content in test.sh: ```
rosrun read_text run_detect ../images/test_image.jpg ../fonts/correlation.txt ../dictionary/full-dictionary
```

First input is any image file readable by OpenCV, either color or
gray-scale image.

The second is a correlation measurement for letter appearance, generated
from letter templates under fonts/. The correlation file is a plain text
file contains 62\*62 float numbers between (0-1\], indicating
correlation between \[a-z,A-Z,0-9\]. Script for generating your own
correlation file is coming soon.

The third input is the dictionary file, plain ASCII file with one word
each line. The default dictionary provided in the package has 74550
words with both capital initial, capital all, lower all cases(e.g.
Literate, LITERATE, literate), thus in size of 223650, 3 times larger.
You can easily generate your own dictionary with all cases using
scripts/dictionary.py. (Note: if you give smaller dictionary, the
results will be more accurate.)

#### batch run detection

A script for batching up detection for images under the same directory
(recursively) is also provided. ```
mkdir results
cd results
python scripts/filelist.py <path/to/input/folder>
``` The script
recursively checks all images for certain formats(see the script for
more detail) under input directory and run detection, outputting results
under current directory where you run the script. Note, the input images
should have different names, otherwise the results will be overwritten.

### TODO List

1\. Currently, we use linear search over dictionary when correcting OCR
results. A hash based search scheme will be implemented.

2\. Following text region detection, we will add an additional step to
rotate text into horizontal aligned, for better OCR results.

3\. Maybe rewrite implementation in stroke width transform using OpenCV
line iterator, may be faster.
