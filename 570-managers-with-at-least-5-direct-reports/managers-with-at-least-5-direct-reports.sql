
SELECT m.name
FROM Employee AS m
JOIN Employee AS e ON m.id = e.managerId
GROUP BY m.id, m.name
HAVING COUNT(*) >= 5;
