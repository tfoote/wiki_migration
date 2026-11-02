[Calibrating the battery display](#battery_calibration)

## battery_calibration

- On the parameter server, define the parameter "/recording_filename",
  e.g. `rosparam set /recording_filename cob3-3_1.csv`
- Run the script that should be executed during recording (e.g. moving
  the robot back and forth)
- `rosrun cob_relayboard record_voltage.py`
- Check if the recording works ok, e.g. `tail cob3-3_1.csv`
