"""
Sockets and Network Programming

We're talking about how to send data over networks, how to exchange data,
 how to build connections between clients and servers

Socket - it's the endpoint of a communication channel
 when you have a communication in a network you always have two endpoints which we call sockets
 you have a server and a client, or two clients, whatever
 two sockets that try to exchange some data
 
 that communication may happen in the same proccess, or accross different continents over the internet
 sockets are not limited to your network in your home, they can also be used over the internet - a big network

In Python we have a lot of different access levels when it comes to networking
 if we're dealing with sockets, we're always dealing with the lower levels of connectivity
 we have the connection oriented protocol - TCP
 and the connectionless protocol - UDP

If we want to use some higher level/leyers protocol, we'd need to use applications like
   FTP, HTTP, and the different modules that we have because they would run on the application layer - 7
We're dealing with TCP and UDP and they run on the transport layer - 4 - look up the OSI model
""" 

import socket

# now we have to answer 4 questions

# 1.) Are we going to use the internet socket or the UNIX socket
#    we're not dealing at the UNIX level here, we want to have a network socket 
#     so we pick the internet socket
#    This is important when we define the socket we define what kind it is

# 2.) What kind of protocol will we use? TCP or UDP
#    TCP - connection oriented, better for any sensible data
#           i.e. if you want all the data to be sent and received, but it's slower than UDP
#           if you want to transfer some very accurate data TCP is bett
#    UDP - you have the risk of losing some data but it's way faster
#            think Online video games, or Skype calls, UDP is the better choice
#        
#   In this case we're going to transfer messages and we're going to use TCP
  
# 3.) Which IP are we going to use / which IP are we going to connect to
#       / which IP do we want to host our server on?

# 4.) Which port are we going to use?
#       are we going to use 3333 or 2160?
#       we need to take care of the reserved ports, and the standardized ports
#        that's why maybe port 80 isn't the best idea because it's usually for HTTP
# #

# s = socket.socket(which kind of socket, specify the protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# internet socket - AF_INET

# TCP - SOCK_STREAM
# UDP - SOCK_DGRAM

"""
this is now just a socket that works with TCP and is an internet socket
 we can now choose what we want to do with this socket,
 do we just want to connect to another socket on the internet, 
 or if we have another program running somewhere else on a specific port, 
 we might want to connect with the socket to this

To learn how sockets work, we're going to create our own server here
 basically we're going to make our own socket that listens for input
 and then we're going to create a second Python script - "a client" that connects to our socket
"""

# we use the bind method to pass the tuple of the IP address and the port that we want to run the socket on
# IP - localhost '127.0.0.1'   because we're running on our own machine
# Port 55555
# bind method - this is the host I want my socket to run on and port

s.bind(('127.0.0.1', 55555)) 

# to have a server, we put our socket in listen mode
# are any clients trying to connect or is anything happening

s.listen()

# now we run an endless loop that accepts the connection
while True:
    client, address = s.accept()
    # accept - method that we want to use when the client 
    #  is trying to connect to the server/socket and we want to accept it
    # endless loop, we accept every single client
    # we get an address and a client we can use to send the information
    #  even though this socket/script is the server script
    #  we get a client in return which we can use to send data to the client

    print("Connected to {}".format(address))
    client.send("You are connected!".encode('UTF-8')) # .encode() - default poglej desno dol na VSCode
    client.close() # we always have to close the client so that we don't have unlimited clients running in the background


"""
This is basically our server script right now

Now we need to connect to the server using our client, so we're going to make
 a new python script thats going to connect to our server

We're first going to run our server, and then run our client

I can run this on a public server and host it, and someone else can connect with a client to my machine
"""

# Connected to ('127.0.0.1', 55602)
# for some reason it connected to a different port than specified

app.get("/asd", (req,res) => {
    console.log(res, req)
})