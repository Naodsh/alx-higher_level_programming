-- This script creates the database hbtn_0d_usa and the table cities on your MySQL server

-- Create database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Specify the database name
USE `hbtn_0d_usa`;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Create the cities table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
);

-- Insert data into the cities table
INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco');
