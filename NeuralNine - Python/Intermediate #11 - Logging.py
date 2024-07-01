# Logging
"""
very important topic, every system introduces a lot of messages, states, errors, conditions
 these need to be stored somewhere, because if you have a system crashing
 you need an administrator/someone who knows what they're doing to look at that system
Sometimes we make backups and need to log when it was made
 or we have a condition we'd like to know "you're running low on space"
When something crashes, doesn't work the way we expected it too, we want to know why,
 how to prevent it, ...
Everything gets logged. The larger a system gets you need a systematic way to do it
Not every message is equally important but the print statement treats it as such
 sometimes we need critical messages, security levels, priorities, ...
"""


# the 5 SECURITY LEVELS when it comes to logging
# 
# DEBUG - when testing, playing around, troubleshooting, for devs, nothing that interests the end consumer
# INFO - all about informational messages, "made 2 backups rn", "17 users online rn", ...
# WARNING - nothing bad happened yet, but something might happen, "you're running low on space"
# ERROR - classical exception, error in code, important, something needs to be done, but system not crashed
# CRITICAL - when an esential part of your system breaks down, requires immediate attention, "server is down", "power supply is down"

import os
import logging

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# we can either use the default root logger, more or less setup and created
#  or we can create our own logger, with our own name, settings, ...

# Default Root Logger

# logging.securitylevel
logging.info("You have got 20 mails in your inbox!")
logging.critical("All components failed!")
"""
output: CRITICAL:root:All components failed!

it will only print the critical message

Python has the default security level of Warning

if you have a security level DEBUG, you see all the messages, 
if you have the CRITICAL you only see the critical message because it's the highest security level
it builds in priorities
"""

logging.warning("You have got 20 mails in your inbox!")
logging.critical("All components failed!")
# now it prints both

# we can change the basic level
logging.basicConfig(level=logging.DEBUG)
# this means we will see all messages even info 

logging.info("You have got 20 mails in your inbox!")
logging.critical("All components failed!")


# Creating my own logger
logging.basicConfig(level=logging.INFO) # this doesn't work for some reason
logger = logging.getLogger("NeuralNine Logger")
logger.info("The best logger was just created!")
logger.critical("Your YouTube channel was deleted!")

logger.log(logging.ERROR, "An error occured!") # same output


# We really want LOG FILES, files from the past
# we have to create a filehandler
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(script_directory+"\\"+'mylog.log')
handler.setLevel (logging.INFO)

logger.addHandler (handler)

logger.debug ("This is a debug message!")
logger.info("This is important information!")
"""
we get both messages printed out

DEBUG:NeuralNine Logger:This is a debug message!
INFO:NeuralNine Logger:This is important information!

but in the created 'mylog.log' file we only get the INFO message
 as that is the level of our handler
"""

# when we open the log file we have no structure unlike the terminal
#  it just prints the message into the log file
# we can create a formator

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(script_directory+"\\"+'mylog2.log')
handler.setLevel (logging.INFO)

# string with desired format
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler (handler)

logger.debug ("This is a debug message! 2")
logger.info("This is important information! 2")

"""
otuput:
INFO - 2023-09-15 15:55:21,630: This is important information! 2
"""