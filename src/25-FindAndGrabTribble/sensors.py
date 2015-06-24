# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# sensors.py
'''
@author: Dead Robot Society
'''

from time import sleep

import kovan as link
import constants as c

#
# public camera routines
#
'''
    Returns the X position of the center of the red blob
    in number of pixels to left or right of center
    (left is negative)
    Returns -1000 if nothing seen
'''
def getRedPosition(blob=0):
    takePicture()
    # do we see anything?
    x = getRedBlobX(blob)
    if x == -1:
        return c.nothingSeen
    
    # is what we see large enough?
    size = getRedBlobSize(blob)
    print "X: ", x, "Size: ",size
    if size < c.minBlobSize:
        return c.nothingSeen
        
    # calculate how far to left or right
    # (left is negative)
    return (c.centerPoint - x)


#
# public ET routines
#
'''
    Returns True when the tribble is close enough to grab
    Returns False otherwise
'''
def pomInRange():
    i = readET()
    print "Dist: ", i
    if i > c.minDist:
        return True
    return False

#
# camera helper routines
#
def takePicture():
    link.camera_update()

'''
    
'''
def getRedBlobX(blob=0):
    return link.get_object_centroid(c.chanRed, blob).x

def getRedBlobSize(blob=0):
    return link.get_object_area(c.chanRed, blob)

#
# sensor helper routines
#
def readET():
    return link.analog_et(c.etSensor)


#
# initialization/shutdown routines
#
def init():
    if (link.camera_open()):
        pass
    else :
        link.camera_close()
        link.camera_open()
    # warm up the camera
    for _ in range(1, 10):
        takePicture()
        sleep(0.25)
        

def shutdown() :
    link.camera_close()