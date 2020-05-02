import csv
event_report = {}
with open('data_example1.csv') as f:
    csv_reader = csv.DictReader(f)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        print(row)

#         event_report[row["User Name"]] = row["Access Key"]
#         line_count += 1
# print(event_report)