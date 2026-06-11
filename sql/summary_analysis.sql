-- Tickets by category
SELECT category, COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY category
ORDER BY ticket_count DESC;

-- Average resolution time
SELECT category, AVG(resolution_time_hours) AS avg_resolution_hours
FROM support_tickets
WHERE status = 'Closed'
GROUP BY category;
