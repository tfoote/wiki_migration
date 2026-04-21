

```wiki
'''This documentation is under construction.'''

It is currently in an alpha state and will be completed soon.
```



## Overview

The arni_countermeasure package provides the possibillity to define
specific reactions when a ros environement is not behaving as defined
with [arni_processing](arni_processing).

It is possible to define complex constraints containing the definition
of how the environement has to behave in order to trigger a specific
reaction.

## Documentation

### Constraints

Constraints are definitions of how [entities](todo_add_link) need to
behave for a certain amount of time to trigger
[reactions](todo_add_link). They can be set as parameters withing the
namespace /arni/countermeasure/constraints.

A constraint consists of:

-   a unique name (mostly for the user to distinguish them)
-   a statement that has to be true
-   reactions to be executed

#### Constraint statement

A statement has to start with only one entry. Multiple statements can be
combined with **or** and **and**.

Its possible to negate a statement with **not**.

A entry consists of:



```
seuid: { statistic_type: expected_value, another_s_type: another_value }
```

 Where expected_value can be **okay**, **high**,
**low**, **unknown**

#### Constraint parameter

A constraint has the following parameters:

  -- ----------------------- -- --------------------------------------------------------------------------------------------- --
     **parameter**              **description**                                                                               
     constraint                 Contains a statement that gets evaluated.                                                     
     min_reaction_interval      The time (in seconds) that the constraint has to be true to execute the reactions.            
     reaction_timeout           Time (in seconds) that the constraint has to wait till its reactions can be executed again.   
     reactions                  A dict of reactions.                                                                          
  -- ----------------------- -- --------------------------------------------------------------------------------------------- --

#### Reaction

A reaction is an action taken after the constraint statement had been
true for min_reaction_interval seconds.

There are the following action types:

  -- ----------------- -- ---------------------------------------------- -- ------------------------ --
     **action type**      **description**                                   **additional entries**   
     publish              Publish a message to rosout.                      message, loglevel        
     stop                 Stops a node.                                     node                     
     restart              Restarts a node.                                  node                     
     run                  Runs a command on the host the node runs on.      node, command            
  -- ----------------- -- ---------------------------------------------- -- ------------------------ --

Additionally a **autonomy_level** can be set. Only reactions with an
autonomy_level <= config/reaction_autonomy_level get executed.

### Example

An example yaml file containing constraints to be loaded to the
parameter server: 

```
arni:
  countermeasure:
    constraints:
      unique_constraint_name:
        constraint:
        - or:
            some_seuid: {
              cpu_usage_mean: high,
              node_bandwith_mean: low
              }
            another_seuid: {
              ram_usage_mean: high}
        min_reaction_interval: 5
        reaction_timeout: 20
        reactions:
          reaction_name: {
            action: stop,
            autonomy_level: 100,
            node: node1}
          another_reaction_name: {
            action: publish,
            autonomy_level: 13,
            message: node1 has a problem,
            node: node1,
            loglevel: info}
      another_constraint:
        constraint:
        - and:
            some_seuid: {
              node_bandwith_mean: unknown
            }
            another_seuid: {
              node_bandwith_max: ok 
            }
            not:
              third_seuid: {
                cpu_usage_mean: high 
              }
    config:
      reaction_autonomy_level: 50
      storage_timeout: 10
```



### Reloading Constraints

1\. Load new constraints to the parameter server. 1. Call the service
reload_constraints. (Takes no arguments and returns nothing) Constraints
can be reloaded during runtime with the service reload_constraints.
