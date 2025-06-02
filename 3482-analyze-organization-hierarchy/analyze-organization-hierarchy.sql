WITH RECURSIVE hier AS (
    SELECT employee_id, employee_name, manager_id, salary, 1 AS level
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.employee_name, e.manager_id, e.salary, h.level + 1
    FROM Employees e
    JOIN hier h ON e.manager_id = h.employee_id
),
sub AS (
    SELECT employee_id AS anc, employee_id AS desc_id, salary
    FROM Employees
    UNION ALL
    SELECT s.anc, e.employee_id, e.salary
    FROM sub s
    JOIN Employees e ON e.manager_id = s.desc_id
)
SELECT
    h.employee_id,
    h.employee_name,
    h.level,
    COUNT(s.desc_id) - 1 AS team_size,
    SUM(s.salary) AS budget
FROM hier h
JOIN sub s ON h.employee_id = s.anc
GROUP BY h.employee_id, h.employee_name, h.level
ORDER BY h.level ASC, budget DESC, h.employee_name ASC;