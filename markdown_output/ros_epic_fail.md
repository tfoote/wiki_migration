## Overview

Often, users create complex integration tests using ros tools, such as
the gazebo door demos. Unfortunately, due to bugs such as race
conditions, these tests often fail randomly. Because these failures
often happen at an extremely low frequency, it is virtually impossible
to track down the source of the failure. In addition, since the tests
fail randomly, there is often confusion as to whether a new failure is
due to a newly introduced bug or the latent random failure bug(s).
[ros_epic_fail](ros_epic_fail) helps track down random failure by
capturing bag files of the test failures. Users can then view the bag
files using ros tools and locate the source of the problem.

While one could simply add `rosbag record` commands to a failing test;
bag files from every run would be stored, and this would consume a great
deal of disk space. Ros_epic_fail only stores bags from actual test
failures, and limits the number of stored bags. This prevents excessive
disk space usage.

## The Trapper

The ros_epic_fail_trapper is a small python node that runs rosrecord to
capture bag files from tests.

## The Keeper

The keeper runs after all ros_epic_fail enabled tests have run and
stores the generated bag files from the trapper. These bag files are
stored in a specified directory.
