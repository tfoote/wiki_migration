## SRS OBJECT DATABASE

The package srs_object_database allow storing information about an
object in a database postgresql. It provides also service to insert,
update and retrieve this information.

### Installing and Configuring Database

Data about objects, such as: mesh,grasp,surface points, images, is
stored in file inside a file repository while the database keep track,
for each object, of the data files associated with it.

#### Postgresql Database

The first step is to install postgresql database. General information on
how to install and configure the database are described in
[ Installing a PostgreSQL Server ](http://www.ros.org/wiki/sql_database/Tutorials/Installing%20a%20PostgreSQL%20Server ).

##### Database Creation

After the previous step is completed an empty database must be created
using a script found inside the folder \'\'db_scripts\'\' of the package
\'\'srs_object_database\'\'. The first time you need to create an empty
database with the internal structure and data. To do this simply enter
the \'\'db_scripts\'\' folder and run: ```
. createDatabase.sh databaseName
```

NOTE: database name must not include capital letters.

This will create an empty database named \'\'databaseName\'\'. You can
usethis script also to create additional database in case you want to do
some test. Also if you want to create an empty database you can use the
following script:

```
. createemptyDb.sh databaseName
```

In general if you have already a user which is different from \'willow\'
and database should be assigned to this user, you can specify an
additional parameter which is the name of the sql user to be used to
create database. This second command can be used in all previous scripts
and the one used to restore and delete database. For example to create a
database with owner the user \'srs_user\', which must be already created
before executing the script.

```
. createemptyDb.sh databaseName srs_user
```

##### Database Restore

Database can be restored to original data using the following script:

```
. resetDatabase.sh databaseName
```

PS: warning this command will drop the previous database so your data
will be lost!

##### Database Delete

Database can be deleted completely in some case:

```
. deleteDatabase.sh databaseName
```

PS: warning this command will drop the previous database so your data
will be lost!

#### File repository

After the database creation is required to create the fileRepository
which can be retrieved in the git repository
\'\'[ git file share repository](https://github.com/ipa320/srs_data )\'\'.
This share contains a root folder named \'\'ros_data_files\'\' Upload
the laters version of the repository that will be syncronized with the
latest data created by the script in the folder \'\'db_scripts\'\'.

#### Configuration of SRS object services

Environment configuration is passed to services through the launch file
which run \'\'srs_object_database\'\' services. The file called
\'\'srs_db.launch\'\' is stored in the folder \'\'launch\'\' of the
\'\'srs_object_database\'\'.

```
<launch>

   <param name="instanceName" value="localhost" type="str"/>
   <param name="dbPort" value="5432" type="str"/>
   <param name="databaseName" value="srs_template_database" type="str" />
   <param name="userName" value="user" type="str" />
   <param name="pwd" value="pwd" type="str" />
   <param name="repoPath" value="/path_to_ros_fileshare/ros_data_files/" type="str"/>

   <node pkg="srs_object_database" name="get_model_server" type="get_model_server" output="screen"/>
   <node pkg="srs_object_database" name="get_model_mesh" type="get_model_mesh" output="screen"/>
   <node pkg="srs_object_database" name="get_model_surf" type="get_model_surf" output="screen"/>
   <node pkg="srs_object_database" name="get_model_urdf" type="get_model_urdf" output="screen"/>
   <node pkg="srs_object_database" name="get_model_pcl" type="get_model_pcl" output="screen"/>
   <node pkg="srs_object_database" name="get_model_grasp" type="get_model_grasp" output="screen"/>
   <node pkg="srs_object_database" name="get_model_img" type="get_model_img" output="screen"/>
   <node pkg="srs_object_database" name="insert_object_service" type="insert_object_service" output="screen"/>
   <node pkg="srs_object_database" name="dispacherService" type="dispacherService" output="screen" />


</launch>
```

The configuration is controlled by the param element inside the launch
file.

Localhost set the ip addres of the postgreSQL server. For local
installation use \'localhost\'. ```
<param name="instanceName" value="localhost" type="str"/>
```

dbPort set the port on which the database server is listening. Default
for postgres is \'\'5432\'\' ```
<param name="dbPort" value="5432" type="str"/>
```

databaseName must be set to the name of database created before.
```
<param name="databaseName" value="srs_template_database" type="str" />
```

username must be set to the user which own read and write right on the
\'\'srs_database\'\'. ```
<param name="userName" value="user" type="str" />
```

pwd must provide the password for the user specified at the previous
point. ```
. createemptyDb.sh databaseName
```0

repoPath is used to set the root folder where the file repository is
stored. Note that at the end \'\'/\'\' is added otherwise services will
fail to return object data. ```
. createemptyDb.sh databaseName
```1

Once this parameters are correctly configured the services provided by
\'\'srs_object_database\'\' are ready to be run.

```
. createemptyDb.sh databaseName
```2

## Usage/Examples

In order to run all ros services for both insert and retrieval execut
the launch file. ```
. createemptyDb.sh databaseName
```3

### clientTest

A simple client has been created to allow inserting and updating
information on database. This service make use of service provided by
\'\'srs_object_database\'\' and should be used only for the purpose of
testing data. It is executed with \'\'rosrun\'\'. Is mandatory to
execute the \'\'srs_object_database\'\' launch file to start all
services before running the client.

```
. createemptyDb.sh databaseName
```4

After running the client it will be possible to specify an action to
take:

```
. createemptyDb.sh databaseName
```5

The selection of the action should be consequence of the input
parameters.

#### how to search data with clientTest

clientTest can be used to retrieve data. To achieve this provide
parameters as specified in this section and use \'\'r\'\' to specify
that you want to retrieve data. The client calls the
\'\'srs_object_database/GetObjecId\'\' service and by command line is
possible to search in database for object id using the following
combination of input:

Search all objects:

Providing all as parameter allows retrieve all object currently stored
in the sql database. ```
. createemptyDb.sh databaseName
```6

Search by object id:

It is possible to specify id as key search and provide a numeric object
id to verify if an object with a give id is present in database and in
case retrieve its infomation.

```
. createemptyDb.sh databaseName
```7

Search by object category: It is possible to search all object which
have a specified class. Use class as first parameter and provide an
object_class such as glass. ```
. createemptyDb.sh databaseName
```8

Search by object name: It is possible to search a specific object using
its name. Use nameas first parameter and provide an object_name such as
\"milkBox1\". ```
. createemptyDb.sh databaseName
```9

##### how to force retrieve of data with clientTest without user interaction

Adding the key \'retrieve\' after the previous command will allow the
client to direclty retrieve object data, the general data, without
requiring additional user interaction.

```
. createemptyDb.sh databaseName srs_user
```0

#### how to retrieve data with clientTest

after an object as been retrieved the clienTest allow to return the data
using the command line:

```
. createemptyDb.sh databaseName srs_user
```1

Selecting 3, for example, will allow to retrieve, if available, image of
the current object retrieved by the search.

#### how to insert data with clientTest

Inserting new object is usefull to test functionality of other
components which make use of database. clientTest provide such
functionality in order to allow developer to test object information and
services. A file with a list of property for a give object is provided
and then the client retrieve the files with its data and load them in an
appropriate way to be sent to InsertObject service.

The input file must be stored inside the Input folder available in the
git repository
\'\'[ git file share repository](https://github.com/ipa320/srs_data )\'\'
with the data files. The input file is

```
. createemptyDb.sh databaseName srs_user
```2

Each attribute will be insert in database in the respective table. For
object such as: urdf,image,grasp,mesh,pcl or surf. It mush be provided
the filename, with extenstion, of the file containing the data to be
inserted. This file must be placed in the Input folder inside the file
repository. Once the data will be inserted, a file will be created
inside the appropiate folder of the file repository. One example is
\'\'testInputInsert.txt\'\' which allow to insert a new object simply
calling the clientTest:

```
. createemptyDb.sh databaseName srs_user
```3

In the output you will be able to see which id is assigned to this new
object.

##### how to force insertion of data with clientTest without user interaction

Adding the key \'insert\' after the previous command will allow the
client to direclty insert object and its data without requiring
additional user interaction.

```
. createemptyDb.sh databaseName srs_user
```4

#### how to update data with clientTest

Updating an object with the client work in the same way as the insert,
the only difference is that when providing an input file you will change
information so that the service will repleace old information with the
new information or will insert additional information that previouvsly
where not provided. It is mandatort that in the input file the id will
not be empty, otherwise it will be interpreted as an insert, but you
will provide the id of the object to be updated.

##### how to force update of data with clientTest without user interaction

Adding the key \'update\' after the previous command will allow the
client to direclty update object and its data without requiring
additional user interaction.

```
. createemptyDb.sh databaseName srs_user
```5

### general usage of srs_object_database services

The clienTest which is used for test purpose, build request for
srs_object_database services. In run time scenario those are the
services that other components should invoke.

#### Inserting/Updating Objects

To insert and update object data the service \'\'\"InsertObject\"\'\'
should be used. Note that you should provide a type of mesh (usually
iv.txt) and an Image type such as: icon,top-view,front-view.

```
. createemptyDb.sh databaseName srs_user
```6

#### Getting Objects data

To retrieve data a dispacher service can be invoked. It has some boolean
flag which must be put to 1 to indicate the data that should be
retrieved if available for the provided objects ids.

```
. createemptyDb.sh databaseName srs_user
```7

#### Getting objects id of objects

In order to get objects ids the getObjectId service must be invoked. It
requires a type parameters which specify the search criteria as well as
an item which is the value of the key provided for the search. It can be
specified as type: all, to retrieve all objects id in database, name, to
search a specific object based on its name, class, to search ids of
object using their class.

```
. createemptyDb.sh databaseName srs_user
```8

This service will return general information for the objects retrieved,
such as name, description, size.

#### Calling a specific service

While using getData allow to retrieve more information at the same time,
if the object id is know and only a specific service need to be called
it is possible to just call the respective service. For instance if it
is required to get only image information for a give object id, the
service getImg can be directly called. In this specific case calling
directly this service allow to use additional parameter such as the type
of the image to be retrieved for the object id provided in the request
message. It works like a filter to select, for instance, only icon
image.

```
. createemptyDb.sh databaseName srs_user
```9

#### Managing object category

The database allow management of knowledge category associated to an
object. The category could be managed through services or clientTest
with the following command line:

```
. resetDatabase.sh databaseName
```0

The key \'category\' tells the client to enter a submenu where it is
possible to query database for the existing category, insert new
category, search category associated with an object.
