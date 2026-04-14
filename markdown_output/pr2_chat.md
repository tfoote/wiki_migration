A demo of how to use speech recognition and generation.

## Input

Here are the valid input sentences: ```
hello
what's your name
what is your name
harris report
what is the first law of robotics
what is the second law of robotics
what is the third law of robotics
high five
pound it
``` Note: Must
be recognized exactly by pocketsphinx

## Output

Node will either use the sound_play library to verbalize a response, or
will use the roslaunch api to make the robot perform one of the
pr2_props.
