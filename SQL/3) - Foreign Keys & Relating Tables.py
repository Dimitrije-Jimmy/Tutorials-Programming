# Foreign keys and relating tables

#  the point is to be able to reference one table from another
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost", # usually you connect to server
    user="sqluser",
    passwd="password",

    # connects to specific database
    database="testdatabase"
    )

users = [("tim", "techwithtim", "12345", "tim@gmail.com"),
         ("joe", "joey123", "password123", "joe@hotmail.com"),
         ("sarah", "sarah1234", "pass234", "sarah123@gmail.com")]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]


mycursor = db.cursor()

mycursor.execute("DROP TABLE IF EXISTS Scores")
mycursor.execute("DROP TABLE IF EXISTS Users")

# we need to create the parent table first - the table thats referenced
#  by the other table

# first we create the user table
# We're storing queries in variable so it's easier to look at
Q1 = "CREATE TABLE IF NOT EXISTS Users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), username VARCHAR(50), passwd VARCHAR(50), email VARCHAR(255))"

# now the scores table
# you can make the primary key be a foreign key
#  since we know our relationship is 1to1 - for every Score there's one netry in Users table and vice versa
#  we can say foreign key can be primary key
# for the "IG posts" example we had a 1:n relationship so we couldn't use it as the primary key since it's not unique
Q2 = "CREATE TABLE IF NOT EXISTS Scores (userId INT PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 INT DEFAULT 0, game2 INT DEFAULT 0)"

mycursor.execute(Q1)
mycursor.execute(Q2)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


Q3 = "INSERT INTO Users (name, username, passwd, email) VALUES (%s, %s, %s, %s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"


# add users in table, you can do it manually with for loop or execute this command
#  it runs the query for the range of the list of passed values

 # mycursor.executemany(Q3, users)

for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    
    # now to insert scores at the same time

    # this is the last row ID that was inserted into the table, which in this 
    #  case is the id of the user because it's getting the primary key 
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])
     # (last_id,) + user_scores[x] - just makes tuple (id, game1, game2) 

db.commit()

    
mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)
        
mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
    print(x)
