## Example

Using this node is discussed in
[ROSARIA/Tutorials\|target=\"\_blank\"](ROSARIA/Tutorials/How to use ROSARIA#Using_iPhone.2BAC8-iPad_as_a_joystick).
Below is a demo video.

[Youtube](https://www.youtube.com/watch?v=E2Ll3JcqZN0)

## ROS API

```clearsilver
name = pyoj.py
desc = Publishes data from the [[http://code.google.com/p/accelerometer-simulator/|accelerometer-simulator]]
pub {
  0.name = joy
  0.type = joy/Joy
  0.desc = publishes joystick information from [[http://code.google.com/p/accelerometer-simulator/|accelerometer-simulator]]
}
```
