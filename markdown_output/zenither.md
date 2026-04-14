Code to control an Animatics Smart Servo. We use the Animatics servos to
control Festo linear actuators.

## Usage

Prior to using this package to control a Festo linear actuator, a set of
parameters calibration parameters associated with your individual
actuator must be present in zenither_config.py. These calibration
parameters are stored using Python dictionaries and will be referred to
in code using that set of parameter\'s key.

After calibration (in Python): ```
import zenither.zenither as zen
z = zen.Zenither('CALIBRATION_KEY')
z.move_position(.3) # move to a pose 30cm from the ground
```
