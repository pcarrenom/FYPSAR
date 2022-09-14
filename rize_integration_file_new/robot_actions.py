import nep
from rize import *
from my_robot import Robot
import YanAPI

class RIZEAction(object):


    def __init__(self):
        print("Initialising")
        ip_addr = '160.69.69.103'
        #YanAPI.yan_api_init(ip_addr)
        self.rize_robot = ActionEngine("ROS", "listen") #Receives
        self.my_robot = Robot("TestRobot") #Publishes
        print(self.my_robot)
        self.robot_actions = {
            "say": self.my_robot.say,
            "walk": self.my_robot.move,
        }

    def run(self):
        try:
            print("Robot ready")
            self.rize_robot.onConnectSuccess()
            print("Connection success")

            # Set actions
            print("actions activated")
            self.rize_robot.setRobotActions(self.robot_actions)

            # Spin node
            self.rize_robot.spin()
        except:
            self.rize_robot.onConnectError()
            print("There has been a connection error")

if __name__ == '__main__':
    node = RIZEAction()
    print("node run")
    node.run()