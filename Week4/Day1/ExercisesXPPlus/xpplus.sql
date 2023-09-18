-- create table students(
-- 	id serial primary key,
-- 	last_name varchar(50),
-- 	first_name varchar(50),
-- 	birth_date date
-- );

-- insert into students (first_name, last_name, birth_date)
-- values 
-- ('Marc', 'Benichou', '11/02/1998'),
-- ('Yoan', 'Cohen', '12/03/2010'),
-- ('Lea', 'Benichou', '07/27/1987'),
-- ('Amelia', 'Dux', 	'04/07/1996'),
-- ('David', 'Grez', 	'06/14/2003'),
-- ('Omer', 'Simpson', '10/03/1980');

-- insert into students(last_name, first_name, birth_date) values('Nissim', 'Sarit', '04/23/1990')

select * from students;
select first_name, last_name from students;
select first_name, last_name from students where id=2;
select first_name, last_name from students where first_name= 'Marc' and last_name = 'Benichou';
select first_name, last_name from students where first_name='Marc' or last_name='Benichou'
select first_name, last_name from students where first_name like '%a%'
select first_name, last_name from students where first_name like 'a%'
select first_name, last_name from students where first_name like '%a'
select first_name, last_name from students where first_name like '%a_'
select first_name, last_name from students where id=1 and id=3

select * from students where birth_date >= '01/01/2000'


