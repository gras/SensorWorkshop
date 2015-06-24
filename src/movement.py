# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# movement.py
'''
@author: Dead Robot Society
'''
from time import sleep 
import kovan as link
import constants as c



#
# motor routines
#
'''
    stops the create motors
'''
def stop() :
    link.create_stop()

'''
    starts to spin counter-clockwise
    default speed is 40 m/sec
'''
def spinLeft(speed=40) :
    link.create_spin_CCW(speed)

'''
    starts to spin clockwise 
    default speed is 40 m/sec
'''
def spinRight(speed=40) :
    link.create_spin_CW(speed)

'''
    starts to drive forward 
    default speed is 100 m/sec
'''
def forward(speed=100) :
    link.create_drive_straight(-speed)

'''
    drive forward and stop after a given time
    default speed is 100 m/sec
    default time is 5 sec
'''
def distance(speed=100, time=5.0) :
    link.create_drive_straight(-speed)
    sleep(time)
    link.create_stop()
'''
    starts to spin counter-clockwise
    default speed is 40 m/sec
'''
def left(speed=80) :
    link.create_spin_CCW(speed)
    sleep(0.1)
    link.create_stop()

'''
    starts to spin clockwise 
    default speed is 40 m/sec
'''
def right(speed=80) :
    link.create_spin_CW(speed)
    sleep(0.1)
    link.create_stop()


#
# servo routines
#
def armDown():
    moveServo(c.armPort, c.armDown, speed=10)

def armUp():
    moveServo(c.armPort, c.armUp, speed=10)

def clawOpen():
    moveServo(c.clawPort, c.clawOpen, speed=10)

def clawClosed():
    moveServo(c.clawPort, c.clawClosed, speed=10)

#
# servo helper routine
#
def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = link.get_servo_position( servo )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        link.set_servo_position( servo, i)
        sleep(0.010)
    link.set_servo_position( servo, endPos )
    sleep( 0.010 )

#
# initialization/shutdown routines
#
def init() :
    print "Turn on Create..."
    link.create_connect()
    link.create_full()
    link.set_servo_position(c.armPort, c.armUp)
    link.set_servo_position(c.clawPort, c.clawOpen)
    link.enable_servo(c.armPort)
    link.enable_servo(c.clawPort)
    print "...Ready!"
    
def shutdown() :
    link.disable_servos()
    link.create_stop()
    link.create_disconnect()
