SELECT Start_Date, MIN(End_Date) 
FROM 
    /*Find the start date not in end date so that is the start date for a project*/
    (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) AS s,
    
    /*Find the end date not in start date so that is the end date for a project*/
    (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) AS e

/*cross join and find the minmum end date that is larger than start date*/
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY DATEDIFF(MIN(End_Date), Start_Date), Start_Date
