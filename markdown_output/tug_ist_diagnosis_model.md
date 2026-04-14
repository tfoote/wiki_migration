## Overview

The diagnosis model server is an action server that provides the
diagnosis model. The diagnosis model is stored as a \'\'YAML\'\' file
(similar to XML) and contains five sections: (1) a string that denotes
the proposition that represents the \'\'AB\'\' predicate, (2) the same
for \'\'AB\'\', (3) a string for a prefix denoting a negative literal,
(4) a set of all propositions, (5) a set of clauses that defines the
diagnosis model.

## Nodes

```clearsilver
node.0 {
name= diagnosis_model_server.py
desc= This node acts like a action server. It takes diagnosis model in yaml file and publishes the model.
}
pub {
    0.name = /diagnosis_model
    0.type = tug_ist_diagnosis_msgs/SystemModelResult
    0.desc = It provides system model for the diagnosis.
}
param{
    0.name = ~model
    0.type = string
    0.default = `"diagnosis_modle.yaml"`
    0.desc = This parameter gets the model yaml file. It should include complete path if the model exists somewhere outside the package.
}
}
```
