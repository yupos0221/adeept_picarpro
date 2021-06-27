import pygame
from pygame.locals import *
import time
 
def main(joys) :
    pygame.init()
    print("Joystick Name: " + joys.get_name())
    print("Number of Button : " + str(joys.get_numbuttons()))
    print("Number of Axis : " + str(joys.get_numaxes()))
    print("Number of Hats : " + str(joys.get_numhats()))



    # while True:
    #     # PS4
    #     turn = round(joys.get_axis(0),1)
    #     forward = round(joys.get_axis(1),1)
    #     yaw = round(joys.get_axis(2),1)
    #     pitch = round(joys.get_axis(5),1)
        
    #     print("forward: {:.1f}".format(forward))
    #     print("turn: {:.1f}".format(turn))
    #     print("yaw: {:.1f}".format(yaw))
    #     print("pitch: {:.1f}".format(pitch))


    #     pygame.event.pump()
    #     time.sleep(0.01)

    while True:
        for e in pygame.event.get():

            # ジョイスティックのボタンの入力
            if e.type == pygame.locals.JOYAXISMOTION:
                turn = round(joys.get_axis(0),1)
                forward = round(joys.get_axis(1),1)
                yaw = round(joys.get_axis(2),1)
                pitch = round(joys.get_axis(5),1)
                print("forward: {:.1f}".format(forward))
                print("turn: {:.1f}".format(turn))
                print("yaw: {:.1f}".format(yaw))
                print("pitch: {:.1f}".format(pitch))
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print('ボタン'+str(e.button)+'を押した')
            elif e.type == pygame.locals.JOYBUTTONUP:
                print('ボタン'+str(e.button)+'を離した')

 
 
if __name__ == '__main__':
    pygame.joystick.init()
    try:
        joys = pygame.joystick.Joystick(0)
        joys.init()
        main(joys)
    except pygame.error:
        print('error has occured')