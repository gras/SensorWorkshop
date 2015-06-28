# 00-SampleIncludeFiles
##The goal of this discussion is to understand the benefits
of having multiple files, rather than putting all of your
code in a big steaming pile inside of a single file.

**Suggested File:**
* main - starting point of your program.  It contains the high level commands 
that you want to accomplish.
* actions - a set of functions that move the robot.  Good names start with verbs like:
** getOutOfStartBox()
** moveToMesa()
** grabBotGal()
* movement - lower level commands that run motors and move servos.
* sensor - lower level commands that interact with the camera and other sensors.
* constants - a common file that specifies all of the settings needed for your robot.
