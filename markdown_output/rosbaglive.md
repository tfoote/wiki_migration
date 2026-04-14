## Usage

rosrun rosbaglive play.py path/to/a/useful.bag

## Effect

The script will load all of the messages FIRST (resulting in a pause)
and then play all of the messages with the timestamps changed to reflect
the current time, not the time that the messages were recorded. The
script also attempts to sleep for the appropriate amount of time to
replicate the relative timing of the original recording.
