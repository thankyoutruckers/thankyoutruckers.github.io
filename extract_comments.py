import csv
import json

data = []

with open("convoy_donations.csv", 'r', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        if len(row[10]) > 0:
            name = row[9] + " " + row[10][0] + "."
        else:
            name = row[9]
        obj = {
            "name": name,
            "country": row[13],
            "comment": row[15]
        }
        data.append(obj)

with open("convoy_donation_comments.json", "w") as fp:
    json.dump(data, fp)
