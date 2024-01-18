-- This script lists all shows without the genre Comedy in the hbtn_0d_tvshows database

-- Get the genre id for the genre Comedy
SET @comedy_genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy' LIMIT 1);

-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.id IS NULL OR tv_genres.id != @comedy_genre_id
ORDER BY tv_shows.title ASC;
