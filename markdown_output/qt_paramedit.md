## Usage

After startup rxparamedit will acquire parameters from the param server
and display them for editing. ```
rosrun qt_paramedit qt_paramedit [parameter root] (default: /)
``` If you pass an
optional parameter root, only parameters from that namespace will be
listed. The parameter root has to be a dictionary (i.e. no single
variables).

### Screenshot

![](attachment:rxparamedit.png)

Note: This package replaces groovy's [rxparamedit](rxparamedit) in
hydro.
