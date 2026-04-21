## Installation

Please refer to the installation instructions here:
<http://www.knowrob.org/installation>

## Documentation and Package List

-   Starting and accessing Prolog
-   [rosprolog](rosprolog): Start an interactive Prolog shell
-   [json_prolog](json_prolog): Start ROS service that offers a query
    interface

```{=html}
<!-- -->
```
-   Base system
-   [ias_knowledge_base](ias_knowledge_base): Core ontology and basic
    reasoning modules
-   [knowrob_common](knowrob_common): Common utilities for handling OWL
    (import/export, OWL reasoner interface, convenience query
    predicates), units of measure, and other generic functionality
-   [knowrob_objects](knowrob_objects): Object-related functionality,
    supporting spatio-temporal reasoning, generation of the internal
    object representation, representation and conversion of coordinates
-   [knowrob_actions](knowrob_actions): Read action properties, project
    effects of actions and processes, reason about transformations of
    objects induced by actions
-   [ias_semantic_map](ias_semantic_map): Semantic environment map
    representation in OWL
-   [ias_prolog_addons](ias_prolog_addons): Prolog extensions such as
    the interface to the Weka and Mallet classification libraries,
    Jython interface, computation of semantic similarity measures
    between concepts
-   [semweb](semweb): Semantic Web library of SWI prolog with
    extensions, e.g. computable properties
-   [thea](thea): OWL parser library

```{=html}
<!-- -->
```
-   Reasoning packages
-   [comp_spatial](comp_spatial): Compute qualitative spatial relations
    from object poses
-   [comp_temporal](comp_temporal): Compute temporal relations, e.g.
    Allen's interval algebra
-   [mod_vis](mod_vis): Visualization of the content of the knowledge
    base
-   [knowrob_cad_models](knowrob_cad_models): Load Collada models for
    visualization and reasoning
-   [mod_srdl](mod_srdl): Description of robot components and
    capabilities and methods for matching these descriptions against
    requirements of actions
-   [mod_probcog](mod_probcog): Interface to the
    [ProbCog](https://ias.cs.tum.edu/software/probcog) statistical
    relational learning library

```{=html}
<!-- -->
```
-   Interfaces to perception components
-   [prolog_perception](prolog_perception): (deprecated) Integration of
    perception using a Prolog module
-   [comp_cop](comp_cop): Interface to the [CoP perception system](cop)
-   [knowrob_objects](knowrob_objects): Generic library for creating the
    KnowRob-internal object representation

```{=html}
<!-- -->
```
-   Probabilistic reasoning
-   [srldb](srldb): Package with the
    [ProbCog](https://ias.cs.tum.edu/software/probcog) library

```{=html}
<!-- -->
```
-   Related packages:
-   [comp_ehow](comp_ehow): Import of natural-language web instructions,
    removed from KnowRob to reduce dependencies

Further documentation can be found here: <http://www.knowrob.org/doc>

## Tutorials

More tutorials can be found in the extensive
[documentation section](www.knowrob.org/doc) of the KnowRob wiki.

## Issue tracker

Please file bugs and feature requests here:
<https://github.com/knowrob/knowrob/issues>

## Publications

The most comprehensive overview of the KnowRob system and related
research can be found in
[Moritz Tenorth's PhD thesis](http://nbn-resolving.de/urn/resolver.pl?urn:nbn:de:bvb:91-diss-20111125-1079930-1-7).
The full list of KnowRob-related publications is available at
<http://www.knowrob.org/publications>

When you publish a paper using KnowRob, please cite the 2013 IJRR
article:



```
@Article{tenorth13knowrob,
  author  = {Moritz Tenorth and Michael Beetz},
  title   = {{KnowRob -- A Knowledge Processing Infrastructure for
              Cognition-enabled Robots. Part 1: The KnowRob System}},
  journal = {International Journal of Robotics Research (IJRR)},
  year    = {2013},
  volume  = {32},
  number  = {5},
  pages   = {566 -- 590},
  month   = {April},
  year    = {2013}
}
```



## Acknowledgments

The development of KnowRob has received funding from the DFG excellence
initiative research cluster
[Cognition for Technical Systems (CoTeSys)](http://www.cotesys.org) and
the EU FP7 projects [RoboEarth](https://roboearth.org) and
[RoboHow](https://robohow.eu).
