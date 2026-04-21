This is a third party package that pulls a specific version (currently,
1.0.37) of the SBCL Lisp compiler, used by [roslisp](roslisp) (roslisp
doesn't directly depend on this package, but
[roslisp_runtime](roslisp_runtime), which is required to run roslisp
nodes, does).

This downloaded version will coexist peacefully with any existing
installations on your system. Roslisp standalone executables will use
this version, and if you're developing roslisp nodes interactively, you
should use it too. This is done by running the following script:
```
rosrun sbcl run-sbcl.sh <any-additional-sbcl-params>
```
