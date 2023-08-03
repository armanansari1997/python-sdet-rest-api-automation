import csv 
from typing import List


def write_csv_file():
    with open('CSV_Files\loanapp.csv', 'a') as wFile:
        write = csv.writer(wFile)
        # We have to send the data in the List format only
        # because we are getting the result in the list format
        # Note: make sure file is not opened
        write.writerow(['Arman', 'accepted'])
        print('Data is added successfully !!!')


# Calling the write_csv_file() function
write_csv_file()
    