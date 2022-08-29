# End-User Interface Final Year Project
These are the Python scripts that are used to code the Yanshee Robot for the final year project.
## YanAPI checklist
All Yanshee Robots connected remotely must have YanAPI.yan_api_init() function set up.

## Setting up the Yanshee Robot
1. Find the IP Address
    - This can be done by checking the Yanshee App. <span style="color: red"> Note that the robot and the phone must be connected to the same WiFi router. Do not use a WiFi router that dynamically changes its IP address such as eduroam.</span> In the Yanshee App, touch on the top-left icon.
    ![Step 1](images/IP_Address_1.jpg)
    - Click on Setup.
    ![Step 2](images/IP_Address_2.jpg)
    - Then Robot Information.
    ![Step 3](images/IP_Address_3.jpg)
    - The IP Address will be displayed at the bottom of the list.
    ![Step 4](images/IP_Address_4.jpg)
2. Insert it into your code.
    - Make sure to import the YanAPI and a string variable to store the IP Address. Use the function YanAPI.yan_api_init() to connect to the robot.

## Emergency Button
In case of an emergency, push the button on the head of the robot.
![Emergency](Emergency_Stop.jpg)
