SET @r1 = 0, @r2 = 0, @r3 = 0, @r4 = 0;

SELECT MAX(Doctor), MAX(Professor), MAX(Singer), MAX(Actor)
FROM
    /* Turn to a pivot table where the Rowline indicate the number of each occupation so far */
    /* Name shown in the corresponding occupation column; other columns are 'NULL' */
    (SELECT (CASE Occupation WHEN 'Doctor' THEN @r1:=@r1+1
                            WHEN 'Professor' THEN @r2:=@r2+1
                            WHEN 'Singer' THEN @r3:=@r3+1
                            WHEN 'Actor' THEN @r4:=@r4+1 END) AS Rowline,
             CASE WHEN Occupation='Doctor' THEN Name ELSE NULL END AS Doctor,
             CASE WHEN Occupation = 'Professor' THEN Name END AS Professor,
             CASE WHEN Occupation = 'Singer' THEN Name END AS Singer,
             CASE WHEN Occupation = 'Actor' THEN Name END AS Actor
    /* Group by the Rowline and select the Max (Min works as well) to compact the table */
    FROM OCCUPATIONS ORDER BY Name) as t
GROUP BY Rowline;
