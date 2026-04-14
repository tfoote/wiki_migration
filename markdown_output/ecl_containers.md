## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/containers.hpp>

// The container types
using ecl::Array;
using ecl::Stencil;
using ecl::FiFo
using ecl::PushAndPop;
```

## Tutorials

-   [Arrays](ecl_containers/Tutorials/Arrays) - fixed and dynamic
    arrays, comma initialisation and blueprints.
-   [Stencils](ecl_containers/Tutorials/Stencils) - windows onto ecl
    arrays.
-   [Buffer Overflow Detection](ecl_containers/Tutorials/Buffer Overflow Detection) -
    detecting array under and over runs.
-   [Fifo](ecl_containers/Tutorials/Fifo) - A simple first in, first out
    class.
-   [Utilities](ecl_containers/Tutorials/Utilities) - container
    formatters and converters.

## Examples

See the programs in the \`src/test\` and \`src/examples\`
subdirectories.
