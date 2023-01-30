#%%
import zmq
import time
import nep
import sys
sys.path.append("/Users/jeffreyjahja/Documents/Uni/FYP/Code/FYPSAR/third-party") #Please change directory accordingly
import YanAPI


if sys.version_info[0] == 3:
    import _thread as thread
else:
    import thread

try:
    if sys.argv[1] == "network":
        # Get IP of the PC
        ip = nep.getMyIP()
        print ("NEP MASTER in " + ip)
    else:
        print ("NEP MASTER in local-host")
        ip = "127.0.0.1"
except:
    print ("NEP MASTER in local-host")
    ip = "127.0.0.1"
    

print("system info printed")
#print (sys.version) 
server = nep.master(ip) 
print("Running Server")  
  
server.run()#Code is unable to proceed from this line
print("Run Ended")

perception_node = nep.node("python_sender")
sub_perception = perception_node.new_pub('/blackboard','json')


#rize_node = nep.node("rize")
#action_node = nep.node("ROS")

