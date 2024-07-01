-- relationships between tables and joins

-- now we're going to be working with multiple tables
-- there can also be relationships between the same table

-- joins allow us to make select statements accross multiple tables

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
    
    -- to make it so that a thing can be owned by multiple people we'd need to remove the 't_owner'
    -- and put this code here
    -- p_thing INTEGER,
    -- FOREIGN KEY (p_thing) REFERENCES (t_id)
	);
      
-- Different type of relationships between tables
-- 1:1 - one to one
-- 1:n, n:1 - one to many
-- n:m - many to many

-- a thing can be owned by 1 person, and a person can only own exactly 1 thing - 1:1
-- a thing can be owned by 1 person, but a person can own multiple things - 1:n (or swapped)
-- a thing can be owned by multiple people, and multiple people can own multiple things - n:m


CREATE TABLE IF NOT EXISTS things (
	t_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    t_name VARCHAR(255) NOT NULL,
    t_description VARCHAR(255),
    t_owner INTEGER, -- UNIQUE,
    -- this will be the type of the primary key of people
    -- this references that primary key
    FOREIGN KEY (t_owner) REFERENCES people (p_id)
    
    -- this is currently a 1:n relationship, 1 person many things
    -- to make it a 1:1, you make the 't_owner' UNIQUE
	);
   
   
-- to model many to many relationships we need a third table

CREATE TABLE IF NOT EXISTS ownership (
	o_owner INTEGER,
    o_thing INTEGER,
    -- the previous two together are our primary key
    PRIMARY KEY (o_owner, o_thing),
    FOREIGN KEY (o_owner) REFERENCES people (p_id),
    FOREIGN KEY (o_thing) REFERENCES things (t_id)
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
        

-- how can we select something from this structure, / formulate queries
-- when dropping tables you can't drop them if they're being used somewhere else

SELECT * FROM people;

-- give me the names of the people and everything they own
-- to do this we have to introduce a 'JOIN' which joins a table to a specific column
SELECT p_name, t_name FROM people INNER JOIN things on people.p_id = things.t_owner;
-- we say people.p_id is the same as things.t_owner, join these tables on these two columns, match the records and select them

-- p_name 			t_name
-- John Doe			Bicycle
-- John Doe			Guitar
-- Jane Smith		Laptop
-- Alice Johnson	Camera
-- Bob Brown		Watch

-- we can now see that 'Mike Nonowner' isn't listed because he doesn't own anything
-- and the 'MATLAB Fan Membership' isn't listed either
-- things that have no match aren't listed, this is the concept of the INNER JOIN

-- if we also want to see 'Mike Nonowner' included, so all people even if they dont own anything
-- we do a LEFT JOIN - everything from the left table will be included even if there's no match
SELECT p_name, t_name FROM people LEFT JOIN things on people.p_id = things.t_owner;

-- the other way around, RIGHT JOIN - everything from the right table
SELECT p_name, t_name FROM people RIGHT JOIN things on people.p_id = things.t_owner;

-- in MySQL there is no FULL OUTER JOIN or FULL JOIN, some other dialects have it
-- when you just use JOIN it does the INNER JOIN

-- there's also CROSS JOIN, that matches every item matched with every item from the other table 
SELECT p_name, t_name FROM people CROSS JOIN things;


-- we can query specific things
-- give me all the things that share ownership
SELECT p1.p_name AS Person1, p2.p_name AS Person2, t_name AS SharedThing
FROM ownership o1
JOIN ownership o2 ON o1.o_thing = o2.o_thing AND o1.o_owner <> o2.o_owner 
 -- we access the same table twice and the same thing with the condition that the owner isn't the same
JOIN people p1 ON o1.o_owner = p1.p_id
JOIN people p2 ON o2.o_owner = p2.p_id
JOIN things t ON o1.o_thing = t.t_id;

-- we're accessing the ownership table twice with the condition that a thing present in both tables o1 and o2
--  which is the same table, we find the same item but with different owner
-- and we say that owner1 = o1 has to be the same as person1 = p1, ... for o2 = p2, and the thing is the thing
-- and give me the shared thing
-- this is a query just with joins no advanced structures


-- let's introduce another table
CREATE TABLE IF NOT EXISTS friendships (
	f_friend1 INTEGER,
    f_friend2 INTEGER,
    PRIMARY KEY (f_friend1, f_friend2),
    FOREIGN KEY (f_friend1) REFERENCES people (p_id),
    FOREIGN KEY (f_friend2) REFERENCES people (p_id)
	);
    
INSERT INTO friendships (f_friend1, f_friend2)
VALUES  (1, 2),	  -- John Doe is friends with Jane Smith
		(2, 3),	  -- Jane Smith is friends with Alice Johnson
        (3, 1),	  -- John Doe is friends with John Doe
        (4, 1),	  -- Bob Brown is friends with John Doe
        (4, 2);	  -- Bob Brown is friends with Jane Smith
        

-- I want to see all the friendships
SELECT p1.p_name AS Friend1, p2.p_name AS Friend2
FROM friendships
JOIN people p1 ON friendships.f_friend1 = p1.p_id
JOIN people p2 ON friendships.f_friend2 = p2.p_id

-- you can combine joins howevermuch you want, this is how to model relationships and use joins