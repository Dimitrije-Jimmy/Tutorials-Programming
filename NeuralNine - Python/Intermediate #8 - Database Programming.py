# How to implement database programming in Python

# in this tutorial he uses sqlite3, which is already 
# 'You don't need to install sqlite3 module. It is included in the standard library (since Python 2.5).'
# https://stackoverflow.com/questions/19530974/how-can-i-add-the-sqlite3-module-to-python

import sqlite3 as sql

# to work with database we need to create a connection to the database (this time localy)
connection = sql.connect('mydata.db')

# when you run this it created a 'mydata.db' file in your working directory


# to execute SQL queries we need a cursor, the interface to the database
cursor = connection.cursor()


# almost everything from now on is SQL

# drop table so that I don't have to delete it everytime
cursor.execute("""
        DROP TABLE IF EXISTS persons
    """)


# create new table
cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
    )
    """)


# inserting data into the table
cursor.execute("""
        INSERT INTO persons VALUES
        (1, 'Paul', 'Smith', 24),
        (2, 'Mark', 'Johnson', 42),
        (3, 'Anna', 'Smith', 34)
    """)


# selecting objects to print
cursor.execute("""
        SELECT * FROM persons
        WHERE last_name = 'Smith'
    """)

# to get results
rows = cursor.fetchall()
print(rows)


# nothing get's applied to the database until you commit it to the database
connection.commit()
connection.close()



# now we can combine OOP with Database Programming
#  we have these persons entries in our database
#  we could try to load these database entries as objects in our script
#  or vice versa objects into database
class Person:

    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sql.connect('mydata.db')
        self.cursor = self.connection.cursor()

    # Now we can define a method which load a person from the table and converts it to a Python object
    def load_person(self, id_number):
        self.cursor.execute(""" 
                SELECT * FROM persons
                WHERE id = {}
            """.format(id_number))

        results = self.cursor.fetchone() # gets just one

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    # Here we define a function that will insert a person into our table in our database
    def insert_person(self):
        self.cursor.execute("""
            INSERT INTO persons VALUES
            ({}, '{}', '{}', {})                
            """.format(self.id_number, self.first, self.last, self.age))
            # '{}' is to specify that it's a string to the format function for SQL
            #  only necessary around first name and last name since they're supposed to be strings 

        self.connection.commit()
        # self.connection.close()

    # side function to print SELECT * FROM 
    def select_all(self):
        self.cursor.execute("SELECT * FROM persons")
        results = self.cursor.fetchall()
        print(results)

        self.connection.close()


# now the database with the values already exists we can delete that code

p1 = Person() # empty class with default values, waiting to be assigned
p1.load_person(1)
print(p1.id_number, p1.first, p1.last, p1.age)
# this prints 'Paul' since he is the load_person(1) at key 1


# We successfully loaded an object from the database into the Python script as Python object
# Now we gotta do it the other way around
#  we define an object 

p2 = Person(7, "Alex", "Robbins", 30)
p2.insert_person()

p2.select_all()


