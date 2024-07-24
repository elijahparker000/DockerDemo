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

and install Docker. Docker allows us to build containers that the code runs inside. In theory, any system that supports Docker will run any given Docker container in the exact same way which would be great for us as we develop software. Once you've installed Docker, navigate to the directory with all of this code in it and run the following commands on your terminal:

```
docker build -t my_python_app .
docker run -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/dri --device /dev/video0 --privileged my_python_app
```

The first command builds the Dockerfile. It'll take a minute to run, and you'll see lots of blue text on the terminal as it goes through all the steps. It'll put a basic version of Ubuntu in the container, install Python in the container, install necessary Python libraries in the container, and a couple other things. 

The second command actually runs the container. If all is well, you should see this:

<img width="219" alt="GUI" src="https://github.com/user-attachments/assets/17bb6383-63b6-4afa-b180-e451808d1453">

Click the button for an inside joke :)

