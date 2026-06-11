-- Missing category check
SELECT COUNT(*) AS missing_category_count
FROM support_tickets
WHERE category IS NULL OR category = '';

-- Duplicate ticket check
SELECT ticket_id, COUNT(*)
FROM support_tickets
GROUP BY ticket_id
HAVING COUNT(*) > 1;

-- Invalid status check
SELECT *
FROM support_tickets
WHERE status NOT IN ('Open', 'Closed', 'Pending');
