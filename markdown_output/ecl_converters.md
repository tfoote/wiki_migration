## Introduction

The converters here provide a \_fast\_ and \_type-safe\_ means of doing
type conversion, but lack formatting capabilities. If you need
formatting capabilities with conversion to text types, use the formatter
classes provided in [ecl_formatters](ecl_formatters).

They\'re also used to provide generic conversions between existing
classes.

## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/converters.hpp>

// The error interfaces
using ecl::Converter;
```
