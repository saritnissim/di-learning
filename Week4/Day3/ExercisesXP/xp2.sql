UPDATE film
SET language_id = 2
WHERE film.language_id = 6;

-- Constraints on customer table: address_id.  
--When inserting data into the "customer" table, 
-- you need to ensure that the value for this field matches the primary key 
--values in the referenced tables

DROP TABLE customer_review; -- Easy step

SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

SELECT f.title, f.rental_rate
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;

SELECT title
FROM film
WHERE description ILIKE '%sumo wrestler%'
AND actor_id IN (SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe');

SELECT title
FROM film
WHERE length < 60 
AND rating = 'R';

SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND r.rental_date BETWEEN '2005-07-28' AND '2005-08-01'
AND r.rental_rate > 4.00;


SELECT f.title, f.replacement_cost
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
order by f.replacement_cost desc
limit 3;