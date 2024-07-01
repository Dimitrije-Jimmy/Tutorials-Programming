# XML Processing
"""
up to now we've stored data in simple files or proffesionall databases
Sometimes we need a structured way to save files but dont want a big database
 but keep things organised

XML - eXtensible Markup Language
very scalable, can build proffesional graphical user interfaces
great way to structure data, platform and application independent
 i.e if you make a python script that puts data in the XML file, 
 you can also read it and proccess it in C++
"""

# We can use the 'SAX - Simple API for XML' module
#  or we can use the 'DOM - Document Object Model' module

# example of XML file: 'data.xml'

"""
SAX - you mainly use it when you have very limited memory, 
 the main difference to DOM is that it never loads the entire XML file to memory
 it's either useful when you have very very large XML files or very limited memory
With the SAX module you cannot manipulate anything, no changing values in the XML file
 you can only read and proccess them in the script
To change them you need to use the DOM module
"""
import os
import xml.sax

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
print(script_path)
print(script_directory)

# to work with the file we need a content handler and a parser
# handler - works with the file
# parser - translates the file, it's tagging the XML tags and converting them into our Python script

#handler = xml.sax.ContentHandler() # one way
# but we want to customize it, so we're going to create our own class that inherits from ContentHandler()

class GroupHandler(xml.sax.ContentHandler):

    # 3 methods we use
    
    # this function is called when our handler proccesses an element
    # when we get into an element this is the first function called
    def startElement(self, name, attrs): #name and attributes
        #print(name)
        """
        OUTPUT:

        group
        person
        name
        age
        weight
        height
        person
        name
        age
        weight
        height
        person
        name
        age
        weight
        height
        person
        name
        age
        weight
        height
        person
        name
        age
        weight
        height

        printing the name just prints the tag name of the element
        """

        self.current = name 
        # what is the current name of the element
        #  am I proccessing a name, age, weight, ...?
        if self.current == "person":
            print("-----PERSON------")
            print("ID: {}".format(attrs['id']))
            # we're printing the ID of the person, we access the dictionary attributes - attrs['id']
            """
            OUTPUT: 

            -----PERSON------
            ID: 1
            -----PERSON------
            ID: 2
            -----PERSON------
            ID: 3
            -----PERSON------
            ID: 4
            -----PERSON------
            ID: 5
            """

    # we also want to print all the other vaues, therefore we need to proccess
    #  the individual text/ content of the individual text
    # we do that by overwriting the 'characters' method
    def characters(self, content):
        # if this current element is name: add the content of the element to self.name
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
    
    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "age":
            print("Age: {}".format(self.age))
        elif self.current == "weight":
            print("Weight: {}".format(self.weight))
        elif self.current == "height":
            print("Height: {}".format(self.height))
        self.current = "" # make the self.current empty so that it doesn't start
                          #  with height when it get's to the next element
    
    """
    Now it outputs:
    -----PERSON------
    ID: 1
    Name: Mike Smith
    Age: 34
    Weight: 90
    Height: 175
    -----PERSON------
    ID: 2
    Name: Anna Smith
    Age: 54
    Weight: 91
    Height: 188
    -----PERSON------
    ID: 3
    Name: Bob Johnson
    Age: 25
    Weight: 76
    Height: 190
    -----PERSON------
    ID: 4
    Name: Sara Jones
    Age: 56
    Weight: 82
    Height: 170
    -----PERSON------
    ID: 5
    Name: Patrick Star
    Age: 36
    Weight: 73
    Height: 175
    """
    # we can ofc make a class Person and save these values into an object

handler = GroupHandler()
parser = xml.sax.make_parser() # here we're using a method not a constructor
parser.setContentHandler(handler) # we're setting it's content handler
parser.parse(script_directory+"\\"+'data.xml') # parses the file
# parse gets into all the elements


# Now we're going to do the same thing with the 'DOM' module

import xml.dom.minidom # minimal implementation of the DOM module

"""
In DOM we work with DOM Trees - they build a hierarchichal structure
- they view the XML file as a tree, and every element,
 every tag, is just a branch in that tree

To create a DOM tree we just parse it
"""

domtree = xml.dom.minidom.parse(script_directory+"\\"+'data.xml')
# now we parsed that whole xml file into our script and have the entire tree loaded in RAM

# now we need to find the main object - the document element - <group>...</group>
group = domtree.documentElement # the root of the DOMTree

# to get a collection of all the persons in that group
persons = group.getElementsByTagName('person')
print(persons)
"""
Output:
[<DOM Element: person at 0x29b5b9c9ee0>, <DOM Element: person at 0x29b5b9ec1f0>, <DOM Element: person at 
0x29b5b9ec4c0>, <DOM Element: person at 0x29b5b9ec790>, <DOM Element: person at 0x29b5b9eca60>]

This is a collection of the locations in RAM of each element tagged as 'person' that are contained in <group>
"""

for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))
    
    # now we're going to print all the values of the inidivdual subnotes in the DOM way
    print(
        "Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data)
        )
    # Even tho we only have one name we get a list so we need to pick the first object
    # this is just the element so we need to get the ChildNodes - collection of values of the element
    # finally we want the data of the ChildNode

    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))
    # it outputs the same as we did with the SAX


# we can also manipulate our XML file
#  first we manipulate it in our RAM
#  then we export it into the file

# changing the third person
persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute('id', '100')   # we need to pass a string here
persons[2].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"

# now we've only changed the values in my DOMTree in my Python code in my RAM
# to write it to the file
domtree.writexml(open(script_directory+"\\"+'data.xml', 'w'))

"""
changed:

-----PERSON-----
ID: 100
Name: Mike Smith
Age: 34
Weight: 90
Height: 175
-----PERSON-----
ID: 3
Name: New Name
Age: -10
Weight: 76
Height: 190

it also added a tag with the version: <?xml version="1.0" ?><group>
"""
# you can also save to a new file


# How to create new elements and add them to the xml files
#  first we define how the elements look individually
#  and then put them all together into the file
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

# we need to create the subelements independently and then add them to the newperson
name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))
age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('19'))
weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('80'))
height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('179'))

# now we add to the newperson
newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

# now we add the person to the group object/ to the document element
group.appendChild(newperson)

# flush it to the file
domtree.writexml(open(script_directory+"\\"+'data.xml', 'w'))
