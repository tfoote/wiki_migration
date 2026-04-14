## At A Glace

\<\<MsgLink(people_msgs/PositionMeasurement)\>\> - Generic message for
detecting the location of a person. Includes a 3-D point estimate,
reliability estimate and covariance matrix.

\<\<MsgLink(people_msgs/PositionMeasurementArray)\>\> - An array of
!PositionMeasurements as well as a co-occurence array.

\<\<MsgLink(people_msgs/Person)\>\> - A position estimate with an added
velocity vector, as well as the ability to add tags to the person. Has
no header, should only be used in conjunction with !PersonStamped or
People.

\<\<MsgLink(people_msgs/PersonStamped)\>\> - A header + a person

\<\<MsgLink(people_msgs/People)\>\> - A header + an array of persons
