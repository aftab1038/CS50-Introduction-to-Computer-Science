SELECT AVG(rating) FROM ratings
where movie_id IN (
    SELECT id FROM movies
    WHERE year = "2012"
);

