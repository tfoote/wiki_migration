## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/type_traits.hpp>

// The error interfaces
using ecl::numeric_limits;
using ecl::is_integral;
using ecl::is_float;
using ecl::is_signed;
using ecl::is_unsigned;
using ecl::is_byte;
```

If outside ros, you will also need to link to *ecl_type_traits*.

## Tutorials

-   [Numerical Limits](ecl_type_traits/Tutorials/Numerical Limits) -
    fixing a few rough edges around c++ numeric limits.
-   [The 'Is A' Traits](ecl_type_traits/Tutorials/The 'Is A' Traits) -
    temporary fillers for the 'is a xxx' fundamental type traits till
    C++0x is widespread.
