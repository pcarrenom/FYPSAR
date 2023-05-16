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
    walkingdict = {
        'steady':{
            "RightHipLR":90,
            "RightHipFB":34,
            "RightKneeFlex":25,
            "RightAnkleFB":137,
            "RightAnkleUD":90,
            "LeftHipLR":90,
            "LeftHipFB":147,
            "LeftKneeFlex":156,
            "LeftAnkleFB":45,
            "LeftAnkleUD":90         #Get Robot Ready
        },
        'leftForward':{
            "RightHipLR":98,
            "RightHipFB":46,
            "RightKneeFlex":35,
            "RightAnkleFB":135,
            "RightAnkleUD":78,
            "LeftHipLR":102,
            "LeftHipFB":150,
            "LeftKneeFlex":147,
            "LeftAnkleFB":60,
            "LeftAnkleUD":70
           #Lifts Left Foot forward
        },
        'leftBackward':{
            "RightHipLR":99,
            "RightHipFB":32,
            "RightKneeFlex":28,
            "RightAnkleFB":128,
            "RightAnkleUD":78,
            "LeftHipLR":102,
            "LeftHipFB":129,
            "LeftKneeFlex":156,
            "LeftAnkleFB":30,
            "LeftAnkleUD":65            #Lifts Left Foot backwards
        },

        'rightBackward':{
            "RightHipLR":73,
            "RightHipFB":55,
            "RightKneeFlex":26,
            "RightAnkleFB":159,
            "RightAnkleUD":113,
            "LeftHipLR":79,
            "LeftHipFB":148,
            "LeftKneeFlex":152,
            "LeftAnkleFB":49,
            "LeftAnkleUD":100              #Lifts Right foot backwards
        },

        'rightForward':{
            "RightHipLR":78,
            "RightHipFB":30,
            "RightKneeFlex":40,
            "RightAnkleFB":117,
            "RightAnkleUD":104,
            "LeftHipLR":82,
            "LeftHipFB":131,
            "LeftKneeFlex":143,
            "LeftAnkleFB":45,
            "LeftAnkleUD":100          #Lifts Right foot forward
        }
    }

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
        YanAPI.start_voice_tts("I have successfully connected to Robot Actions.", interrupt=False)
        YanAPI.set_robot_led("button", "purple", "on")
        YanAPI.start_play_motion(name='reset')

    def robot_pause(self):
        while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
            pass

    def speech_pause(self):
        while YanAPI.get_voice_tts_state()['status'] != "idle":
            pass

    def my_walk(self, speedLevel, direction, steps):
        speed = round(-8.56*speedLevel + 1086)
        YanAPI.set_servos_angles(Robot.walkingdict['steady'],300)
        time.sleep(0.25)
        if direction == 'forward':
            for i in range(steps):
                YanAPI.set_servos_angles(Robot.walkingdict['leftBackward'],speed)
                time.sleep(speed/2000)
                YanAPI.set_servos_angles(Robot.walkingdict['leftForward'],round(speed*0.9))
                time.sleep(speed*0.84/2000)
                YanAPI.set_servos_angles(Robot.walkingdict['rightBackward'],speed)
                time.sleep(speed/2000)
                YanAPI.set_servos_angles(Robot.walkingdict['rightForward'],round(speed*0.9))
                time.sleep(speed*0.84/2000)
        else:
            for i in range(steps):
                YanAPI.set_servos_angles(Robot.walkingdict['leftForward'],speed)
                time.sleep(speed/2000)
                YanAPI.set_servos_angles(Robot.walkingdict['leftBackward'],round(speed*0.9))
                time.sleep(speed*0.84/2000)
                YanAPI.set_servos_angles(Robot.walkingdict['rightForward'],speed)
                time.sleep(speed/2000)
                YanAPI.set_servos_angles(Robot.walkingdict['rightBackward'],round(speed*0.9))
                time.sleep(speed*0.84/2000)

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
            steps = int(parameters.get('steps', 1))
        except:
            steps = 1
        try:
            speed_act = int(np.clip(int(parameters['speed']), 1, 100))
        except:
            speed_act = 50
        speed_dict = {0: "very slow", 1: "slow", 2: "normal", 3: "fast", 4: "very fast"}
        if value not in ['backwards','forward','left','right']:
            value = "forward"
            

        logger.info("move "+ value + " by " + str(steps)+ " times, with speed " + str(speed_act))
        if value == "forward" or value == "backwards":
            self.my_walk(speed_act, value, steps)
        else:
            for i in range(steps):
                speedString = speed_dict.get(np.clip(speed_act//5, 0, 4))
                YanAPI.start_play_motion(name = 'walk', direction = value, speed = speedString)
                self.robot_pause()
    
        YanAPI.stop_play_motion()
        
        time.sleep(2)
        return "success"
    
    def sidestep(self, value, parameters):
        try:
            steps = int(parameters.get('steps', 1))
        except:
            steps = 1
        try:
            speed_act = int(np.clip(int(parameters['speed']), 1, 100))
        except:
            speed_act = 50
        speed_dict = {0: "very slow", 1: "slow", 2: "normal", 3: "fast", 4: "very fast"}
        if value not in ['backwards','forward','left','right']:
            value = "left"
            

        logger.info("move "+ value + " by " + str(steps)+ " times, with speed " + str(speed_act))
        if value == "forward" or value == "backwards":
            self.my_walk(speed_act, value, steps)
        else:
            for i in range(steps):
                speedString = speed_dict.get(np.clip(speed_act//5, 0, 4))
                YanAPI.start_play_motion(name = 'walk', direction = value, speed = speedString)
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
        guide = bool(parameters.get('speechGuide', False))
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
        body = bool(parameters.get('body',0))
        head = bool(parameters.get('head',0))
        if body == 0 and head == 1:
            degrees = int(np.clip(int(parameters.get(degrees,70)), 0 ,75))
            logger.info("turn head to the " + value + " with " +  str(degrees) + " degrees")
        elif body == 1:
            degrees = int(np.minimum(int(parameters.get(degrees,180)), 0))
            repeat = int(np.clip(degrees // 180, 1, None))
            logger.info("turn body to the " + value + ", " +  str(repeat) + " times")
        else:
            body = 0
            head = 1
            degrees = int(np.clip(int(parameters.get(degrees,70)), 0 ,75))
            logger.info("Default try turn head to the " + value + " with " +  str(degrees) + " degrees")
            
        
        if value == "left":
            if body == 1:
                logger.info("body turn")
                YanAPI.start_play_motion(name='TurnLeft', repeat = repeat)
                self.robot_pause()
                YanAPI.stop_play_motion()
                
            else:
                logger.info("head turn")
                YanAPI.set_servos_angles({"NeckLR": (90-int(degrees))}, 2000)
                time.sleep(2)

        else:
            if body == 1:
                logger.info("body turn")
                YanAPI.start_play_motion(name='TurnRight', repeat = repeat)
                self.robot_pause()
                YanAPI.stop_play_motion()
            else:
                logger.info("head turn")
                YanAPI.set_servos_angles({"NeckLR": (90+int(degrees))}, 800)
                time.sleep(0.8)
                
        return "success"
    
    def mode(self, value, parameters):
        
        if value == "rest":
            YanAPI.start_play_motion(name = 'SleepMode')
            self.robot_pause()
            logger.info("mode sleep")
        else:
            YanAPI.start_play_motion(name = 'Awake')
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
    
    def shoulder(self, value, parameters):
        left_arm = bool(parameters.get('LeftArm', 0))
        right_arm = bool(parameters.get('RightArm', 0))
        if value not in ['forward','side','backwards']:
            value = 'forward'
        logger.info(value +" raise " + " with left arm " + str(left_arm) + " and right arm " + str(right_arm))
        if value == 'side':
            angle = int(np.clip(int(parameters.get('angle', 0)),0,180))
            logger.info("angle value: " + str(angle))
            if left_arm == 1:
                YanAPI.set_servos_angles({"LeftShoulderRoll": 90, "LeftShoulderFlex": angle},2000)
            if right_arm == 1:
                YanAPI.set_servos_angles({"RightShoulderRoll":90,"RightShoulderFlex": 180-angle},2000)
            time.sleep(2)
        else:
            angle = int(np.clip(int(parameters.get('angle', 0)),0,90))
            if value == "backwards":
                angle = -angle
            logger.info("angle value: " + str(angle))
            if left_arm == 1:
                YanAPI.set_servos_angles({"LeftShoulderRoll":180, "LeftShoulderFlex": 90-angle},2000)
            if right_arm == 1:
                YanAPI.set_servos_angles({"RightShoulderRoll":0,"RightShoulderFlex": 90+angle},2000)
            time.sleep(2)

    def elbow(self, value, parameters):
        left_arm = bool(parameters.get('LeftArm', 0))
        right_arm = bool(parameters.get('RightArm', 0))
        logger.info(value +" raise " + " with left arm " + str(left_arm) + " and right arm " + str(right_arm))
        #left_shoulder = YanAPI.get_servo_angle_value("LeftShoulderFlex")
        #right_shoulder = YanAPI.get_servo_angle_value("RightShoulderFlex")
        if value not in ['flexion','extension']:
            value = 'flexion'
        angle = int(np.clip(int(parameters.get('angle', 0)),0,90))
        if value == 'extension':
            angle = -angle
        #else:
        #    if right_arm == 1 and right_shoulder > 135 and angle > (180-right_shoulder):
        #        angle = 180-right_shoulder
        #    elif left_arm == 1 and left_shoulder < 45 and angle > left_shoulder:
        #        angle = left_shoulder
        if left_arm == 1:
            YanAPI.set_servos_angles({"LeftElbowFlex": 90-angle},2000)
        if right_arm == 1:
            YanAPI.set_servos_angles({"RightElbowFlex": 90+angle},2000)
        time.sleep(2)

    def leg(self, value, parameters):

        left_leg = bool(parameters.get('LeftLeg', 0))
        right_leg = bool(parameters.get('RightLeg', 0))
        time = float(parameters.get('hold_time', 5))
        leg_motion_map = {
            'backwards': {
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
        logger.info("Robot resets")
        YanAPI.start_play_motion(name = 'reset')
        self.robot_pause()
        YanAPI.stop_play_motion()
        return "success"