Proser creates a top level X window in which users can type. The
application provides statistical word completion suggestions. The
suggestions are displayed on five buttons at the top of the window. Two
methods are available to select one of the suggestions: Click the
respective onscreen button, or type one of F5-F9. Completion is based on
the word_completion package, which uses a frequency-ranked 6000 word
dictionary.

![](attachment:proser.png)

A Copy button copies the entire typed text into the X cut buffer (a.k.a.
clipboard), from where it may be pasted into any other window.

A special link exists between Proser and SpeakEasy. Proser provides two
SpeakEasy related buttons: 1. Erase the SpeakEasy text display 2. Send
the entire Proser window text to SpeakEasy and have it spoken by the
currently selected voice. The SpeakEasy window may be in a minimized
state during this operation.

Users may type their text from a physical, or onscreen keyboard or from
the [morser_input](http://ros.org/wiki/morse_input) package.
