import nep
from rize import *
from my_robot import Robot
import logging

class RIZEAction(object):

    def __init__(self):

        self.rize_robot = ActionEngine("ROS", "listen")
        self.my_robot = Robot("TestRobot")

        self.robot_actions = {
            "say": self.my_robot.say,
            "walk": self.my_robot.move,
            "stretch": self.my_robot.stretch,
            "turn": self.my_robot.turn,
            "mode": self.my_robot.mode,
            "arm": self.my_robot.arm,
            "leg": self.my_robot.leg,
            "wait": self.my_robot.idle,
            "reset": self.my_robot.reset,
        }

    def run(self):
        try:
            logging.info('Robot ready')
            self.rize_robot.onConnectSuccess()

            # Set actions
            self.rize_robot.setRobotActions(self.robot_actions)

            # Spin node
            self.rize_robot.spin()
        except:
            self.rize_robot.onConnectError()
            logging.error('There is a connection error')

if __name__ == '__main__':
    # Set up the logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Define the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler
    file_handler = logging.FileHandler('../log/robot_actions.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

#    Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    node = RIZEAction()
    node.run()