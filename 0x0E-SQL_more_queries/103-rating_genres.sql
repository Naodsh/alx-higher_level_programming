-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating

-- Specify the database name as a command-line argument
USE `hbtn_0d_tvshows_rate`;

-- List all genres by their rating in descending order
SELECT tv_genres.name, SUM(tvshow_ratings.rating) AS rating_sum
FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
JOIN tvshow_ratings ON tv_shows.id = tvshow_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating_sum DESC;
