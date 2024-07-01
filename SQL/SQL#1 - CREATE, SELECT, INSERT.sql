SHOW DATABASES;
/* 
# shows what databases you have

In SQL code you comment by putting:
 '#' in front of text
 '--' in fron of text
 or for multiple line '/*' at the start and '*/' at the end

# in databases we have data structured in rows, the rows are located in tables and tabnles are located in a database
#  different columns/ different attributes
*/
# CREATE DATABASE tutorialdb; -- # always end command with semicolon */
CREATE DATABASE IF NOT EXISTS tutorialdb; /* less error based */

/*
# 1	4	21:46:54	CREATE DATABASE IF NOT EXISTS tutorialdb	1 row(s) affected, 1 warning(s):
#  1007 Can't create database 'tutorialdb'; database exists	0.000 sec
# so the "if not exists" gives error that it doesn't create a new database

# now we have empty database
# we have to specify which database we're using
*/
USE tutorialdb;

-- # shows the tables
-- # you can write commands in lower case but it's standard to write with upper case for SQL
SHOW TABLES;


-- # we can create a new table
-- #  we need to specify what columns/attributes are going to be in the table
CREATE TABLE IF NOT EXISTS people (
	p_id INTEGER PRIMARY KEY,
    -- we need to specify what datatype it is ('INT' or 'INTEGER' both work)
    -- we can set the constraints (not null, unique, ...)
    -- every row in the table needs to have a unique identified - 'PRIMARY KEY'
    --  that means it can't be null (empty) and can't be duplicated in this table
	--  this is important when we later have foreign keys referencing the primary key to make connections
    
    -- p_ssn CHAR(32) PRIMARY KEY, # another possibility
    -- social security number
       
    -- DATA TYPES
	-- a field can be an integer - INT, 
    -- character of fixed size - CHAR(size),
    -- character of variable size - VARCHAR(maxsize),
    -- for very long texts - TEXT
       
    -- enumerations of values, we have a certain number of values possible
    -- ENUM('C++, 'Java', 'Python')
    
    -- FLOAT, DOUBLE, DECIMAL - amount of decimal places
    -- BOOLEAN, DATE, TIME, DATETIME, TIMESTAMP
    
    p_name VARCHAR(255),
    p_age INTEGER,
    p_height FLOAT
    
);

-- # to run code press CTRL + ENTER or the execute/flash button up top
-- # do the same on SHOW TABLES command to show the tables
-- # we now have an empty table people, we can see it's empty by trying to select everything from the table
-- 
-- # you select which columns you want to select
SELECT * FROM people; # * - gives all data
-- # we can also select specific columns
SELECT p_name, p_age FROM people;

-- # everything is null value so now we have to insert data
INSERT INTO people (p_id, p_name) VALUES (1, 'Mike');
-- # you don't need to put all data in, it can be null

-- # you limit yourself by passing in tuple what values youre going to give
-- #  if you don't limit yourself you have to pass all of it in
INSERT INTO people VALUES (2, 'John', 78, 180);

-- you can insert multiple ones at the same time
INSERT INTO people (p_id, p_name, p_age, p_height) VALUES 
(3, 'Anna', 28, 180),
(4, 'Bob', 38, 178),
(5, 'Kate', 48, 182),
(6, 'James', 55, 183),
(7, 'Samuel', 38, 181),
(8, 'Lisa', 28, 177);


-- how do we select only those with age above 40?
SELECT p_name, p_age FROM people
WHERE p_age > 40;
-- # works with >,<,=, noteq - <>,
-- #  WHERE p_age IS NOT NULL
-- #  WHERE p_height > 180 even if we're not displaying the height attribute

SELECT p_name, p_age FROM people
WHERE p_height >180 OR p_age > 40;
-- # works with AND, OR, XOR - either or but not both


-- default port is - 3306
-- machine: localhost
-- user: root
-- username: Dimitrije
-- password: M1n3craft

/*
in cmd from the location: C:\Program Files\MySQL\MySQL Server 8.0\bin>
type in: mysql -u root -p
and provide password

execute these 3 queries to create new user:

 CREATE USER 'sqluser'@'%' IDENTIFIED WITH mysql_native_password BY 'password' ;

 GRANT ALL PRIVILEGES ON *.* TO 'sqluser'@'%' ;

 FLUSH PRIVILEGES;

to establish connection in VSCode, press bottom left 'MYSQL' tab and add new connection
 with the same localhost, this time user: sqluser, password: password
Now we can run queries

*/
