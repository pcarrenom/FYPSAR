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
YanAPI.start_play_motion(name = '青春修炼手册', speed = "slow")
robot_pause()
YanAPI.start_play_motion(name = 'reset')

#def robot_pause():
#    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
#        pass


#Y
#YanAPI.set_robot_language('zh')
#print(YanAPI.get_media_music_list())
#YanAPI.start_play_motion(name = 'walk', speed = "slow") #Unknown which movements are available
#robot_pause()
#YanAPI.start_play_motion(name = 'reset')
#Run 'hostname -I' on Yanshee terminal to retrieve IP Address
