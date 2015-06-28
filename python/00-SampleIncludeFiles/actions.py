# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 00-SampleIncludeFiles
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
    I like to document where the robot is when this
    action starts.  For example:
    outside the startbox, facing North    
'''
def getOutOfStartBox() :
    print "getOutOfStartBox()"
    move.forward() 
    sleep(2.0)       

'''
    tell the world what this function does
'''
def doSomething() :
    print "doSomething()"
    move.forwardNoStop() 
    move.armDown()
    move.armUp()
    move.stop()       
    
          
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
