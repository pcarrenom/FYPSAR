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
        "upperandlowerstretch": "UpperLower",
        "footrotation": "FootRotation",
        "forwardstretch": "ForwardStretch",
        "backarch": "BackwardsArch",
        "Pectoral": "pectoral",
        "sidebend": "SideBend",
        "chintuck": "ChinTuck",
        "headroll": "HeadRoll",
        "shoulderroll": "ShoulderRoll",
        "eyerest": "EyeRest",
        "heelraise": "HeelRaise"
        }

    arm_motion = {
        "leftForward":{"LeftShoulderRoll": 180, "LeftShoulderFlex": 0, "LeftElbowFlex": 90, "RightShoulderRoll":90,"RightShoulderFlex": 140,"RightElbowFlex":165},
        "rightForward":{"RightShoulderRoll": 0, "RightShoulderFlex": 180, "RightElbowFlex": 90, "LeftShoulderRoll": 90, "LeftShoulderFlex": 40, "LeftElbowFlex": 15},
        "bothForward":{"LeftShoulderRoll": 180, "LeftShoulderFlex": 0, "LeftElbowFlex": 90, "RightShoulderRoll": 0, "RightShoulderFlex": 180, "RightElbowFlex": 90},
        "leftSide":{"LeftShoulderRoll": 90, "LeftShoulderFlex": 90, "LeftElbowFlex": 90, "RightShoulderRoll":90,"RightShoulderFlex": 140,"RightElbowFlex":165},
        "rightSide":{"RightShoulderRoll": 90, "RightShoulderFlex": 90, "RightElbowFlex": 90, "LeftShoulderRoll": 90, "LeftShoulderFlex": 40, "LeftElbowFlex": 15},
        "bothSide":{"LeftShoulderRoll": 90, "LeftShoulderFlex": 90, "LeftElbowFlex": 90, "RightShoulderRoll": 90, "RightShoulderFlex": 90, "RightElbowFlex": 90},
        "leftUp":{"LeftShoulderRoll": 90, "LeftShoulderFlex": 170, "LeftElbowFlex": 100, "RightShoulderRoll":90,"RightShoulderFlex": 140,"RightElbowFlex":165},
        "rightUp":{"RightShoulderRoll": 90, "RightShoulderFlex": 10, "RightElbowFlex": 80, "LeftShoulderRoll": 90, "LeftShoulderFlex": 40, "LeftElbowFlex": 15},
        "bothUp":{"LeftShoulderRoll": 90, "LeftShoulderFlex": 170, "LeftElbowFlex": 100,"RightShoulderRoll": 90, "RightShoulderFlex": 10, "RightElbowFlex": 80},
        "leftCrane":{"LeftShoulderRoll": 90, "LeftShoulderFlex": 135, "LeftElbowFlex": 5, "RightShoulderRoll":90,"RightShoulderFlex": 140,"RightElbowFlex":165},
        "rightCrane":{"RightShoulderRoll": 90, "RightShoulderFlex": 45, "RightElbowFlex": 170, "LeftShoulderRoll": 90, "LeftShoulderFlex": 40, "LeftElbowFlex": 15},
        "bothCrane":{"LeftShoulderRoll": 90, "LeftShoulderFlex": 135, "LeftElbowFlex": 5,"RightShoulderRoll": 90, "RightShoulderFlex": 45, "RightElbowFlex": 170}
    }

    def __init__(self, name):
        self.name = name
        YanAPI.yan_api_init(robot_ip)
        YanAPI.start_voice_tts("Robot Action actuated", interrupt=False)

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
            time.sleep(4.8)
            YanAPI.start_voice_tts("And the other side.", interrupt=False)
            time.sleep(2)
            YanAPI.start_voice_tts("Feel free to do it as many times as you wish.", interrupt=False)
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
        elif stretch == "WristStretch":
            YanAPI.start_voice_tts("Now, bring your hands to the front and stretch one of your wrist to the front. Don't forget to alternate.", interrupt=False)
        else:
            YanAPI.start_voice_tts("Have yourself doing this stretch when seated. Roll one of your foot.", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
            time.sleep(11)
            YanAPI.start_voice_tts("Now roll the other foot", interrupt=False)
            self.speech_pause()
            YanAPI.stop_voice_tts()
    
    def leg_motion(self, motion, timer):
        if motion == "leftForward":
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":90,"LeftAnkleFB":90,"LeftKneeFlex":25,"LeftHipFB":155,"LeftHipLR":88}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
        elif motion == "rightForward":
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":100,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":90,"RightKneeFlex":155,"RightHipFB":25,"RightHipLR":93,"LeftAnkleUD":100,"LeftAnkleFB":75,"LeftKneeFlex":110,"LeftHipFB":120,"LeftHipLR":88}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":100,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
        elif motion == "bothForward":
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":90,"LeftAnkleFB":90,"LeftKneeFlex":25,"LeftHipFB":155,"LeftHipLR":88}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":100,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":90,"RightKneeFlex":155,"RightHipFB":25,"RightHipLR":93,"LeftAnkleUD":100,"LeftAnkleFB":75,"LeftKneeFlex":110,"LeftHipFB":120,"LeftHipLR":88}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":100,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
        elif motion == "leftBackward":
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":77,"RightAnkleFB":112,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":106,"LeftAnkleFB":180,"LeftKneeFlex":90,"LeftHipFB":154,"LeftHipLR":93}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":82,"RightAnkleFB":112,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":90,"LeftAnkleFB":90,"LeftKneeFlex":30,"LeftHipFB":0,"LeftHipLR":88}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":77,"RightAnkleFB":112,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":106,"LeftAnkleFB":180,"LeftKneeFlex":90,"LeftHipFB":154,"LeftHipLR":93}, 2000)
            time.sleep(1.9)
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 900)
            time.sleep(0.8)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
        elif motion == "rightBackward":
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":102,"LeftAnkleFB":70,"LeftKneeFlex":103,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":74,"RightAnkleFB":0,"RightKneeFlex":90,"RightHipFB":25,"RightHipLR":87,"LeftAnkleUD":103,"LeftAnkleFB":68,"LeftKneeFlex":104,"LeftHipFB":120,"LeftHipLR":86}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":85,"RightKneeFlex":150,"RightHipFB":180,"RightHipLR":93,"LeftAnkleUD":98,"LeftAnkleFB":68,"LeftKneeFlex":104,"LeftHipFB":120,"LeftHipLR":86}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":74,"RightAnkleFB":0,"RightKneeFlex":90,"RightHipFB":25,"RightHipLR":87,"LeftAnkleUD":103,"LeftAnkleFB":68,"LeftKneeFlex":104,"LeftHipFB":120,"LeftHipLR":86}, 2000)
            time.sleep(1.9)
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":102,"LeftAnkleFB":70,"LeftKneeFlex":103,"LeftHipFB":120}, 900)
            time.sleep(0.8)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
        elif motion == "bothBackward":
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":77,"RightAnkleFB":112,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":106,"LeftAnkleFB":180,"LeftKneeFlex":90,"LeftHipFB":154,"LeftHipLR":93}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":82,"RightAnkleFB":112,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":90,"LeftAnkleFB":90,"LeftKneeFlex":30,"LeftHipFB":0,"LeftHipLR":88}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":77,"RightAnkleFB":112,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":93,"LeftAnkleUD":106,"LeftAnkleFB":180,"LeftKneeFlex":90,"LeftHipFB":154,"LeftHipLR":93}, 2000)
            time.sleep(1.9)
            YanAPI.set_servos_angles({"RightAnkleUD":80,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":60,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 900)
            time.sleep(0.8)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":102,"LeftAnkleFB":70,"LeftKneeFlex":103,"LeftHipFB":120}, 600)
            time.sleep(0.6)
            YanAPI.set_servos_angles({"RightAnkleUD":74,"RightAnkleFB":0,"RightKneeFlex":90,"RightHipFB":25,"RightHipLR":87,"LeftAnkleUD":103,"LeftAnkleFB":68,"LeftKneeFlex":104,"LeftHipFB":120,"LeftHipLR":86}, 1000)
            time.sleep(1)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":85,"RightKneeFlex":150,"RightHipFB":180,"RightHipLR":93,"LeftAnkleUD":98,"LeftAnkleFB":68,"LeftKneeFlex":104,"LeftHipFB":120,"LeftHipLR":86}, 1200)
            time.sleep(1.2 + timer)
            YanAPI.set_servos_angles({"RightAnkleUD":74,"RightAnkleFB":0,"RightKneeFlex":90,"RightHipFB":25,"RightHipLR":87,"LeftAnkleUD":103,"LeftAnkleFB":68,"LeftKneeFlex":104,"LeftHipFB":120,"LeftHipLR":86}, 2000)
            time.sleep(1.9)
            YanAPI.set_servos_angles({"RightAnkleUD":120,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"LeftAnkleUD":102,"LeftAnkleFB":70,"LeftKneeFlex":103,"LeftHipFB":120}, 900)
            time.sleep(0.8)
            YanAPI.set_servos_angles({"RightAnkleUD":90,"RightAnkleFB":110,"RightKneeFlex":75,"RightHipFB":60,"RightHipLR":90,"LeftAnkleUD":90,"LeftAnkleFB":70,"LeftKneeFlex":105,"LeftHipFB":120,"LeftHipLR":90}, 600)
            time.sleep(0.6)

    def say(self, value, parameters):
        #print("Value", value, "Parameters", parameters)
        if value is None:
            value = "This is a default message"
        logger.info("say "+ value)
        
        try:
            volume = np.clip(int(parameters['volume']), 1, 100)
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
            metre = np.absolute(float(parameters['meters']))
            repetition = int(metre//0.08)
        except:
            repetition = 1
        eq_dict = {'backwards': 'backward', 'forwards': 'forward', 'left':'left', 'right':'right'}
        speedlist = ['very slow','slow','normal','fast','very fast']
        try:
            speed_act = speedlist[int(np.clip(int(parameters['speed'])//20, 0, 4))]
        except:
            speed_act = 'normal'
        if value not in ['backwards', 'forwards','left','right']:
            value = "forwards"
            
        direction = eq_dict[value]

        logger.info("move "+ direction + " by " + str(repetition)+ " times, with speed " + speed_act)
        for i in range(repetition):
            YanAPI.start_play_motion(name = 'walk', direction = direction, speed = speed_act)
            self.robot_pause()
    
        YanAPI.stop_play_motion()
        
        time.sleep(2)
        return "success"

    def stretch(self, value, parameters):
        speedlist = ['Slow','Normal','Fast']
        try:
            speed = speedlist[int(np.clip(int(parameters['speed'])//33, 0, 2))]
        except:
            speed = 'Normal'
        try:
            repetition = int(np.clip(int(parameters['repetition']), 1, 100))
        except:
            repetition = 1
        guide = bool(parameters.get('guide', False))
        stretch = Robot.stretchdict.get(value.strip().lower(), "HeadStretch")
        logger.info("play "+ stretch+ " of speed " + speed +" " + str(repetition) + " times, with guide " + str(guide))
        YanAPI.start_play_motion(name = str(stretch + speed), repeat = repetition)
        if guide:
            YanAPI.set_robot_volume_value(int(parameters.get('volume', 50)))
            self.stretch_guide(stretch)
        self.robot_pause()
        YanAPI.stop_play_motion()

        return "success"

    def turn(self, value, parameters):
        degrees = 0
        try:
            if parameters['body'] == 0:
                degrees = np.clip(int(parameters['degrees']), 0, 75)
                logger.info("turn head to the " + value + " with " +  str(degrees) + " degrees")
            else:
                degrees = int(parameters['degrees'])
                repeat = degrees // 90
                logger.info("turn body  to the " + value + ", " +  str(repeat) + " times")
        except:
            parameters['body'] = 0
            degrees = 70
            logger.info("turn head to the " + value + " with " +  str(degrees) + " degrees")
        
        if value == "left":
            if parameters['body'] == 0:
                logger.info("head turn")
                YanAPI.set_servos_angles({"NeckLR": (90-degrees)}, 2000)
                time.sleep(2)
            else:
                logger.info("body turn")
                YanAPI.start_play_motion(name='TurnLeft', repeat = repeat)
                self.robot_pause()
                YanAPI.stop_play_motion()

        else:
            if parameters['body'] == 0:
                logger.info("head turn")
                YanAPI.set_servos_angles({"NeckLR": (90+degrees)}, 2000)
                time.sleep(2)
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
        left_arm = bool(parameters.get('LeftArm', 0))
        right_arm = bool(parameters.get('RightArm', 0))
        arm_motion_map = {
            'up': {
                (1, 0): 'leftUp',
                (0, 1): 'rightUp',
                (1, 1): 'bothUp'
            },
            'side': {
                (1, 0): 'leftSide',
                (0, 1): 'rightSide',
                (1, 1): 'bothSide'
            },
            'forward': {
                (1, 0): 'leftForward',
                (0, 1): 'rightForward',
                (1, 1): 'bothForward'
            },
            'crane': {
                (1, 0): 'leftCrane',
                (0, 1): 'rightCrane',
                (1, 1): 'bothCrane'
            }
        }
        if (left_arm, right_arm) in arm_motion_map.get(value, {}):
            logger.info(value +" raise")
            logger.info("left arm: " + str(left_arm) + " right arm: " + str(right_arm))
            logger.info("leg motion played: " + str(arm_motion_map[value][(left_arm, right_arm)]))
            YanAPI.set_servos_angles(self.arm_motion[arm_motion_map[value][(left_arm, right_arm)]], 2000)
            time.sleep(2)
        else:
            logger.info("no arm")
            YanAPI.set_servos_angles(self.arm_motion['bothCrane'], 2000)
            time.sleep(2)
        return "success"

    def leg(self, value, parameters):

        left_leg = bool(parameters.get('LeftLeg', 0))
        right_leg = bool(parameters.get('RightLeg', 0))
        time = float(parameters.get('remain_time', 5))
        leg_motion_map = {
            'backward': {
                (1, 0): 'leftBackward',
                (0, 1): 'rightBackward',
                (1, 1): 'bothBackward'
            },
            'forward': {
                (1, 0): 'leftForward',
                (0, 1): 'rightForward',
                (1, 1): 'bothForward'
            }
        }
        if (left_leg, right_leg) in leg_motion_map.get(value, {}):
            logger.info(value +" raise")
            logger.info("left leg: " + str(left_leg) + " right leg: " + str(right_leg))
            logger.info("leg motion played: " + str(leg_motion_map[value][(left_leg, right_leg)]) + " for "+ str(time) + " seconds")
            self.leg_motion(leg_motion_map[value][(left_leg, right_leg)],time)

        else:
            logger.info("no leg")
            self.leg_motion('bothForward')

        return "success"

    def idle(self, value, parameters):
        logger.info("idle for " + value)
        time.sleep(int(value))
        return "success"
    
    def reset(self, value, parameters):
        YanAPI.start_play_motion(name = 'reset')
        self.robot_pause()
        YanAPI.stop_play_motion()
        return "success"