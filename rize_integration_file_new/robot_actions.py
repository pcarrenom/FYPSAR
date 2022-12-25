import nep
from rize import *
from my_robot import Robot

class RIZEAction(object):

    def __init__(self):

        self.rize_robot = ActionEngine("ROS", "listen")
        self.my_robot = Robot("TestRobot")

        self.robot_actions = {
            "say": self.my_robot.say,
            "walk": self.my_robot.move,
            "headroll": self.my_robot.headroll,
            "wriststretch": self.my_robot.wriststretch,
            "shoulderstretch": self.my_robot.shoulderstretch,
            "upperlower": self.my_robot.upperlower,
            "footrotation": self.my_robot.footrotation,
            "forwardstretch": self.my_robot.forwardstretch,
            "sidebend": self.my_robot.sidebend,
            "backarch": self.my_robot.backarch,
            "pectoralstretch": self.my_robot.pectoralstretch,
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