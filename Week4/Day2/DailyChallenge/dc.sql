-- Questions --
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- A: Inner query is null. Null is a non-value and can't be compared. So 0

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- A: The inner query is 5, The outer query will have 2 rows, so the answer is 2.

 SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- A: Inner join is 5 and null. NULL in not a value to compare. So 0

SELECT COUNT(*) 
	FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- A: Inner query should give a 5. The outer query should be 2, because you can't compare the ft.id null