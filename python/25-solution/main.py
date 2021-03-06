# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble
# main.py
'''
@author: Dead Robot Society
'''

import actions as act

##################################
# main routine
##################################

'''
    This routine controls everything that happens.
    Remember to start with act.init("program name")
    and end with act.shutdown()  
'''
def main() :
    act.init("25--FindAndGrabTribble")
    act.findTribble()
    act.gotoTribble()
    act.grabTribble()
    act.shutdown()
    
    
##################################
# initialization/shutdown routines
##################################
'''
    This chunk of code sets print output to unbuffered
    (so that print statements are displayed in real-time)
    then calls main() to start the program

'''
if __name__ == '__main__':
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()