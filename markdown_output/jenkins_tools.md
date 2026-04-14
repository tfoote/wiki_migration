## Overview

Jenkins Tools contains a set of command line tools to schedule, run and
debug scripts on a Jenkins cluster.

## Installation

After you\'ve set up the ros apt sources, you can simply install
jenkins-tools using apt: ```
sudo apt-get install python-jenkins-tools
```

## Chroot Tools

This package allows you to run scripts in a chroot environment, either
locally on your machine, or remotely on a Jenkins node. Both approaches
will run the script in exactly the same Ubuntu environment.

### run_chroot_local

This command line tool allows you to run a script in a chroot
environment, on your local machine. This can be useful when you want to
try out a new version of the script before you schedule it on Jenkins,
or when you want to find out why a script is failing on Jenkins.

Usage: ```
run_chroot_local ubuntu_distro arch workspace script [script_args]
```

Arguments:

-   \'\'\'ubuntu_distro\'\'\': the ubuntu distribution you want to run
    in your chroot. Examples are lucid, oneiric, precise, etc
-   \'\'\'arch\'\'\': the architecture you want to run in your chroot.
    You can either use \'amd64\' or \'i386\'. Note that when the base
    installation of your own system is 32 bit, you can\'t use the amd64
    option. When the base installation of your system is 64 bit, you can
    use both amd64 and i386.
-   \'\'\'workspace\'\'\': this is a local folder on your machine that
    will get mounted into the chroot. So it\'s pretty much a shared
    folder between your local machine and the chroot. When your script
    runs, it can store data in this workspace folder, and you\'ll have
    access to this data from your local machine, even when the chroot
    disappears.
-   \'\'\'script\'\'\': the name of the script you want to run. This
    must be a name of a script in the jenkins_scripts repository. You
    can check out a copy of this repo here at
    <https://github.com/ros-infrastructure/jenkins_scripts.git>
-   \'\'\'\[script_args\]\'\'\': a list of arguments for the script you
    are running.

Example: ```
run_chroot_local precise amd64 /home/user/workspace prerelease groovy common_msgs
```

Script Development: When you\'re developing a script in the
jenkins_scripts repository, you obviously don\'t want to commit every
little change to try it out. Therefore there is a special option to run
on a local copy of the jenkins_scripts repository. When you run the
run_chroot_local script, it will check out a copy of jenkins_scripts in
the workspace. You could start developing new code in this local
checkout, but your changes would be wiped out every time you run the
run_chroot_local script. To avoid the wipe, you can put a file called
\'run_debug_mode\' in the root of your workspace. When this file exists,
the jenkins_scripts repository will not get wiped. Make sure you commit
your changes before you remove the \'run_debug_mode\' file!

### run_chroot_jenkins_now

This command line tool allows you to run a script in a chroot
environment, remotely, on a Jenkins node. The script will be scheduled
immediately.

Usage: ```
run_chroot_jenkins_now ubuntu_distro arch job_name email script [script_args]
```

Arguments:

-   \'\'\'ubuntu_distro\'\'\': the ubuntu distribution you want to run
    in your chroot. Examples are lucid, oneiric, precise, etc
-   \'\'\'arch\'\'\': the architecture you want to run in your chroot.
    You can either use \'amd64\' or \'i386\'. Note that when the base
    installation of your own system is 32 bit, you can\'t use the amd64
    option. When the base installation of your system is 64 bit, you can
    use both amd64 and i386.
-   \'\'\'job_name\'\'\': a string you can freely choose, to create a
    unique name for your job on Jenkins. The resulting name will be:
    \'script-job_name-ubuntu_distro-arch\'
-   \'\'\'email\'\'\': the email address where Jenkins will send the
    script results to
-   \'\'\'script\'\'\': the name of the script you want to run. This
    must be a name of a script in the jenkins_scripts repository. You
    can check out a copy of this repo here at
    <https://github.com/ros-infrastructure/jenkins_scripts.git>
-   \'\'\'\[script_args\]\'\'\': a list of arguments for the script you
    are running.

Example: ```
run_chroot_jenkins_now precise amd64 groovy-common_msgs you@hidof.com prerelease groovy common_msgs
```

### run_chroot_jenkins_periodic

This command line tool allows you to run a script in a chroot
environment, remotely, on a Jenkins node. The script will be scheduled
periodically.

Usage: ```
run_chroot_jenkins_periodic ubuntu_distro arch job_name email period script [script_args]
```

Arguments:

-   \'\'\'ubuntu_distro\'\'\': the ubuntu distribution you want to run
    in your chroot. Examples are lucid, oneiric, precise, etc
-   \'\'\'arch\'\'\': the architecture you want to run in your chroot.
    You can either use \'amd64\' or \'i386\'. Note that when the base
    installation of your own system is 32 bit, you can\'t use the amd64
    option. When the base installation of your system is 64 bit, you can
    use both amd64 and i386.
-   \'\'\'job_name\'\'\': a string you can freely choose, to create a
    unique name for your job on Jenkins. The resulting name will be:
    \'script-job_name-ubuntu_distro-arch\'
-   \'\'\'email\'\'\': the email address where Jenkins will send the
    script results to
-   \'\'\'period\'\'\': when you want the script to run. Acceptable
    values are \'continuous\', \'nightly\', \'daily\', \'weekly\' or
    \'monthly\'.
-   \'\'\'script\'\'\': the name of the script you want to run. This
    must be a name of a script in the jenkins_scripts repository. You
    can check out a copy of this repo here at
    <https://github.com/ros-infrastructure/jenkins_scripts.git>
-   \'\'\'\[script_args\]\'\'\': a list of arguments for the script you
    are running.

Example: ```
run_chroot_jenkins_periodic precise amd64 groovy-common_msgs you@hidof.com nightly prerelease groovy common_msgs
```

### run_chroot_jenkins_vcs

This command line tool allows you to run a script in a chroot
environment, remotely, on a Jenkins node. The script will be scheduled
when a commit happens to a vcs repository.

Usage: ```
chroot_jenkins_vcs ubuntu_distro arch job_name email vcs uri branch script [script_args]
```

Arguments:

-   \'\'\'ubuntu_distro\'\'\': the ubuntu distribution you want to run
    in your chroot. Examples are lucid, oneiric, precise, etc
-   \'\'\'arch\'\'\': the architecture you want to run in your chroot.
    You can either use \'amd64\' or \'i386\'. Note that when the base
    installation of your own system is 32 bit, you can\'t use the amd64
    option. When the base installation of your system is 64 bit, you can
    use both amd64 and i386.
-   \'\'\'job_name\'\'\': a string you can freely choose, to create a
    unique name for your job on Jenkins. The resulting name will be:
    \'script-job_name-ubuntu_distro-arch\'
-   \'\'\'email\'\'\': the email address where Jenkins will send the
    script results to
-   \'\'\'vcs\'\'\': the type of vcs repository that is used to trigger
    this job. Acceptable values are \'git\', \'hg\' or \'svn\'.
-   \'\'\'uri\'\'\': the url of the vcs repository that is used to
    trigger this job.
-   \'\'\'branch\'\'\': the branch in the vcs repository that is used to
    trigger this job.
-   \'\'\'script\'\'\': the name of the script you want to run. This
    must be a name of a script in the jenkins_scripts repository. You
    can check out a copy of this repo here at
    <https://github.com/ros-infrastructure/jenkins_scripts.git>
-   \'\'\'\[script_args\]\'\'\': a list of arguments for the script you
    are running.

Example: ```
run_chroot_jenkins_vcs precise amd64 groovy-common_msgs you@hidof.com git https://github.com/ros-infrastructure/jenkins_scripts.git default prerelease groovy common_msgs
```

## Job Generation Tools

### Devel Jobs

This tool generates all the development regression tests for a given ros
distribution.

Usage: ```
generate_jenkins_devel ros_distro [--delete] [--run]
```

Arguments:

-   \'\'\'ros_distro\'\'\': the ros distribution you want to generate
    jobs for.
-   \'\'\'\--delete\'\'\': Delete all doc jobs for the distro specified
    that are no longer in the index.
-   \'\'\'\--run\'\'\': In addition to scheduling jobs to be triggered
    by commits, schedule a build of each repository immediately.

Example: ```
run_chroot_local ubuntu_distro arch workspace script [script_args]
```0

### Documentation Jobs

This tool generates documentation jobs for a given ros distribution. For
more information about how to add a documentation job to the index of
jobs used by this tool, please see this
[ page](Get Involved#Indexing_Your_.2A-ros-pkg_Repository_for_Documentation_Generation ).

Usage: ```
run_chroot_local ubuntu_distro arch workspace script [script_args]
```1

Options:

-   \'\'\'\--delete\'\'\': Delete all doc jobs for the distro specified
    that are no longer in the index.
-   \'\'\'\--run\'\'\': In addition to scheduling jobs to be run
    periodically on Jenkins, schedule a build of each repository
    immediately.

Arguments:

-   \'\'\'ros_distro\'\'\': the ros distribution you want to generate
    jobs for.

Example: ```
run_chroot_local ubuntu_distro arch workspace script [script_args]
```2

### Prerelease Jobs

This tool generates all the development regression tests for a given
release repository.

Usage: ```
run_chroot_local ubuntu_distro arch workspace script [script_args]
```3

Arguments:

-   \'\'\'ros_distro\'\'\': the ros distribution you want to generate
    jobs for.
-   \'\'\'distro_name\'\'\': the name of the distribution you want to
    generate jobs for.

Example: ```
run_chroot_local ubuntu_distro arch workspace script [script_args]
```4
