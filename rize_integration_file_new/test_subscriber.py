import nep
import time

# Create a new node
node = nep.node("subscriber_sample")
#sub_per = node.new_sub('/blackboard','json')
sub_rize = node.new_sub('action_state','json')

while True:
    s, msg = sub_rize.listen()    # Non-blocking socket
    if s == True:
        print(msg)
    else:
        time.sleep(5)

