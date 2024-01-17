-- This script creates the table force_name on your MySQL server

-- Specify the database name as a command-line argument
USE `hbtn_0d_2`;

-- Create the force_name table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
