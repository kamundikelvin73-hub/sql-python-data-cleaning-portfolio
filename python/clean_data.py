import csv

INPUT = "../datasets/messy_customer_support_data.csv"
OUTPUT = "../datasets/cleaned_support_data.csv"

CATEGORY_MAP = {
    "account access": "Account Access",
    "billing": "Billing",
    "tech support": "Technical Support",
    "technical support": "Technical Support",
    "security": "Security",
    "": "Unknown"
}

STATUS_MAP = {
    "open": "Open",
    "closed": "Closed",
    "pending": "Pending"
}

def clean_row(row):
    row["user_email"] = row["user_email"].lower().strip()
    row["category"] = CATEGORY_MAP.get(row["category"].lower().strip(), "Unknown")
    row["status"] = STATUS_MAP.get(row["status"].lower().strip(), row["status"])
    return row

with open(INPUT, newline="", encoding="utf-8") as infile, open(OUTPUT, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        writer.writerow(clean_row(row))

print("Data cleaning completed.")
