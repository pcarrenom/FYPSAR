import YanAPI

#    初始化SDK
# *  @param robot_ip  参数：机器人IP地址
# *  @return 无返回值
def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        print("robot running")
        pass

ip_addr = '160.69.69.103'
YanAPI.yan_api_init(ip_addr)
#print(YanAPI.get_motion_list())
YanAPI.set_robot_volume_value(70)
YanAPI.start_play_motion(name = 'walk', direction='right', repeat = 3)
robot_pause()         
YanAPI.start_play_motion(name = 'reset')
"""
distance = float(input("Type distance in metres: "))
repetition = int(distance // 0.06)
YanAPI.start_play_motion(name = 'walk', direction="forward",repeat=repetition,speed="slow") #One iteration 6cm
robot_pause()
YanAPI.start_play_motion(name = 'reset')
"""
#YanAPI.start_play_motion(name = 'TurnLeft', speed = "slow") #Unknown which movements are available
#robot_pause()
#YanAPI.start_play_motion(name = 'reset')
#print(YanAPI.get_motion_list())
#print(YanAPI.get_robot_battery_info())

#print(YanAPI.get_voice_iat())
#YanAPI.start_play_motion(name = 'squat', speed = "slow")
#robot_pause()
#YanAPI.start_play_motion(name = 'reset')

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
