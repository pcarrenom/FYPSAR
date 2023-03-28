# Test code
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

#    初始化SDK
# *  @param robot_ip  参数：机器人IP地址
# *  @return 无返回值
def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

def stretch_guide():
    YanAPI.start_voice_tts("Have yourself doing this stretch when seated. Roll one of your foot.", interrupt=False)
    time.sleep(11)
    YanAPI.start_voice_tts("Now roll the other foot", interrupt=False)

ip_addr = '160.69.69.103'
YanAPI.yan_api_init(ip_addr)
#print(robot_actions)

YanAPI.set_robot_volume_value(100)
#YanAPI.set_robot_language('en')
#YanAPI.start_play_motion(name = 'ActionAging1', speed = 'slow')
#interrupt = input("Type X to stop: ")

YanAPI.start_play_motion(name = 'FootRotationNormal')
stretch_guide()
robot_pause()
YanAPI.start_play_motion(name = 'reset')