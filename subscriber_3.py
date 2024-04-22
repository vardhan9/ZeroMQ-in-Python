import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:3000')
socket.setsockopt_string(zmq.SUBSCRIBE,'')

listner = [0,1,2]
while(True):
    message = socket.recv_pyobj()
    msg_keys = list(message.keys())
    if msg_keys:  # check if there are keys in the message
        msgIndex = msg_keys[0]
        if msgIndex in listner:
            print(message.get(msgIndex))