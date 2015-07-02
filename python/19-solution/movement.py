# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 18-DisplayTribbleInfo
# movement.py
'''
@author: Dead Robot Society
'''
import time 
import kovan as link


def init() :
    link.create_connect()
    link.create_full()
    
def shutdown() :
    link.create_stop()
    link.create_disconnect()


def forward(speed=100) :
    link.create_drive_straight(speed)
    time.sleep(50)
    link.create_stop()

def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = link.get_servo_position( servo )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        link.set_servo_position( servo, i)
        time.sleep(0.010)
    link.set_servo_position( servo, endPos )
    time.sleep( 0.010 )