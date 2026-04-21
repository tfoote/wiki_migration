# Morser: Morse Code Input to Linux Systems

## Overview

The Morser package enables computer operators to input text via Morse
code. The user interface is designed to work when only cursor movement
and single clicks are available to the user. For example, the interface
works with a head tracker and a mouse switch.

![](attachment:morserMainWindow.png)

Operating the interface generates Morse code, which Morser translates to
text. The text is sent both to a ticker tape that is part of the UI, and
to the X11 window that is in focus.

Special cursor physics are active during Morse code generation to
maximize accuracy, comfort, and speed. A speed timer is available in the
interface to self monitor progress.

A number of motion parameters are controlled in an options screen. A
Morse code reference sheet is also built in.

## Starting the Application

Morser is started via:



```
roslaunch morse_input morse.launch
```



The resulting main window may be moved to a convenient place. If the
window is resized, the new size is remembered, and subsequent starts of
the application will size the main window accordingly.

## Operation

The Morser interface is modeled after single-paddle electronic telegraph
keys. During operation, the cursor is situated inside the *rest zone,*
the area with the crosshair between the buttons. When the cursor is
moved against the *dot* button, a series of Morse dots is automatically
generated, until the cursor is backed away from the button edge.
Generation of dash sounds is analogous.

It is important to click on the intended text destination window before
beginning Morse generation in the Morser window. Make sure the Morser
window and the text destination window do not overlap to avoid flicker
of the Morser window.

Once that destination window is selected, move the cursor into the
Morser window. In order to avoid spurious input while passing over one
of the buttons when moving the cursor into the rest zone, keep the left
mouse button depressed during the cursor move. The button acts as a
clutch that temporarily deactivates the dash and dot buttons.

Once the cursor has reached the rest zone, release the mouse button. The
cursor will then be constrained to move horizontally. Morser will also
prevent the cursor from penetrating into the dot and dash button areas.
If moved against one of these buttons, the cursor is kept touching the
respective button's edge. This constraint enables the user to 'slam'
the cursor into the button edges, while keeping the return distance into
the rest zone constant.

To move the cursor out of the rest zone, hold down the left mouse button
before moving the cursor. While Morser is not in use, the buttons can be
disabled via the virtual power switch in the upper right corner of the
Morser window. This precaution is recommended to prevent text to be
inserted into focused windows while moving the cursor across the Morser
window.

Use of the *Space* and *Backspace* buttons is not recommended. Their use
is very time consuming, and disrupts input rhythm, which is essential
for speedy operation. Instead, spaces can be inserted by one of two
methods:

-   Use a pause between Morse letters to insert a space between two
    words automatically. This behavior is the default, but it can be
    modified in the options panel (See [#OptionsPanel](#OptionsPanel)
    section below).
-   Use the fusion of the H and S Morse signals into a single sequence
    of seven dots: four for *H*, and three for *S* (ligature). HS stands
    for Horizontal Space.

Backspace can similarly be produced via BS (*dash-dot-dot-dot
dot-dot-dot*)

## Options Panel

A number of operational parameters can be adjusted in the ''Options
Panel,'' which is reached either via the Edit menu, or the keyboard
shortcut `cnt-O` (that is *oh* as in option). Hovering over any of the
elements raises a short tooltip that explains the purpose of each
widget.

![](attachment:morserOptions.png)

The options panel consists of several sections. The '''Dwell
segmentation*' section's *Word stop'' checkbox controls whether or
not pauses beyond a certain threshold between Morse letters
automatically insert a space. When a long enough pause is detected, the
crosshair in the rest zone briefly blinks yellow. The length of the
pause is controlled by the inter-letter delay slider of the options
panel.

The **Output** section controls where decoded text is sent. The ticker
tape inside the main Morser window can always be targeted in addition to
other destinations. Outside the Morser window, options are to have the
text sent to the currently focused screen window, or to have it sent to
SpeakEasy for text-to-speech conversion.

The **Cursor constraint** section controls cursor behavior. The default
of having the cursor be constraint to horizontal travel inside the rest
zone may be altered by unchecking the *Constrain cursor* checkbox. The
*Deceleration* slider controls cursor speed inside the rest zone. It is
generally recommended to slow the cursor in the zone. The slider
controls the factor by which the cursor is slowed, relative to the
current mouse cursor speed as set in the operating system settings.

The **Speed Controls** section holds three controls. The ''Key
speed'' adjusts the speed at which dots and dashes are generated while
the cursor abuts the respective *dot* or *dash* button. The
*Inter-letter delay* controls the threshold of time lapse between
successive dots or dashes that has Morser conclude that one Morse letter
has been entered to completion. For example: a Morse *dot* encodes the
letter 'e', while *dot-dot* encodes the letter 'i'. Morsing the
sequence 'ei' requires a brief pause between the first *dot* and the
following sequence of two *dots*. This pause is the inter-letter delay.
If the operator does not provide this pause, then Morser interprets the
total of three *dots* as a single letter 's'. The inter-letter delay
is measured in milliseconds.

The *Inter-word delay* is only relevant when Word stop is turned on. The
slider's units are milliseconds, and its setting determines when Morser
concludes that an inter-word space is to be inserted.

All options settings are permanently stored below the user's home
directory, in `\$HOME/.morser/morser.cfg`.

## Speed Timer

Clicking the plus sign on the Morser window opens a Morse input timing
tool. The tool measures words per minute, where a word is any sequence
of five Morse letters or spaces. To start the timer, click the *TimeMe*
button. The crosshair will begin to blink, indicating that the timer is
cocked. Timing only starts with the beginning of the first Morse letter.

The timer can be temporarily suspended by holding down the left mouse
button.

## Morse Reference Table

The View menu allows users to raise a Morse code reference table. The
keyboard shortcut `cnt-m` also exposes the table. All Morse letters in
the table are standard, except for horizontal space and backspace.

![](attachment:morserRefTable.png)

## MorseChallenger for Learning Morse Keying

The MorseChallenger program is a simple game that comes with Morser.
Users select a level of difficulty, and the characters they have already
learned to key. Random selections of these characters will then descend
from the top of the MorseChallenger window. If they reach the bottom of
the window, they 'explode.' However, any letter that is keyed in as
Morse code before the letter reaches the bottom of the MorseChallenger
application window is 'defused' and disappears.

Difficulty level settings include the speed at which the letters
descend, and the number of letters in flight at the same time. To start
MorseChallenger:



```
rosrun morse_input morse_challenger.py
```



Note: Make sure that:

-   the MorseChallenger window and the Morser window do not overlap on
    the screen, and as usual,
-   that you make MorseChallenger the active window before beginning to
    Morse. That is, click somewhere on the MorseChallenger window
    surface before moving the mouse to the Morser window to start
    morsing.

## Use With Head Trackers

The Tracker 2000, and presumably other head tracker models, calibrate
the cursor position relative to head position when the head is turned
while the cursor is prevented from moving. For example, when the cursor
is flush against the right edge of the display, where it cannot move
further, users can continue to turn their heads to the right. This
motion effects a re-calibration of the cursor movement to the left.

Unfortunately, pushing the cursor against the Morse button edges
triggers the same calibration. To avoid this unwanted effect, the
operator should avoid pushing the cursor hard into the buttons. That is
as much as possible, the head should stop moving once the cursor reaches
the desired button edge.

When the cursor does get out of calibration from Morse entry, press the
right mouse button, and turn your head to the position that has you
expect the cursor to hover around the crosshair. Once the right mouse
button is released, the head tracker calibration is corrected.
