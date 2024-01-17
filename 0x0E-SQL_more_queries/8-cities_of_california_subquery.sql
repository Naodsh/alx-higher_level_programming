-- This script lists all the cities of California in the hbtn_0d_usa database using a subquery

-- Specify the database name as a command-line argument
USE `hbtn_0d_usa`;

-- List all the cities of California without using JOIN
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1)
ORDER BY id ASC;
