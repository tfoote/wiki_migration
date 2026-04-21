## Overview

`anj_featurenav` implements a feature-based learning and navigating
jockey based on free OpenCV feature descriptor and matcher. The package
defines the feature extractor and the descriptor matcher functions
required by the `featurenav_base` package to obtain a working couple
learning/navigating jockeys.

## Usage

### ROS API

The words feature and descriptor are used as synonymous.

```clearsilver
param {
  group.0 {
    name = General

    0.name = ~<name>/feature_detector/type
    0.type = String
    0.default = "FAST"
    0.desc = algorithm for feature detection. Can be one of "FAST", "STAR", "ORB", "MSER", "GFTT" (!GoodFeaturesToTrack), "Dense", "!SimpleBlob". They make use of their corresponding algorithm in the OpenCV library (for example "FAST" implies the use of "cv::!FastFeatureDetector")

    1.name = ~<name>/descriptor_extractor/type
    1.type = String
    1.default = "BRIEF"
    1.desc = algorithm for feature extraction. Can be one of "ORB", "BRIEF". They make use of their corresponding algorithm in the OpenCV library (for example, "SIFT" implies the use of "cv::!BriefDescriptorExtractor")

    2.name = ~<name>/descriptor_matcher/type
    2.type = String
    2.default = "!FlannBased"
    2.desc = algorithm for feature matching. Can be one of "!BruteForce", "!FlannBased". They make use of their corresponding algorithm in the OpenCV library (for example, "!FlannBased" implies the use of "cv::!FlannBasedMatcher")
  }

  group.1 {
    name = For the FAST algorithm
  
    0.name = ~<name>/feature_detector/threshold
    0.type = Int
    0.default = 1
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/feature_detection_and_description.html#fast
 
    1.name = ~<name>/feature_detector/nonmax_suppression
    1.type = Bool
    1.default = true
    1.desc = cf. OpenCV documentation
  }

  group.2 {
    name = For the STAR algorithm
  
    0.name = ~<name>/feature_detector/max_size
    0.type = Int
    0.default = 16
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_feature_detectors.html?highlight=star#starfeaturedetector
 
    1.name = ~<name>/feature_detector/response_threshold
    1.type = Int
    1.default = 30
    1.desc = cf. OpenCV documentation
  
    2.name = ~<name>/feature_detector/line_threshold_projected
    2.type = Int
    2.default = 10
    2.desc = cf. OpenCV documentation
  
    3.name = ~<name>/feature_detector/line_threshold_binarized
    3.type = Int
    3.default = 8
    3.desc = cf. OpenCV documentation

    4.name = ~<name>/feature_detector/suppress_nonmax_size
    4.type = Int
    4.default = 5
    4.desc = cf. OpenCV documentation
  }

  group.3 {
    name = For the ORB algorithm, as feature detector
  
    0.name = ~<name>/feature_detector/scale_factor
    0.type = Float
    0.default = 1.2
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/feature_detection_and_description.html#orb
  
    1.name = ~<name>/feature_detector/n_features
    1.type = Int
    1.default = 500
    1.desc = cf. OpenCV documentation
  
    2.name = ~<name>/feature_detector/n_levels
    2.type = Int
    2.default = 8
    2.desc = cf. OpenCV documentation
  
    3.name = ~<name>/feature_detector/edge_threshold
    3.type = Int
    3.default = 31
    3.desc = cf. OpenCV documentation
  
    4.name = ~<name>/feature_detector/first_level
    4.type = Int
    4.default = 0
    4.desc = cf. OpenCV documentation
  
    5.name = ~<name>/feature_detector/wta_k
    5.type = Int
    5.default = 2
    5.desc = cf. OpenCV documentation
  
    6.name = ~<name>/feature_detector/score_type
    6.type = Int
    6.default = 0 (i.e. Harris score)
    6.desc = 0 for Harris score, 1 for FAST score, cf. OpenCV documentation
  
    7.name = ~<name>/feature_detector/patch_size
    7.type = Int
    7.default = 31
    7.desc = cf. OpenCV documentation
  }

  group.4 {
    name = For the MSER algorithm
  
    0.name = ~<name>/feature_detector/delta
    0.type = Int
    0.default = 5
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/feature_detection_and_description.html#mser
  
    1.name = ~<name>/feature_detector/min_area
    1.type = Int
    1.default = 60
    1.desc = cf. OpenCV documentation

    2.name = ~<name>/feature_detector/max_area
    2.type = Int
    2.default = 14400
    2.desc = cf. OpenCV documentation
  
    3.name = ~<name>/feature_detector/max_variation
    3.type = Float
    3.default = 0.25
    3.desc = cf. OpenCV documentation
  
    4.name = ~<name>/feature_detector/min_diversity
    4.type = Float
    4.default = 0.2
    4.desc = cf. OpenCV documentation
  
    5.name = ~<name>/feature_detector/max_evolution
    5.type = Int
    5.default = 200
    5.desc = cf. OpenCV documentation
  
    6.name = ~<name>/feature_detector/area_threshold
    6.type = Float
    6.default = 1.01
    6.desc = cf. OpenCV documentation
  
    7.name = ~<name>/feature_detector/min_margin
    7.type = Float
    7.default = 0.003
    7.desc = cf. OpenCV documentation
  
    8.name = ~<name>/feature_detector/edge_blur_size
    8.type = Int
    8.default = 5
    8.desc = cf. OpenCV documentation
  }

  group.5 {
    name = For the GFTT algorithm
  
    0.name = ~<name>/feature_detector/max_corners
    0.type = Int
    0.default = 1000
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_feature_detectors.html?highlight=gftt#goodfeaturestotrackdetector
  
    1.name = ~<name>/feature_detector/block_size
    1.type = Int
    1.default = 3
    1.desc = cf. OpenCV documentation

    2.name = ~<name>/feature_detector/quality_level
    2.type = Float
    2.default = 0.01
    2.desc = cf. OpenCV documentation
  
    3.name = ~<name>/feature_detector/min_distance
    3.type = Float
    3.default = 1
    3.desc = cf. OpenCV documentation
  
    4.name = ~<name>/feature_detector/k
    4.type = Float
    4.default = 0.04
    4.desc = cf. OpenCV documentation
  
    5.name = ~<name>/feature_detector/use_harris_detector
    5.type = Bool
    5.default = false
    5.desc = cf. OpenCV documentation
  }

  group.6 {
    name = For the Dense algorithm
  
    0.name = ~<name>/feature_detector/feature_scale_levels
    0.type = Int
    0.default = 1
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_feature_detectors.html?highlight=gftt#densefeaturedetector
  
    1.name = ~<name>/feature_detector/init_xy_step
    1.type = Int
    1.default = 6
    1.desc = cf. OpenCV documentation
  
    2.name = ~<name>/feature_detector/init_img_bound
    2.type = Int
    2.default = 0
    2.desc = cf. OpenCV documentation
  
    3.name = ~<name>/feature_detector/init_feature_scale
    3.type = Float
    3.default = 1
    3.desc = cf. OpenCV documentation
  
    4.name = ~<name>/feature_detector/feature_scale_mul
    4.type = Float
    4.default = 0.1
    4.desc = cf. OpenCV documentation
  
    5.name = ~<name>/feature_detector/vary_xy_step_with_scale
    5.type = Bool
    5.default = true
    5.desc = cf. OpenCV documentation
  
    6.name = ~<name>/feature_detector/vary_img_bound_with_scale
    6.type = Bool
    6.default = false
    6.desc = cf. OpenCV documentation
  }

  group.7 {
    name = For the ORB algorithm, as descriptor extractor
  
    0.name = ~<name>/descriptor_extractor/scale_factor
    0.type = Float
    0.default = 1.2
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/feature_detection_and_description.html#orb
  
    1.name = ~<name>/descriptor_extractor/n_features
    1.type = Int
    1.default = 500
    1.desc = cf. OpenCV documentation
  
    2.name = ~<name>/descriptor_extractor/n_levels
    2.type = Int
    2.default = 8
    2.desc = cf. OpenCV documentation
  
    3.name = ~<name>/descriptor_extractor/edge_threshold
    3.type = Int
    3.default = 31
    3.desc = cf. OpenCV documentation
  
    4.name = ~<name>/descriptor_extractor/first_level
    4.type = Int
    4.default = 0
    4.desc = cf. OpenCV documentation
  
    5.name = ~<name>/descriptor_extractor/wta_k
    5.type = Int
    5.default = 2
    5.desc = cf. OpenCV documentation
  
    6.name = ~<name>/descriptor_extractor/score_type
    6.type = Int
    6.default = 0 (i.e. Harris score)
    6.desc = 0 for Harris score, 1 for FAST score, cf. OpenCV documentation
  
    7.name = ~<name>/descriptor_extractor/patch_size
    7.type = Int
    7.default = 31
    7.desc = cf. OpenCV documentation
  }
  
  group.8 {
    name = For the BRIEF algorithm
  
    0.name = ~<name>/descriptor_extractor/bytes
    0.type = Int
    0.default = 32
    0.desc = cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_descriptor_extractors.html?highlight=brief#briefdescriptorextractor
  }
  
  group.10 {
    name = For the BruteForce algorithm
  
    0.name = ~<name>/descriptor_matcher/norm
    0.type = String
    0.default = "L2"
    0.desc = one of "L1", "L2", "HAMMING", "HAMMING2", cf. OpenCV documentation http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_descriptor_matchers.html#bfmatcher
  
    1.name = ~<name>/descriptor_matcher/cross_check
    1.type = Bool
    1.default = false
    1.desc = cf. OpenCV documentation
  }
}
```

The !SimpleBlog algorithm takes no parameter, cf.
<http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_feature_detectors.html?highlight=simpleblob#simpleblobdetector>.

The !FlannBased algorithm takes no parameter, cf.
<http://docs.opencv.org/modules/features2d/doc/common_interfaces_of_descriptor_matchers.html?highlight=flannbasedmatcher#bfmatcher>.
