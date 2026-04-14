# Deployment for Connected Robotics

The deployment package aims to deliver an easy deployment and onboarding
process to the Connected Robotics platform. It consolidates a few
technologies that allow to automate the process of provisioning the
required architecture in the local and cloud environments.

## Infrastructure as code deployment base

### Robot onboarding

Onboarding of a new robot requires an Onboarding file that may be
available in guide mentioned in the link. If your robot is in this list
you may use this template and just adjust it to the minor changes you
may have. If your robot, however, is not on the list, you will have to
generate the onboarding template before. This template is a json that
needs to be included in the body of the http request. Download the
script and run it in your robot: The guide for robot onboarding can be
found here:
<https://github.com/5G-ERA/middleware/blob/main/docs/User/Onboarding/Robot.md>

### Network Application onboarding

This section shows how to deploy a Network Application to the Middleware
system. Essentially, this is the execution of robotics tasks that have
been previously onboarded. So, for the deployment of a network
application, the taskid containing the app to be deployed is necessary.
Follow the tutorial:
<https://github.com/5G-ERA/middleware/blob/main/docs/User/Onboarding/Network%20Application%20Onboarding.md>

### Cloud Edge onboarding

For the middleware to plan optimal network application placement, it is
important to import the network topology into the system. This section
shows how to create a new Cloud or edge entity in the Redis backend of
the Middleware.

Adding a new entry in the Middleware topology allows Middleware to
better optimize the resource and task planning to provide the best
network capabilities to the Robot. Thanks to this, the Network
Application placement can be adjusted to specific needs like low latency
network thanks to the closer placement from the Robot or specific
network slice requirement (upcoming!). The full guide on cloud and edge
onboarding can be found here :
<https://github.com/5G-ERA/middleware/blob/main/docs/User/Onboarding/Cloud%20Onboarding.md>

## AWS deployment with Terraform

The Terraform package aims to deliver a simplified onboarding process of
the Middleware working under the private cloud provider AWS. It
automates the deployment process of the required architecture that will
be ready for the Middleware deployment. The package provisions required
VPC with public-private subnet architecture and deploys the Kubernetes
EKS Cluster in the subnets. Additionally, the Kubernetes cluster is
configured already to be ready to deploy the Middleware with all
required security features.

## Micro K8s deployment

The Microk8s deployment allows provisioning the Middleware in the local
Edge locations. It is the local Kubernetes cluster that will allow quick
onsite processing by utilising all the capabilities provided by the
platform.
