# Type of messages

## Object

The **Object** message is used to define the location and the quality of
a detection. The msg also hold a shape field to define the real
appearance of the object useful for debugging and visualization.

## ObjectStamped

Same a **Object** with header information

## ObjectWithCovariance

Same a **Object** but with information about the pose uncertainty as
covariance

## ObjectWithCovarianceStamped

Same a **ObjectWithCovariance** with header information

## ObjectDetection

The **ObjectDetection** message represents the result of a detector with
the detector settings such as field of view, or noise model.

## ObjectWithCovarianceArray

The **ObjectWithCovarianceArray** message represents a map of objects
and a result of filter (SLAM). It can also be used to publish a Feature
map for a feature based self-localization.
