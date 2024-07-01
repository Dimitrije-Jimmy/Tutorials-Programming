-- Basic - SELECT what FROM where
-- Advanced - ordering, grouping, aggregate functions

USE tutorialdb;

DROP TABLE people;

CREATE TABLE IF NOT EXISTS people (
    p_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(255),
    p_age INTEGER,
    p_height FLOAT,
    p_gender ENUM('male', 'female')
    );

INSERT INTO people (p_name, p_age, p_height, p_gender) VALUES 
('Mike', 55, 188, 'male'),
('Anna', 55, 182, 'female'),
('Lisa', 22, 167, 'female'),
('Bob', 34, 178, 'male'),
('John', 29, 180, 'male'),
('Jeff', 89, 182, 'male'),
('Angela', 77, 180, 'female'),
('Samuel', 55, 175, 'male'),
('Kate', 27, 167, 'female'),
('Andrew', 23, NULL, 'male'),
('Jim', 65, 187, 'male');

SELECT p_name, p_age FROM people
WHERE p_age > 30;
-- * for everything

-- Keywords:
-- DISTINCT - removes duplicate rows i.e. 20 times 'Mike' 20, we only see it once
-- IN - specifying specific things
-- LIKE - for names, it doesn't match the string exactly
-- AS - for presentation when looking at the database


SELECT DISTINCT p_name, p_age FROM people;
-- here nothing will change because there are no duplicate names
SELECT DISTINCT p_age FROM people;
-- here it does change, as we have multiple people aged 55
SELECT DISTINCT p_gender FROM people;
-- now we just get male and female, no repetitions

SELECT * FROM people
WHERE p_age IN (55, 65);
-- it outputs only those with either of these ages

SELECT * FROM people
WHERE p_name = 'Mike';
-- exact comparison

SELECT * FROM people
WHERE p_name LIKE 'J%';
-- 'J%' - name has to start with a 'J'
-- '%a' - name has to end with an 'a'
-- '%e%' - name has to include an 'e' in between
-- % can also just be nothing though so %e% can be for 'egg' and 'Mike'

SELECT p_name AS 'Name', p_age AS 'Age' FROM people;


-- AGGREGATE functions:
-- SUM
-- AVG
-- MIN
-- MAX
-- COUNT, COUNT(*) - count everything, COUNT(p_height) - outputs the number of all besides where NULL
-- LIMIT

SELECT SUM(p_age) AS 'Age Sum' FROM people;

SELECT AVG(p_height) AS 'Average Height' FROM people WHERE p_gender = 'male';
SELECT AVG(p_height) AS 'Average Height' FROM people WHERE p_gender = 'female';

-- if I want to GROUP BY' a certain attribute (i.e. separate by male and female)
--  then we can apply the aggregate functions on the different groups / subsets
SELECT p_gender, AVG(p_height) FROM people
GROUP BY p_gender;
-- p_gender		AVG(p_height)
-- male		181.66666666666666
-- female	174

-- we can also group by multiple attributes
SELECT p_gender, p_age, AVG(p_height) FROM people
GROUP BY p_gender, p_age;
-- p_gender		p_age		AVG(p_height)
-- male		55		181.5
-- female	55		182
-- female	22		167
-- male		34		178
-- male		29		180
-- male		89		182
-- female	77		180
-- female	27		167
-- male		23		Null	
-- male		65		187

SELECT p_gender, p_age, p_height FROM people
GROUP BY p_gender, p_age;
-- 0	126	13:56:00	SELECT p_gender, p_age, p_height FROM people GROUP BY p_gender, p_age LIMIT 0, 1000	
 -- Error Code: 1055. Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'tutorialdb.people.p_height' 
 --  which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by		0.000 sec

-- you either have to group by the attributes you're showing or use the aggregate function
--  here we're grouping by age and gender, but height is no longer able to be shown for each indiivudal person, 
--  we have to show it with respect to a group, because of that we need to aggregate it to that group

-- we can also order the results
SELECT * FROM people
ORDER BY p_age;
-- ORDER BY column - orders it in ascending order of values for specified column
SELECT * FROM people
ORDER BY p_age DESC;
-- DESC - now orders it in descending order

-- we can also order by multiple attributes
SELECT * FROM people
ORDER BY p_age DESC, p_name;

-- swapping the order, it prioritizes the first keyword
SELECT * FROM people
ORDER BY p_name, p_age DESC;


-- we can limit the output
SELECT * FROM people
ORDER BY p_age
LIMIT 5;
-- now we limit ourselves to the 5 youngest people/entries


