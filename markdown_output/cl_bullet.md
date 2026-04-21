# Overview

`cl_bullet` is a common lisp wrapper around the Bullet physics engine.
It consists of a C++ library that wraps Bullet classes and methods into
C structs and functions and the corresponding common lisp FFI
definitions. In addition, it provides a higher-level CLOS library that
provides a lispy interface for Bullet and which hooks into the garbage
collector to free unused Bullet objects automatically when they are not
required anymore. Rigid bodies and the discrete-dynamics-world class are
well tested, support from constraints is untested and might be broken.
