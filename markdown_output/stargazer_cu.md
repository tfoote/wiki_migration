------------------------------------------------------------------------

## API Documentation



```clearsilver
node.0 {
 name = stargazer_cu
 desc << EOM 
`stargazer_cu` is responsible for interfacing with the Stargazer indoor positioning sensor, and then publishing global position information to the rest of the system. Stargazer outputs its position and orientation (or pose) with respect to an observed psudolite in world coordinates (`/world_cu`). Psudolite locations are stored in an XML file. 
EOM
pub {
  0.name= /cu/stargazer_pose_cu
  0.type= geometry_msgs/Pose2D
  0.desc= Pose from (indoor) global positioning system in world coordinates (`/world_cu`).
 }
}
```


