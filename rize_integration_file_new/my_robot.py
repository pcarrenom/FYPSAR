import time
import YanAPI

robot_ip = "160.69.69.103"

def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

class Robot():

    def __init__(self, name):
        self.name = name
        YanAPI.yan_api_init(robot_ip)
        print("Robot Connected")

    def say(self, value, parameters):
        YanAPI.start_play_motion(name = '青春修炼手册')
        robot_pause()
        YanAPI.start_play_motion(name = 'reset')
        print("Hello, I'm saying something")
        print("Value", value, "Parameters", parameters)
        # Insert YanAPI
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        print("Hello, I'm moving")
        print("Value", value, "Parameters", parameters)
        if value == 'forwards':
            YanAPI.start_play_motion(name = 'Forward')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
        elif value == 'backwards':
            YanAPI.start_play_motion(name = 'Backward')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
        
        time.sleep(2)
        return "success"