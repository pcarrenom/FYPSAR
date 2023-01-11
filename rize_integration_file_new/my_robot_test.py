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

    def animation(self, value, parameters): 
        if value == "headroll":
            print("Time to roll my head")
        
        elif value == "wriststretch":
            print("time to stretch my wrist")

        elif value == "shoulderstretch":
            print("time to stretch my shoulder")

        elif value == "upperlower":
            print("time for some upper and lower stretches")

        elif value == "footrotation":
            print("Let me rotate my foot")

        elif value == "forwardstretch":
            print("forward stretch")

        elif value == "backarch":
            print("Back Arch")

        elif value == "pectoral":
            print("pectoral")

        elif value == "sidebend":
            print("side bends")