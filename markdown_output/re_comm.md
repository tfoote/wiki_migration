## What does re_comm do?

The [re_comm](re_comm) package provides ROS services to submit, update,
request, delete and search for database entries and to forward semantic
queries to !RoboEarth\'s [Sesame](http://www.openrdf.org/) repository:

-   re_comm/get_action_recipe (\<\<SrvLink(re_comm/GetActionRecipe)\>\>)
-   re_comm/get_binary_file (\<\<SrvLink(re_comm/GetBinaryFile)\>\>)
-   re_comm/get_environment (\<\<SrvLink(re_comm/GetEnvironment)\>\>)
-   re_comm/get_object (\<\<SrvLink(re_comm/GetObject)\>\>)

```{=html}
<!-- -->
```
-   re_comm/set_action_recipe (\<\<SrvLink(re_comm/SetActionRecipe)\>\>)
-   re_comm/set_binary_file (\<\<SrvLink(re_comm/SetBinaryFile)\>\>)
-   re_comm/set_environment (\<\<SrvLink(re_comm/SetEnvironment)\>\>)
-   re_comm/set_object (\<\<SrvLink(re_comm/SetObject)\>\>)

```{=html}
<!-- -->
```
-   re_comm/update_action_recipe
    (\<\<SrvLink(re_comm/UpdateActionRecipe)\>\>)
-   re_comm/update_binary_file
    (\<\<SrvLink(re_comm/UpdateBinaryFile)\>\>)
-   re_comm/update_environment
    (\<\<SrvLink(re_comm/UpdateEnvironment)\>\>)
-   re_comm/update_objectowl (\<\<SrvLink(re_comm/UpdateObjectOWL)\>\>)

```{=html}
<!-- -->
```
-   re_comm/del_action_recipe (\<\<SrvLink(re_comm/DelActionRecipe)\>\>)
-   re_comm/del_binary_file (\<\<SrvLink(re_comm/DelBinaryFile)\>\>)
-   re_comm/del_environment (\<\<SrvLink(re_comm/DelEnvironment)\>\>)
-   re_comm/del_object (\<\<SrvLink(re_comm/DelObject)\>\>)

```{=html}
<!-- -->
```
-   re_comm/search_action_recipes
    (\<\<SrvLink(re_comm/SearchActionRecipes)\>\>)
-   re_comm/search_environments
    (\<\<SrvLink(re_comm/SearchEnvironments)\>\>)
-   re_comm/search_objects (\<\<SrvLink(re_comm/SearchObjects)\>\>)

```{=html}
<!-- -->
```
-   re_comm/query_action_recipes
    (\<\<SrvLink(re_comm/QueryActionRecipes)\>\>)
-   re_comm/query_environments
    (\<\<SrvLink(re_comm/QueryEnvironments)\>\>)
-   re_comm/query_objects (\<\<SrvLink(re_comm/QueryObjects)\>\>)

If data in the !RoboEarth database is to be changed, the corresponding
ROS service expects an API key as an argument. Services that provide
only read access to the DB don\'t need such a key. You can request your
API key at the web interface of the !RoboEarth database:
<http://roboearth.informatik.uni-stuttgart.de/>

## Syntactic Search

It is possible to search for database entries, which share a common
prefix for their unique identifier (UID) using the
\'\'/re_comm/search\_\<type\>\'\' services. As the class of an entity is
built from categories and subcategories (separated by dots) a prefix
search can be used to find all entities that are part of the same
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
and the \'\'/re_comm/query\_\<type\>\'\' services, you may access
server-side reasoning based on the RDF triples. Example queries:

-   Get all OWL classes:

```
SELECT C FROM
{C} rdf:type {owl:Class}
WHERE isURI(C)
```

-   query_action_recipes: Get all recipes having a label, which contains
    \"serve a drink\":

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
