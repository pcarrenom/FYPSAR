# Code for test purposes ONLY
import nep
from rize import *
from my_robot_test import Robot

class RIZEAction(object):

    def __init__(self):

        self.rize_robot = ActionEngine("ROS", "listen")
        self.my_robot = Robot("TestRobot")

        self.robot_actions = {
            "say": self.my_robot.say,
            "walk": self.my_robot.move,
        }

    def run(self):
        try:
            print("Robot ready")
            self.rize_robot.onConnectSuccess()

            # Set actions
            self.rize_robot.setRobotActions(self.robot_actions)

            # Spin node
            self.rize_robot.spin()
        except:
            self.rize_robot.onConnectError()
            print("There has been a connection error")

if __name__ == '__main__':
    node = RIZEAction()
    node.run()