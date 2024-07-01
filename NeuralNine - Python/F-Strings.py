# Format modifiers for F-Strings and Advanced formating for strings in Python

"""
String Formatting - taking expressions and variables and formating it into a string
"""
name = 'Mike'
age = 25


# String concatonation - the stupid way to do it
print(name + ' is ' + str(age) + ' years old.')

# String formatting - is doing the same but dynamically
#  we can do that with the .format function or % sing
#  but we're going to use the F string, just using {} brackets
print(f'{name} is {age} years old.')

# In this tutorial we focus on Format Modifiers - that allow us to change
#  how things are represented
"""
float modifier - for when you have too many decimals and want to format it
    {number:.4f} , number with 4 decimal places and it's a float
"""
weight = 80.65784

print(f'{name} is {age} years old and weighs {weight} kg.')
print(f'{name} is {age} years old and weighs {weight:.2f} kg.')

floating_point_error = 10.65
print(f'floating point error: {floating_point_error:.40f}')


# we can also do percentage formating
win_rate = 0.67
print(f'wins {win_rate:.2%} of the time')
#win_rate = 0.678943        # can't stack them
#print(f'wins {win_rate:.2%:.2f} of the time')


"""
# we can do a bunch of formatting for numbers

f'n:b'

:x - displaying in HEX
:X - uppercase in HEX
:o - Octal representation
:b - binary
:032b - 32-bit binary with leading zeroes
:e - scientific notation
"""
age = 35
print(f'hex representation: {age:x}')
print(f'uppercase hex representation: {age:X}')
print(f'octal representation: {age:o}')
print(f'binary representation: {age:b}')
print(f'23-bit binary representation with leading zeros: {age:032b}')
print(f'scientific representation: {age:e}')


"""
# for financial application

{variable:,} - thousands separator ,
{variable:_} - thousands separator _
"""
net_worth = 63784651726
print(f'net worth: ${net_worth:,}')
print(f'net worth: ${net_worth:_}')

# we can also do this based on locale (in EU / Germany, Slovenia, Austria we separate
#  decimals with , instead of .)
import locale

locale.setlocale(locale.LC_NUMERIC, locale='de_DE.utf-8')

net_worth = 637856.32423
print(f'net worth: ${net_worth:n}')


# often times you want to use leading zeros/ zero padding
#  usually you do this with dates
# instead of displaying day = 7 you want day = 07
day = 16  # 07
month = 6  # 06
year = 2023

# it expects 2 digits if you give it one so sub 10 it fills/pads the rest with 0s
print(f'{day}.{month}.{year}')
print(f'{day:02}.{month:02}.{year}')
print(f'{day:07}.{month:02}.{year}')
print(f'{day:07x}.{month:02}.{year}') # you can also combine things
print(f'{day:_b}.{month:02}.{year}') # binary and underscore spearators


"""
Width formatting: it gives us n number of spaces

let's say we have a sentence that we want to format as a table,
 so we need to have the same amount of spacing between things
 imagine a .dat file and columns basically like inputing tabs in between
"""
sentence = 'Each column has a width of ten'

table1 = ''
for word in sentence.split(' '):
    table1 += f'{word:10}'

print(table1)


# We can also do string alignment - to the right, left, center, ...
# > - right align
# < - left align
# ^ - centering
table2 = ''
for word in sentence.split(' '):
    table2 += f'{word:>10}'
print(table2)
table3 = ''
for word in sentence.split(' '):
    table3 += f'{word:<10}'
print(table3)
table3 = ''
for word in sentence.split(' '):
    table3 += f'{word:^10}'
print(table3)


# example of what it can be used for
words = ['Hello', 'these', 'are', 'words']

# we use the fill characters 20 of them left aligned <, if there is space left, 
#  fill it up with the picked element .
print(f'1. {words[0]:.<20} $100')   # Fill space with dots (can be used for tables)
print(f'2. {words[1]:.<20} $200')
print(f'3. {words[2]:.<20} $300')
print(f'3. {words[2]:_<20} $300')
print(f'3. {words[2]:,<20} $300')
print(f'3. {words[2]:#<20} $300')
print(f'3. {words[2]:K<20} $300')
"""
1. Hello............... $100
2. these............... $200
3. are................. $300
3. are_________________ $300
3. are,,,,,,,,,,,,,,,,, $300
3. are################# $300
3. areKKKKKKKKKKKKKKKKK $300
"""

# formatting dates
import datetime

current = datetime.datetime.now()

print(f'{current}') # default
print(f'{current:%Y}') # only the year
print(f'{current:%m}') # same for the month
print(f'{current:%d}') # same for the day
print(f'{current:%H}') # the current hour
print(f'{current:%M}') # the current minute
print(f'{current:%S}') # the current second
print(f'{current:%j}') # day of the year
# more exists: day of the week, weekname, ...
"""
2023-09-23 20:20:42.445974
2023
09
23
20
20
42
266
"""


# you can also combine into your own date formatting
print(f'{current:%Y-%m-%d %H:%M:%S}')   # 2023-09-23 20:21:54