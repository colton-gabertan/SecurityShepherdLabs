# WordPress vs. Kali Docker Setup

In order to simplify the installation and configuration of our at-home pentesting lab, CodePath has created and pre-configured Docker containers to help us get set up with a few simple keystrokes.
> For those of you who don't know, Docker is a service that allows developers to pre-configure packages with all the dependencies needed in order to successfully run a program or service. It runs at the kernel level and allows for extremely fast, light-weight, virtual environments in which you can do a multitude of things such as develop software and, in our case, set up a penetration testing lab for WordPress.

Our Docker containers will include:
* WordPress vulnerable server (hosted locally)
* A kali vm as root
* A mySql Server as a database

## Step 1: Getting Docker

Docker install links: 

* [Windows]
* [Mac OSX]

[Windows]: https://docs.docker.com/docker-for-windows/install/
[Mac OSX]: https://docs.docker.com/docker-for-mac/install/

> Windows 10 users, you must be running version 19041 or higher. Windows 11 users, you must be running version 21H2 or higher. WSL2 must also be installed to support Docker. For Mac OSX users, you must start up Docker from the CLI.

