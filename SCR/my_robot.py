import time
import sys
sys.path.append("/Users/jeffreyjahja/Documents/Uni/FYP/Code/FYPSAR/third-party") #Please change directory accordingly
import YanAPI

robot_ip = "160.69.69.103"

def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

def speech_pause():
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

    def stretch(self, value, parameters): 
        print(value)
        if value == "headroll":
            print("Time to roll my head")
            YanAPI.start_play_motion(name = 'HeadTurn')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
        
        elif value == "wriststretch":
            print("time to stretch my wrist")
            YanAPI.start_play_motion(name = 'WristStretch')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "shoulderstretch":
            print("time to stretch my shoulder")
            YanAPI.start_play_motion(name = '肩膀连动')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "upperlower":
            print("time for some upper and lower stretches")
            YanAPI.start_play_motion(name = 'UpperLower')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "footrotation":
            print("Let me rotate my foot")
            YanAPI.start_play_motion(name = 'FootRotation')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "forwardstretch":
            print("forward stretch")
            YanAPI.start_play_motion(name = 'ForwardStretch')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "backarch":
            print("Back Arch")
            YanAPI.start_play_motion(name = 'BackwardsArch')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "pectoral":
            print("pectoral")
            YanAPI.start_play_motion(name = 'Pectoral')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "sidebend":
            print("side bends")
            YanAPI.start_play_motion(name = 'Outreach')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "chintuck":
            print("chin tuck")
            YanAPI.start_play_motion(name = 'ChinTuck')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "headroll":
            print("head roll")
            YanAPI.start_play_motion(name = 'HeadRoll')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "shoulderroll":
            print("shoulder roll")
            YanAPI.start_play_motion(name = 'ShoulderRoll')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "eyerest":
            print("eye rest")
            YanAPI.start_play_motion(name = 'EyeRest')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

    def turn(self, value, parameters):
        if value == "left" and parameters['body'] == "head":
            YanAPI.start_play_motion(name = 'LookLeft')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "right" and parameters['body'] == "head":
            YanAPI.start_play_motion(name = 'LookRight')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "left" and parameters['body'] == "body":
            YanAPI.start_play_motion(name = 'TurnLeft')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        elif value == "right" and parameters['body'] == "body":
            YanAPI.start_play_motion(name = 'TurnRight')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
    
    def mode(self, value, parameters):
        if value == "wake_up":
            YanAPI.start_play_motion(name = 'Awake')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
            robot_pause()
        elif value == "rest":
            YanAPI.start_play_motion(name = 'SleepMode')
            robot_pause()

    def arm(self, value, parameters):
        if value == "forward":
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftArmForward')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightArmForward')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothArmForward')
                robot_pause()
        elif value == "side":
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftArmSide')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightArmSide')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothArmSide')
                robot_pause()
        elif value == "circle":
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftArmCircle')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightArmCircle')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothArmCircle')
                robot_pause()

    def leg(self, value, parameters):
        if value == "forward":
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftFootForward')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightFootForward')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothFootForward')
                robot_pause()
        elif value == "side":
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftFootSide')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightFootSide')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothFootSide')
                robot_pause()
        elif value == "backwards":
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftFootBack')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightFootBack')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothFootBack')
                robot_pause()

    def idle(self, value, parameters):
        time.sleep(int(value))