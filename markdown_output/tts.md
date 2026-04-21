## Overview

The `tts` ROS node enables a robot to speak with a human voice by
providing a Text-To-Speech service. Out of the box this package listens
to a speech topic, submits text to the Amazon Polly cloud service to
generate an audio stream file, retrieves the audio stream from Amazon
Polly, and plays the audio stream via the default output device. The
nodes can be configured to use different voices as well as custom
lexicons and SSML tags which enable you to control aspects of speech,
such as pronunciation, volume, pitch, speed rate, etc. A
[sample ROS application](https://github.com/aws-robotics/aws-robomaker-sample-application-voiceinteraction)
with this node, and more details on speech customization are available
within the
[Amazon Polly documentation](https://docs.aws.amazon.com/polly/latest/dg/what-is.html).

**Amazon Polly Summary**: Amazon Polly is a service that turns text into
lifelike speech, allowing you to create applications that talk, and
build entirely new categories of speech-enabled products. Amazon Polly
is a Text-to-Speech service that uses advanced deep learning
technologies to synthesize speech that sounds like a human voice. With
dozens of lifelike voices across a variety of languages, you can select
the ideal voice and build speech-enabled applications that work in many
different countries.

**Features in Active Development**:

-   Offline TTS

### License

The source code is released under an
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Kinetic
-   Lunar
-   Melodic
