SET @rowIndex := -1;

SELECT ROUND(AVG(n.LAT_N), 4)

/* create a new column 'rowIndex' and order by LAT_N*/
FROM(SELECT @rowIndex := @rowIndex + 1 as rowIndex, s.LAT_N
        FROM STATION AS s
        ORDER BY s.LAT_N) AS n
        
/* find the midian row index */        
WHERE n.rowIndex IN (FLOOR(@rowIndex/2), CEIL(@rowIndex/2));
