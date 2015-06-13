# Making Sense of Sensors Workshop
# Educators Edition 2015
#
# 25-FindAndGrabTribble

# main.py
'''
@author: Dead Robot Society
'''
import actions as act

def main() :
    act.init()
    act.findTribble()
    act.shutdown()
    

if __name__ == '__main__':
    import os
    import sys
    # set print to unbuffered then call main()
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()