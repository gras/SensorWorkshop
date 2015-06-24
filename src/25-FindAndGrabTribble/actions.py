# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# actions.py
'''
@author: Dead Robot Society
'''


from time import sleep

import movement as move
import sensors 

#
# Main routines
#

# rotate to the left, until a red pom is seen
def findTribble() :
    tribbleFound = 0
    move.spinLeft()
    while not tribbleFound :
        sleep(0.2)        
        pos = sensors.getRedPosition()
        print "Pos: ", pos
        if pos >  0:
            move.stop()
            tribbleFound = 1
    print "found Tribble..."

# rotate until the pom is centered
# then move a bit closer
# repeat until the pom is close enough to grab
def gotoTribble():
    tribbleNear = False
    while not tribbleNear:
        move.distance(80, 0.2)        
        centered = False
        while not centered:
            pos = sensors.getRedPosition()
            print "Pos: ", pos
            if pos > -10 & pos < 10:
                centered = True
            elif pos > 0:
                move.right()
            else:
                move.left()
        tribbleNear = sensors.pomInRange() 
    print "near tribble.."      

# rotate until the pom is centered
# then move a bit closer
# repeat until the pom is close enough to grab
def grabTribble():
    move.armDown()
    move.distance(50, 1.0)
    move.clawClosed()
    move.armUp()       
    move.clawOpen()
    print "grabbed tribble..."            
        
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