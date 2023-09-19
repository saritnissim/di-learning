-- Exercise 1 --
select * 
from items
order by price asc;

select * 
from items
where price >= 80
order by price desc

select first_name, last_name
from customers
order by first_name
limit 3;