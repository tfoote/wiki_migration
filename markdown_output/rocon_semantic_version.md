## Overview

A very convenient, simple python package for interacting with standard
`MAJOR.MINOR.PATCH` version number strings.

```highlight
import rocon_semantic_version as semantic_version

version = semantic_version.Version("1.5.2")
print("Major Version: %s" % version.major)   # 1
print("Minor Version: %s" % version.minor)   # 5
print("Patch Version: %s" % version.patch)   # 2

version2 = semantic_version.Version("1.5.3")
version < version2                           # True
```

Note that it has been renamespaced to `rocon_semantic_version` to
avoid conflicts with a locally installed module. See the
[original documentation](https://github.com/rbarrois/python-semanticversion)
for more information.
