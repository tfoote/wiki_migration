## Overview

This package contains regression tests for
[qualification](qualification) and [life_test](life_test). It has no
supported ROS or code API.

## Invent Submit Testing

Most tests in this package run during the \"make test\" command to this
package. Two scripts must be run manually. These scripts test that
submitting data to Invent works properly.

-   \`test/test_invent/qual_invent_submit.py\` - Tests that
    qualification data loads properly.
-   \`test/test_invent/test_logger_invent_submit.py\` - Tests that Test
    Manager data loads to Invent properly.
