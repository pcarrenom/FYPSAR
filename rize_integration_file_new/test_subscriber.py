import nep
import time

# Create a new node
node = nep.node("subscriber_sample")
sub = node.new_sub('/blackboard','json')

while True:
    s, msg = sub.listen()    # Non-blocking socket
    print(msg)
    time.sleep(5)

