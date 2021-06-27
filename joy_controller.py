import pygame
from pygame.locals import *
import time
from server import move, RPIservo
 
def main(joys) :
    pygame.init()
    print("Joystick Name: " + joys.get_name())
    print("Number of Button : " + str(joys.get_numbuttons()))
    print("Number of Axis : " + str(joys.get_numaxes()))
    print("Number of Hats : " + str(joys.get_numhats()))
    
    max_vel = 100
    max_angle = 0

    scGear = RPIservo.ServoCtrl()
    scGear.moveInit()

    P_sc = RPIservo.ServoCtrl()
    P_sc.start()

    T_sc = RPIservo.ServoCtrl()
    T_sc.start()

    H_sc = RPIservo.ServoCtrl()
    H_sc.start()

    G_sc = RPIservo.ServoCtrl()
    G_sc.start()


    while True:
        # PS4
        turn = round(joys.get_axis(0),1)
        forward = round(joys.get_axis(1),1)
        yaw = round(joys.get_axis(2),1)
        pitch = round(joys.get_axis(5),1)
        
        print("forward: {:.1f}".format(forward))
        print("turn: {:.1f}".format(turn))
        print("yaw: {:.1f}".format(yaw))
        print("pitch: {:.1f}".format(pitch))

        vel = max_vel * forward
        direction = "no"
        if(vel < -0.1):
            direction = "forward"
        elif vel > 0.1:
            direction = "backward"
        move.move(abs(vel), direction)

        if abs(turn) > 0.1:
            turn_angle = max_angle * (-turn)
            scGear.moveAngle(0, turn_angle)

        if yaw < 0.5:
            P_sc.singleServo(1, 1, 3)
        elif yaw > 0.5:
            P_sc.singleServo(1, -1, 3)

        if pitch < 0.5:
            T_sc.singleServo(1, 1, 3)
        elif pitch > 0.5:
            T_sc.singleServo(1, -1, 3)



        pygame.event.pump()
        time.sleep(0.01)

 
 
if __name__ == '__main__':
    pygame.joystick.init()
    try:
        joys = pygame.joystick.Joystick(0)
        joys.init()
        main(joys)
    except pygame.error:
        print('error has occured')