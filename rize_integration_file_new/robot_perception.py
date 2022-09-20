import nep
import time
import YanAPI

node = nep.node('python_sender')
pub = node.new_pub('/blackboard','json')

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
    msg = {'primitive':''}	
    input_f = input("Type F to actuate: ")
    if input_f == 'F':
        msg = {'primitive':'touched', 'input':{"head":1}, "robot":"ROS"}	
        pub.publish(msg)
        print("perception send")

    
    time.sleep(10)