SELECT h.hacker_id, h.name, SUM(m.score) total
FROM(SELECT hacker_id, MAX(score) score
    FROM Submissions 
    GROUP BY hacker_id, challenge_id) m
JOIN Hackers h ON h.hacker_id = m.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total > 0
ORDER BY total DESC, h.hacker_id
