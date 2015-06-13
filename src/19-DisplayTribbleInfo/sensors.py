# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 18-DisplayTribbleInfo
# sensors.py
'''
@author: Dead Robot Society
'''

import kovan as link

def camTakePicture():
    link.camera_update()

def camGetBlobX(color, blob=0):
    return link.get_object_centroid(color, blob).x

def camGetBlobSize(color, blob=0):
    return link.get_object_area(color, blob)

def init() :
    if ( link.camera_open() ) :
        pass
    else :
        link.camera_close()
        link.camera_open()

def shutdown() :
    link.camera_close()