# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 2-DriveStop
# actions.py
'''
@author: Dead Robot Society
'''


import os
import sys
import time

import kovan as link

import movement as move



def init() :
    # set print to unbuffered
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    print "starting 2-DriveStop"
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