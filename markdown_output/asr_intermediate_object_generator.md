![\|height=\"200\",width=\"333\"](attachment:Logo-white-medium.jpg)

# Description

The intermediate object generator generates intermediate object for a
domain composed from scenes. It is used to restrain the amount of object
searched during the direct search
([asr_state_machine](http://wiki.ros.org/asr_state_machine)) phase by
selecting appropriate objects to search.

# Functionality

The intermediate objects are calculated by using 3 criteria :

1\. The position variance of the object. The more an object moves, the
less likely it is to be an intermediate object. To get this value, first
we need to get the average position, and then calculate the distance
between the average object qnd the seen object in every snapshot.

![\|height=\"200\",width=\"400\"](attachment:Download.png)

2\. The average distance between the current tested object and others
objects in the scene. The value is calculated with the average distance
in each snapshot. Then we average the value between all snaposhots.

![height=\"200\",width=\"333\"](attachment:Download (1).png)

3\. The presence of the object in the scene. This value is quite simple
to calculate : It is number of snapshot where the object is present
divided by the total number of snapshots.

The second part of the process is to normalize all values to hqve the
same scale of comparison between all 3 criteria.

![height=\"200\",width=\"333\"](attachment:Download (2).png)

Then we apply the Evaluation Function F (either by addition or by
multiplication ):

![height=\"200\",width=\"333\"](attachment:Download (3).png)

After that we can apply the following algorithm to filter the object
list and only get the intermediate object.

At every step we calculate the average F value of the list qnd once the
gain by removing an object is under a defined threshold, we stop the
process. In addition, we have to test the validity of the list at each
steps (Each scene is represented by at least one object). Please note
that the list is sorted by F value before applying the Filter.

![height=\"200\",width=\"333\"](attachment:Download (4).png)

This package needs a database of objects and their absolute positions
during the time (can be set in the
[asr_recognizer_prediction_ism](http://wiki.ros.org/asr_recognizer_prediction_ism)).
On basis of this information it will be determined which objects have a
heigher chance to be found in a 3D-object-search. There will be two
files saved.

In one a subset of the current objects will be saved, to limit the
search objects while the direct search of the
[asr_state_machine](http://wiki.ros.org/asr_state_machine).

In the second the calculated weight for each object will be saved. This
can be used in the
[asr_next_best_view](http://wiki.ros.org/asr_next_best_view) to prefer
some objects about the others.

The weights will also be saved in a new table in the database.

# Usage

he asr_recognizer_prediction_ism/launch/helpers/scene_recognition.yaml
is needed to access the path to the current database.

Every scene has to have at least 3 objects or the program crashes.

## Needed software

[Boost (1.54.0.1)](http://www.boost.org/)

sqlite3

## Start system

Update the path to the database in
asr_recognizer_prediction_ism/launch/helpers/scene_recognition.yaml

roslaunch asr_intermediate_object_generator
asr_intermediate_object_generator.launch

The [asr_world_model](http://wiki.ros.org/asr_world_model) will launch
this package automatically if the generated files for the current
database were not generated yet. There is an option in asr_world_model
to activate this function.

# ROS Nodes

## Parameters

### Launch file

\'\'\'asr_intermediate_object_generator/launch/asr_intermediate_object_generator.launch\'\'\'

!\'\'\'AutomatPath\'\'\': The path were the intermediate_objects xml
file should be created. If there is an XXX in the name, the XXX will be
replaced with the current database name. So the name has not to be
changed manually after a database change.

\'\'\'NBVPath\'\'\': The path were the intermediate_object_weights xml
file should be created. The XXX works analog here, too.

### yaml file

\'\'\'asr_intermediate_object_generator/param/Domain.yaml\'\'\'

!\'\'\'RankingMethod\'\'\' : 0 or 1, 0 is additive and 1 is
multiplicative \'\'\'Alpha\'\'\' : weight for the presence in scene
criteria \'\'\'Beta\'\'\' : weight for the position variance criteria
\'\'\'Gamma\'\'\' : weight for the average distance between object
criterias! \'\'\'GainValueThreshold\'\'\' : gain threshold for the
object filtering !\'\'\'DomainName\'\'\' : name of the domain
