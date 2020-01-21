/*Find pairs which x = y and appears more than one time*/
SELECT f1.X, f1.Y FROM Functions AS f1 
WHERE f1.X = f1.Y GROUP BY f1.X, f1.Y HAVING COUNT(*) > 1
UNION
/*Find pairs x1 = y2 and y1 = x2*/
SELECT f1.X, f1.Y FROM Functions AS f1, Functions AS f2
WHERE f1.X = f2.Y AND f2.X = f1.Y AND f1.X < f1.Y
ORDER BY X;
