## How to use cv_mech_turk to label data from annotated_map_builder

1\. ` roscore `

2\. Run snapper

` rosrun cv_mech_turk snapper.py -block_submit=1 `

(setting block_submit=1 blocks the submission from occurring, so you can
check that it is working before uploading for real)

3\. Make a launch file to remap raw_stereo_throttled from your bag file
to raw_stereo: 

```
<node pkg="rosrecord" type="rosplay" args="<absolute path to your bag file>" output="screen">
<remap from="/stereo/raw_stereo_throttled" to-"/raw_stereo" />
</node>
```



## Video

[Youtube](https://www.youtube.com/watch?v=1LruqPbRY64)
