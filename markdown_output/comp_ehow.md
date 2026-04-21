**This package has been moved to the knowrob_addons repository on
github:**

<https://github.com/knowrob/knowrob_addons>

Related paper:

Moritz Tenorth, Daniel Nyga, and Michael Beetz, Understanding and
Executing Instructions for Everyday Manipulation Tasks from the World
Wide Web, IEEE International Conference on Robotics and Automation
(ICRA), 2010
<https://ias.in.tum.de/_media/spezial/bib/tenorth10webinstructions.pdf>

## Description:

Using the computables defined here, it is possible to query for a plan
by giving a natural-language command like 'set the table' and retrieve
a description of all required steps in form of an OWL TBOX
specification.

The temporary OWL file returned from the Java-based import system is
directly parsed and the main concept describing the plan as a whole is
returned.

## Requirements:

For proper functioning, the Cyc ontology (opencyc.org) has to be
installed and must be running:

roscd opencyc make roslaunch opencyc opencyc.launch

## Usage:

You can either start a ROS service that responds with an OWL action
description to a natural language command like 'set a table' or use
the system from within KnowRob.

For the first option, just call roslaunch comp_ehow comp_ehow.launch

For calling comp_ehow from within KnowRob, call ```
roscd comp_ehow
rosrun rosprolog rosprolog comp_ehow
rdf_triple(knowrob:forCommand, A, 'set a table').
A = 'http://www.owl-ontologies.com/Ontology1252257693.owl#SetATable'
```

The variable (here: A) will be bound to the identifier of the plan that
has been generated and already been parsed, so that you can use it for
reasoning.

## GUI

A description how to use the GUI can be found here:
<http://ias.in.tum.de/kb/wiki/index.php/Manual>

## Notes

At the moment, the howtos are read from text files in the howtos
directory
