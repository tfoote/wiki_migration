This package provides Python and C++ interfaces for
[universally unique identifiers (UUIDs)](http://en.wikipedia.org/wiki/Uuid),
as described in [RFC 4122](http://tools.ietf.org/html/rfc4122.html).

## Interfaces Provided

-   Python
    [unique_id module](https://docs.ros.org/en/melodic/api/unique_id/html/python/unique_id.html)

```{=html}
<!-- -->
```
-   C++
    [<unique_id/unique_id.h> header](https://docs.ros.org/en/melodic/api/unique_id/html/c++/namespaceunique__id.html)

The C++ interface is not released on Fuerte, because the Lucid boost
(1.40) has no uuid module. Users can compile and use it on other Fuerte
platforms, but it is not officially supported.
