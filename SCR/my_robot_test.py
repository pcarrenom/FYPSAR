#Code for testing purposes ONLY
import time
import os
import sys
import json
import numpy as np
import logging

with open('../config/config.json', 'r') as config_file:
    config_data = json.load(config_file)

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, config_data["directory"]["yan"])) 

import YanAPI

robot_ip = config_data["ip"]["robot"] #Must use config file

## Add to Robot Class


class Robot():
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

    def __init__(self, name):
        self.name = name
        # YanAPI.yan_api_init(robot_ip)
        #print("Robot Connected")

    # def robot_pause(self):
    #     while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
    #         pass

    # def speech_pause(self):
    #     while YanAPI.get_voice_tts_state()['status'] != "idle":
    #         pass

    def say(self, value, parameters):
        #print("Value", value, "Parameters", parameters)
        if value is None:
            value = "This is a default message"
        logging.info("say "+ value)
        
        try:
            volume = np.clip(int(parameters['velocity'], 0, 100))
        except:
            volume = 50.0
        logging.info("volume: "+ str(volume))
        # YanAPI.set_robot_volume_value(volume)
        # YanAPI.start_voice_tts(value, interrupt=False)
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):

        try:
            metre = float(parameters['meters'])
            repetition = int(metre//0.08)
        except:
            repetition = 1
        eq_dict = {'backwards': 'backward', 'forwards': 'forward'}

        if value not in ['backwards', 'forwards']:
            value = "forwards"
            
        direction = eq_dict[value]

        logging.info("move "+ direction + " by " + str(repetition)+ " times")
        # for i in range(repetition):
        #     YanAPI.start_play_motion(name = 'walk', direction = 'backward')
        #     self.robot_pause()
    
        # YanAPI.start_play_motion(name = 'reset')
        
        time.sleep(2)
        return "success"

    def stretch(self, value, parameters): 

        try:
            # YanAPI.start_play_motion(name = Robot.stretchdict[value])
            # self.robot_pause()
            # YanAPI.start_play_motion(name = 'reset')
            logging.info("played "+ str(Robot.stretchdict[value]))

        except:
            logging.error("stretch not recognised")
            # YanAPI.start_voice_tts("Stretch not recognised. No motion will be played.", interrupt=True)

        return "success"

    def turn(self, value, parameters):
        try:
            if parameters['body'] == "head":
                degrees = np.clip(int(parameters['degrees'], 0, 75))
            else:
                degrees = parameters['degrees']
        except:
            degrees = 0
        logging.info("turn " + str(parameters["degrees"]) + " degrees")
        try:
            # if value == "left" and parameters['body'] == "head":
            #     YanAPI.set_servos_angles({"NeckLR": (90-degrees)})
            #     self.robot_pause()
            # #YanAPI.start_play_motion(name = 'reset')

            # elif value == "right" and parameters['body'] == "head":
            #     YanAPI.set_servos_angles({"NeckLR": (90+degrees)})
            #     self.robot_pause()
            # #YanAPI.start_play_motion(name = 'reset')

            # elif value == "left" and parameters['body'] == "body":
            #     YanAPI.start_play_motion(name = 'TurnLeft')
            #     self.robot_pause()
            #     YanAPI.start_play_motion(name = 'reset')

            # else:
            #     YanAPI.start_play_motion(name = 'TurnRight')
            #     self.robot_pause()
            #     YanAPI.start_play_motion(name = 'reset')
            logging.info("turn " + value + str(parameters['body']))
        except:
            logging.error("Default move")
            # YanAPI.start_play_motion(name = 'TurnRight')
            # self.robot_pause()
            # YanAPI.start_play_motion(name = 'reset')
            
        return "success"
    
    def mode(self, value, parameters):
        
        if value == "rest":
            # YanAPI.start_play_motion(name = 'SleepMode')
            # self.robot_pause()
            logging.info("mode sleep")
        else:
            # YanAPI.start_play_motion(name = 'Awake')
            # self.robot_pause()
            # YanAPI.start_play_motion(name = 'reset')
            # self.robot_pause()
            logging.info("mode awake")

        return "success"

    def arm(self, value, parameters):
        #print(parameters)
        try:
            # if value == "side":
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
            logging.info(parameters + "arms movement " + value)
        except:
            logging.error("no parameter")
            # YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        return "success"

    def leg(self, value, parameters):
        try:
            # if value == "side":
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
            logging.info(parameters + "leg movement " + value)
        except:
            logging.error("no parameter")
            # YanAPI.start_voice_tts("No legs chosen.", interrupt=True)
        return "success"

    def idle(self, value, parameters):
        logging.info("idle for " + value)
        time.sleep(int(value))
        return "success"