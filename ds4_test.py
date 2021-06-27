from pyPS4Controller.controller import Controller

def norm(value):
    return value*2/(2**16)

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_up(self, value): 

        print("on_L3_up: ", norm(value)) 
        
    def on_L3_down(self, value): 
        print("on_L3_down: ", norm(value)) 
    
    def on_L3_left(self, value): 
        print("on_L3_left: ", norm(value)) 
        
    def on_L3_right(self, value): 
        print("on_L3_right: ", norm(value)) 
        
    def on_L3_release(self): 
        print("on_L3_release") 
        
    def on_R3_up(self, value): 
        print("on_R3_up: ", norm(value)) 
        
    def on_R3_down(self, value): 
        print("on_R3_down: ", norm(value)) 
        
    def on_R3_left(self, value): 
        print("on_R3_left: ", norm(value)) 
        
    def on_R3_right(self, value): 
        print("on_R3_right: ", norm(value)) 
        
    def on_R3_release(self): 
        print("on_R3_release")



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()