Roslisp_runtime is a dummy package that exists so the ros stack, which
contains [the actual roslisp package](roslisp), need not have a
dependency on the SBCL lisp compiler. Instead, if your package uses
roslisp, its manifest should contain a dependency on this package. See
the [roslisp](roslisp) package documentation for instructions on using
roslisp.
