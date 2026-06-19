-- This script lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, it displays NULL in the genre column.
-- Each record displays: tv_shows.title - tv_genres.name.
-- It sorts results in ascending order by the show title and genre name.
-- It uses only one SELECT statement.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;