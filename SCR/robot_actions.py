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
            "animation": self.my_robot.stretch,
            "turn": self.my_robot.turn,
            "mode": self.my_robot.mode,
            "walk_toward": self.my_robot.arm,
            "track_redball_with": self.my_robot.leg,
            "wait": self.my_robot.idle,
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