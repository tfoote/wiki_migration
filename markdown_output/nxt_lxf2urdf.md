## Where to Start

Download [Lego Digital Designer (LDD)](http://ldd.lego.com/). Then
replace the ldraw.xml in the assets folder of Lego Digital Designer with
the ldraw.xml file provided in this package. The ldraw.xml file defines
a part mapping from the Lego pieces in LDD to the ldraw.org models.

Once you have overwritten the ldraw.xml file, create a Lego robot using
the NXT parts in LDD. Save the LDD file as an \*.lxf file and export it
as \*.ldr file. Currently nxt_dscriptions has a subset of the ldraw.org
parts library converted to Collada meshes, so not all parts will be
modelled in rviz. We are still looking for ways to make converting the
ldraw models to Collada.

## Converting the Model

Now that you have created and exported the \*.lxf and \*.ldr files, run
the conversion program nxt_lxf2urdf.py and pipe the output into a urdf
file. 

```
rosrun nxt_lxf2urdf nxt_lxf2urdf.py robot.lxf robot.ldr > robot.urdf
```



## Labelling and Positioning the Sensors and Motors

Looking at the model generated in rviz will reveal that the sensors and
motors are in odd positions with generic names. The positions and
orientations of the sensors have been shifted so that the axes are X
forward and the origins properly located in the body of the sensor.
Inside the urdf there are comments marking the individual sensors and
motors. Start by renaming the motors and sensors according to the names
in your robot.yaml file. Then change the joint origins for each sensors
so that they look like the original model in LDD.
