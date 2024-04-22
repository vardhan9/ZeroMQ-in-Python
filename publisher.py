import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:3000')

messages = ['first', 'second', 'third']

currentMessage = 0

while(True):
    sleep(1)
    socket.send_pyobj({currentMessage:messages[currentMessage]})

    if(currentMessage ==2):
        currentMessage = 0
    else:
        currentMessage = currentMessage + 1