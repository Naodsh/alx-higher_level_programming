-- This script creates a table called first_table in the current database

-- Specify the database name as a command-line argument

-- Create the first_table if it doesn't exist
USE `hbtn_0c_0`;

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
