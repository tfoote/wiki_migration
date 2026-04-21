Contains a pair of nodes to save and reload poses of the PR2. Both nodes
expect the standard suite of PR2 controllers to be up. Also check out
the `bash/compgen_hooks.sh` script for tab completion on pose files.

## save.py

```
save.py FILENAME
```

Saves the current pose of the pr2 to the given file.

### load.py

```
load.py FILENAME
```

Make the pr2's pose (not including the base pose) be the one specified
in the file. Does no collision avoidance, so make sure there aren't any
obstacles around. Also, if it fails for some reason, e.g., its arms get
tangled up, it currently has no way of signalling failure, so will just
stop eventually.
