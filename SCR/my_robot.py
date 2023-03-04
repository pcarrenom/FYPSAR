import time
import sys
sys.path.append("/Users/jeffreyjahja/Documents/Uni/FYP/Code/FYPSAR/third-party") #Please change directory accordingly
import YanAPI
import logging

robot_ip = "160.69.69.103"

stretchdict = {
    "headturn": "HeadTurn",
    "wriststretch": "WristStretch",
    "shoulderstretch": "ShoulderStretch",
    "upperlowerstretch": "UpperLower",
    "footrotation": "FootRotation",
    "forwardstretch": "ForwardStretch",
    "backarch": "BackwardsArch",
    "Pectoral": "pectoral",
    "sidebend": "SideBend",
    "chintuck": "ChinTuck",
    "headroll": "HeadRoll",
    "shoulderroll": "ShoulderRoll",
    "eyerest": "EyeRest"
}

def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

def speech_pause():
    while YanAPI.get_voice_tts_state()['status'] != "idle":
        pass

class Robot():

    def __init__(self, name):
        self.name = name
        YanAPI.yan_api_init(robot_ip)
        #print("Robot Connected")

    def say(self, value, parameters):
        #print("Value", value, "Parameters", parameters)
        if len(parameters) == 0:
            YanAPI.set_robot_volume_value(50)
        YanAPI.set_robot_volume_value(parameters['velocity'])
        YanAPI.start_voice_tts(value, interrupt=False)
        # Insert YanAPI
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        #print("Hello, I'm moving")
        #print("Value", value, "Parameters", parameters)
        #print(parameters['meters'])
        if len(parameters) == 0:
            repetition = 1
        else:
            metre = float(parameters['meters'])
            repetition = int(metre//0.08)
        #print(repetition)
        if value == 'backwards':
            for i in range(repetition):
                YanAPI.start_play_motion(name = 'walk', direction = 'backward')
                robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        else:
            for i in range(repetition):
                YanAPI.start_play_motion(name = 'walk', direction = 'forward')
                robot_pause()
                #print(i)
            YanAPI.start_play_motion(name = 'reset')
        
        time.sleep(2)
        return "success"

    def stretch(self, value, parameters): 
        #print(value)
        if value not in stretchdict:
            YanAPI.start_voice_tts("Stretch not recognised. No motion will be played.", interrupt=True)

        else:
            YanAPI.start_play_motion(name = stretchdict[value])
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
        return "success"

    def turn(self, value, parameters):
        if parameters['body'] == "head" and int(parameters['degrees']) > 75:
            parameters['degrees'] = 75
        if value == "left" and parameters['body'] == "head":
            YanAPI.set_servos_angles({"NeckLR": (90-int(parameters['degrees']))})
            robot_pause()
            #YanAPI.start_play_motion(name = 'reset')

        elif value == "right" and parameters['body'] == "head":
            YanAPI.set_servos_angles({"NeckLR": (90+int(parameters['degrees']))})
            robot_pause()
            #YanAPI.start_play_motion(name = 'reset')

        elif value == "left" and parameters['body'] == "body":
            YanAPI.start_play_motion(name = 'TurnLeft')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')

        else:
            YanAPI.start_play_motion(name = 'TurnRight')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
        return "success"
    
    def mode(self, value, parameters):
        if value == "rest":
            YanAPI.start_play_motion(name = 'SleepMode')
            robot_pause()
        else:
            YanAPI.start_play_motion(name = 'Awake')
            robot_pause()
            YanAPI.start_play_motion(name = 'reset')
            robot_pause()
        return "success"

    def arm(self, value, parameters):
        print(parameters)
        if len(parameters) == 0:
            YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
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
            else:
                YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
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
            else:
                YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        else:
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftArmForward')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightArmForward')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothArmForward')
                robot_pause()
            else:
                YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        return "success"

    def leg(self, value, parameters):
        if len(parameters) == 0:
            YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
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
            else:
                YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
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
            else:
                YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        else:
            if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
                YanAPI.start_play_motion(name = 'LeftFootForward')
                robot_pause()
            elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'RightFootForward')
                robot_pause()
            elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
                YanAPI.start_play_motion(name = 'BothFootForward')
                robot_pause()
            else:
                YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        return "success"

    def idle(self, value, parameters):
        time.sleep(int(value))
        return "success"