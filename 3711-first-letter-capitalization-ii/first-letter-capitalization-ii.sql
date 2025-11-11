WITH RECURSIVE tokens AS (
    SELECT
        content_id,
        content_text,
        1 AS token_no,
        REGEXP_SUBSTR(content_text, '[^ ]+| +', 1, 1) AS token
    FROM user_content
    UNION ALL
    SELECT
        content_id,
        content_text,
        token_no + 1,
        REGEXP_SUBSTR(content_text, '[^ ]+| +', 1, token_no + 1)
    FROM tokens
    WHERE token IS NOT NULL
), hyphen_parts AS (
    SELECT
        content_id,
        token_no,
        token,
        1 AS part_no,
        REGEXP_SUBSTR(token, '[^-]+', 1, 1) AS part
    FROM tokens
    WHERE REGEXP_LIKE(token, '^[A-Za-z]+(-[A-Za-z]+)+$')
    UNION ALL
    SELECT
        content_id,
        token_no,
        token,
        part_no + 1,
        REGEXP_SUBSTR(token, '[^-]+', 1, part_no + 1)
    FROM hyphen_parts
    WHERE part IS NOT NULL
), transformed_hyphens AS (
    SELECT
        content_id,
        token_no,
        GROUP_CONCAT(
            CONCAT(UPPER(LEFT(part, 1)), LOWER(SUBSTRING(part, 2)))
            ORDER BY part_no SEPARATOR '-'
        ) AS converted_token
    FROM hyphen_parts
    GROUP BY content_id, token_no
)
SELECT
    t.content_id,
    t.content_text AS original_text,
    COALESCE(GROUP_CONCAT(
        CASE
            WHEN REGEXP_LIKE(t.token, '^[A-Za-z]+(-[A-Za-z]+)+$') THEN h.converted_token
            WHEN REGEXP_LIKE(t.token, '^[A-Za-z]') THEN CONCAT(UPPER(LEFT(t.token, 1)), LOWER(SUBSTRING(t.token, 2)))
            ELSE t.token
        END
        ORDER BY t.token_no SEPARATOR ''
    ), '') AS converted_text
FROM tokens t
LEFT JOIN transformed_hyphens h
    ON h.content_id = t.content_id AND h.token_no = t.token_no
GROUP BY t.content_id, t.content_text;