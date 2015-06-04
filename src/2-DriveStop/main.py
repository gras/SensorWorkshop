'''
Created on Jun 3, 2015

@author: gras
'''
import actions as act

def main() :
    act.init()
    act.testMotors()
    #act.runMotors()
    #act.testCamera()
    act.shutdown()
    

if __name__ == '__main__':
    main()