The TLDL version of the discourse server generates semantics in the form
of temporal logic (TL) and dynamic logic (DL) expressions. TL semantics
map onto goal expressions, while DL semantics map onto action
expressions. TL goals can include specification of when goal states
should hold (e.g., always, eventually, after some other goal is
achieved).

This package contains three nodes:

interpretCommand interpretCommandTester interpretCommandImplementor

The tester node simply takes your command line input and requests
interpretCommand to interpret it. The interpreter then interprets it.
The result is sent back as a string as well as being sent out as a
system topic message. The implementer listens on the correct topic
thread and tries to perform actions in the simulator based on commands.

Instead of trying to write a grammar for the dictionary files, I'll
just document a few examples.

reading: NP, N : \# x. x @ reading : \# x. x @ reading

This entry for the word "reading" indicates ("NP, N") that it can be
a NP or a N. The TL semantics come after the first colon. It helps to
keep in mind that these are simply lambda expressions. In this case, \#
x. x is just the identity function, and the "@" indicates that the
next expression is the value to be substituted. Similarly, the DL
semantics come after the second colon.

a: NP / N : \# x. x : \# x. x

The "a" entry just turns a N into a NP. The identity function ("# x.
x") is applied to the subsequent N, yielding that N.

take: S / NP : \# x. take(x) : \# x. take(x)

This entry for the word "take" indicates ("S / NP") that it
generates a S by consuming a NP. The TL and DL semantics are the same:
the lambda expression "# x. take(x)" is applied to the subsequent NP,
which is substituted for "x" in the expression. So, for example, if
the expression "take a reading" were input, the reductions would look
something like this:

(# x. take(x)) (# x. x) (# x. x @ reading)

(# x. take(x)) (# x. x) reading

(# x. take(x)) reading

take(reading)

transmit: S / NP , V : \# x. transmit(x) , \# x. x @ transmit : \# x.
transmit(x) , \# x. x @ transmit

The "transmit" entry is more complex, because "transmit" can assume
more than one role (S or V). The commas indicate disjunction, so the TL
will be either "# x. transmit(x)" or "# x. x @ transmit" depending
on the context (i.e., whether it's being treated as a S or a V). Given
the additional entries:

prepare: S / NP : \# x. prepare(x) : \# x. prepare(x)

to: NP / V : \# x. x : \# x. x

data: NP, N : \# x. x @ data : \# x. x @ data

the input "transmit data" would lead to reductions:

(# x. transmit(x)) (# x. x @ data)

(# x. transmit(x)) data

transmit(data)

while the input "prepare to transmit" would lead to:

(# x. prepare(x)) (# x. x) (# x. x @ transmit)

(# x. prepare(x)) (# x. x) transmit

(# x. prepare(x)) transmit

prepare(transmit)
