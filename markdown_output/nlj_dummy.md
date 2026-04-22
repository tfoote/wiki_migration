The role of this jockey is to demonstrate some functionalities of the
Large Maps Framework ([LaMa](Large Maps Framework)). The node
`nlj_dummy` starts two jockeys ([actionlib](actionlib) servers): a
localizing jockey and a navigating jockey. The localizing jockey
(`lj_dummy`) generates 4 randoms integer values
([nlj_dummy/msg/Dummy](https://docs.ros.org/en/rolling/p/nlj_dummy/msg/Dummy.html))
and stores them into the map. The navigating jockey (`nj_dummy`)
prints on the console the edge it was asked to traversed and its
associated descriptor, and waits a random time.

## Usage



```
roslaunch nlj_dummy random_walk.launch
```


