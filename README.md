# DockerDemo
This repo shows the basics of Docker by letting you run a container that shows a basic GUI. If I understand correctly, we could run this exact same code on a Raspberry Pi and things would look the exact same. Below are the instructions to make the code in this repository work. 

## Clone the repo
Assuming you already have git installed (if not, go do that. It's easy), navigate to where you would like to put this code, and run this command:

```
git clone https://github.com/elijahparker000/DockerDemo.git
```
Assuming things went well, you should be able to navigate to that directory in VS Code or whatever editor you prefer and see all the files from this repo.

## Install VcXsrv
It's a little annoying that you have to do this, but visit this link:

https://sourceforge.net/projects/vcxsrv/

and download and install the software. This will allow the Docker container access to your Windows screen when it's running. I'm pretty sure Linux comes with this sort of software, so it wouldn't be a problem with Raspberry Pi. I think once you've installed this software you need to go to your Desktop and open the XLaunch application and step through the menu that comes up to actually allow Docker to use this properly.

## Install Docker
Finally, navigate to this link:

https://docs.docker.com/desktop/install/windows-install/

and install Docker. Docker allows us to build containers that the code runs inside. In theory, any system that supports Docker will run any given Docker container in the exact same way which would be great for us as we develop software.
