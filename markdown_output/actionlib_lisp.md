# Overview

actionlib_lisp is a native implementation of [actionlib](actionlib) in
Common Lisp. It provides a simple server and a client. In contrast to
the implementations of actionlib in C++ and Python which provide a
simple action client/server and a complex one, the lisp equivalent
provides only one server and client implementation. The server is
similar to the simple action server and the client is a little bit more
powerful than the simple action client but not as complex as the complex
C++ equivalent.

# Client

## API

The interface consists of the following methods:

-   \`(make-action-client action-name action-type)\` constructs a new
    action client on the action named \`action-name\` with type
    \`action-type\`.

```{=html}
<!-- -->
```
-   \`(wait-for-server action-client &optional timeout)\` waits for the
    server to appear. If \`timeout\` is set and expires, returns
    \`NIL\`, otherwise returns \`T\`.

```{=html}
<!-- -->
```
-   \`(send-goal client goal &optional done-cb feedback-cb active-cb
    state-change-cb)\`: Sends a goal to the action server and returns a
    corresponding goal handle. The following parameters can be
    specified:

```{=html}
<!-- -->
```
-   \`client\` is an instance of \`ACTION-CLIENT\`.

```{=html}
<!-- -->
```
-   \`done-cb\` is a function that takes exactly two parameters, the
    final status and the result of the goal. It is executed when the
    execution of the goal terminated.

```{=html}
<!-- -->
```
-   \`feedback-cb\` is a function that takes exactly one parameter, the
    feedback message of the goal. It is executed whenever feedback for
    that specific goal is received.

```{=html}
<!-- -->
```
-   \`active-cb\` is a function with no parameters. It is executed when
    the goal turns active, i.e. is accepted by the server.

```{=html}
<!-- -->
```
-   \`state-change-cb\` is a function with one parameter that is called
    whenever the state of the goal transitions. The parameter is
    indicating the new status. Please note that this state is the the
    simple client state, i.e. either :pending, :active or :done. A done
    transition can be performed \_before\_ a result has been received.

```{=html}
<!-- -->
```
-   \`(cancel-goal goal-handle)\` cancels the goal bound to
    \`goal-handle\`

```{=html}
<!-- -->
```
-   \`(wait-for-result goal-handle &optional timeout)\` waits for the
    goal to terminate and send a result message. It returns two values,
    the result message and the corresponding action status (:done,
    :preempted, :lost or :aborted).

```{=html}
<!-- -->
```
-   \`(send-goal-and-wait client goal &key exec-timeout result-timeout
    feedback-cb)\`: Sends a goal to the action server and waits until
    termination of the goal. It returns two values, the result message
    and the status of the goal, similar to \`wait-for-result\`.
    Additionally, every received feedback message raises the signal
    \`feedback-signal\` which is connect to a restart \`abort-goal\`.
    This mechanism is the intended way of cancelling a running action
    based on a feedback message.

```{=html}
<!-- -->
```
-   \`client\` is an instance of ACTION-CLIENT.

```{=html}
<!-- -->
```
-   \`goal\` is the goal message to be sent

```{=html}
<!-- -->
```
-   \`exec-timeout\` specifies the timeout for execution of the goal

```{=html}
<!-- -->
```
-   \`result-timeout\` specifies the maximal time between status
    transition of the goal to :done and the reception of the result
    message.

```{=html}
<!-- -->
```
-   \`feedback-cb\` callback that takes exactly one argument, the
    feedback message. It is executed whenever a feedback message is
    received. Please note that the feedback callback is not executed in
    the subscriber-thread of the feedback topic but in the current
    thread that called \`send-goal-and-wait\`.

```{=html}
<!-- -->
```
-   \`(call-goal client goal &key timeout result-timeout feedback-cb)\`:
    deprecated version of \`send-goal-and-wait.

```{=html}
<!-- -->
```
-   \`(connected-to-server client)\` returns \`T\` if the client is
    connected to a server.

```{=html}
<!-- -->
```
-   \`(make-action-goal client &rest args)\`: macro to construct a goal
    message. \`client\` is the action client. The rest of the parameters
    are similar to [roslisp](roslisp)\'s \`make-msg\`, i.e. are used to
    specify the value of message slots.

## Example

This example shows how to construct an action client for the fibonacci
action of the actionlisp_tutorials package, send a goal to it and wait
for the result.

```
(defparameter *ac* (make-action-client "/fibonacci" "actionlib_tutorials/FibonacciAction"))

(send-goal-and-wait *ac* (make-action-goal *ac* :order 10) :exec-timeout 20 :result-timeout 0.5)
```

To run it, you need to have the actionlib-lisp and
actionlib_tutorials-msg loaded and be in a package that uses the
actionlib package.

# Server

The server is similar to the C++ simple action server. It can handle
only one goal at a time and if another goal is received while the server
is processing an old goal, it is preempted and the new goal is executed.

## API

-   \`(start-action-server action-name action-type exec-callback &key
    separate-thread)\` starts an action server with name \`action-name\`
    and type \`action-type\`. Whenever a goal is received, the callback
    with name \`exec-callback\` is executed. If \`separate-thread\` is
    non-NIL, spawns a new thread in which the server is run.

```{=html}
<!-- -->
```
-   \`(def-exec-callback name args &body body)\`: A macro for defining
    actionlib execution callbacks. It works like defun, except

1\. The argument list is treated like the argument list of with-fields:
it binds (possibly nested) fields of the goal object

2\. The forms \`preempt-current\`, \`succeed-current\`,
\`abort-current\`, \`cancel-request-received\` and \`publish-feedback\`
can be used inside \`body\`

3\. If we reach the end of the body without a dynamic nonlocal exit
(i.e., caused by preempting, aborting, or succeeding), an error is
signalled.

-   \`(succeed-current &rest args)\`: macro that succeeds the current
    goal. \`args\` is similar to the arguments \`make-msg\` takes and is
    used to construct the result message.

```{=html}
<!-- -->
```
-   \`(abort-current &rest args)\`: macro that aborts the current goal.
    \`args\` is similar to the arguments \`make-msg\` takes and is used
    to construct the result message.

```{=html}
<!-- -->
```
-   \`(preempt-current &rest args)\`: macro that preempts the current
    goal. \`args\` is similar to the arguments \`make-msg\` takes and is
    used to construct the result message.

```{=html}
<!-- -->
```
-   \`(publish-feedback &rest args)\`: macro that constructs and sends a
    feedback message. \`args\` is similar to the arguments \`make-msg\`
    takes and is used to construct the feedback message.

```{=html}
<!-- -->
```
-   \`(cancel-request-received)\` returns \`T\` if the current goal is
    requested to preempt.

## Example

This example shows how to implement a simple fibonacci action server.
```
(def-exec-callback fib-callback (order)
  "This function takes in the FibonacciGoal message and pursues the action."
  (ros-debug (fib callback) "entering callback with goal ~a" order)
  (let ((a 1) (b 1) (seq (make-array 0 :adjustable t :fill-pointer 0)))
    (dotimes (i order)
      (when (cancel-request-received)
        (ros-debug (fib callback) "goal ~a canceled" order)
        (preempt-current :sequence seq)) ;; Note that this exits the callback
        
      (psetq a b b (+ a b))
      (vector-push-extend a seq) 
      (ros-debug (fib callback) "publishing feedback for goal ~a" order)
      (publish-feedback :sequence seq)
      (sleep 1.0))
    (ros-debug (fib callback) "succeeding on goal ~a" order)
    (succeed-current :sequence seq)))

      
(defun fib-server ()
  (with-ros-node ("fib")
    (start-action-server "fibonacci" "actionlib_tutorials/FibonacciAction" #'fib-callback)))
```
