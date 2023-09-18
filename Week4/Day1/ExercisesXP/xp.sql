-- create table items (
-- 	id serial primary key,
-- 	item_name varchar(50),
-- 	price float
-- ); 

-- insert into items (item_name, price) values ('small desk', 100), ('large desk', 300), ('fan', 80)

-- create table customers (
-- 	id serial primary key, 
-- 	first_name varchar(50),
-- 	last_name varchar(50)
-- );

-- insert into customers(first_name, last_name) values 
-- ('Greg', 'Jones'), 
-- ('Sandra', 'Jones'), 
-- ('Scott', 'Scott'), 
-- ('Trevor', 'Green'), 
-- ('Melanie', 'Johnson')

-- select * from items;
-- select * from items where price > 80;
-- select * from items where price <= 300;
-- select * from customers where last_name = 'Smith'; -- Answer: None
-- select * from customers where last_name = 'Jones';
-- select * from customers where first_name != 'Scott';