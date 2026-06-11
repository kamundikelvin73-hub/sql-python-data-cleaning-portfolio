import csv
from collections import Counter

PATH = "../datasets/cleaned_support_data.csv"

with open(PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

categories = Counter(row["category"] for row in rows)
statuses = Counter(row["status"] for row in rows)

print("Ticket counts by category:")
for category, count in categories.items():
    print(category, count)

print("\nTicket counts by status:")
for status, count in statuses.items():
    print(status, count)
