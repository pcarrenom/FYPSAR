import YanAPI

#    初始化SDK
# *  @param robot_ip  参数：机器人IP地址
# *  @return 无返回值

ip_addr = '160.69.69.103'
print(YanAPI.get_motion_list())

def robot_pause():
    while YanAPI.get_current_motion_play_state()['data']['status'] != "idle":
        pass

'''
YanAPI.yan_api_init(ip_addr)
YanAPI.start_play_motion(name = movement_name, speed = "slow") #Unknown which movements are available
robot_pause()
YanAPI.start_play_motion(name = 'reset')
#Run 'hostname -I' on Yanshee terminal to retrieve IP Address
'''