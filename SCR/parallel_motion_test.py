# Test code of robot doing parallel actions
import time
import os
import sys
import json
with open('../config/config.json', 'r') as config_file:
    config_data = json.load(config_file)

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, config_data["directory"]["yan"])) 
import YanAPI
robot_ip = config_data["ip"]["robot"]

def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

YanAPI.yan_api_init("192.168.0.106")
# YanAPI.start_play_motion(name = 'walk',repeat = 4, direction = 'forward')
# robot_pause()
# YanAPI.start_play_motion(name = 'reset')

pose1 = {
            "RightShoulderRoll":92,
            "RightShoulderFlex":148,
            "RightElbowFlex":133,
            "LeftShoulderRoll":88,
            "LeftShoulderFlex":36,
            "LeftElbowFlex":48,
            "RightHipLR":90,
            "RightHipFB":34,
            "RightKneeFlex":25,
            "RightAnkleFB":137,
            "RightAnkleUD":90,
            "LeftHipLR":90,
            "LeftHipFB":147,
            "LeftKneeFlex":156,
            "LeftAnkleFB":45,
            "LeftAnkleUD":90,
            "NeckLR":90             #Get Robot Ready
        }
pose2 = {
            "RightShoulderRoll":90,
            "RightShoulderFlex":143,
            "RightElbowFlex":131,
            "LeftShoulderRoll":90,
            "LeftShoulderFlex":34,
            "LeftElbowFlex":45,
            "RightHipLR":98,
            "RightHipFB":46,
            "RightKneeFlex":35,
            "RightAnkleFB":135,
            "RightAnkleUD":78,
            "LeftHipLR":102,
            "LeftHipFB":150,
            "LeftKneeFlex":147,
            "LeftAnkleFB":60,
            "LeftAnkleUD":70,
            "NeckLR":90             #Lifts Left Foot forward
        }

pose3 = {
            "RightShoulderRoll":108,
            "RightShoulderFlex":143,
            "RightElbowFlex":131,
            "LeftShoulderRoll":121,
            "LeftShoulderFlex":34,
            "LeftElbowFlex":45,
            "RightHipLR":99,
            "RightHipFB":32,
            "RightKneeFlex":28,
            "RightAnkleFB":128,
            "RightAnkleUD":78,
            "LeftHipLR":102,
            "LeftHipFB":129,
            "LeftKneeFlex":156,
            "LeftAnkleFB":30,
            "LeftAnkleUD":65,
            "NeckLR":90                 #Lifts Left Foot backwards
        }

pose4 = {
            "RightShoulderRoll":59,
            "RightShoulderFlex":146,
            "RightElbowFlex":135,
            "LeftShoulderRoll":72,
            "LeftShoulderFlex":37,
            "LeftElbowFlex":49,
            "RightHipLR":73,
            "RightHipFB":55,
            "RightKneeFlex":26,
            "RightAnkleFB":159,
            "RightAnkleUD":113,
            "LeftHipLR":79,
            "LeftHipFB":148,
            "LeftKneeFlex":152,
            "LeftAnkleFB":49,
            "LeftAnkleUD":100,
            "NeckLR":90                 #Lifts Right foot backwards
        }

pose5 = {
            "RightShoulderRoll":90,
            "RightShoulderFlex":146,
            "RightElbowFlex":135,
            "LeftShoulderRoll":90,
            "LeftShoulderFlex":37,
            "LeftElbowFlex":49,
            "RightHipLR":78,
            "RightHipFB":30,
            "RightKneeFlex":40,
            "RightAnkleFB":117,
            "RightAnkleUD":104,
            "LeftHipLR":82,
            "LeftHipFB":131,
            "LeftKneeFlex":143,
            "LeftAnkleFB":45,
            "LeftAnkleUD":100,
            "NeckLR":90                 #Lifts Right foot forward
        }

YanAPI.set_servos_angles(pose1,500)
time.sleep(0.6)
for i in range(4):
    YanAPI.set_servos_angles(pose3,200)
    time.sleep(0.15)
    YanAPI.set_servos_angles(pose2,200)
    time.sleep(0.15)
    YanAPI.set_servos_angles(pose4,200)
    time.sleep(0.15)
    YanAPI.set_servos_angles(pose5,200)
    time.sleep(0.15)

YanAPI.start_play_motion(name = 'reset')