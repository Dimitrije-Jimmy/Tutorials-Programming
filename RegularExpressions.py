# Regular Expressions - RegEx- are used to validate inputs
# patterns in strings and texts, i.e. user inputs username for example
#  the username can only consists lowercase letters and numbers
#  same with codes, zipcodes, emails, credit card numbers
#  we have certain formats and patterns that we're looking for
#  and we use regular expressions instead of IF statements

# core python module
import re

# uppercase word - starts and ends completely with uppercase letters and nothing else
pattern = re.compile("^[A-Z]+$")
# you can also do match and search without compiling the patterns first
# but if you compile it first you can use it directly for searching and matching
#  and we dont have to specify the pattern everytime

"""
^ - anchor tag, whatever the pattern is it has to start at the beggining
"" - without the anchor tag we can look for a pattern anywhere in the string
[] - you specify inside of brackets the things you want to look for
[A-Z] - this marks all the letters from A-Z in uppercase
+ - means whatever we have in [] needs to occur atleast once but can occur multiple times
     i.e. an empty string wouldn't match the [A-Z] pattern
$ - anchor tag, represents the end of the string

idk what PyCharm he has but he says you can press into the RegEx string
 and press ALT+ENTER and go to Check RegEx, and Sample whether it matches the RegEx sample

 
[a-zA-Z] - uppercase or lowercase
[a-zA-Z\s] - also allows for spaces, but no digits
[a-zA-Z0-9\s] - everything

[...]{3} - the curly brackets specify exactly how many elements should fit the pattern in []
[...]{3,5} - means 3 to 5 items

a symbol - everything that's not an uppercase or lowercase letter, or digit, or space
[^a-zA-Z0-9] - the ^ refers to NOT operation

"^.{10}$" - any string with length of 10, . represents any character
"\." - \. escapes the . command and it now represents the character .

"""

print(pattern.search("Hello World")) # None
print(pattern.search("HELLO WORLD")) # None
print(pattern.search("HELLOWORLD"))  # <re.Match object; span=(0, 10), match='HELLOWORLD'>

# you define pattern, and se whether the rules we've set apply to a string

# we remove the anchor tags
pattern = re.compile("[a-z]+")
print(pattern.search("Hello World")) # <re.Match object; span=(1, 5), match='ello'> 
print(pattern.search("hello world")) # <re.Match object; span=(0, 5), match='hello'>
print(pattern.search("helloworld"))  # <re.Match object; span=(0, 10), match='helloworld'>


# the search function looks into the whole string, 
#  whilst the match function only look at the beginning/ stops at first breaking of the desired pattern
pattern = re.compile("[a-z]+")
print(pattern.match("Hello World")) # None 
print(pattern.match("hello world")) # <re.Match object; span=(0, 5), match='hello'>
print(pattern.match("helloworld"))  # <re.Match object; span=(0, 10), match='helloworld'>


# we can allow for mixed case
pattern = re.compile("[a-zA-Z]+") # uppercase or lowercase
pattern = re.compile("[a-zA-Z\s]+") # uppercase or lowercase and spaces, no digits



# let's try an example
# we want 3 lowercase letters
# followed by 3-5 digits
# then one symbol (symbol - not a letter, digit or space)
# up to two uppercase characters (optional)

# "hzu6682#K" - this would be a string that fits that criteria
"""
^ - from the start of the string
[a-z]{3} - 3 lowercase letters
[0-9]{3,5} - 3 to 5 digits
[^a-zA-Z0-9]{1} - 1 symbol
[A-Z]{0,2} - optional up to two uppercase letters
$ - till the end of the string
"""

pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
print(pattern.search("hzu6682#K"))      # <re.Match object; span=(0, 9), match='hzu6682#K'>
print(pattern.search("ahd2331#AJ"))     # <re.Match object; span=(0, 10), match='ahd2331#AJ'>
print(pattern.search("lll44511.K"))     # <re.Match object; span=(0, 10), match='lll44511.K'>
print(pattern.search("lll44511."))      # <re.Match object; span=(0, 9), match='lll44511.'>
print(pattern.search("abc123456#JJ"))   # None

# we have a rule as a RegEx pattern and we look for it and validate a string

# another simple patter
# any string as long as it's length of 10
pattern = re.compile("^.{10}$")
print(pattern.search("abcdefghij"))  # <re.Match object; span=(0, 10), match='abcdefghij'>
print(pattern.search("0123456789"))  # <re.Match object; span=(0, 10), match='0123456789'>
print(pattern.search("0.2#4JJ 89"))  # <re.Match object; span=(0, 10), match='0.2#4JJ 89'>
print(pattern.search("abcdefghijk")) # None
print(pattern.search("abcdefghi"))   # None

# you define the rules, you apply them, you search for them

# VALIDATING EMAILS
# simple RegEx
# any name with any characters how ever many characters
# followed by @ symbol
# the mail provider
# the .
# and some ending of length 2 - 3
# the _ underscore doesn't need to be escaped
pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}")
print(pattern.search("mail@neuralnine.com"))             # <re.Match object; span=(0, 19), match='mail@neuralnine.com'>    
print(pattern.search("mymail@test.com"))                 # <re.Match object; span=(0, 15), match='mymail@test.com'>        
print(pattern.search("my_fancy.e-mail@fancyurl123.de"))  # <re.Match object; span=(0, 30), match='my_fancy.e-mail@fancyurl123.de'>
print(pattern.search("something.something.com"))         # None
print(pattern.search("mail@something"))                  # None

# fancy domain names like .travel, .game - they wont work