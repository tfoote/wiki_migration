## Notes

When installing, it is highly recommended to have CUDA installed, though
not strictly required. A message during compilation will indicate
whether or not CUDA has been detected on your system. If detected, it
will be automatically used for the beam-based sensor model error
evaluation.

For test programs, including tools for running pose_corrector over bag
data and a preliminary integration with [tod](tod), see
[pose_corrector_test](pose_corrector_test).

To perform pose refinement as part of an
[Ecto](http://ecto.willowgarage.com/) graph, Python bindings for this
package are available in
[ecto_corrector](https://github.com/mkrainin/ecto_corrector).
