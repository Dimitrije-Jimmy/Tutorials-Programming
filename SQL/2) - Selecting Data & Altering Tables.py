import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost", # usually you connect to server
    user="sqluser",
    passwd="password",

    # connects to specific database
    database="testdatabase"
    )


mycursor = db.cursor()

# datetime is a python object

mycursor.execute("CREATE TABLE IF NOT EXISTS Test (name VARCHAR(50) NOT NULL," +
                 "created datetime NOT NULL, gender ENUM('M', 'F', 'O'), ID INT PRIMARY KEY AUTO_INCREMENT)")
# this works, lovely

#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('TIM', datetime.now(), 'M'))
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('Joe', datetime.now(), 'M'))
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ('Joey', datetime.now(), 'F'))

db.commit()


# selecting different values from the table
mycursor.execute("SELECT * FROM Test WHERE gender = 'M'")
"""
('TIM', datetime.datetime(2023, 8, 16, 0, 12, 22), 'M', 1)
('Joe', datetime.datetime(2023, 8, 16, 0, 12, 22), 'M', 2)
"""
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")
"""
('Joe', datetime.datetime(2023, 8, 16, 0, 12, 22), 'M', 2)
('TIM', datetime.datetime(2023, 8, 16, 0, 12, 22), 'M', 1)
"""
for x in mycursor:
    print(x)


mycursor.execute("SELECT id FROM Test WHERE gender = 'M' ORDER BY id DESC")

for x in mycursor:
    print(x)
"""
(2,)
(1,)
"""

# first have to print out / read out what ive selected with execute
#  then I can select a new thing
# errormsg: handle_unread_result raise InternalError("Unread result found")
#            mysql.connector.errors.InternalError: Unread result found



# how can we modify a column, i.e. add column, change from smallint to bigint
"""
mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

mycursor.execute("DESCRIBE Test")
"""
#for x in mycursor:
#    print(x)
"""
('name', b'varchar(50)', 'NO', '', None, '')
('created', b'datetime', 'NO', '', None, '')
('gender', b"enum('M','F','O')", 'YES', '', None, '')
('ID', b'int', 'NO', 'PRI', None, 'auto_increment')
('food', b'varchar(50)', 'NO', '', None, '')
"""

# if I know I'm only getting one line of output we can do it this way instead of looping and printing
# print(mycursor.fetchone()) # it'll return just the first entry of it
"""
if I already empty the cursor with the other print statement it'll print: None
else: ('name', b'varchar(50)', 'NO', '', None, '')
"""


# deleting a column
"""
mycursor.execute("ALTER TABLE Test DROP food")

mycursor.execute("DESCRIBE Test")
print(mycursor.fetchone())
"""
"""
now the output is: ('name', b'varchar(50)', 'NO', '', None, '')
"""

# changing the name of the column
mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

mycursor.execute("DESCRIBE Test")
for x in mycursor:
    print(x)
"""
('first_name', b'varchar(50)', 'YES', '', None, '')
('created', b'datetime', 'NO', '', None, '')
('gender', b"enum('M','F','O')", 'YES', '', None, '')
('ID', b'int', 'NO', 'PRI', None, 'auto_increment')
('food', b'varchar(50)', 'NO', '', None, '')
"""

#mycursor.execute("ALTER TABLE Test CHANGE first_name first_name VARCHAR(2)")
# be careful doing this because we already have data that's bigger than 2 characters in the table

# we can also change the name of the table and a bunch of other things