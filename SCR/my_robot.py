import time
import os
import sys
import json
import numpy as np
import logging
logger = logging.getLogger(__name__)

with open('../config/config.json', 'r') as config_file:
    config_data = json.load(config_file)

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, config_data["directory"]["yan"])) 

import YanAPI

robot_ip = config_data["ip"]["robot"] #Must use config file

## Add to Robot Class


class Robot():
    stretchdict = {
        "headstretch": "HeadStretch",
        "wriststretch": "WristStretch",
        "elbowstretch": "ShoulderStretch",
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

    speeddict = {
        "slow": "Slow",
        "normal": "Normal",
        "fast": "Fast"
    }

    def __init__(self, name):
        self.name = name
        YanAPI.yan_api_init(robot_ip)
        #print("Robot Connected")

    def robot_pause(self):
        while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
            pass

    def speech_pause(self):
        while YanAPI.get_voice_tts_state()['status'] != "idle":
            pass

    def stretch_guide(self, stretch):

        if stretch == "HeadStretch":
            YanAPI.start_voice_tts("It's time to do a head stretch, Turn your head to the left and hold for 10 seconds.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(10)
            YanAPI.start_voice_tts("Now, Turn your head to the right and hold for another 10 seconds.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(10)
            YanAPI.start_voice_tts("I would recommend repeating for another few times.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "EyeRest":
            YanAPI.start_voice_tts("You have been looking at your screen for a long time. Please rest your eyes, look out of the window, look at the birds, look at the sky.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "ChinTuck":
            YanAPI.start_voice_tts("Now, I need you to have your head to follow the tip of my hands as you tuck your chin.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "UpperLower":
            YanAPI.start_voice_tts("Interlace your fingers. Turn your palm upwards above your head. Slowly turn to one side.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(6)
            YanAPI.start_voice_tts("And the other side.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "ShoulderRoll":
            YanAPI.start_voice_tts("I need you to circle your shoulders as this is something that I can't do as a robot.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "HeadRoll":
            YanAPI.start_voice_tts("I need you to follow the tip of my hand. roll your head from your right to the left.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(14)
            YanAPI.start_voice_tts("Now to the right.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "Pectoral":
            YanAPI.start_voice_tts("Now i need you to raise your arms and bend your elbows. Pull back and repeat.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "BackwardsArch":
            YanAPI.start_voice_tts("Support your lower back and arch. Hold..", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "ShoulderStretch":
            YanAPI.start_voice_tts("Have your shoulders to the back and pull one elbow to one side", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(10.5)
            YanAPI.start_voice_tts("Now pull the other elbow to the other side", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "HeelRaise":
            YanAPI.start_voice_tts("As a robot i can't do this. But i need you to raise your heels every now and then. Feel free to hold on a chair if it helps you.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "ForwardStretch":
            YanAPI.start_voice_tts("Clasp your hands in front of you and lower your head in line with your arms. Press forward and hold.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        elif stretch == "SideBend":
            YanAPI.start_voice_tts("Place one hand on your hip and the other above your head. Lean to one side.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(14)
            YanAPI.start_voice_tts("Now alternate and lean to the other side.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
        else:
            YanAPI.start_voice_tts("Have yourself doing this stretch when seated. Roll one of your foot.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(11)
            YanAPI.start_voice_tts("Now roll the other foot", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
 

    def say(self, value, parameters):
        #print("Value", value, "Parameters", parameters)
        if value is None:
            value = "This is a default message"
        logger.info("say "+ value)
        
        try:
            volume = np.clip(int(parameters['velocity']), 0, 100)
        except:
            volume = 50
        logger.info("volume: "+ str(volume))
        YanAPI.set_robot_volume_value(int(volume))
        YanAPI.start_voice_tts(value, interrupt=False)
        self.speech_pause()
        YanAPI.stop_voice_tts()
        
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

        logger.info("move "+ direction + " by " + str(repetition)+ " times")
        for i in range(repetition):
            YanAPI.start_play_motion(name = 'walk', direction = direction)
            self.robot_pause()
    
        YanAPI.stop_play_motion()
        
        time.sleep(2)
        return "success"

    def stretch(self, value, parameters): #add repetition parameter
        speed = Robot.speeddict.get(parameters.get('speed', 'Normal'), 'Normal')
        repetition = int(parameters.get('repeat', 1))
        guide = bool(parameters.get('guide', False))
        stretch = Robot.stretchdict.get(value, "HeadStretch")
        logger.info("play "+ stretch+ " of speed " + speed + str(repetition) + " times, with guide " + str(guide))
        YanAPI.start_play_motion(name = str(stretch + speed), repeat = repetition)
        if guide:
            self.stretch_guide(stretch)
        self.robot_pause()
        YanAPI.stop_play_motion()

        return "success"

    def turn(self, value, parameters):
        degrees = 0
        try:
            if parameters['body'] == "head":
                degrees = np.clip(int(parameters['degrees']), 0, 75)
                logger.info("turn head to the " + value + " with " +  str(degrees) + " degrees")
            else:
                degrees = int(parameters['degrees'])
                repeat = degrees // 90
                logger.info("turn body  to the " + value + ", " +  str(repeat) + " times")
        except:
            parameters['body'] = "body"
            repeat = 1
        
        if value == "left":
            if parameters['body'] == "head":
                logger.info("head turn")
                YanAPI.set_servos_angles({"NeckLR": (90-degrees)})
                self.robot_pause()
            else:
                logger.info("body turn")
                YanAPI.start_play_motion(name='TurnLeft', repeat = repeat)
                self.robot_pause()
                YanAPI.stop_play_motion()

        else:
            if parameters['body'] == "head":
                logger.info("head turn")
                YanAPI.set_servos_angles({"NeckLR": (90+degrees)})
                self.robot_pause()
            else:
                YanAPI.start_play_motion(name='TurnRight', repeat = repeat)
                self.robot_pause()
                YanAPI.stop_play_motion()
                
        return "success"
    
    def mode(self, value, parameters):
        
        if value == "rest":
            YanAPI.start_play_motion(name = 'SleepMode')
            self.robot_pause()
            YanAPI.stop_play_motion()
            logger.info("mode sleep")
        else:
            YanAPI.start_play_motion(name = 'Awake')
            self.robot_pause()
            YanAPI.stop_play_motion()
            YanAPI.start_play_motion(name = 'reset')
            self.robot_pause()
            YanAPI.stop_play_motion()
            logger.info("mode awake")

        return "success"

    def arm(self, value, parameters):
        try:
            left_arm = parameters.get('LeftArm', 0)
            right_arm = parameters.get('RightArm', 0)
            arm_motion_map = {
                'side': {
                    (1, 0): 'LeftArmSide',
                    (0, 1): 'RightArmSide',
                    (1, 1): 'BothArmSide'
                },
                'circle': {
                    (1, 0): 'LeftArmCircle',
                    (0, 1): 'RightArmCircle',
                    (1, 1): 'BothArmCircle'
                },
                'forward': {
                    (1, 0): 'LeftArmForward',
                    (0, 1): 'RightArmForward',
                    (1, 1): 'BothArmForward'
                }
            }
            if (left_arm, right_arm) in arm_motion_map.get(value, {}):
                logger.info(value +" raise")
                logger.info("left arm: " + str(left_arm) + " right arm: " + str(right_arm))
                YanAPI.start_play_motion(name=arm_motion_map[value][(left_arm, right_arm)])
                self.robot_pause()
                YanAPI.stop_play_motion()
        except:
            logger.info("no arm")
            YanAPI.start_voice_tts("No arms chosen.", interrupt=True)
        return "success"

    def leg(self, value, parameters):
        try:
            left_leg = parameters.get('LeftArm', 0)
            right_leg = parameters.get('RightArm', 0)
            leg_motion_map = {
                'side': {
                    (1, 0): 'LeftFootSide',
                    (0, 1): 'RightFootSide',
                    (1, 1): 'BothFootSide'
                },
                'backward': {
                    (1, 0): 'LeftFootBack',
                    (0, 1): 'RightFootBack',
                    (1, 1): 'BothFootBack'
                },
                'forward': {
                    (1, 0): 'LeftFootForward',
                    (0, 1): 'RightFootForward',
                    (1, 1): 'BothFootForward'
                }
            }
            if (left_leg, right_leg) in leg_motion_map.get(value, {}):
                logger.info(value +" raise")
                logger.info("left leg: " + str(left_leg) + " right leg: " + str(right_leg))
                YanAPI.start_play_motion(name=leg_motion_map[value][(left_leg, right_leg)])
                self.robot_pause()
                YanAPI.stop_play_motion()
        except:
            logger.info("no leg")
            YanAPI.start_voice_tts("No leg chosen.", interrupt=True)

        return "success"

    def idle(self, value, parameters):
        logger.info("idle for " + value)
        time.sleep(int(value))
        return "success"