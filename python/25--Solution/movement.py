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

##################################
# public routines
##################################

'''
    stops the create motors
'''
def stop() :
    link.create_stop()

'''
    starts to drive forward 
    default speed is 100 mm/sec
'''
def forwardNoStop(speed=100) :
    link.create_drive_straight(-speed)

'''
    drive forward and stop after a given time
    default speed is 100 mm/sec
    default time is 5 sec
'''
def forward(speed=100, time=5.0) :
    link.create_drive_straight(-speed)
    sleep(time)
    link.create_stop()

'''
    starts to spin counter-clockwise
    default speed is 40 mm/sec
'''
def spinLeftNoStop(speed=40) :
    link.create_spin_CCW(speed)

'''
    starts to spin clockwise 
    default speed is 40 mm/sec
'''
def spinRightNoStop(speed=40) :
    link.create_spin_CW(speed)

'''
    spin counter-clockwise and stop after a given time
    default speed is 80 mm/sec
    default time is 0.1 sec
'''
def spinLeft(speed=80) :
    link.create_spin_CCW(speed)
    sleep(0.1)
    link.create_stop()

'''
    spin clockwise and stop after a given time
    default speed is 80 mm/sec
    default time is 0.1 sec
'''
def spinRight(speed=80) :
    link.create_spin_CW(speed)
    sleep(0.1)
    link.create_stop()

'''
    Set the arm to the down position
'''
def armDown():
    moveServo(c.armPort, c.armDown, speed=10)

'''
    Set the arm to the up position
'''
def armUp():
    moveServo(c.armPort, c.armUp, speed=10)

'''
    Set the claw to the open position
'''
def clawOpen():
    moveServo(c.clawPort, c.clawOpen, speed=10)

'''
    Set the claw to the closed position
'''
def clawClosed():
    moveServo(c.clawPort, c.clawClosed, speed=10)


##################################
# helper routines
##################################

'''
    The function moves the a servo slowly
    * speed of 1 is slow
    * speed of 2000 is fast
    * speed of 10 is the default
'''
def moveServo( servo, endPos, speed=10 ) :
    now = link.get_servo_position( servo )
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        link.set_servo_position( servo, i)
        sleep(0.010)
    link.set_servo_position( servo, endPos )
    sleep( 0.010 )

##################################
# initialization/shutdown routines
##################################

'''
    setup the create and enable the servos
'''
def init() :
    print "Turn on Create..."
    link.create_connect()
    link.create_full()
    link.set_servo_position(c.armPort, c.armUp)
    link.set_servo_position(c.clawPort, c.clawOpen)
    link.enable_servo(c.armPort)
    link.enable_servo(c.clawPort)
    print "...Ready!"
    
'''
    disable the servos and disconnet the create
'''
def shutdown() :
    link.disable_servos()
    link.create_stop()
    link.create_disconnect()
