# How to open a file, we need to open a file stream
file = open('myfile.txt', 'r')

"""
3 modes: reading - r, writing - w, appending - a 
there are special ones for rb- reading bytes, and others
"""

file.close()

"""
every stream that is opened needs to be close, find a file.close statement

if you don't want to do this manually you use a with statement
you dont have to close, everything that needs to be done in the stream happens in the indented with statement
if you need to use the stream over and over again this isn't a good method
"""

with open('file.txt', 'r') as f:
    # ALL OF MY CODE
    pass

# now for reading the code
with open('file.txt', 'r') as f:
    content = f.read()

print(content)
# ofc in this code I have issues cause I'm not running the script from the same directory that the file is located in

file = open('file.txt', 'r')
content = file.read()
file.close()

print(content)


# for writing into the file
file = open('file.txt', 'r')
content = file.write("Hello youtube!")
file.close()

# this overwrites the content with the new information because it's in "writing" mode and not "appending"
with open('file.txt', 'r') as f:
    content = f.write("Hello youtube!")

"""
The close method is especially important for writing because it doesnt just close the stream it also flushes the content
if we don't close the stream after writing into the file, nothing is written in the file, you need to use flush method to flush it into the file or close the file

file.flush() <-- this will keep the stream open but put the content into the file

if you try to write a file that doesnt exist itll create it, whilst if you try to read a file that doesnt exist youll get an exception "FileNotFoundError"
now you can catch exceptions
"""

try:
    # some stream code
    pass
except:
    # catch
    pass
finally:
    # close
    pass


file = open('file.txt', 'a')
file.write("Hello World!")
file.flush()


"""
we can also rename, remove files, change directory, makedirectory
we use OS
"""

import os

os.rename
os.remove

from os import rename, remove
from os import * # this imports everything

# A module has functions, classes, different things in it
# when you use '*' to import from a module you no longer have to call it by name os.mkdir, because it treats it like you defined all the functions in your script

mkdir("test") # makes directory in the specified directory with name
chdir("test") # this moves you into the directory and making a file will make it in that directory
mkdir("newdir")


# if we have "file.txt"
rename("file.txt", "myfile.txt") # renames the file to 'myfile.txt'
remove("myfile.txt") # removes the file

# file handling in python  



