## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/mpl.hpp>

// The concept definition/validation classes.
using ecl::Bool;        // compile time logic testing of template parameters
using ecl::enable_if;   // selective specialisation of classes via the template parameters   
using ecl::Unsigned;    // type converters
```



## Tutorials

-   [Boolean Logic](ecl_mpl/Tutorials/Boolean Logic) : using compile
    time boolean types for metaprogramming.
-   [Enable If](ecl_mpl/Tutorials/Enable If) : an if operator for
    template type arguments.
-   [Converters](ecl_mpl/Tutorials/Converters) : compile time type
    converters.
