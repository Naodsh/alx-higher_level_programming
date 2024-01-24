-- Modify the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the table and field to utf8mb4
ALTER TABLE hbtn_0c_0.first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Modify the field in first_table to utf8mb4
ALTER TABLE first_table
    MODIFY COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
