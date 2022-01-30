import csv
import json

available = []
unavailable = []

with open('result.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == "Available":
            available.append(row[0])
        else:
            unavailable.append(row[0])

print(len(available), len(unavailable))

with open('available.json', 'w') as f:
    json.dump(available, f)