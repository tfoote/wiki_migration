## What are Lexical Units?

In `RoboFrameNet`, a **lexical unit** provides a mapping from parsed
natural language to semantic frames. Lexical units contain a verb, which
is said to *evoke* a semantic frame, as well as the verb's
dependencies, for instance the verb's direct object, indirect object,
etc.

## Creating and Adding New Lexical Units

The natural language processing capabilities of `RoboFrameNet` can be
extended by creating new lexical units and adding them into
`semantic_framer`. This guide will help you create new lexical units
and add them to `RoboFrameNet`.

### Creating Lexical Units

#### Overview and Examples

Files are in standard yaml notation. The layout is most explained by
example; individual elements will be described below.

This is a minimal example, which binds the verb "moo" to the
"mooing" semantic frame:



```
frame_name: mooing
verb: moo
```



This is a "maximal" example, which will bind sentences such as "Move
forward 2 feet." to the moving semantic frame:



```
frame_name: moving
verb: [go, move, drive]
description: ""
frame_element_grammatical_relations:
  - name: direction
    relation: prt
  - name: distance_unit
    relation: dobj
  - name: distance
    relation: num/dobj
```



See also the
[corresponding example frames for frame_registrar](frame_registrar#Overview and Examples).

#### Notation

Below, the phrase "one or more" for an entry signifies that either a
single instance can be entered, or a list of multiple instances can be
entered. For instance, with verb, "one or more verbs" means all the
following entries are legal:



```
verb: moo
verb: [moo]
verb: [moo, speak]
```



#### Required Values

Each lexical unit must specify the following values:

-   **frame_name**: The name of the semantic frame to which this lexical
    unit binds.
-   **verb**: One or more verbs that evoke the semantic frame.

#### Optional Values

Each lexical unit may specify the following values:

-   **description**: A description of the lexical unit, what it does,
    what it's supposed to bind, etc.
-   **frame_element_grammatical_relations**: A set of relations that map
    from dependencies (direct object, indirect object, etc.) to the
    elements of the semantic frame.

`frame_element_grammatical_relations` is a list. Each entry in this
list must have the following values:

-   **name**: The name of the frame element in the semantic frame.
-   **relation**: The dependency with respect to the verb. Dependencies
    may be multiple levels out. (For instance, saw we want the adjective
    describing the direct object of the verb \-- that is, "red" in
    "Pick up the red ball.") In this case, each relation is separated
    by a `/`. (In our example, we would type amod/dobj.)

#### Determining relations

Assuming one is using [stanford_parser_ros](stanford_parser_ros), a
complete set of relations can be found in the
[Stanford Dependencies Manual](http://nlp.stanford.edu/software/dependencies_manual.pdf).

Additionally, relations can be found empirically. First, start the
natural language processing half of roboframenet:



```
roslaunch roboframenet_bringup nlp.launch
```



Then, send example sentences:



```
rostopic pub command std_msgs/String "Pick up the red ball."
```



The terminal which is running `nlp.launch` will display the resultant
parse tree and dependencies:



```
(ROOT (S (NP (PRP You)) (VP (VBP pick) (PRT (RP up)) (NP (DT the) (JJ red) (NN ball))) (. .)))
nsubj(pick-2, You-1)
prt(pick-2, up-3)
det(ball-6, the-4)
amod(ball-6, red-5)
dobj(pick-2, ball-6)
```



(Note: The implicit "you" was added by
[imperative_to_declarative](imperative_to_declarative).)

#### Multiple Lexical Units in a Single File

A single yaml file can also contain multiple lexical units. In this
case, the lexical units are just a top level list:



```
- frame_name: mooing
  verb: moo
  [...]

- frame_name: navigating
  verb: move
  [...]
```



### Adding Lexical Units to RoboFrameNet

[rfnserver](rfnserver) allows you to add lexical units in the form of
yaml files to the RoboFrameNet framework.
