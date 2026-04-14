# Overview

\'\'\'stdr_resources\'\'\' package is the container for the resources
needed by [STDR Simulator](stdr_simulator) to operate. The resources are
divided in two main groups: \'\'\'maps\'\'\' and \'\'\'yaml/xml
files\'\'\'.

## Maps

In the maps section six indicative maps are provided. Note that each
\'\'\'map\'\'\' is actually a pair of files:

-   A png file that holds the plane overview of the environment
-   A yaml file that holds the map meta-information (resolution, origin
    etc).

## Yaml/XML files

In this section the files under the \'\'\'stdr_resources/resources\'\'\'
folder are described. These are Yaml or XML files that describe robots
and sensors. The available folders, each holding some sample resource
files, are:

-   \'\'\'robots\'\'\': Contains samples of robots.
-   \'\'\'laser_sensors\'\'\': Various LRF sensors
-   \'\'\'range_sensors\'\'\': Various Sonar and IR sensors
-   \'\'\'footprint\'\'\': Different robot footprints (only circlular
    footprint available at v0.1)

For more information about the use of resource files please visit
[stdr_parser](stdr_parser) or the following tutorial :
[Create robots and sensors using files](stdr_simulator/Tutorials/Create resources using files)
