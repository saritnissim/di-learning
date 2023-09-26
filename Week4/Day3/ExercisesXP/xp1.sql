SELECT * FROM language;

SELECT film.title, film.description, language.name AS language_name
FROM film
JOIN language ON film.language_id = language.language_id;

SELECT film.title, film.description, language.name AS language_name
FROM language
LEFT JOIN film ON language.language_id = film.language_id;


CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR
);

INSERT INTO new_film (name)
VALUES
    ('Film A'),
    ('Film B');
	
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR,
    score INT CHECK (score >= 1 AND score <= 10),
    review_text TEXT,
    last_update TIMESTAMP
);

-- Add movie reviews
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES
    (1, 1, 'Review 1', 8, 'This is a good film.', CURRENT_TIMESTAMP),
    (2, 2, 'Review 2', 7, 'Enjoyable movie experience.', CURRENT_TIMESTAMP);

DELETE FROM new_film WHERE id = 1; -- It is removed from new_film
