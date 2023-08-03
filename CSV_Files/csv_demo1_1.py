import csv
from typing import List


def read_csv_file() -> List[List[str]]:
    with open('CSV_Files\loanapp.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  # Returns reader_object
        # print(csvReader)
        csvList = list(csvReader)
        return csvList

csv_res = read_csv_file()
names = []
stats = []

for row in csv_res:
    names.append(row[0])
    stats.append(row[1])
    
print(names)
print(stats)
