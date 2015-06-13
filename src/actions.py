# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# actions.py
'''
@author: Dead Robot Society
'''


import time as t

import movement as move
import sensors 

#
# Main routines
#

def findTribble() :
    tribbleFound = 0
    while not tribbleFound :
        t.sleep(0.5)        
        pos = sensors.getRedPosition()
        print "Pos: ", pos
        tribbleFound = 1
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