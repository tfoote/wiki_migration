## Package Overview

  -- ------------------------------------------------------------------------------------------------------------------------------------------- --
     In this package we estimate the grasp position for the robot.\                                                                              
     Therefore we assume that there is a PointCloud which describe the recognized object.\                                                       
     We filter these PointCloud with a PassThrough filter.\                                                                                      
     Here you get more informations about the [PassThrough](http://pointclouds.org/documentation/tutorials/passthrough.php#passthrough)filter\   
     Then extract the leftest and rightest point from the filtered_cloud as grasp_points for the PR2.\                                           
     Publish these two points and for visualization on rviz the whole filtered_cloud.                                                            

  -- ------------------------------------------------------------------------------------------------------------------------------------------- --

## Tutorial

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     For information on how to use estimate_grasp_positions, read the \"How does it work\" section of the [chair_grasping](http://www.ros.org/wiki/chair_grasping) page.   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
