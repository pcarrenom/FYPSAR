import nep
import time
import sys
sys.path.append("../Posture-Detection/Demo/")
from Detection import Detection


node = nep.node('python_sender')
pub = node.new_pub('/blackboard','json')

detector = Detection(pub)
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
#         # msg = {'primitive': 'human_detected', 'input':{"yes":1}, "robot":"ROS"}
#         # msg = {'primitive': 'posture_change', 'input':{"yes":1}, "robot":"ROS"}
#         # msg = {'primitive': 'posture_detected', 'input':{"slouching":1}, "robot":"ROS"}
#         # msg = {'primitive': 'posture_detected', 'input':{"neck_extension":1}, "robot":"ROS"}
#         # msg = {'primitive': 'posture_detected', 'input':{"forward_head":1}, "robot":"ROS"}
#         # msg = {'primitive': 'posture_detected', 'input':{"leaning_forward":1}, "robot":"ROS"}
#         # msg = {'primitive': 'posture_detected', 'input':{"twisting":1}, "robot":"ROS"}
#         pub.publish(msg)
#         print("perception send")
#     time.sleep(10)