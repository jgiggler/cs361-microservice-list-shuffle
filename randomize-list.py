#   server in Python
#   Binds REP socket to tcp://*:5555
#   
#

import zmq
import random
import json

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Waiting for messages...")
    while True:
        #  Wait for next request from client
        message = socket.recv()

        data = json.loads(message)
        list = data.get('list', [])
        seed = data.get('seed', None)

        print(f"Deserialized: list = {list} seed = {seed}")
        #  Randomize the list
        if seed is not None:
            random.seed(seed)
        random.shuffle(list)
        
        print(list)

        #  Send reply back to client
        response = json.dumps(list)
        print(f"Sending reponse: {response}")
        socket.send_string(response)

if __name__ == "__main__":
    main()