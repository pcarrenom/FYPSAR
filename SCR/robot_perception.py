import nep
import time
import sys
sys.path.append("../Posture-Detection/Demo/")
from Detection import Detection

node = nep.node('python_sender')
pub = node.new_pub('/blackboard','json')

detector = Detection()
detector.start_detection()

# # Dummy perceptual function
# def isHeadTouched():
# 	return True

# #  Publish the current state when 
# while True:
#     # Here your code that recognize something
#     # Example: 
#     head_touched = isHeadTouched()
#     if head_touched:
#         msg = {'primitive':'touched', 'input':{"head":1}, "robot":"ROS"}	
#         pub.publish(msg)
#         print("perception send")
#     time.sleep(5)