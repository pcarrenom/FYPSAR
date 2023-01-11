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
        print("Value", value, "Parameters", parameters)
        YanAPI.set_robot_volume_value(parameters['velocity'])
        YanAPI.start_voice_tts(value, interrupt=False)
        # Insert YanAPI
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        print("Hello, I'm moving")
        print("Value", value, "Parameters", parameters)
        print(parameters['meters'])
        metre = float(parameters['meters'])
        print(metre)
        repetition = int(metre//0.08)
        print(repetition)
        if value == 'forwards':
            for i in range(repetition):
                YanAPI.start_play_motion(name = 'walk', direction = 'forward')
                robot_pause()
                print(i)
            YanAPI.start_play_motion(name = 'reset')
        elif value == 'backwards':
            for i in range(repetition):
                YanAPI.start_play_motion(name = 'walk', direction = 'backward')
                robot_pause()
            YanAPI.start_play_motion(name = 'reset')
        
        time.sleep(2)
        return "success"

    def animation(self, value, parameters): 
        print(value)
        if value == "headroll":
            print("Time to roll my head")
            YanAPI.start_play_motion(name = 'HeadTurn')
        
        elif value == "wriststretch":
            print("time to stretch my wrist")
            YanAPI.start_play_motion(name = 'WristStretch')

        elif value == "shoulderstretch":
            print("time to stretch my shoulder")
            YanAPI.start_play_motion(name = '肩膀连动')

        elif value == "upperlower":
            print("time for some upper and lower stretches")
            YanAPI.start_play_motion(name = 'UpperLower')

        elif value == "footrotation":
            print("Let me rotate my foot")
            YanAPI.start_play_motion(name = 'FootRotation')

        elif value == "forwardstretch":
            print("forward stretch")
            YanAPI.start_play_motion(name = 'ForwardStretch')

        elif value == "backarch":
            print("Back Arch")
            YanAPI.start_play_motion(name = 'BackwardsArch')

        elif value == "pectoral":
            print("pectoral")
            YanAPI.start_play_motion(name = 'Pectoral')

        elif value == "sidebend":
            print("side bends")
            YanAPI.start_play_motion(name = 'Outreach')