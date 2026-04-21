## Overview

This package provides the [portrait_bot](portrait_bot) stack project
with a GUI and the functionality to recognize and extract faces.

## How does it work?

The [face_detector](face_detector) package is used to detect faces in
the wide_stereo camera's stream images. Then the tilting laser scanner
is adjusted to scan the area around the face and a portrait is extracted
from the prosilica camera's high-definition stream. Then a mask image
is generated from the laser's point cloud. At last, both the portrait
image and the mask image are sent to the face_contour_detector.

The GUI enables the user to take a portrait image of a face, let the
PR-2 robot take a pen and then paint an outlined version of the portrait
onto a canvas. It mainly provides information about the project's
stages and allows for easy interaction.

## Tutorial

For information on how to use the portrait_bot project, read the
"Tutorial" section of the [portrait_bot](portrait_bot) page.
