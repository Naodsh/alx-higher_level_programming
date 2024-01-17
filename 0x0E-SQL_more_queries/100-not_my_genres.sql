-- This script lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database

-- Specify the database name as a command-line argument
USE `hbtn_0d_tvshows`;

-- Get the genre id linked to the show Dexter
SET @dexter_genre_id = (SELECT tv_genres.id
                        FROM tv_shows
                        JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
                        WHERE tv_shows.title = 'Dexter'
                        LIMIT 1);

-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id != @dexter_genre_id
ORDER BY tv_genres.name ASC;
