## Overview

\'\'\'\[0\] Changchang Wu SiftGPU: A GPU Implementation of Scale
Invariant Feature Transform (SIFT), 2007\'\'\'

For more details go to the
[SiftGPU homepage](http://www.cs.unc.edu/~ccwu/siftgpu/)

SiftGPU is an implementation of SIFT \[1\] for GPU. SiftGPU processes
pixels parallely to build Gaussian pyramids and detect DoG Keypoints.
Based on GPU list generation\[3\], SiftGPU then uses a GPU/CPU mixed
method to efficiently build compact keypoint lists. Finally keypoints
are processed parallely to get their orientations and descriptors.

SiftGPU is inspired by Andrea Vedaldi\'s sift++\[2\] and Sudipta N Sinha
et al\'s GPU-SIFT\[4\] . Many parameters of sift++ ( for example, number
of octaves, number of DOG levels, edge threshold, etc) are also
available in SiftGPU. The shader programs are dynamically generated
according to the parameters that user specified.

SiftGPU also includes a GPU exhaustive/guided sift matcher SiftMatchGPU.
It basically multiplies the descriptor matrix on GPU and finds the
closest feature matches on GPU. Both GLSL and CUDA implementations are
provided.

\'\'\'\[1\] D. G. Lowe. Distinctive image features from scale-invariant
keypoints . International Journal of Computer Vision, November
2004.\'\'\'

\'\'\'\[2\] A. Vedaldi. sift++,
<http://www.vlfeat.org/~vedaldi/code/siftpp.html>.\'\'\'

\'\'\'\[3\] G. Ziegler, et al. GPU point list generation through
histogram pyramids. In Technical Report, June 2006.\'\'\'

\'\'\'\[4\] Sudipta N Sinha, Jan-Michael Frahm, Marc Pollefeys and Yakup
Genc, \"GPU-Based Video Feature Tracking and Matching \", EDGE 2006,
workshop on Edge Computing Using New Commodity Architectures, Chapel
Hill, May 2006\'\'\'
