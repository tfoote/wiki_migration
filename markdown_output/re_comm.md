## What does re_comm do?

The [re_comm](re_comm) package provides ROS services to submit, update,
request, delete and search for database entries and to forward semantic
queries to !RoboEarth's [Sesame](http://www.openrdf.org/) repository:

-   re_comm/get_action_recipe
    ([re_comm/srv/GetActionRecipe](https://docs.ros.org/en/rolling/p/re_comm/srv/GetActionRecipe.html))
-   re_comm/get_binary_file
    ([re_comm/srv/GetBinaryFile](https://docs.ros.org/en/rolling/p/re_comm/srv/GetBinaryFile.html))
-   re_comm/get_environment
    ([re_comm/srv/GetEnvironment](https://docs.ros.org/en/rolling/p/re_comm/srv/GetEnvironment.html))
-   re_comm/get_object
    ([re_comm/srv/GetObject](https://docs.ros.org/en/rolling/p/re_comm/srv/GetObject.html))

```{=html}
<!-- -->
```
-   re_comm/set_action_recipe
    ([re_comm/srv/SetActionRecipe](https://docs.ros.org/en/rolling/p/re_comm/srv/SetActionRecipe.html))
-   re_comm/set_binary_file
    ([re_comm/srv/SetBinaryFile](https://docs.ros.org/en/rolling/p/re_comm/srv/SetBinaryFile.html))
-   re_comm/set_environment
    ([re_comm/srv/SetEnvironment](https://docs.ros.org/en/rolling/p/re_comm/srv/SetEnvironment.html))
-   re_comm/set_object
    ([re_comm/srv/SetObject](https://docs.ros.org/en/rolling/p/re_comm/srv/SetObject.html))

```{=html}
<!-- -->
```
-   re_comm/update_action_recipe
    ([re_comm/srv/UpdateActionRecipe](https://docs.ros.org/en/rolling/p/re_comm/srv/UpdateActionRecipe.html))
-   re_comm/update_binary_file
    ([re_comm/srv/UpdateBinaryFile](https://docs.ros.org/en/rolling/p/re_comm/srv/UpdateBinaryFile.html))
-   re_comm/update_environment
    ([re_comm/srv/UpdateEnvironment](https://docs.ros.org/en/rolling/p/re_comm/srv/UpdateEnvironment.html))
-   re_comm/update_objectowl
    ([re_comm/srv/UpdateObjectOWL](https://docs.ros.org/en/rolling/p/re_comm/srv/UpdateObjectOWL.html))

```{=html}
<!-- -->
```
-   re_comm/del_action_recipe
    ([re_comm/srv/DelActionRecipe](https://docs.ros.org/en/rolling/p/re_comm/srv/DelActionRecipe.html))
-   re_comm/del_binary_file
    ([re_comm/srv/DelBinaryFile](https://docs.ros.org/en/rolling/p/re_comm/srv/DelBinaryFile.html))
-   re_comm/del_environment
    ([re_comm/srv/DelEnvironment](https://docs.ros.org/en/rolling/p/re_comm/srv/DelEnvironment.html))
-   re_comm/del_object
    ([re_comm/srv/DelObject](https://docs.ros.org/en/rolling/p/re_comm/srv/DelObject.html))

```{=html}
<!-- -->
```
-   re_comm/search_action_recipes
    ([re_comm/srv/SearchActionRecipes](https://docs.ros.org/en/rolling/p/re_comm/srv/SearchActionRecipes.html))
-   re_comm/search_environments
    ([re_comm/srv/SearchEnvironments](https://docs.ros.org/en/rolling/p/re_comm/srv/SearchEnvironments.html))
-   re_comm/search_objects
    ([re_comm/srv/SearchObjects](https://docs.ros.org/en/rolling/p/re_comm/srv/SearchObjects.html))

```{=html}
<!-- -->
```
-   re_comm/query_action_recipes
    ([re_comm/srv/QueryActionRecipes](https://docs.ros.org/en/rolling/p/re_comm/srv/QueryActionRecipes.html))
-   re_comm/query_environments
    ([re_comm/srv/QueryEnvironments](https://docs.ros.org/en/rolling/p/re_comm/srv/QueryEnvironments.html))
-   re_comm/query_objects
    ([re_comm/srv/QueryObjects](https://docs.ros.org/en/rolling/p/re_comm/srv/QueryObjects.html))

If data in the !RoboEarth database is to be changed, the corresponding
ROS service expects an API key as an argument. Services that provide
only read access to the DB don't need such a key. You can request your
API key at the web interface of the !RoboEarth database:
<http://roboearth.informatik.uni-stuttgart.de/>

## Syntactic Search

It is possible to search for database entries, which share a common
prefix for their unique identifier (UID) using the
*/re_comm/search_<type>* services. As the class of an entity is built
from categories and subcategories (separated by dots) a prefix search
can be used to find all entities that are part of the same
category/subcategory. For example:



```
UID1: animal.mammal.cat.kitty
UID2: animal.mammal.dog.pluto
```



Valid prefix searches are:



```
a                  // => UID1 and UID2 found
animal.            // => UID1 and UID2 found
animal.mam         // => UID1 and UID2 found
animal.mammal.cat  // => UID1 found
animal.mammal.d    // => UID2 found
```



## Semantic Query

By using the
[SeRQL query language](http://www.openrdf.org/doc/sesame2/users/ch09.html)
and the */re_comm/query_<type>* services, you may access server-side
reasoning based on the RDF triples. Example queries:

-   Get all OWL classes:



```
SELECT C FROM
{C} rdf:type {owl:Class}
WHERE isURI(C)
```



-   query_action_recipes: Get all recipes having a label, which contains
    "serve a drink":



```
SELECT S FROM
{S} rdfs:label {L}
WHERE L LIKE "serve a drink"
```



-   query_objects: Get all !ColoredPointCloudModels, which provide a
    model for a hand:



```
SELECT S FROM
{S} rdf:type {re:ColoredPointCloudModel}; re:providesModelFor {kr:Hand}
USING NAMESPACE
re=<http://www.roboearth.org/kb/roboearth.owl#>,
kr=<http://ias.cs.tum.edu/kb/knowrob.owl#>
```



-   query_objects: Get all object models, which include a
    !ColoredPointCloudModel for a hand



```
SELECT source FROM CONTEXT source
{S} rdf:type {re:ColoredPointCloudModel}; re:providesModelFor {kr:Hand}
USING NAMESPACE
re=<http://www.roboearth.org/kb/roboearth.owl#>,
kr=<http://ias.cs.tum.edu/kb/knowrob.owl#>
```


