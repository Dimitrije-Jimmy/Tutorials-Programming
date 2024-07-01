"""
This is our client script that will connect to our server script

We're going to create the same socket to be able to connect to our server
 we need to use the same protocol and port
 you can't send with TCP and receive with UDP
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now we're not using bind and listen method because we're not making a server we're connecting to it
# we say .connect((IP, Port))  has to be tuple
s.connect(('127.0.0.1', 55555))

# Im trying to receive the message that the client sends
# .recv(bites) - we specify how many bites we want to receive
#  in this case 1024 bites should be enough

message = s.recv(1024)
s.close()

print(message.decode()) # we need to decode it

# You are connected!
# we received the message
