-- This script lists all shows with their associated genre_id in the hbtn_0d_tvshows database

-- Specify the database name as a command-line argument
USE `hbtn_0d_tvshows`;

-- List all shows with their associated genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
