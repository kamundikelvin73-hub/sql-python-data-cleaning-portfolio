-- Standardize category values
SELECT
  ticket_id,
  LOWER(user_email) AS user_email,
  CASE
    WHEN LOWER(category) = 'account access' THEN 'Account Access'
    WHEN LOWER(category) = 'billing' THEN 'Billing'
    WHEN LOWER(category) IN ('tech support', 'technical support') THEN 'Technical Support'
    WHEN LOWER(category) = 'security' THEN 'Security'
    ELSE 'Unknown'
  END AS cleaned_category,
  status,
  created_date,
  resolution_time_hours
FROM support_tickets;
