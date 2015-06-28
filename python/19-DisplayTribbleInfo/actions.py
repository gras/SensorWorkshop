# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 18-DisplayTribbleInfo
# actions.py
'''
@author: Dead Robot Society
'''


import time as t

import kovan as link

import constants as c
import movement as move
import sensors 

#
# Main routines
#

def displayInfo() :
    print "Press the A button to exit"
    while not link.a_button_clicked() :
        sensors.camTakePicture()
        x = sensors.camGetBlobX(c.chanRed)
        size = sensors.camGetBlobSize(c.chanRed)
        print "X: ", x, "Size: ",size
        t.sleep(1.0)
    print "Stopping..."
        
#
# Helper functions
#

def init() :
    print "starting 25--FindAndGrabTribble"
    move.init()
    sensors.init()
    print "Initialized"
    
def shutdown() :
    move.shutdown()
    sensors.shutdown()
    print "finished"
          
def DEBUG() :
    print "DEBUG"
    shutdown()
    exit()