import time
import YanAPI

def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

class Robot():

    def __init__(self, name):
        self.name = name

    def say(self, value, parameters):
        print("Hello, I'm saying something")
        print("Value", value, "Parameters", parameters)
        # Insert YanAPI
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        print("Hello, I'm moving")
        print("Value", value, "Parameters", parameters)
        #YanAPI.start_play_motion(name = 'raisehand')
        #robot_pause()
        #YanAPI.start_play_motion(name = 'reset')
        time.sleep(2)
        return "success"