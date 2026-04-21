## What are Semantic Frames?

In `RoboFrameNet`, a **semantic frame** describes a scene being played
out. It consists of an overall concept, the *frame name*, as well as
related actors and objects, its *frame elements*.

## Creating, Adding, and Registering to Semantic Frames

The natural language processing capabilities of `RoboFrameNet` can be
extended by creating new semantic frames, adding them to the
`frame_registrar`, and registering your own code to semantic frames.

-   To **create** new semantic frames for `RoboFrameNet`, follow the
    guide [below](#Creating Semantic Frames).
-   To **add** the created semantic frames, see [rfnserver](rfnserver).
-   To **register** to a frame, see [rfnserver](rfnserver).

## Creating Semantic Frames

### Overview and Examples

Files are in standard yaml notation. The layout is most explained by
example; individual elements will be described below.

This is a **minimal example**, which describes a scene where the robot
emits a mooing sound:



```
name: mooing
description: The robot moos.
```



This is the first **"maximal" example**, which describes a robot
turning. Additionally, it describes its relation to two semantic frames,
which specifically describe the robot moving forwards or backwards:



```
name: moving
description: Robot moves in a direction (forwards or backwards) for distance distance_unit(s).  (eg, 3 feet)
frame_elements:
  - name: direction
    is_core: True
  - name: distance
    is_core: True
  - name: distance_unit
    is_core: True
children:
  - name: moving_forward
    frame_element_relations:
      - parent_name: distance
        child_name: distance
      - parent_name: distance_unit
        child_name: distance_unit
      - parent_name: direction
        child_value: [forward, forwards]
  - name: moving_backward
    frame_element_relations:
      - parent_name: distance
        child_name: distance
      - parent_name: distance_unit
        child_name: distance_unit
      - parent_name: direction
        child_value: [backward, backwards]
```



This is the second **"maximal" example**, which describes the robot
retrieving an object. Additionally, it describes its relation to a
series of other semantic frames, whose sequence performs the same task
as the master:



```
name: retrieving
description: Agent goes to object, picks up object, and gives it to the operator.
frame_elements:
  - name: object
    is_core: True
children:
  # This is a sequence of frames
  - - name: navigating_to_object
      frame_element_relations:
        - parent_name: object
          child_name: object
    - name: picking_up
      frame_element_relations:
        - parent_name: object
          child_name: object
    - name: navigating_to_master
```



See also some
[corresponding lexical units in the semantic_framer](semantic_framer#Overview and Examples),
which describe mappings for the first two examples.

### Notation

Below, the phrase "one or more" for an entry signifies that either a
single instance can be entered, or a list of multiple instances can be
entered. For instance, with verb, "one or more verbs" means all the
following entries are legal:



```
verb: moo
verb: [moo]
verb: [moo, speak]
```



### Required Values

Each semantic frame must specify the following values:

-   **name**: The name of the semantic frame.
-   **description**: A description of the semantic frame's scene.

### Optional Values

Each semantic frame may specify the following values:

#### frame_elements

**frame_elements** is a list of frame elements. Each frame element
describes an object or actor in the frame's scene and must have two
values:

-   **name**: The name of the frame element.
-   **is_core**: A boolean describing whether or not the frame element
    is core \-- that is, whether or not a value needs to be given to the
    frame element for a mapping to the semantic frame to be valid. (If
    no value is specified, the argument of the frame element will be
    "" (the blank string).)

#### children

**children** is a list of relation sequences from the parent frame to
child frames. A *relation sequence* describes a set of frames which \--
when executed serially \-- complete an action equivalent to the parent
frame. Each relation sequence contains one or more relations.

For each entry in a relation sequence, one value is required:

-   **name**: The name of the child frame.

Additionally, one value is optional:

-   **frame_elements_relations**: A list of mappings between the current
    frame's frame elements and the child frame's frame elements.

Each relation in frame_element_relations must have exactly one of the
following values:

-   **parent_name**: The name of the frame element in the current
    (parent) frame.
-   **parent_value**: An argument to fill into the child's frame
    element. (See below.)

Additionally, each frame element relation must have exactly one of the
following values:

-   **child_name**: The name of the frame element in the child frame.
-   **child_value**: One or more values which the parent's frame
    element's argument must have to allow the child's semantic frame
    to be filled.
