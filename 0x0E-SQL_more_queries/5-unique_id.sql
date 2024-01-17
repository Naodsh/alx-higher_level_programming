-- This script creates the table unique_id on your MySQL server

-- Specify the database name as a command-line argument
USE `hbtn_0d_2`;

-- Create the unique_id table if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
