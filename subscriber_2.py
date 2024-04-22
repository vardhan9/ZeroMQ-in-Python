import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:3000')
socket.setsockopt_string(zmq.SUBSCRIBE,'')

listner = 0
while(True):
    message = socket.recv_pyobj()
    if(message.get(listner)!= None):
        print(message.get(listner)) # prints only the message with index 0