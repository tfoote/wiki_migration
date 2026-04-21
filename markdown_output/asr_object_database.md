![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package stores object models and their information which can be
used by other packages like object recognizers.

*Samples of objects stored in the database:*
![\|width="600",height="337"](attachment:objects_1.jpg)

## Functionality

There are several services this package offers to access the object
models which are stored in the *rsc* directory located at the base path
of it. Inside this directory in */rsc/databases *there are
subdirectories which group the objects together based on their usage
(mostly depending on the recognizer which is used to detect them in a
scene). Take note that groups and their objects within can only be
queried by services if they are declared in config.xml in the *rcs*
directory. This doesn't apply for example to the environment objects,
which are only used for visualization purposes by other packages; they
can be accessed by specifying the path to them directly without any
service call.

Each object is represented as a folder, the (unique) name of the folder
being the one of the object, and at least a mesh file inside of it. In
addition there can/should be more information stored inside, for example
the object's normal vectors (by default stored as a file ending with
.nv.txt) which describe the orientations from where the object is best
visible (usually created with this package's normal generator tool;
check the provided tutorial for more information) or a file containing
information about how large a recognizer's uncertainty concerning the
object is allowed to be (by default stored as a file ending with
.dev.txt). If those files don't exist but are needed when a service
regarding those is called, they are created with default values and
should be adjusted accordingly.

## Usage

### Needed packages

-   [asr_ros_uri](asr_ros_uri)
-   [asr_xsd2cpp](asr_xsd2cpp)
-   [assimp_devel](assimp_devel)

### Needed software

-   xsdcxx
-   libxerces

### Start system

To start this package simply run

```
rosrun asr_object_database asr_object_database
``` After this you can call a service of your
choice to query the objects stored in this package.

## ROS Nodes

### Provided Services

Several services are provided to query the database and get information
about the objects within:

-   *object_meta_data: *Returns information about a specific object
-   Parameters:
-   object_type (string): The name of the object (see
    *object_type_list*)
-   recognizer (string): The name of the recognizer used to detect the
    object in a scene (see *recognizer_list*)
-   Returns:
-   object_folder (string): The path to the directory containing the
    files of this object as a package-url (see
    [resource_retriever](resource_retriever) for more information)
-   object_mesh_resource (string): The path to this object's mesh file
    as a package-url
-   normal_vectors (geometry_msgs/Point\[\]): A list of normals
    representing the orientations the object can be detected the best
    from
-   deviations (float64\[\]): A list of deviation values describing a
    recognizer's possible uncertainty about this object
-   is_valid (bool): If this is false, then there is no object in the
    database with the given name and recognizer
-   is_rotation_invariant (bool): If this is false, then the object can
    be rotated around at least on axis by certain degrees without
    changing its geometrical view (e.g. a cylindrical object)
-   *recognizer_list: *Returns all available recognizer categories
    (which contain objects)
-   Parameters: -
-   Returns:
-   recognizer_list (string\[\]): A list of names of the available
    recognizers
-   *object_type_list: *Returns the objects of a given recognizer
    category
-   Parameters:
-   recognizer (string): The name of the recognizer to query for objects
    (see *recognizer_list*)
-   Returns:
-   object_type_list (string\[\]): A list of names of the objects the
    given recognizer category contains
-   *recognizer_list_meshes: *Returns a list of paths to the mesh files
    of all objects in a given recognizer category
-   Parameters:
-   recognizer (string): The name of the recognizer category to query
-   Returns:
-   meshes (string\[\]): A list of paths (as package-urls) to the mesh
    files of the given category
-   *generate_object_type: *Generates an entry (folder, meta information
    and Collada-mesh-file) in the database for a given textured object
    (Currently the conversion of the mesh file does not work properly
    but can be done manually with meshlab for example)
-   Parameters:
-   sourcefile (string): A file path to a mesh which has to end with
    "*_tex.obj*". There also have to be a *.mtl* and a* .png* file in
    the same directory.
-   Returns: -

## Tutorials

[Generate normals for an object](asr_object_database/normal_generation_tutorial)
