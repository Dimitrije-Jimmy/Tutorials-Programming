-- SET OPERATIONS - allow us to combine the results of different queries in different ways

USE tutorialdb;

DROP TABLE IF EXISTS people;

SHOW TABLES;

DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS things;
DROP TABLE IF EXISTS ownership;


CREATE TABLE IF NOT EXISTS people (
	p_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(255),
    p_age INTEGER,
    p_height FLOAT,
    p_gender ENUM('male', 'female')
	);


CREATE TABLE IF NOT EXISTS things (
	t_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    t_name VARCHAR(255) NOT NULL,
    t_description VARCHAR(255),
    t_owner INTEGER, -- UNIQUE,
    FOREIGN KEY (t_owner) REFERENCES people (p_id)
	);
   

CREATE TABLE IF NOT EXISTS ownership (
	o_owner INTEGER,
    o_thing INTEGER,
    -- the previous two together are our primary key
    PRIMARY KEY (o_owner, o_thing),
    FOREIGN KEY (o_owner) REFERENCES people (p_id),
    FOREIGN KEY (o_thing) REFERENCES things (t_id)
	);
    

-- let's introduce another table
CREATE TABLE IF NOT EXISTS friendships (
	f_friend1 INTEGER,
    f_friend2 INTEGER,
    PRIMARY KEY (f_friend1, f_friend2),
    FOREIGN KEY (f_friend1) REFERENCES people (p_id),
    FOREIGN KEY (f_friend2) REFERENCES people (p_id)
	);


-- Inserting data into the 'people' table
INSERT INTO people (p_name, p_age, p_height, p_gender)
VALUES  ('John Doe', 35, 1.75, 'male'),
	    ('Jane Smith', 30, 1.65, 'female'),
		('Alice Johnson', 28, 1.7, 'female'),
		('Bob Brown', 40, 1.8, 'male'),
        ('Mike Nonowner', 30, 1.72, 'male'); -- Nonowner isn't going to own anything
        
-- Inserting data into the 'people' table
INSERT INTO things (t_name, t_description, t_owner)
VALUES  ('Bicycle', 'Blue mountain bike', 1),
		('Laptop', 'MacBook Pro', 2),
        ('Guitar', 'Acoustic Yamaha guitar', 1),
        ('Camera', 'Canon DSL', 3),
        ('Watch', 'Rolex', 4),
        ('MATLAB Fan CLub Membership', 'Fan Pass', NULL); -- will not be owned by anyone


-- Inserting data into the 'ownerships' table
INSERT INTO ownership (o_owner, o_thing)
VALUES  (1, 1),
		(1, 3),
		(2, 2),
        (3, 4),
        (4, 5),
        (2, 5); -- Jane also owns the Rolex watch


INSERT INTO friendships (f_friend1, f_friend2)
VALUES  (1, 2),	  -- John Doe is friends with Jane Smith
		(2, 3),	  -- Jane Smith is friends with Alice Johnson
        (3, 1),	  -- John Doe is friends with John Doe
        (4, 1),	  -- Bob Brown is friends with John Doe
        (4, 2);	  -- Bob Brown is friends with Jane Smith



-- only displays the matches that have a match
SELECT p_name, t_name FROM people INNER JOIN things ON p_id = t_owner;

-- FULL OUTER JOIN - combines all people and all things even if they own nothing and are owned by noone
-- to make a FULL OUTER JOIN you do it using SET OPERATIONS
SELECT p_name, t_name FROM people LEFT JOIN things ON p_id = t_owner
UNION
SELECT p_name, t_name FROM people RIGHT JOIN things ON p_id = t_owner;
-- UNION - combines 
-- UNION ALL - will output duplicates too

SELECT p_name, t_name FROM people LEFT JOIN things ON p_id = t_owner
INTERSECT
SELECT p_name, t_name FROM people RIGHT JOIN things ON p_id = t_owner;
-- INTERSECT - logical AND, only things in common, basically just an INNER JOIN
-- MySQL Workbench doesn't highlight INTERSECT but it works and VSCode highlights it


SELECT p_name, t_name FROM people LEFT JOIN things ON p_id = t_owner
EXCEPT
SELECT p_name, t_name FROM people RIGHT JOIN things ON p_id = t_owner;
-- outputs just 'Mike Nonowner'
-- EXCEPT - everything from first, except the INTERSECT of the first and second

SELECT p_name, t_name FROM people LEFT JOIN things ON p_id = t_owner
EXCEPT
SELECT p_name, t_name FROM people RIGHT JOIN things ON p_id = t_owner WHERE p_age > 30;