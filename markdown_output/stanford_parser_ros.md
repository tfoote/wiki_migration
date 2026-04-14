```wiki
'''WARNING:''' This documentation refers to an outdated version of rosjava and is probably incorrect. Use at your own risk.
```

## Interpreting Output Messages

### Parse tree

A python utility is provided to unsquash the parse trees and
dependencies output by \`stanford_parser_ros\`. This will create a tree
structure:

```
from stanford_parser_msgs import unsquash_tree

[...]

def callback(msg): # msg type: stanford_parser_msgs/Parse
  [...]
  parse_tree = unsquash_tree(msg)
  [...]
```

Each node in the tree \-- an instance of the class Tree \-- has the
following elements:

```
node.tag        # string
node.score      # double -- confidence rating of the Stanford Parser
node.word       # string
node.word_index # integer -- node.word = msg.words[node.word_index]
node.children   # listof(Tree)
```

The part-of-speech tags used in the Stanford Parser come from Penn
Treebank II and can be found
[here](http://bulba.sdsu.edu/jeanette/thesis/PennTags.html).

### Dependencies

Dependencies (a list located under \`msg.dependencies\`) have the
following 3 elements:

-   \'\'\'relation\'\'\': Relation between the governor and dependent. A
    complete set of relations can be found in the
    [Stanford Dependencies Manual](http://nlp.stanford.edu/software/dependencies_manual.pdf).
-   \'\'\'governor_index\'\'\': The index of the governor in
    \`msg.words\`. In other words, the governor is
    \`msg.words\[dependency.governor_index\]\`.
-   \'\'\'dependent_index\'\'\': The index of the dependent in
    \`msg.words\`. In other words, the dependent is
    \`msg.words\[dependency.dependent_index\]\`.

For instance, the sentence \"Give Bill the ball.\" has, among others,
the dependency \"dobj(give-2, ball-5)\". For this dependency, relation
is \"dobj\", governor_index is 2, and dependent_index is 5.
