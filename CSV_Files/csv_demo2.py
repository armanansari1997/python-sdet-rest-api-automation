import csv
from typing import List

# Building a logic 
# to get the data from CSV files
# based on conditional  query

def read_csv_file() -> List[List[str]]:
    with open('CSV_Files\loanapp.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  # Returns reader_object
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

# Changes is here
index = names.index('joshua')
loan_status = stats[index]
print('loan status is ', loan_status)
