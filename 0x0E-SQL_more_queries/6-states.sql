-- This script creates the database hbtn_0d_usa and the table states on your MySQL server

-- Create database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Specify the database name
USE `hbtn_0d_usa`;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data into the states table
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
