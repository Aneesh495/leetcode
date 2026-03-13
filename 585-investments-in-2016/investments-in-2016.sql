
SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
WHERE EXISTS (
  SELECT 1
  FROM Insurance j
  WHERE j.pid <> i.pid AND j.tiv_2015 = i.tiv_2015
)
AND NOT EXISTS (
  SELECT 1
  FROM Insurance k
  WHERE k.pid <> i.pid AND k.lat = i.lat AND k.lon = i.lon
);
