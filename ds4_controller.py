from pyPS4Controller.controller import Controller
from server import move, RPIservo

def norm(value):
    return abs(round(value*2/(2**16),2))

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

        self.max_vel = 100
        self.max_angle = 0
        
        self.scGear = RPIservo.ServoCtrl()
        # self.scGear.moveInit()
        self.scGear.start()

        self.P_sc = RPIservo.ServoCtrl()
        self.P_sc.start()

        self.T_sc = RPIservo.ServoCtrl()
        self.T_sc.start()

        self.H_sc = RPIservo.ServoCtrl()
        self.H_sc.start()

        self.G_sc = RPIservo.ServoCtrl()
        self.G_sc.start()

        self.init_pwm = []
        for i in range(16):
            self.init_pwm.append(self.scGear.initPos[i])

        move.setup()
        self.servoPosInit()

    def servoPosInit(self):
        self.scGear.initConfig(0,self.init_pwm[0],1)
        self.P_sc.initConfig(1,self.init_pwm[1],1)
        self.T_sc.initConfig(2,self.init_pwm[2],1)
        self.H_sc.initConfig(3,self.init_pwm[3],1)
        self.G_sc.initConfig(4,self.init_pwm[4],1)

    def on_L3_up(self, value): 
        val = norm(value)
        print("on_L3_up: ", val)
        if val > 0.1: 
            move.move(val, "forward")
        else:
            move.move(0, "no")

    def on_L3_down(self, value): 
        val = norm(value)
        print("on_L3_down: ", val) 
        if val > 0.1: 
            move.move(val, "backward")
        else:
            move.move(0, "no")
    
    def on_L3_left(self, value): 
        val = norm(value)
        print("on_L3_left: ", val) 
        # if val > 0.1:
        #     turn_angle = self.max_angle * val
        #     self.scGear.moveAngle(0, turn_angle)
        if val > 0.5:
            self.scGear.singleServo(0, 1, 3)
        else:
            self.scGear.stopWiggle()

    def on_L3_right(self, value): 
        val = norm(value)
        print("on_L3_right: ", val) 
        # if val > 0.1:
        #     turn_angle = self.max_angle * val
        #     self.scGear.moveAngle(0, -turn_angle)
        if val > 0.5:
            self.scGear.singleServo(0, -1, 3)
        else:
            self.scGear.stopWiggle()

    def on_L3_release(self): 
        print("on_L3_release") 
        # move.motorStop()
        move.move(0, "no")
        
    def on_R3_up(self, value): 
        val = norm(value)
        print("on_R3_up: ", val) 
        if val > 0.5:
            self.T_sc.singleServo(2, 1, 3)
        else:
            self.T_sc.stopWiggle()
        
    def on_R3_down(self, value): 
        val = norm(value)
        print("on_R3_down: ", val) 
        if val > 0.5:
            self.T_sc.singleServo(2, -1, 3)
        else:
            self.T_sc.stopWiggle()
        
    def on_R3_left(self, value): 
        val = norm(value)
        print("on_R3_left: ", val) 
        if val > 0.5:
            self.P_sc.singleServo(1, 1, 3)
        else:
            self.P_sc.stopWiggle()
        
    def on_R3_right(self, value): 
        val = norm(value)
        print("on_R3_right: ", val) 
        if val > 0.5:
            self.P_sc.singleServo(1, -1, 3)
        else:
            self.P_sc.stopWiggle()
        
    def on_R3_release(self): 
        print("on_R3_release")
        move.motorStop()



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()