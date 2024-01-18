-- This script lists all cities with their respective states in the hbtn_0d_usa database using JOIN

-- List all cities with their respective states using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
