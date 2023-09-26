CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL
);

INSERT INTO Book (title, author)
VALUES
    ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To Kill a Mockingbird', 'Harper Lee');
	
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

INSERT INTO Student (name, age)
VALUES
    ('John', 12),
    ('Lera', 11),
    ('Patrick', 10),
    ('Bob', 14);
	
CREATE TABLE Library (
    book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
    ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
    ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
    ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
    ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-12-08');

SELECT * FROM Library;
--Select the name of the student and the title of the borrowed books--
SELECT S.name, B.title
FROM Student S
INNER JOIN Library L ON S.student_id = L.student_fk_id
INNER JOIN Book B ON L.book_fk_id = B.book_id;

SELECT AVG(S.age) AS average_age
FROM Student S
INNER JOIN Library L ON S.student_id = L.student_fk_id
INNER JOIN Book B ON L.book_fk_id = B.book_id
WHERE B.title = 'Alice In Wonderland';

DELETE FROM Student WHERE name = 'John'; -- Will remove from libray as well