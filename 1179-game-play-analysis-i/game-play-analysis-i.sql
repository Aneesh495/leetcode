
-- Find the earliest event_date per player as their first login
SELECT
  player_id,
  MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
