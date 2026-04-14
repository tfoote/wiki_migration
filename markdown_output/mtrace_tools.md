## Introduction

When pr2_etherCAT drivers detect certain types of motor problem, they
will publish an ethercat_hardware/MotorTrace message. The message
contains a trace of motor voltage, current, position, and speed from the
second before the motor halted.

With tools from this stack its possible to look at these motor traces to
get a better understanding of what was happening with the motor leading
up to the error condition.

See the [ Tutorials](mtrace_tools/Tutorials ) for usage examples.
