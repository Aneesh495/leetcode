
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
  SELECT 1
  FROM Orders o
  JOIN Company c ON c.com_id = o.com_id
  WHERE o.sales_id = s.sales_id
    AND c.name = 'RED'
);
