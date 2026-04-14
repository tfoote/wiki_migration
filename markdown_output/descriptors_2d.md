## Contact Info

![](attachment:email-alex.jpg)

## Descriptors

\`descriptors_2d\` is a package for providing a common interface to many
different image descriptors. Currently, the descriptors that are
recommended for use are:

-   Superpixel color histogram
-   SURF
-   HOG
-   Daisy

The daisy descriptor is currently in descriptors_2d_gpl until we can get
it BSD licensed.

Notes

-   \`descriptor.getName()\` is guaranteed to be unique for any setting
    of parameters.
-   All descriptors work with both BGR and grayscale (\`IPL_DEPTH_8U\`)
    images unless otherwise noted.
-   SURF will give you different numbers on 32 and 64bit machines, at
    least in our tests.

## Tutorials

See \`descriptors_2d/src/example.cpp\`.

## Video (Hand detection)

[Youtube](https://www.youtube.com/watch?v=2MStTgDZSsU)
