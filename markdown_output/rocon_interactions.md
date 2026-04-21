## Overview

Rocon interactions are designed to fill a hole in the ros ecosystem for
the human user/developer. They address the following problems:

-   How can I **interact** with this running ros system?
-   How can I easily configure (**params** and **remaps**) android and
    web apps?
-   How can I filter the set of interactions for a particular kind of
    user (e.g. dev, admin, user)?

Interactions can be one of any number of means of connecting **you**,
with your ros system. It could be as simple as finding documentation,
running monitoring programs, introspecting the system or directly
interacting with some part via a qt, android or web app.

For a ros environment, the problem isn\'t so dramatic. You can usually
poke around the documentation and installed packages and roslaunchers,
but if your project becomes sufficiently complex, you\'ll find yourself
having to either wade through documentation (some of which may be out of
date) and a maze of launchers (some of which may no longer be relevant,
or even work).

For android and web apps, the situation is difficult since you generally
don\'t have a tool like roslaunch to aid you in customising the
configuration for your application (parameters and remappings). Rocon
interactions is also designed to help with that.

  -- -------------------------------------------------------------------------------------------------- --
     \<style=\"text-align:center;\" tablewidth=\"100%\"\>![\|width=100%](attachment:interactions.png)   
  -- -------------------------------------------------------------------------------------------------- --

## Goal

Rather than require the user to work out where everything is, we\'d like
to shift that responsibility to the developer. Since he already knows
the ins and outs of what is available, he is the best person to expose
that information.

## Tutorials

## Specifications

### Entity Relationship Diagram

The diagram below visualises how the interactivity specifications
(bottom) are served by an interactions node (middle) through remocons on
different platforms to launch a wide variety of applications (top).

![Entity Relationship\|width=100%](https://docs.google.com/drawings/d/1kcbfnfhJBIS38HrusW8DdXkpln4f3hgzwiBxy5ZFc5E/pub?w=896&h=1058)

### Code Specifications

-   [Interaction Node RosApi](http://docs.ros.org/hydro/api/rocon_interactions/html/rosapi.html)
-   [Interaction YAML Specification](http://docs.ros.org/hydro/api/rocon_interactions/html/specification.html)

## Roadmap

-   [Current Status and Future Work](rocon_interactions/Roadmap)
