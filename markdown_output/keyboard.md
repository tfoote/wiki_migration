## Overview

This package allows you to receive keyboard events (key-up, key-down),
similar to how the joy node works.

Since it uses SDL to capture keyboard events, a separate window will be
opened when the node starts, and this is where all keyboard input will
be received. In other words, the node will receive key-presses only when
this window is focused.



```clearsilver
name = keyboard
desc = Listens to key-presses and publishes them as messages
pub {
  0.name = keydown
  0.type = keyboard/Key
  0.desc = key-down events are published in this topic
  1.name = keyup
  1.type = keyboard/Key
  1.desc = key-up events are published in this topic
}
param {
  0.name= ~allow_repeat
  0.type= bool
  0.desc= Enables or disables the keyboard repeat rate ([[http://sdl.beuc.net/sdl.wiki/SDL_EnableKeyRepeat|see SDL documentation]]).
  0.default= false
  1.name= ~repeat_delay
  1.type= int
  1.desc= How long the key must be pressed before it begins repeating.
  1.default= SDL_DEFAULT_REPEAT_DELAY
  2.name= ~repeat_interval
  2.type= int
  2.desc= Key replay speed.
  2.default= SDL_DEFAULT_REPEAT_INTERVAL
 }
```


