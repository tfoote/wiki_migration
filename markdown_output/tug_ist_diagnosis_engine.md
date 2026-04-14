## Overview

Diagnosis engine takes observations in the form of \'\'FOL\'\' sentences
and an abstract diagnosis model (system description) to generate a
diagnosis, a set of components that are faulty and a set of components
that are still working properly. It follows the principles of
model-based diagnosis which uses an abstract model that defines correct
behavior and some current observations of the system. Diagnosis engine
detects a fault if the outcome of the model and the observation lead to
a contradiction. Using a hitting set algorithm the approach calculates
diagnoses that resolve the contradiction, i.e., explain the misbehavior.
The diagnosis engine locates that component or set of components that is
the root cause for the contradiction.

## Nodes

```clearsilver
node.0 {
name= diagnosis_engine_controller
desc= This is a controller of diagnosis engine. It acts like a client. The server is a java based program that connects client over TCP.
}
```
