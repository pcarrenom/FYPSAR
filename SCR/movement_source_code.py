# Test code
import sys
sys.path.append("/Users/jeffreyjahja/Documents/Uni/FYP/Code/FYPSAR/third-party") #Please change directory accordingly
#print(sys.path)
import YanAPI

#    初始化SDK
# *  @param robot_ip  参数：机器人IP地址
# *  @return 无返回值
def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

ip_addr = '160.69.69.103'
YanAPI.yan_api_init(ip_addr)
print(YanAPI.get_motion_list())
#print(robot_actions)

YanAPI.set_robot_volume_value(100)
#YanAPI.set_robot_language('en')
#YanAPI.start_voice_tts('Hello, I am Yanshee, I am ready to play some music', interrupt=False)
#YanAPI.start_play_motion(name = 'ActionAging1', speed = 'slow')
#interrupt = input("Type X to stop: ")
print(YanAPI.get_motion_list_value())
YanAPI.start_play_motion(name = 'LeftTurn')
robot_pause()
