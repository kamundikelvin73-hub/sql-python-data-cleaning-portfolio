import csv

PATH = "../datasets/cleaned_support_data.csv"

required_fields = ["ticket_id", "user_email", "category", "status", "created_date"]

with open(PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

errors = []
ids = set()

for row in rows:
    for field in required_fields:
        if not row.get(field):
            errors.append(f"Missing {field} in ticket {row.get('ticket_id')}")
    if row["ticket_id"] in ids:
        errors.append(f"Duplicate ticket_id: {row['ticket_id']}")
    ids.add(row["ticket_id"])

print(f"Rows checked: {len(rows)}")
print(f"Errors found: {len(errors)}")
for error in errors:
    print(error)
