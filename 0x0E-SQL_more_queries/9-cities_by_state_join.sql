-- This script lists all cities with their respective states in the hbtn_0d_usa database using JOIN

-- Specify the database name as a command-line argument
USE `hbtn_0d_usa`;

-- List all cities with their respective states using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
