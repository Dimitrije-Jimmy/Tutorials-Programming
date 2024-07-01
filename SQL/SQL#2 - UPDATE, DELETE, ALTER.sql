USE tutorialdb

CREATE TABLE IF NOT EXISTS people (
    p_id INTEGER PRIMARY KEY,
    p_name VARCHAR(255),
    p_age INTEGER,
    p_height FLOAT
);

SELECT * FROM people;

-- something
# something
/* something */

-- how to update, delete values
-- how to change the entire table structure, the datastructures, ...

-- Mike currently has no age and no height
-- UPDATE tablename SET variable=value WHERE condition; 
-- you need to set the condition otherwise it'll change all the ages
UPDATE people SET p_age = 30 WHERE p_id = 1; 
-- it would also work WHERE p_name = Mike but it would change all 'Mike's' only one primary key remember

UPDATE people SET p_height = 179 WHERE p_id = 1;

-- you can also delete an entire record
DELETE FROM people WHERE p_id = 6;
-- or idk delete all people above age 50
-- WHERE p_age > 50;

-- you may need to remove safe mode from the database
SET SQL_SAFE_UPDATES = 0;


INSERT INTO people (p_id, p_name, p_height) VALUES (10, "James", 178.23);
-- now let's suppose we want to change the table so that the p_height is no longer a FLOAT
--  we do that with ALTER
ALTER TABLE people MODIFY COLUMN p_height INTEGER;
-- in other sql 'dialects' you may need to use ALTER COLUMN instead
-- now the code outputs for 'James' a height 178 instead of 178.23

-- we can also rename the column
ALTER TABLE people RENAME COLUMN p_height TO p_size;
ALTER TABLE people RENAME COLUMN p_size TO p_height;

-- you can also add new columns to the table
ALTER TABLE people ADD COLUMN p_weight FLOAT;
-- drop the column
ALTER TABLE people DROP COLUMN p_weight;

-- you can also drop the entire table and delete it
-- there's also a truncate table command
--  drop table completely removes it, truncate table keeps the table but deletes all data from it
TRUNCATE TABLE people;

DROP TABLE people;
DROP TABLE IF EXISTS people;

