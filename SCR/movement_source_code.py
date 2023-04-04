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

#    初始化SDK
# *  @param robot_ip  参数：机器人IP地址
# *  @return 无返回值
def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass
def speech_pause():
    while YanAPI.get_voice_tts_state()['status'] != "idle":
        pass
print("connected")
ip_addr = config_data["ip"]["robot"]
YanAPI.yan_api_init(ip_addr)
#print(robot_actions)
#0print(YanAPI.get_motion_list_value())
#YanAPI.set_robot_volume_value(100)
#YanAPI.set_robot_language('en')


YanAPI.start_voice_tts("It's time to do a head stretch, Turn your head to the left and hold for 10 seconds.", interrupt=False)
speech_pause()
YanAPI.stop_voice_tts()
time.sleep(10)
YanAPI.start_voice_tts("Now, Turn your head to the right and hold for another 10 seconds.", interrupt=False)
speech_pause()
YanAPI.stop_voice_tts()