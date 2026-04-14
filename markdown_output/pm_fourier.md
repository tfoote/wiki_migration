\`pm_fourier\` implements a place matching based on FTT for the Large
Maps Framework ([LaMa](Large Maps Framework)).

## Usage

### ROS API

```clearsilver
srv {
  0.name= ~<name>/compute_dissimilarity
  0.type= polygon_matcher/PolygonDissimilarity
  0.desc= Compute the dissimilarity between two polygons
}
param {
  0.name= max_thread
  0.type= int
  0.desc= Max. number of threads
}
```
