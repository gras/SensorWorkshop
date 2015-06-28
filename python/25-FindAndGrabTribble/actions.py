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
import sensor 

##################################
# public routines
##################################

'''
    rotate to the left, until a red pom is seen
'''
def findTribble() :
    print "findTribble()"
    tribbleFound = 0
    move.spinLeftNoStop()
    while not tribbleFound :
        sleep(0.2)        
        pos = sensor.getRedPosition()
        print "Pos: ", pos
        if pos >  0:
            move.stop()
            tribbleFound = 1
    print "found Tribble..."

'''
    rotate until the pom is centered
    then move a bit closer
    repeat until the pom is close enough to grab
'''
def gotoTribble():
    print "gotoTribble()"
    tribbleNear = False
    while not tribbleNear:
        move.forward(80, 0.2)        
        centered = False
        while not centered:
            pos = sensor.getRedPosition()
            print "Pos: ", pos
            if pos > -10 & pos < 10:
                centered = True
            elif pos > 0:
                move.spinRight()
            else:
                move.spinLeft()
        tribbleNear = sensor.pomInRange() 
    print "near tribble.."      

'''
    rotate until the pom is centered
    then move a bit closer
    repeat until the pom is close enough to grab
'''
def grabTribble():
    print "grabTribble()"
    move.armDown()
    move.forward(50, 1.0)
    move.clawClosed()
    move.armUp()       
    move.clawOpen()
    print "grabbed tribble..."            
        
          
##################################
# helper routines
##################################

'''
    This function allows us to stop the code
    for testing
'''
def DEBUG() :
    print "DEBUG"
    shutdown()
    exit()
    
##################################
# initialization/shutdown routines
##################################

'''
    This function announces the program and
    initializes the movement and sensor classes 
'''
def init(codeBase) :
    print "starting ", codeBase
    move.init()
    sensor.init()
    print "Initialized"
    
'''
    This function shuts everything down 
'''
def shutdown() :
    print "shutting down..."
    move.shutdown()
    sensor.shutdown()
    print "finished"
