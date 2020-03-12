# PSYCHE - IMIS
These are the instructions for setting up and running the "psyche-imis-camerabooth.py" application

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SETUP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
YOU CAN IGNORE THESE STEPS IF YOU'RE NOT ON A SYSTEM THAT IS ALREADY SETUP

This was created using Python3. The Raspbian OS should already have 3.7.3 installed.
	You can check if it is using the command: "python3 --version"

To get the camera feed and vision to appear in the GUI we used OpenCV2.
	run these commands: 	
			"sudo apt-get install python3-opencv"

Make sure you have a camera module connected that can be recognized by the Pi. As well as i2c. And remote GPiO
	You can make sure it is enabled using: "raspi-config" 
	
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXECUTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Currently you can start the application by going to the directory it is saved in.
	On this specific machine you can go to it using "cd /Desktop/PSYCHE-IMIS/"

RUN it by using this command: "python3 psyche-imis-camerabooth.py"

The "SNAPSHOT" button will save the current frame that is shown into the directory of the appplication
	The name of the file will be a .jpg named "sample-%d-%m-%Y_%H-%M-%S" (the current time)

The various buttons the exist allow you to control the orientation of the camera.

HAVE FUN!