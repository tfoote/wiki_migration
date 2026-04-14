## Nodes

Both nodes write to a gnuplot file and plot the sharpness of the camera
image.

```clearsilver
name = focus
desc = Collects data on camera focus
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = Image from camera
}
```

```clearsilver
name = focus_prosilica.py
desc = Collects data on prosilica camera focus
sub {
  0.name = prosilica/image
  0.type = sensor_msgs/Image
  0.desc = Image from camera
}
```
