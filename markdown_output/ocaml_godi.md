## Description

ocaml_godi is a wrapper for
[GODI](http://godi.camlcity.org/godi/index.html), which is a package
management system and distribution of the
[OCaml](http://caml.inria.fr/ocaml/) programming language. This wrapper
is provided so as to allow ROS packages depending on OCaml to build in a
self-contained manner inside of ROS.

## Installation

\`rosmake ocaml_godi\` will install a basic GODI distribution into the
\`ocaml_godi\` package directory. This involves downloading the sources
for OCaml and a significant number of supplementary OCaml modules, and
then building these. Therefore, this step may take a while.

**Please note that the installation process will modify your
/.bash_profile.** Specifically, it will append some lines to set
environment variables necessary for OCaml compilation to proceed
successfully. If your shell is invoked in such a way that /.bash_profile
is not sourced (or if you use a shell besides bash), you will need to
source it or set these variables manually.
