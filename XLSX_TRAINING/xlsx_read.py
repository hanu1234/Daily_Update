import csv
user_credentials = {}
with open('example.csv') as f:
    csv_reader = csv.DictReader(f)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        user_credentials[row["User Name"]] = row["Access Key"]
        line_count += 1
print(user_credentials)