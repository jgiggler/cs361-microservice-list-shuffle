#   randomize in Python
#   Connects REQ socket to tcp://localhost:5555
#   
#

import zmq
import json
context = zmq.Context()

def randomize(list, seed=None):
    #  Socket to talk to server
    print("Connecting to hello world server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    data = {'list': list}
    #create message with seed if present
    if seed is not None:
        data['seed'] = seed
    print("data:", data)
    message = json.dumps(data)
    print(f"Sending request: {message} …")
    socket.send_string(message)

    #  Get the reply.
    message = socket.recv_string()
    response = json.loads(message)
    print(f"Received reply: {response} ")
    

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,10]
    seed = 1
    while True:
        request = input("Shuffle list? y or n\n")
        if request == "y":
            randomize(list)
        if request == "n":
            break
        
    

    