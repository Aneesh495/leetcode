WITH ranked AS (
    SELECT
        student_id,
        subject,
        FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) AS first_score,
        FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_score,
        COUNT(*) OVER (PARTITION BY student_id, subject) AS cnt
    FROM Scores
)
SELECT DISTINCT student_id, subject, first_score, latest_score
FROM ranked
WHERE cnt >= 2 AND latest_score > first_score
ORDER BY student_id, subject;