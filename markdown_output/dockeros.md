# dockeros

Simply running ros nodes in docker containers on remote robots.

This is supposed to deliver tools to use the methods of **edge
computing** for ROS enabled robots. These methods include fast and
seamless deployment of software to edge devices (i.e. robots, and
others).

The **dockeros library** is designed to create and update docker images
for ros packages. There is a CLI to use these capabilities in your
development lifecycle that makes use of these tools in a client-server
structure.

## Media

### Video

[![video](https://camo.githubusercontent.com/7bed72d77c3b76b94516e2ac5d1a75556849facc/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f556264633936476b4f334d2f312e6a7067)](https://www.youtube.com/watch?v=Ubdc96GkO3M)

*Presentation at ROS Industrial Conference 2018*

### Podcast

[![podcast](https://camo.githubusercontent.com/26d9add454e04c0825b4e35bea837e3f277a5313/68747470733a2f2f6173736574732e6c696273796e2e636f6d2f7365637572652f636f6e74656e742f32393238323537392f3f6865696768743d39302677696474683d3930)](https://www.theconstructsim.com/rdp-034-docker-ros-dockeros-christian-henkel/)

*Podcast with Ricardo Tellez*

## Prerequesits

### On your PC (the Server)

The python packages required by the server can be installed via pip
install -r requirements.txt. To install docker, you can use
[this](https://docs.docker.com/engine/installation/linux/ubuntu/).

#### Optional: Registry

Without a registry, you will need to build the images on the robot they
should run on. If you want to build them in a central place (the
server), you need to run a docker registry on that server: docker run -d
-p 5000:5000 \--name registry registry. You can also use the
unsafe_registry in this repository. It will allow CORS (which is why it
is called unsafe).

### On the Robot (Client)

On the robot you need to have a
[docker deamon](https://docs.docker.com/edge/engine/reference/commandline/dockerd/)
running with an accesible API. To install docker, you can use
[this](https://docs.docker.com/engine/installation/linux/ubuntu/). A
good way to do this on systems running systemd is can be found
[here](https://www.campalus.com/enable-remote-tcp-connections-to-docker-host-running-ubuntu-15-04/).
We strongly recommend to use
[TLS for your deamons socket](http://lnr.li/60LYw/)

## The CLI

```
usage: dockeros [-h] [-e | -i HOST:PORT] [-f DOCKERFILE] [-n]
                {build,run,stop,push} ...

Simply running ros nodes in docker containers on remote robots.

positional arguments:
  {build,run,stop,push}
                        build: Creates an image that can run roscommand
                        run: Runs an image with your_roscommand (and builds it first)
                        stop: Stops image that runs that command
                        push: Push image to predefined registry
  roscommand            Everything after the subcommand will be interpreted as the ros command to be run in your image

optional arguments:
  -h, --help            show this help message and exit
  -e, --env             use the existing docker environment (see https://dockr.ly/2zMPc17 for details)
  -i HOST:PORT, --ip HOST:PORT, --host HOST:PORT
                        set the host (robot) to deploy image to
  -f DOCKERFILE, --dockerfile DOCKERFILE
                        use a custom Dockerfile
  -n, --no-build        dont (re-)build the image before running
```
[![screencast of dockeros run](https://github.com/ct2034/dockeROS/raw/master/doc/dockeros_run.gif)](https://github.com/ct2034/dockeROS/blob/master/doc/dockeros_run.gif)

## Contribution

All contributions are welcome. Especially important is at the moment:

### Testing

Please open issues for all problems you encounter. Please make sure,
that your problem is reproducible though: Add the rosdistro, package,
exact command and Dockerfile (if applicable) that you are using

## Troubleshooting

### Registry with http

When you get this error: {\"errorDetail\":{\"message\":\"Get
<https://YOUR_REGISTRY:5000/v2/>: http: server gave HTTP response to
HTTPS client\"},\"error\":\"Get <https://YOUR_REGISTRY:5000/v2/>: http:
server gave HTTP response to HTTPS client\"} while trying to push:

Add the server to your unsafe registries in daemon.json (default at
/etc/docker/daemon.json )

```
"insecure-registries":["YOUR_REGISTRY:5000"]
``` and restart your docker deamon.
```
sudo systemctl restart docker
```
