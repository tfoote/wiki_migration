## Package Overview

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     In this package we generate the motion of the two arms form the PR2. For this we need the two points from the estimate_grasp_positions which we get as a pointcloud.\                                                               
     With these two points we generate a pregraspposition by manipulating the y-coordinates. We also estimate the orientation of the gripper and set a start pose.\                                                                      
     Including the [simple_robot_control](http://www.ros.org/wiki/simple_robot_control) we generate the arm trajectorys and are able to grasp, or manipulate the chair.                                                                  

     So, how did we decide if a manipulation is necessary?\                                                                                                                                                                              
     If the PR2 can't reach both grasppositions we have to manipulate the orientation of the chair. To do so we assume that one of the grasppositions is reachable. We grasp this position and pull the arm slightly to the outside.\   
     Because the chair has a swivel he turns a little bit and we try a correct grasping again.                                                                                                                                           
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Tutorial

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------- --
     For information on how to use grasp_motion, read the "How does it work" section of the [chair_grasping](http://www.ros.org/wiki/chair_grasping) page.   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------- --
