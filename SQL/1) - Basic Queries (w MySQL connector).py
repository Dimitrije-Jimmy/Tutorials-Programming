import mysql.connector

# now we try to connect to our database

db = mysql.connector.connect(
    host="localhost", # usually you connect to server
    user="sqluser",
    passwd="password",

    # connects to specific database
    database="testdatabase"
    )

"""
db = mysql.connector.connect(
    host="localhost", # usually you connect to server
    user="Dimitrije",
    passwd="M1n3craft"
    )
"""

# now we're creating a cursor object using this database
#  and execute an SQL query to create a new database
mycursor = db.cursor()


# this is the standard way to execute an SQL query
# mycursor.execute("query")
mycursor.execute("CREATE DATABASE IF NOT EXISTS testdatabase")


# Highlight String Code - extension za formatiranje SQL znotraj python
#  remove when done with  SQL 
#  yeah nah it's shit, use Sublime text for SQL if you can be asked

# Database - inside we have everything
# Tables - you can think of them as classes, limitle4s
# Columns - they have headers that describe what it is, i.e. name, age, fav.food
# Rows - hold info associated with each person, just a different entry

# we usually link tables, i.e. link pizza to entry pizza in food with info about pizza

# we have INT, BIGINT, SMALLINT - they take up different memories, smallint - -32000 do +23000
# UNSIGNED - we save a bit because we know it's always going to be a positive number
"""
mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age SMALLINT UNSIGNED, personID INT PRIMARY KEY AUTO_INCREMENT)")
"""

# if we want to see what's going on, (first comment the queries before)
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)


"""
output
('name', b'varchar(50)', 'YES', '', None, '')
('age', b'smallint unsigned', 'YES', '', None, '')
('personID', b'int', 'NO', 'PRI', None, 'auto_increment')

int(5) - smallint,     int(11) - int
"""

# how to add things into the table:
"""
mycursor.execute("INSERT INTO Person (name, age) VALUES ('tim', 45)") 
"""

# we usually don't pass values in individualy, we do string formatting
#  it allows us to pass values in, in a better, safer way
#  also allows us to pass in variables, useful for code
"""
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('Tim', 19)) 
"""
# "string".format(values) doesn't work here, has to be %s with additional Tuple
"""
mycursor.execute("INSERT INTO Person (name) VALUES (%s)", ('John', )) # this works, just has to be atuple, list or dict
"""
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('Joe', 22))

# to actually make the changes to the database we need to commit them so it saves them permanently

db.commit()


# how do we now look at the table
mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)