Package for speech recognition using Google\'s Speech API

## Git

<https://github.com/achuwilson/gspeech>

## Overview

This package allows the recognition of speech using Google\'s speech
engine. The audio is sampled and send to the Google\'s servers, which in
turn will process it and return the speech content and the confidence
value of the recognition. It has an advantage of speaker indepedent
recognition and no training required. The disadvantage is that it a bit
slower unless you have a good internet connection. The node publishes
two topics: */speech* and */confidence*. */speech* is the recognized
speech which is of the standard String message type.*/confidence* is the
confidence level of recognition which is of the standard Int8 message
type.

## Quick Tutorial

-   sudo apt-get install sox
-   clone the git
-   rosrun gspeech gspeech.py
