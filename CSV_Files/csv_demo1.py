import csv
from typing import List


def read_csv_file() -> List[List[str]]:
    with open('CSV_Files\loanapp.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  # Returns reader_object
        # print(csvReader)
        csvList = list(csvReader)
        return csvList

res = read_csv_file()
# print(res)

# get the result as row by row
for row in res:
    print(row)