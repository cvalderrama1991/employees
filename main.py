import csv

# data = [
#     ["id", "last_name", "first_name", "middle_name", "age", "city", "score"],
#     [1, "smith", "alice", "kate" "25", "new york", 89.5],
#     [2, "thomas", "bob", "dan", 19, "london", 95.0],
#     [3, "laved", "carlos", "otrebla", 31, "madrid", 82.7],
#     [4, "williams", "diana", "nancy", 28, "tokyo", 91.2]
# ]
#
# with open("people.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#
#     # Write all rows at once
#    # writer.writerows(data)
#
#    # print("CSV file created successfully!")

filename = "people.csv"

# # Step 1: Read all data
rows = []
with open(filename, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)           # keep header
    rows.append(header)
#
    for row in reader:
        # Assuming name is in column 0 (index 0)
        if row and row[6]:           # skip empty rows
            row[6] = row[6].title()  # or .capitalize()
        rows.append(row)
#
# # Step 2: Write back to the SAME file
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
#
print("File updated in place!")
