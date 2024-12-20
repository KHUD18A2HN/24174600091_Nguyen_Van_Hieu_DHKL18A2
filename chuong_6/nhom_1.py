import csv
with open(file="file_a.txt, mode="r"") as open_file:
          csv_reader = csv.reader(open,delimiter=",")

csv_file = list(csv_reader).copy()
for row in csv_file:
    print(row)