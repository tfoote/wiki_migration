The CRAM-language is a set of macros and functions on top of Common
Lisp. It is based on the ideas of Drew !McDermott's RPL. Programs in
the CRAM language are compiled down to native machine code and make
heavy use of the operating system's native multithreading
implementation.

## Installation and usage

It is suggested to use SLIME for interactive lisp development. If you
are using rosemacs, you can use `M-x slime-ros` to start up slime with
the version of sbcl that is distributed with the
[roslisp_support](roslisp_support) stack. If you have [roslisp](roslisp)
setup properly, you can load the cram language by invoking
`rosmake cram_language` and then evaluating
`(ros-load:load-system "cram_language" :cram-language)` in the slime
REPL. Change to the CPL package.

If you create a package that uses the CRAM language, don't use the
package COMMON-LISP but the package CPL instead. Example:


```
(defpackage cpl-user
    (:use :cpl))
```



Whenever you want to execute a CRAM language form in the REPL, you need
to enclose it in a `top-level` form: 

```
(top-level
  (par
    (format t "task 1~%")
    (format t "task 2~%")))
```



If you define a top-level plan (with `def-top-level-plan`) it contains
an implicit top-level. That means you can execute top-level plans
directly from the REPL, without top-level.

## Concepts

### Fluents

Fluents are proxy objects on arbitrary common lisp objects. They are
used as variables with changing value, allowing threads to observe the
variable and wait for specific changes. Fluents can be combined to
fluent networks which allow to express complex conditions. They are an
elegant and powerful way to add reactivity to a control program or
synchronize between threads.

With the function `(wait-for fluent)`, the current thread blocks if
`(value fluent)` is nil, until it is non-nil. The function `(wait-for
(pulsed fluent))` blocks until the value of fluent changes, or the
fluent gets pulsed.

The macro `(whenever fluent)` iteratively repeats the body except when
`(value fluent)` is nil before a new iteration. If the fluent is nil
at that time, whenever blocks until the fluent becomes true. The
whenever form never terminates unless `return` is called explicitly in
the body. See fluent pulse below for details on `(whenever (pulsed
fluent))`

Fluents are created with the function `make-fluent`. The fluent's value
can be accessed through the reader `value`, can be set with
`(setf (value fluent) <value>)`, and can be pulsed with
`(pulse fluent)`.

In the following example, a fluent is created and passed to a function
that, for instance, spawns a thread and executes a perception routine.
The result is put into the fluent's value. The main program sleeps
until it receives the value and prints it. 

```
(let ((fl (make-fluent :test-fluent :value nil)))
  (spawn-perception fl)
  (wait-for fl)
  (format t "Received value: ~a~%" (value fl))
```



We can extend the example to do the print until the fluent's value
changes to :done: 

```
(let ((fl (make-fluent :test-fluent :value nil)))
  (spawn-perception fl)
  (whenever (fl)
    (when (eq (value fl :done))
      (return-from whenever))
    (format t "Received value: ~a~%" (value fl))))
```

 Please note that the
`whenever` body is executed continuously, in a loop, as long as the
value of `fl` is non-NIL. If you want to execute the body only on
changes, you can use `pulsed`: 

```
(whenever ((pulsed fl))
  ...)
```

 see fluent
pulses below.

#### Fluent networks

Fluents can be combined to fluent networks. A fluent network updates its
value whenever one of the fluents it is constructed from changes its
value. In the CPL package, the most important comparison and math
operators (<, >, =, eq, eql, +, -, \*, /) are overloaded to construct
a fluent network whenever they are called with at least one fluent as
parameter. Example: 

```
(wait-for (> fl 20))
(wait-for (< (/ fl 3) 1))
```

 In addition, the logical
operators `fl-and`, `fl-or` and `fl-not` are defined. Please note that
they this is necessary since common lisp's logical operators have a
slightly different semantics. For instance, AND returns the first
non-nil value, whereas FL-AND returns a fluent containing T or nil.

To create user defined fluent operators, the combinator `fl-funcall` can
be used. It is similar to funcall, but whenever at least one of its
parameters is a fluent, a fluent network containing the result of the
function call with its parameters. It gets updated whenever one of the
parameter fluents changes its value. This is especially useful when a
fluent contains an instance of a CLOS object and the user wants to wait
for a condition defined on one of its slots. Example (pose-fl is a
fluent containing a pose object with the slots x, y and z:


```
(wait-for (fl-and (> (fl-funcall #'x pose-fl) 10)
                  (< (fl-funcall #'y pose-fl) 3)))
```



#### Fluent pulses

Whenever the value of a fluent is set to a different value, the fluent
is pulsed. To trigger a wait-for to wake up or a whenever body to
execute without actually changing the fluent's value, fluents can also
be pulsed with the `pulse` method. To construct a fluent network that
reacts if its parameter gets pulsed, the combinator `pulsed` can be
used.

The combinator `(pulsed fl)` has 3 optional keywords to deal with
"missed pulses" within a `(whenever)` block. Those are all pulses
that occured during execution of the `whenever` body. `whenever` in
combination with a pulse can be imagined as an infinite loop waiting for
a pulse, then executing the body. `pulsed` supports three different
ways to handle pulses that occur during the execution of a `whenever`
body:

-   `(pulsed fl :handle-missed-pulses :once)` means that any number of
    missed pulses cause exactly one additional execution of the
    `whenever` body. This is the default behavior.

```{=html}
<!-- -->
```
-   `(pulsed fl :handle-missed-pulses :never)` means that missed
    pulses don't cause another execution of the `whenever` body.

```{=html}
<!-- -->
```
-   `(pulsed fl :handle-missed-pulses :always)` means that the number
    of iterations of the `whenever` body exactly matches the number of
    missed pulses. That means that for every value change, the whenever
    body gets executed. Please note that fluents do not support a
    history of values.

Note: `(pulsed)` should never be used outside `(whenever (pulsed
\...))` or `(wait-for (pulsed \...))`. In particular the result of
`(pulsed)` should not be stored in variables or passed around, as the
nature and behavior of the return object is unspecified on purpose and
may change over time.

### Definition of Functions (Plans)

Although it is possible to call normal common lisp functions and methods
within a CRAM program, it is strongly encouraged to use
`def-cram-function`. The reason is that plans that are defined with
`def-cram-function` are transparent to the execution system. That
means, calls to them can be traced (automatic logging), and their code
can be replaced on the fly by transformation rules. In addition, they
can be referenced by the function `task` by specifying a code path. Top
level functions, i.e. functions that are intended to be called from the
lisp top level and not inside a plan are defined with the macro
`def-top-level-cram-function`.

`def-cram-function` uses the same syntax as defun, e.g.


```
(def-cram-function robot-at (location)
    "Attempts to move robot towards location. Succeeds once robot is at given location."
     ...)
```



Plans can be nested into each other. To execute a plan, a top-level
context is required, meaning either a plan defined with
`def-top-level-plan`, or running a plan using: 

```
(top-level
   (let ((location ...))
     (robot-at location)))
```



**TODO:** Explain code-tree and task hierarchy.

### Control Flow

The CRAM Language provides several macros for executing forms in
parallel and synchronize on them. All language constructs introduced
here have clear failure semantics. A sub-form can have status `:failed`,
`:succeeded` and `:evaporated`. `:failed` means that a common lisp
condition has been thrown and the form failed. `:succeeded` means that
the form terminated successfully. `:evaporated` means that the form has
been preempted because it became unnecessary (e.g. due to a failure of a
task running in parallel).

#### top-level

CRAM language forms must be executed in a top-level environment. Please
note that `def-top-level-plan` contains an implicit top-level form.

top-level forms cannot be nested.

#### Sequences and concurrency

When there are several independent functions to execute, different
combination types are possible, with respect to order vs. concurrency,
early success and failure handling. Cram defines 5 different grouping
concepts to deal with the meaningful combinations.

Functions can be called in sequence or in parallel. When called in
sequence, we can run them all, or until the first one succeeds. This is
captured by (seq) and (try-in-order).

When functions are called in parallel, we can fail as soon as one fails,
or only if all have failed. If we continue as long as none fails, we can
succeed (and stop all others) if one succeeded, or we can wait until all
succeeded. Those concepts are captured by (par), (pursue) and (try-all).

##### seq

Execute forms sequentially. This is essentially equivalent to Common
Lisp's `progn`. `seq` fails if one of its sub-forms fails and succeeds
when all succeed.

##### par

Execute forms in parallel. Fail if one fails, succeed after **all**
succeeded. Example: 

```
(par
  (park-left-arm)
  (park-right-arm))
```



##### pursue

Execute forms in parallel. Fail if one fails, succeed when **one**
succeeds. All other forms are evaporated when one form succeeds. This is
especially useful for implementing monitors or run code until a
condition holds: 

```
(top-level
  (par
    (format t "task 1~%")
    (format t "task 2~%")))
```

0 In the example above, the
form terminates successfully when the robot is at the waypoint.
Navigation commands to approach the waypoint are sent to the robot
repeatedly.

##### try-all

Perform concurrently. Fail if **all** fail, succeed if **one**
succeeded.

##### try-in-order

Perform in sequence like seq, but only fail if **all** fail, succeed
after **one** succeeded.

#### with-tags

#### with-task-suspended

#### partial-order

### Evaporation and unwind-protect

The concurrency constructs spawn new independent threads. In contrast to
other multi-threaded languages, cram allows errors to be propagated from
child threads to their parent threads seamlessly.

The consructs for concurrency all also allow implicit evaporation.
Meaning as soon as the construct (par, pursue, try) ends by either
success or failure, the other child threads are evaporated.

The evaporation of threads also allows the lisp construct
(`unwind-protect`), with which code blocks can have guard blocks that
get executed in any case (normal course of action, evaporation and
failure).

TODO: Describe whether code evaporation happens concurrently to
continuation of parent, or whether constructs block until all child
threads have evaporated.

### Exception Handling

#### fail

plan failures are generated and thrown using the (fail \...) function.
Fail is similar to Common Lisp's `error` but adds some special
handling of conditions that are a sub-type of `plan-failure`. These
should not cause Lisp to enter the debugger.

#### with-failure-handling

The `with-failure-handling` macro allows to wrap function calls so that
if a failure occurs, failure handling code is executed. E.g.:


```
(top-level
  (par
    (format t "task 1~%")
    (format t "task 2~%")))
```

1 In this case we monitor for failures of type
`trajectory-controller-failed`, and if they happen we call (retry)
meaning we just run the body again on each failure until we succeed.
`(move-arm-to-point ...)` is the body in this case.

### Goals

In Cram goals are a concept to ground plans in a first-order
representation. That allows to reason about the purpose of plans. A goal
is an expression that describes the semantics of the corresponding code.
For instance, the goal `(achieve ?occ)` indicates that the code only
succeeds if the system beliefs that it could make the occasion ?occ
hold. A more concrete example is `(achieve (loc ?obj ?loc))` which
indicates that the purpose of the code is to achieve that an object is
placed at a specific location.

Which kinds of occasions are needed for a platform depends on the domain
it operates in. It is up to the goal designer to decide which occasion
types to declare. To start with, a common choice could be a general
occasion like `(achieve <occasion>)`.

Declaring occasion types is done like this: 

```
(top-level
  (par
    (format t "task 1~%")
    (format t "task 2~%")))
```

2

TODO: Explain body options for declare-goal

Once an occasion type has been declared like above, goals can be defined
for that type like this: 

```
(top-level
  (par
    (format t "task 1~%")
    (format t "task 2~%")))
```

3 This uses a plan
defined like earlier on this page. (Technical detail: The syntax with
the question marks is specific to the pattern matching used. Since for
one occasion different goals can be defined, the actual goal is
determined during runtime using pattern matching.)

Instead of running the plan robot-at, we can that way make the robot
achieve this goal: 

```
(top-level
  (par
    (format t "task 1~%")
    (format t "task 2~%")))
```

4 Whether the 2d pose object
works with the goal depends on the implementation of the robot-at plan.

By structuring the robots plans as goals the executive framework gains
new meta-abilities, such as the robot being able to explain at any time
what purpose it is following, or handling of failures at runtime given
the context of current purposes.

## Further References

A clear and complete introduction is
[Tobias Christian Rittweiler's bachelor thesis on CRAM](https://common-lisp.net/~trittweiler/bachelor-thesis.pdf)
