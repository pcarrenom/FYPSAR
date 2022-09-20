#Code for test purposes ONLY
import time
import YanAPI

class Robot():

    def __init__(self, name):
        self.name = name
        print("Robot Connected")

    def say(self, value, parameters):
        print("Hello, I'm saying something")
        print("Value", value, "Parameters", parameters)
        # Insert YanAPI
        
        time.sleep(2)
        return "success"

    def move(self, value, parameters):
        print("Hello, I'm moving")
        print("Value", value, "Parameters", parameters)
        if value == 'forwards':
            print("往前走")
        elif value == 'backwards':
            print("往后走")
        
        time.sleep(2)
        return "success"