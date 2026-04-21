## Documentation

Python library to parse SDF and represent it as class hierarchy. Also
supports conversion into URDF.

-   *sdf2urdf.py \[-p plotfile.png\] model.sdf model.urdf* uses the
    pysdf library to convert a SDF model to a URDF model (and optionally
    plot the SDF model). Hierarchical SDF models (<include>) are
    supported. URDF can only express a subset of SDF models, therefore
    the conversion will only result in a valid URDF (use `check_urdf`),
    if the SDF is within this subset - i.e. there is a unique root link.
