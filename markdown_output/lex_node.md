## Overview

The ROS `lex_node` node enables a robot to comprehend natural language
commands by voice or textual input and respond through a set of actions,
which an Amazon Lex Bot maps to ROS messages. Out of the box this node
provides a ROS interface to communicate with a specified Amazon Lex bot
(configured via lex_config.yaml) and requires configuration of AWS
credentials. The Amazon Lex bot needs to be defined with responses and
slots for customer prompts. A set of default slots and mappings are
demonstrated in the
[sample app](https://github.com/aws/aws-robomaker-sample-application-voiceinteraction)
and include actions as "Create <location_name>," "Go to
<location_name>" and "Stop." Additional guides on configuring bots
with are available at
[Getting Started with Amazon Lex](https://docs.aws.amazon.com/lex/latest/dg/getting-started.html).

Delivering a voice-enabled customer experience (e.g. "Robot, go to x")
will require dialog facilitation, wake word, and offline processing
which are not yet provided by this integration. A wake word would
trigger the dialog facilitation node to start recording and send the
audio to Amazon Lex, then prompt the user for more information should
Amazon Lex require it.

The ROS `lex_node` wraps the
[aws-sdk-c++](https://github.com/aws/aws-sdk-cpp) in a ROS service API.

**Amazon Lex Summary**: Amazon Lex is a service for building
conversational interfaces into any application using voice and text.
Amazon Lex provides the advanced deep learning functionality of
automatic speech recognition (ASR) for converting speech to text, and
natural language understanding (NLU) to recognize the intent of the
text, to enable you to build applications with highly engaging user
experiences and lifelike conversational interactions. With Amazon Lex,
the same deep learning technologies that power Amazon Alexa are now
available to any developer, enabling you to quickly and easily build
sophisticated, natural language, conversational bots ("chatbots").

### License

The source code is released under an
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Kinetic
-   Lunar
