# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# sensors.py
'''
@author: Dead Robot Society
'''

import time

import kovan as link
import constants as c

#
# camera routines
#
def takePicture():
    link.camera_update()
    
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
def getRedBlobX(blob=0):
    return link.get_object_centroid(c.chanRed, blob).x

def getRedBlobSize(blob=0):
    return link.get_object_area(c.chanRed, blob)

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
        time.sleep(0.25)
        

def shutdown() :
    link.camera_close()