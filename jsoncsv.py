import json
import csv

# Load the JSON file
with open("followers_1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Collect all usernames (the "value" field inside "string_list_data")
usernames = []
for item in data:
    if "string_list_data" in item and len(item["string_list_data"]) > 0:
        for s in item["string_list_data"]:
            usernames.append(s.get("value", ""))

# Write to CSV
with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["username"])  # header
    for username in usernames:
        writer.writerow([username])

print("Done! Saved to output.csv")
