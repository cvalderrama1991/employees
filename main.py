import csv

# data = [
#     ["id", "last_name", "first_name", "middle_name", "age", "city", "score"],
#     [1, "smith", "alice", "kate" "25", "new york", 89.5],
#     [2, "thomas", "bob", "dan", 19, "london", 95.0],
#     [3, "laved", "carlos", "otrebla", 31, "madrid", 82.7],
#     [4, "williams", "diana", "nancy", 28, "tokyo", 91.2]
# ]

# with open("employees.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)

# Write all rows at once
# writer.writerows(data)

# print("CSV file created successfully!")

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
