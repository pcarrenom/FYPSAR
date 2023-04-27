# End-User Interface Final Year Project
These are the Python scripts that are used to code the Yanshee Robot for the final year project.

## Setting up the Yanshee Robot
1. Find the IP Address
    - This can be done by checking the Yanshee App. <span style="color: red"> Note that the robot and the phone must be connected to the same WiFi router. Do not use a WiFi router that dynamically changes its IP address such as eduroam.</span> In the Yanshee App, touch on the top-left icon.
    ![Step 1](data/images/IP_Address_1.jpg)
    - Click on Setup.
    ![Step 2](data/images/IP_Address_2.jpg)
    - Then Robot Information.
    ![Step 3](data/images/IP_Address_3.jpg)
    - The IP Address will be displayed at the bottom of the list.
    ![Step 4](data/images/IP_Address_4.jpg)
2. Insert it into your code.
    - Make sure to import the YanAPI and a string variable to store the IP Address. Use the function YanAPI.yan_api_init() to connect to the robot.

### YanAPI checklist
All Yanshee Robots connected remotely must have YanAPI.yan_api_init() function set up.

### Emergency Button
In case of an emergency, push the button on the head of the robot. <br />
<img src="data/images/Emergency_Stop.jpg" alt="Emergency" width="260">

## Setting up the Environment and Basecode
### Minimum Requirements
1. Access to a Linux-like terminal
2. Conda (installation instructions here https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
3. Git

### Python Environment
It is recommended to create a virtual environment for development. This will help with dependency management. It will help to make the project self-contained and easier to share and recreate. Below are instructions on creating a virtual environment and installing all required dependencies using conda. Another alternative is to use venvs + pip tools.

1. Create a new conda environment for the project
    ```console
    $ conda create -n <name of your environment>
    ```
2. Install the following dependencies using pip
    ```console
    $ conda activate <name of your environment>
    $ pip install nep transitions rize
    ```
3. Additional dependencies to work with the Yanshee robot might be needed, such as python 3.5
    ```console
    $ pip install python=3.5
    ```

### Base Code and RIZE Interface
1. Create a new folder (The name New_Code is used as an example). Direct to it with the command
    ```console
    $ cd ~/New_Code
    ```
    and eventually clone the following repository with this command.
    ```console
    $ git clone https://github.com/jjah0001/FYPSAR
    ```
2. Follow these instructions to install nvm https://github.com/nvm-sh/nvm#install--update-script
3. Close the terminal used to install nvm and open a new one
4. Install the latest stable version of Node.js
    ```console
    $ nvm install --lts
    ```
5. Activate the latest version of Node.js in your terminal
    ```console
    $ nvm use --lts
    ```
6. Go to the Open-RIZE-beta folder and install all required dependencies
    ```console
    $ npm install
    ```
7. Add the following folder hierarchy to your Documents. All projects will be stored in ~Documents/Rize/projects
![Directory](data/images/directory.png)
8. Using four windows in a terminal, activate your environment that you created earlier, then direct each terminal to your folder directory by typing the following to each window.
    ```console
    $ conda activate <name of your environment>
    $ cd ~/New_Code
    ```
    In sequence, execute the following in each separate window:
    
    1. 
    ```console
    $ cd FYPSAR/SCR
    $ python local_master.py
    ```
    2. 
    ```console
    $ cd FYPSAR/RIZE
    $ npm start
    ```
    3. 
    ```console
    $ cd FYPSAR/SCR
    $ python robot_actions.py
    ```
    4. 
    ```console
    $ cd FYPSAR/SCR
    $ python robot_perception.py
    ```
