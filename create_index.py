import json

with open("convoy_donation_comments.json", "r", encoding="utf8") as fp:
    data = json.load(fp)

header = """| | | |
|-|-|-|
"""

with open("index.md", "w", encoding="utf8") as fp:
    fp.write(header)
    for row in data:
        comment = row["comment"].replace("\n", "<br />")
        fp.write(f"| {row['country']} | {row['name']} | {comment} |\n")
