"""
Strings are sequences of characters. We can treat them like that, a string is a list,
you can slice it and use other functions
"""

text = "Hello World!"

print(len(text)) # 12

# ['H', 'e', ...] including the spaces and special characters

# because it's a list we can also index it
print(text[2]) # 'l'

# we can use slicing
print(text[6:]) # World!

# you can iterate over a string
for letter in text:
    print(letter) # will print each character separately

"""
Escape characters. Certain characters we can't just type into the string
\n - is an escape character that makes a line break,
\t - creates a tab
\b - backspace
\s - space

documentation for more: https://docs.python.org/2.0/ref/strings.html
"""

text = "Hellow World! \n This day is awesome"

"""
String formatting
"""
name = input()
age = input()

print("My name is " + name +  " and I am " + age + " years old!")

# %s - for string if we're expecting a string, and $d - for number
#print("My name is %s and I am %d years old" % (name, age)) 

# general without specifying type 
print("My name is {} and I am {} years old".format(name, age)) 


"""
String functions

Documentation for more: https://docs.python.org/3/library/string.html

the essential ones:
"""


# case manipulation functions
text = 'This is my text!'

# tramsforms all text to upper
text = text.upper()
# tramsforms all text to lower
text = text.lower()
# tramsforms all text to title - capitalizes the first letter of every word
text = text.title()
# swaps cases
text = text.swapcase()
print(text)


# count function
# how many times a substrings is contained in a string (repeating letters, or words, ...)

text = "I am Mike and my life is beautifuly! Because of my job!"

print(text.count("my")) # 2 times
print(text.count(" ")) # how many spaces we have

print(text.count("i") + text.count("I")) 
print(text.count("i") + text.count("i".upper())) # same thing


# Find function
# returns the index of substring in a string

text = " I am Mike and I feel great!"

print(text.find("Mike")) # returns 5 that's the start of the substring in the string
print(text.find("I")) # 0, you get the first found position not all


# Join function
# join a sequence to one string separated by specific separators

separator = ';'

mylist = ['Kitchen', 'Dog', 'Mike']

separator = ' '
mylist = ['I', 'am', 'Mike']
print(separator.join(mylist))



# Split function
# I have a string full of separators and I want to separate it into a list or sequence

text = "I am happy because my name is Mike!"

words = text.split(' ')
print(words) # gives a list of each word
# you can also use a stupid separator like a letter 'a' but you get jumble


# Replace function
# replace a substring in a string with another substring (i.e. changing names)

text = "I am Mike! My name is Mike!"
print(text.replace("Mike", "Sarah"))