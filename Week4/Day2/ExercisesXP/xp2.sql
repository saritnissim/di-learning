-- select * 
-- from customer;

-- select first_name || ' ' || last_name as full_name
-- from customer;

--  Write a query to select all the create_date from the “customer” table (there should be no duplicates).
-- select distinct create_date
-- from customer

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
-- select *
-- from customer
-- order by first_name desc

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
-- select film_id, title, description, release_year, rental_rate
-- from film
-- order by rental_rate asc

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
-- select CONCAT(address, ' ', address2) as address
-- from customer
-- inner join address
-- on customer.address_id = address.address_id
-- where address.district='Texas'

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
-- select * 
-- from film
-- where film_id in (15, 150);

-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
-- select film_id, title, description, length, rental_rate
-- from film
-- where title='Harry Potter'

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
-- select film_id, title, description, length, rental_rate
-- from film
-- where title like'Ha%';

-- Write a query which will find the 10 cheapest movies.
-- select * 
-- from film
-- order by rental_rate desc
-- limit 10;

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
-- select * 
-- from film
-- order by rental_rate desc
-- OFFSET 10 FETCH NEXT 10 ROWS ONLY;

-- Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
-- select c.first_name, c.last_name, p.amount, p.payment_date
-- from customer c 
-- inner join payment p on c.customer_id = p.customer_id
-- order by c.customer_id

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
-- select *
-- from  
--   film f,
-- left join
--   inventory i on f.film_id = i.film_id
-- where
--   inventory_id is null;

-- Write a query to find which city is in which country.
-- select city, country
-- from city 
-- inner join country on city.country_id = country.country_id

-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
-- select customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- from customer
-- inner join payment on payment.customer_id = customer.customer_id
-- order by payment.staff_id