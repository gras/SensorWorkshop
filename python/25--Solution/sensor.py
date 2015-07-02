# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# sensor.py
'''
@author: Dead Robot Society
'''

from time import sleep
import kovan as link
import constants as c

##################################
# public routines
##################################

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

##################################
# helper routines
##################################

'''
    This function takes a picture which
    updates all of the blob values
'''
def takePicture():
    link.camera_update()

'''
    This function returns the X value of the specified red blob
    If a blob is not specified, it defaults to 0, which is the largest red blob
'''
def getRedBlobX(blob=0):
    return link.get_object_centroid(c.chanRed, blob).x

'''
    This function returns the size of the specified red blob
    If a blob is not specified, it defaults to 0, which is the largest red blob
'''
def getRedBlobSize(blob=0):
    return link.get_object_area(c.chanRed, blob)

'''
    This function returns the the distance seen by the ET
'''
def readET():
    return link.analog_et(c.etSensor)

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

##################################
# initialization/shutdown routines
##################################

'''
    This function starts the camera and
    "warms it up" by taking ten fake photos
'''
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
 
'''
    This function shuts down the camera
    (failure to do so can cause the LINK to
    hang during the next run!)
'''
def shutdown() :
    link.camera_close()
    