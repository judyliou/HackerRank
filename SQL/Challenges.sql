SELECT h.hacker_id, h.name, COUNT(*) AS cnt
FROM Hackers h
JOIN Challenges c on h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING 
    /* the max count that anyone has */
    cnt = (SELECT COUNT(*) FROM Challenges GROUP BY hacker_id ORDER BY count(*) DESC limit 1)
    
    /* anyone whose count only exists one time */
    OR cnt IN (
        SELECT temp.cnt
        FROM (SELECT count(*) AS cnt FROM challenges GROUP BY hacker_id) temp
        GROUP BY temp.cnt
        HAVING COUNT(temp.cnt) = 1)
ORDER BY cnt DESC, hacker_id
