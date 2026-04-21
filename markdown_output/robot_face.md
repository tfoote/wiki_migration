# Guidelines for Modeling

To model a robot face for the ros-package *robot_face* you have to
follow this guidelines to get a working model in the application. This
guideline will not tell you how to model a complete face, but helps you
to get things work.

## Required Software

First of all you need Blender and an Ogre3D mesh exporter plugin.

-   [Blender 2.49b](http://www.blender.org/development/release-logs/blender-249/)
-   [Blender Exporter (OgreMeshExporter)](http://www.ogre3d.org/tikiwiki/Blender+Exporter)

It\'s true that there exist newer versions of Blender and the
meshexporter, but the new meshexporter was not showing good results.
Using the old versions is the safest way.

## Preparations

1\. Blender Exporter is installed 1. Blender 2.49b is running 1. in your
3D-view: *View* has to be set to **Front**

## Modeling

To get a working model in the *robot_face* application, please follow
this guidelines.

-   /!\\ All scaling, rotation and translation needs to be done in
    \"Edit Mode\"
-   Ogre3D perceives only coordinatetransformations of the mesh and
    *not* of the object
-   /!\\ All normals need to be flipped to be on the outer side
-   If the normals are pointing inside the mesh, nothing will be
    displayed in Ogre3D
-   The mesh has to be in the center of the coordinatesystem. Viewing
    direction along +Y-axis. Viewing direction of the robot face along
    -Y-axis. Up-vector is +Z-axis.
-   Your mesh should be scaled by 5
-   You must create the following shape keys and name them as followed:
    (optionally add more)
-   *mouth-rest*: mouth in rest position
-   *mouth-wide*: mouth widened
-   *mouth-narrow*: mouth narrowed
-   *mouth-open*: mouth opened
-   *mouth-close*: mouth closed
-   *mouth-smile*: mouth smiling
-   *mouth-sad*: mouth looking sad
-   *mouth-afraid*: mouth looking afraid
-   *mouth-disgusted*: mouth looking disgusted
-   *eyebrows-rest*: eyebrows in rest position
-   *eyebrows-up*: eyebrows higher than resting
-   *eyebrows-down*: eyebrows lower than resting
-   *eyebrows-sad*: eyebrows outer part down
-   Optionally you can add animations for eye blinking, a wiggle and
    breathing naming *blink*, *rotate* and *breathe*
-   important for exporting (see Exporting)
-   /!\\ Name your materials during creation. Naming them later may
    result in errors.
-   Eyebrows and mouth must have different materials and need to be
    different to the rest of the objects materials
-   You have to name at least the following Materials:
-   Iris
-   Head
-   Mouth
-   EyeBrows
-   Eyes

## Export

Check the following options in the meshexporter GUI:

-   Animation Settings of \"\": *Pose*
-   Material Settings: *Export Materials* (name .material file);
    *Rendering Materials*
-   *Export Meshes* (choose save path)
-   *Fix Up Axis to Y*
-   *Require Materials*
-   *Skeleton name follow mesh*
-   *Apply Modifiers*
-   *OgreXMLConverter*
-   Tab \"Preferences\"
-   Location: *Auto*
-   Export Options: *Edge Lists*; tangent; 3 component; *Reorganise
    vertex buffers*; *Optimise animations*
-   To get the breathing, wiggle and blinking animation to work, you
    need to create the following animations under *Pose*:
-   breathe
-   rotate
-   blink
-   If the export fails, try to export with admin rights
