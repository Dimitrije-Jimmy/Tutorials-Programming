-- things like NOT NULL, UNIQUE, IN CERTAIN RANGE

USE tutorialdb;

DROP TABLE IF EXISTS people;

CREATE TABLE IF NOT EXISTS people (
    p_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(255) NOT NULL,
    p_age INTEGER DEFAULT 21,
    p_ssn CHAR(32) UNIQUE, -- social security number
    
    CONSTRAINT age_constraint CHECK (p_age >= 0 AND p_age < 200)
    
    );

SELECT * FROM people;

-- Constraints:
-- PRIMARY KEY - unique (no duplicates) and not null
-- UNIQUE - no duplicates but not necessary / possibly null
-- NOT NULL - have to pass this value
-- DEFAULT value - sets the default value if none provided

-- CONSTRAINT name_of_constraint CHECK (logic)
-- CONSTRAINT age_constraint CHECK (p_age >= 0 AND p_age < 200)

INSERT INTO people (p_id, p_name) VALUES (1, 'Mike');
INSERT INTO people (p_id, p_name, p_age, p_ssn) VALUES (2, 'Jane', 25, 'AH77812');
INSERT INTO people (p_id, p_name, p_age, p_ssn) VALUES (3, 'Angela', 54, 'AH77812');
-- 0	87	12:45:42	INSERT INTO people (p_id, p_name, p_age, p_ssn) VALUES (3, 'Angela', 54, 'AH77812')		
--  Error Code: 1062. Duplicate entry 'AH77812' for key 'people.p_ssn'		0.000 sec
INSERT INTO people (p_id, p_name, p_age, p_ssn) VALUES (4, 'John', 300, 'AH32124');
-- 0	89	12:50:27	INSERT INTO people (p_id, p_name, p_age, p_ssn) VALUES (4, 'John', 300, 'AH32124')	
--  Error Code: 3819. Check constraint 'age_constraint' is violated.		0.016 sec

-- often we have an id as a unique identified but it's essentially a row number
--  it doesn't matter what it is just as long as it is unique and not null, it carries no info
--  therefore we can automatically increment it instead of specifying it
-- you do this by adding PRIMARY KEY AUTO_INCREMENT

INSERT INTO people (p_name) VALUES ('Josh'), ('Zerka');
-- we can run this multiple times and it'll always add it in because the two names aren't unique

-- we can also apply constraints onto multiple fields
DROP TABLE IF EXISTS people;

CREATE TABLE IF NOT EXISTS people (
    p_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	p_firstname VARCHAR(255),
    p_lastname VARCHAR(255),
    
    -- no we want to make it so that firstname and lastname can be each repeatable but only the combination to be unique
    --  basically two people same firstname or same lastname but can't have both the same
    CONSTRAINT name_constraint UNIQUE(p_firstname, p_lastname)
    );

SELECT * FROM people;

INSERT INTO people (p_firstname, p_lastname) VALUES ('Mike', 'Smith'), ('John', 'Smith');
INSERT INTO people (p_firstname, p_lastname) VALUES ('Mike', 'Stone'), ('John', 'Stone');
-- if either ran again:
-- 0	106	13:16:08	INSERT INTO people (p_firstname, p_lastname) VALUES ('Mike', 'Smith'), ('John', 'Smith')	
-- Error Code: 1062. Duplicate entry 'Mike-Smith' for key 'people.name_constraint'		0.000 sec


TRUNCATE TABLE people;

-- we can also add constraints to existing tables
ALTER TABLE people ADD CONSTRAINT unique_lastname UNIQUE(p_lastname);
-- this wont work because we already have data inside the database that violates this constraint
--  we first have to truncate

-- this was just a Syntax Error
-- 0	108	13:24:40	ALTER TABLE people ADD CONSTRAIN unique_lastname UNIQUE(p_lastname)	
--  Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version 
--   for the right syntax to use near 'unique_lastname UNIQUE(p_lastname)' at line 1		0.016 sec

-- 0	113	13:26:19	ALTER TABLE people ADD CONSTRAINT unique_lastname UNIQUE(p_lastname)	
--  Error Code: 1062. Duplicate entry 'Smith' for key 'people.unique_lastname'		0.047 sec