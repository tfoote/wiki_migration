## Overview

This package contains the specification for the XML contact point
description format (RCPDF) and a C++ parser to read the corresponding
RCPDF XML files.

### Robot Contact Point Description Format (RCPDF)

For a complete specification, please see the
[RCPDF XML reference](rcpdf/XML).

The root node \`robot\` is shared with the [URDF](urdf) and [SRDF](srdf)
specifications. It allows to fuse all the robot informations into a
single file as the parser will safely ignore the tags which are not part
of the specification.

### RCPDF Parser

The RCPDF parser creates a C++ representation of a robot that is easy to
browse through. For more details, take a look at the
[C++ code api](http://www.ros.org/doc/api/rcpdf/html/).

### RCPDF Validator

The package includes the command line tool \`check_rcpdf\`. It\'s called
with a single command line argument naming a file. It attempts to parse
the file as a RCPDF description, and either prints a description of the
resulting contact zones description, or an error message.

## Examples

### Nao Robot

TO BE DONE.
