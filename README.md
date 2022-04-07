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

Once installed you can run `docker --version` to ensure that everything ran correctly and that Docker is on your system.

<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/week07/dockerinstall.gif">

## Step 2: Getting the Images and Spinning Up The Containers

Another wonderful thing about Docker is that it heavily supports open source development and people can make their containers available for install and use to the general public. We will be pulling a githup repo that contains all of the necessary Docker files onto our machines. 

From there, all we have to do is spin it up and sit tight for a couple of minutes.

The first thing to do is create a directory in which we can hold all of the files for our lab this week. I've opted to create a codepath folder on my desktop. I recommend doing it this way so nothing gets lost, and we can keep all of our related files together. 

On windows:
```powershell
cd $HOME/desktop
mkdir codepath/kalivswp
cd wpvskali
```

In this directory, we can clone the repo like so
```
git clone https://github.com/0xrutvij/wpVSkali.git
```

After doing so, check if all of the files are in our `kalivswp` directory. Cloning the repository will create a new folder named `wpVSkali`. We can check the files with:
```powershell
cd wpVSkali
ls
```
