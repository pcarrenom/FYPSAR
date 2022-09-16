import nep
import time
import YanAPI

node = nep.node('python_sender')
pub = node.new_pub('/blackboard','json')
robot_ip = '160.69.69.103'

# Dummy perceptual function
def isHeadTouched():
    #Return true under condititon
	return True
    #Return false under condition

#  Publish the current state when 
while True:
    # Here your code that recognize something
    # Example: 
#    sendIP(robot_ip)
    input_f = input("Type F to actuate: ")
    if input_f == 'F':
        msg = {'primitive':'touched', 'input':{"head":1}, "robot":"ROS"}	
        pub.publish(msg)
        print("perception send")
#    try:
#        robot_info = YanAPI.get_robot_version_info(robot_ip)
#        battery_info = YanAPI.get_robot_battery_info()
#        battery_life = battery_info['data']["percent"]
#        print("Robot Battery Life: " + str(battery_life))
#        msg = {'primitive':'touched', 'input':{"head":1}, "robot":"Yanshee"}	
#        pub.publish(msg)
#        print("perception send")
#    except:
#        pass
    
    time.sleep(10)