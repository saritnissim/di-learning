-- Part One --
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR NOT NULL
);

CREATE TABLE Customer_Profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT REFERENCES Customer(id)
);


INSERT INTO Customer (first_name, last_name)
VALUES
    ('John', 'Doe'),
    ('Jerome', 'Lalu'),
    ('Lea', 'Rive');
	
INSERT INTO Customer_Profile (isLoggedIn, customer_id)
VALUES
    (true, (SELECT id FROM Customer WHERE first_name = 'John')),
    (false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));
	 
	 
-- 1. The first_name of LoggedIn customers
SELECT C.first_name
FROM Customer C
INNER JOIN Customer_Profile CP ON C.id = CP.customer_id
WHERE CP.isLoggedIn = true;

-- 2. All customers' first_name and isLoggedIn columns, including those without a profile
SELECT C.first_name, CP.isLoggedIn
FROM Customer C
LEFT JOIN Customer_Profile CP ON C.id = CP.customer_id;

-- 3. The number of customers that are not LoggedIn
SELECT COUNT(*)
FROM Customer C
LEFT JOIN Customer_Profile CP ON C.id = CP.customer_id
WHERE CP.isLoggedIn = false OR CP.isLoggedIn IS NULL;

