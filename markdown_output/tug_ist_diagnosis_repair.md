## Overview

The repair engine takes current observations and diagnoses as input. If
the repair engine receives a diagnosis message, it converts the
diagnosis into to a planning problem and solves it with the help of
*Planning Domain Definition Language (PDDL)* based planner. Currently
diagnosis repair engine finds action plan for the first diagnosis.

## Nodes

```clearsilver
node.0 {
name= diagnosis_repair
desc= This is planning based repair engine. It acts like a client. The server is a java based program that connects client over TCP.
}
```
