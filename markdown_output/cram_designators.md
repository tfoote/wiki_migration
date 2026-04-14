## Introduction

Designators are Common Lisp objects for describing various parameters in
the [CRAM Plan Language](cram_language). To the user, designators are
objects containing sequences of key-value pairs of symbols. For example,
a location to see a specific object would be created as follows (the
variable \`object\` must be bound to an object designator already:
```
(make-designator 'location `((to see) (obj ,object)))
```

The current implementation supports three different designator types,
action designators as inputs for process modules, location designators
for describing locations under constraints and object designators for
describing objects on a symbolic level. The three designator types are
derived from the same class but they are handled differently in the
system.

## Basic Concepts

While the three currently supported designator types vary in the way
they are resolved, they share some common properties:

-   Designators can be effective designators, which means that they can
    be dereferenced. That means that besides their symbolic description,
    they also contain a low-level data structure. For location
    designators, this might be a 3d pose, for action designators an
    action goal and for object designators some low level structures
    such as point clouds, perception, etc. The references are not
    supposed to be used in a high level program but are a way for
    low-level modules to exchange data. For instance, when grasping an
    object, the grasping routine needs to have knowledge about the shape
    of objects.

```{=html}
<!-- -->
```
-   Designators are atomic objects. The properties of a single instance
    must not be changed by the user. This guarantees that users can
    store a designator in a variable and expect it not to change.

```{=html}
<!-- -->
```
-   To indicate that two designators reference the same property, they
    must be equated. For instance, if we have two detections of the same
    object at two different points in time, we equate the two
    designators. That way, the system can reconstruct the history of the
    belief about a single object and reason about object identities.

```{=html}
<!-- -->
```
-   For a given set of key-value-pairs of an effective designator, there
    might exist several solutions.

## User API

The designators package provides a few API functions for constructing,
equating and accessing designators. This API is mostly useful for the
end-user. Besides the user API, the system provides different APIs for
resolving the three different kinds of designators.

-   \`make-designator class properties &optional parent\` constructs a
    designator of type \`class\` and the given properties. If \`parent\`
    is specified, it is equated with it.

```{=html}
<!-- -->
```
-   \`equate parent successor\` equates the two designators.

```{=html}
<!-- -->
```
-   \`desig-equal designator-1 designator-2\` checks if two designators
    describe the same entity, i.e. if they are equated.

```{=html}
<!-- -->
```
-   \`first-desig designator\` returns the first ancestor in the chain
    of equated designators.

```{=html}
<!-- -->
```
-   \`current-desig designator\` returns the newest designator, i.e.
    that one that has been equated last to \`designator\` or one of its
    equated designators.

```{=html}
<!-- -->
```
-   \`reference designator &optional role\` tries to dereference the
    designator and return its data object or throws an error if it is
    not an effective designator, i.e. one that can be dereferenced. By
    specifying a role parameter, different resolution algorithms can be
    selected.

```{=html}
<!-- -->
```
-   \`next-solution designator\` returns another solution for the
    effective designator \`designator\` or NIL if none exists. The next
    solution is newly constructed designator with identical that is
    equated to \`designator\` since it describes the same entity.

```{=html}
<!-- -->
```
-   \`designator-solutions-equal solution-1 solution-2\` compares two
    designator solutions and returns T if they are equal.

```{=html}
<!-- -->
```
-   \`designator-solutions designator &optional from-root\` returns the
    lazy list of all solutions of a designator.

```{=html}
<!-- -->
```
-   \`copy-designator old-designator &key new-description\` returns a
    new designator with the same properties as \`old-designator\`. When
    present, the description parameter \`new-description\` will be
    merged with the old description. The new description will be
    dominant in this relation.

```{=html}
<!-- -->
```
-   \`make-effective-designator parent &key new-properties data-object
    time-stamp\` returns a new effective designator with the same type
    as \`parent\`. The parent\'s properties are used if
    \`new-properties\` is not specified. The internal data slot that is
    used for dereferencing the designator is set to \`data-slot\`.

```{=html}
<!-- -->
```
-   \`newest-effective-designator designator\` returns the newest, i.e.
    the current, equated effective designator.

```{=html}
<!-- -->
```
-   \`desig-prop-value designator property-key\` returns the value part
    of the designator property indicated by \`property-key\`.

## Designator Resolution

As already mentioned, the three currently supported designator classes
\`action\`, \`object\` and \`location\` are resolved differently.
Resolution means to generate real parameters for executing actions from
the symbolic key-value pairs of a designator.

### Object Designators

Object designators are a direct interface between CRAM plans and the
perception subsystem used on a robot. The key-value-pairs of in the
designator\'s properties describe the object that is to be perceived.
Finding the right object based on them is a perception subsystem\'s task
so the system does not provide any sophisticated mechanism for resolving
an object designator. There is only one constraint on object
designators: effective designators must bind the data object to an
instance of \`object-designator-data\` or a class derived from it.
Essentially, the following steps have to be implemented by the
perception subsystem:

1\. Parse the designator\'s properties for a description of the object
to be found.

2\. Find the described object.

3\. Create a new effective designator with the data object bound to an
instance of \`object-designator-data\` containing all relevant
information about the object.

4\. Equate the new effective designator with the original designator.

### Action Designators

Action designator resolution is normally based on using an inference
engine, namely prolog, to convert symbolic action descriptions to actual
ROS action goals or similar data structures. To implement resolution for
an action designator, the user has to provide definitions for the
predicate \`action-desig ?designator ?solution\`. For instance, if we
want to implement navigation, the corresponding action designator could
be constructed like this:

```
(let ((goal-location 
         (make-designator 'location 
           `((pose ,(make-pose-stamped 
                     "base_footprint" 0.0 
                     (make-3d-vector 1.0 0.0 0.0) 
                     (make-identity-rotation)))))))
  (make-designator 'action '((type navigation) (goal ,goal-location)))
```

This designator describes the action of moving one meter forward. The
only important information it contains, besides defining the actual
action \`(type navigation)\` is the goal pose. For resolution it might
be sufficient to just get the goal. The corresponding predicate
\`action-desig\` can be defined as follows:

```
(def-fact-group navigation-action-designator (action-desig)
  (<- (action-desig ?designator ?goal)
    (desig-prop ?designator (type navigation))
    (desig-prop ?designator (goal ?goal))))
```

### Location Designators

The most complex designator resolution mechanism currently is the
implementation of location designators. It is that complex because it
requires great flexibility to implement the computation of poses such as
\"a location to stand for opening a drawer\". Essentially, the
resolution of location designators is done in two steps:

1\. Generation of a lazy list of pose candidates.

2\. Verification if a generated pose candidate is actually a solution.

That way, generation can be kept very general and filters can be applied
to remove invalid solutions. When the \`reference\` method is called on
a location designator, the system first executes so-called generator
functions to generate the sequence of pose candidates. Generator
functions are priorized, i.e. they are ordered and some must be executed
before others. Each generator function must be a function that gets a
location designator as input and returns the (lazy) list of possible
solutions for this designator. The system then appends all lists and
tries to validate one solution after the other until either a solution
is valid or a maximal number of solutions has been tried. In that case,
the designator cannot be resolved and an error is thrown. Validation
functions are functions with two parameters, the designator that is to
be resolved and the pose candidate to validate. Depending on their
result a solution can either be accepted, immediately rejected or
rejected if no other validation function accepts it.

The following list describes the two API functions for registering
generators and validation functions:

-   \`register-location-generator priority function &optional
    doc-string\` registers a location generator function. \`priority\`
    is a fixnum used to order all location generators. Solutions
    generated with functions with smaller priorities are used first.
    \`function\` is a symbol naming the function that generates a list
    of solutions and that takes exactly one argument, the designator.

```{=html}
<!-- -->
```
-   \`register-location-validation-function prority function &optional
    doc-string\` registers a location validation function. \`priority\`
    is a fixnum that indicates the evaluation order of all validation
    functions. \`function\` is a symbol naming a function that takes
    exactly two arguments, the designator and a solution and returns
    \`:accept\`, \`:reject\`, \`:unknown\` or \`:maybe-reject\`.

As mentioned already, generator functions must return (lazy) lists.
Since the system supports lazy lists, it is possible to return sequences
of poses with infinite length. However, if a generator returns such an
infinite list, its priority should be chosen high to ensure that it is
processed last. Otherwise, generators that return finite lists would not
be processed at all.

Validation functions must return one of the following values:

-   \`:accept\`: Explicitly mark a solution candidate as acceptable.

```{=html}
<!-- -->
```
-   \`:unknown\`: The validation function cannot decide if the solution
    is valid.

```{=html}
<!-- -->
```
-   \`:maybe-reject\`: If the solution is not explicitly accepted, i.e.
    if all other validation functions return \`:unknown\`, the solution
    is rejected.

```{=html}
<!-- -->
```
-   \`:reject\`: Immediately reject a solution. No subsequent validation
    functions are called on that solution candidate.

A solution candidate is only accepted when all validation functions
either returned \`:unknown\` or \`:accept\`, or, if at least one
returned \`:maybe-reject\`, at least one returned \`:accept\`.

## Handling of Symbols and Packages

Designator properties are lisp lists of pairs of symbols. Let\'s
consider the following example of a designator description for an object
designator:

```
'((type cup) (color red))
```

The user might want to use the same designator properties across
different lisp packages that not necessarily know about each other. For
instance, if implementing two libraries that could be used independent
of each other and that use the same property symbols, we need a way to
make sure that both designator properties are really \`eq\` in terms of
Common Lisp comparison functions. We achieve that by enforcing all
designator properties to be in the same package and by interning these
symbols in all packages that declare the properties. In other words, a
package that uses a specific set of designator properties needs to
explicitly declare the corresponding symbols as designator properties.
The underlying system then interns them in the package \`DESIG-PROPS\`
and imports them in the package that contains the declarations.
cram_designators provides a macro that wraps Common Lisp\'s DEFPACKAGE
for implementing that behavior. To declare the above properties and a
few more as designator properties in package \`foo\`, we use the
following package definition for creating \`foo\` (instead of
DEFPACKAGE):

```
(in-package :cl-user)

(desig-props:def-desig-package foo
  (:use #:common-lisp)
  (:export some-awesome-functon some-even-more-awesome-function)
  (:desig-properties type cup pot plate color red blue black green))
```

Please note that all packages that are either using or implementing
designator properties are required to declare them properly.
