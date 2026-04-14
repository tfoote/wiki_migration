Automagically convert .rviz config files to Robot Web Tools
configurations.

The syntax is rosrun rwt_config_generator convert_rviz.py display.rviz
output.html

[Youtube](https://www.youtube.com/watch?v=U8bBus27kSg)

Above, you can see a showcase of all the different rviz components that
can be converted to RWT components. The following components are
supported by the conversion script (and therefore RWT). (Not all RWT
components are in the conversion script)

  -- -------------------- -- --------- --
     Axes                    Yes       
     Camera                  No        
     DepthCloud              No        
     Effort                  No        
     FluidPressure           No        
     Grid                    Yes       
     GridCells               No        
     Group                   No        
     Illuminance             No        
     Image                   No        
     Interactivemarkers      Yes       
     LaserScan               Yes       
     Map                     Not yet   
     Marker                  Yes       
     MarkerArray             Yes       
     Odometry                Yes       
     Path                    Yes       
     PointCloud              No        
     PointCloud2             Yes       
     PointStamped            Yes       
     Polygon                 Yes       
     Pose                    Yes       
     PoseArray               Yes       
     Range                   No        
     RelativeHumidity        No        
     RobotModel              Yes       
     TF                      No        
     Temperature             No        
     WrenchStamped           No        
  -- -------------------- -- --------- --
