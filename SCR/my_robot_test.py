#Code for test purposes ONLY
import time
import sys
import json
sys.path.append("/Users/jeffreyjahja/Documents/Uni/FYP/Code/FYPSAR/config") #Please change directory accordingly


with open('../config/config.json', 'r') as config_file:
    config_data = json.load(config_file)

sys.path.append(config_data["directory"]["yan"]) 
import YanAPI

robot_ip = config_data["ip"]["robot"] #Must use config file

## Add to Robot Class


class Robot():

    def __init__(self, name):
        self.name = name
        # YanAPI.yan_api_init(robot_ip)
        #print("Robot Connected")

    def robot_pause(self):
        while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
            pass

    def speech_pause(self):
        while YanAPI.get_voice_tts_state()['status'] != "idle":
            pass

    def say(self, value, parameters):
        #print("Value", value, "Parameters", parameters)
        logging.info("say "+ value)
        # if "velocity" not in parameters or type(parameters["velocity"]) != int or parameters["velocity"] < 0 or parameters["velocity"] > 100:
        #     YanAPI.set_robot_volume_value(50)
        # YanAPI.set_robot_volume_value(parameters['velocity'])
        # YanAPI.start_voice_tts(value, interrupt=False)
        # Insert YanAPI
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        #print("Hello, I'm moving")
        #print("Value", value, "Parameters", parameters)
        #print(parameters['meters'])
        logging.info("move "+ value + " by " + parameters['meters']+ " metres")
        # if "meters" not in parameters or type(parameters["meters"]) != float:
        #     repetition = 1
        # else:
        #     try:
        #         metre = float(parameters['meters'])
        #         repetition = int(metre//0.08)
        #     except:
        #         repetition = 1
            
        # #print(repetition)

        # ## Remove if else statement
        # if value == 'backwards':
        #     for i in range(repetition):
        #         YanAPI.start_play_motion(name = 'walk', direction = 'backward')
        #         self.robot_pause()
        #     YanAPI.start_play_motion(name = 'reset')

        # else:
        #     for i in range(repetition):
        #         YanAPI.start_play_motion(name = 'walk', direction = 'forward')
        #         self.robot_pause()
        #         #print(i)
        #     YanAPI.start_play_motion(name = 'reset')
        
        time.sleep(2)
        return "success"

    def stretch(self, value, parameters): 
        logging.info("stretch "+ value)
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
        if value not in stretchdict:
            logging.error("stretch not recognised")
            # YanAPI.start_voice_tts("Stretch not recognised. No motion will be played.", interrupt=True)

        else:
            logging.info("stretch actuated")
            # YanAPI.start_play_motion(name = stretchdict[value])
            # self.robot_pause()
            # YanAPI.start_play_motion(name = 'reset')
        return "success"

    def turn(self, value, parameters):
        logging.info("turn "+value+ " by "+parameters + " degrees")
        # if value == "left" and parameters['body'] == "head":
        #     if int(parameters['degrees']) > 75 or int(parameters['degrees']) < 0: #Replace with function, clip between 0 and 75
        #         parameters['degrees'] = 75
        #     YanAPI.set_servos_angles({"NeckLR": (90-int(parameters['degrees']))})
        #     self.robot_pause()
            #YanAPI.start_play_motion(name = 'reset')

        # elif value == "right" and parameters['body'] == "head":
        #     if int(parameters['degrees']) > 75:
        #         parameters['degrees'] = 75
        #     YanAPI.set_servos_angles({"NeckLR": (90+int(parameters['degrees']))})
        #     self.robot_pause()
            #YanAPI.start_play_motion(name = 'reset')

        # elif value == "left" and parameters['body'] == "body":
        #     YanAPI.start_play_motion(name = 'TurnLeft')
        #     self.robot_pause()
        #     YanAPI.start_play_motion(name = 'reset')

        # else:
        #     YanAPI.start_play_motion(name = 'TurnRight')
        #     self.robot_pause()
        #     YanAPI.start_play_motion(name = 'reset')
        return "success"
    
    def mode(self, value, parameters):
        logging.info("mode " + value)
        # if value == "rest":
        #     YanAPI.start_play_motion(name = 'SleepMode')
        #     self.robot_pause()
        # else:
        #     YanAPI.start_play_motion(name = 'Awake')
        #     self.robot_pause()
        #     YanAPI.start_play_motion(name = 'reset')
        #     self.robot_pause()
        return "success"

    def arm(self, value, parameters):
        #print(parameters)
        logging.info(parameters + "arms movement" + value)
        # if len(parameters) == 0:
        #     YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        # elif value == "side":
        #     if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
        #         YanAPI.start_play_motion(name = 'LeftArmSide')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'RightArmSide')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'BothArmSide')
        #         self.robot_pause()
        #     else:
        #         YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        # elif value == "circle":
        #     if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
        #         YanAPI.start_play_motion(name = 'LeftArmCircle')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'RightArmCircle')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'BothArmCircle')
        #         self.robot_pause()
        #     else:
        #         YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        # else:
        #     if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
        #         YanAPI.start_play_motion(name = 'LeftArmForward')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'RightArmForward')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'BothArmForward')
        #         self.robot_pause()
        #     else:
        #         YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        return "success"

    def leg(self, value, parameters):
        logging.info(parameters + "legs movement" + value)
        # if len(parameters) == 0:
        #     YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        # elif value == "side":
        #     if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
        #         YanAPI.start_play_motion(name = 'LeftFootSide')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'RightFootSide')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'BothFootSide')
        #         self.robot_pause()
        #     else:
        #         YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        # elif value == "backwards":
        #     if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
        #         YanAPI.start_play_motion(name = 'LeftFootBack')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'RightFootBack')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'BothFootBack')
        #         self.robot_pause()
        #     else:
        #         YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        # else:
        #     if parameters['LeftArm'] == 1 and parameters['RightArm'] == 0:
        #         YanAPI.start_play_motion(name = 'LeftFootForward')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 0 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'RightFootForward')
        #         self.robot_pause()
        #     elif parameters['LeftArm'] == 1 and parameters['RightArm'] == 1:
        #         YanAPI.start_play_motion(name = 'BothFootForward')
        #         self.robot_pause()
        #     else:
        #         YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        return "success"

    def idle(self, value, parameters):
        logging.info("idle for " + value)
        # time.sleep(int(value))
        return "success"