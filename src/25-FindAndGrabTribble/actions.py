# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# actions.py
'''
@author: Dead Robot Society
'''


import os
import sys
import time

import kovan as link

import movement as move
import sensors 



def init() :
    print "starting 25--FindAndGrabTribble"
    link.create_connect()
    link.create_full()
    sensors.init()
    print "Initialized"
    
def driveStop():
    
    time.sleep(60)
    link.ao()           
        
def shutdown():
    print "finished"
    link.ao()
    time.sleep(1.0)


    

    
def DEBUG() :
    print "DEBUG"
    link.camera_close()
    link.ao()
    exit()