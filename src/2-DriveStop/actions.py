'''
Created on Jun 3, 2015

@author: gras
'''

import os
import sys

import kovan as link

import constants as c 
import servo
import time



def init() :
    # set print to unbuffered
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    print "starting 2-DriveStop"
    '''
    link.enable_servos()
    link.camera_open()
    time.sleep(5.0)
    servo.moveShutter( c.shutterOpen )
    '''
    print "Initialized"
    
def runMotors():
    for motorPort in range(0,4):
        speed = 100
        print "motor %i at speed %i", motorPort, speed
        link.motor(motorPort,speed)
    for minLeft in range(15,0,-1):
        print "%i minutes remaining", minLeft
        time.sleep(60)
    link.ao()           
        
def shutdown():
    print "finished"
    '''
    link.camera_close()
    '''
    link.ao()
    time.sleep(1.0)


    

    
def DEBUG() :
    print "DEBUG"
    link.camera_close()
    link.ao()
    exit()