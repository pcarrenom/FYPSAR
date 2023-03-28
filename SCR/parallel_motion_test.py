# Test code of robot doing parallel actions
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

YanAPI.yan_api_init(robot_ip)
YanAPI.start_voice_tts('Hello. Nice to meet you. I am walking towards you', interrupt=False)
YanAPI.start_play_motion(name = 'walk',repeat = 2, direction = 'forward')
robot_pause()
YanAPI.start_play_motion(name = 'reset')
robot_pause()
YanAPI.start_play_motion(name = 'FootRotationSlow')
robot_pause()
YanAPI.start_play_motion(name = 'reset')