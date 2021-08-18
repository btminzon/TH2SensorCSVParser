import csv
import dblib

lines = []
with open('door.csv', 'r') as mycsv:
    reader = csv.DictReader((x.replace('\0', '').replace('ÿþ', '') for x in mycsv), delimiter='\t')
    rowwritten = 0
    rowskipped = 0
    print("Writting in db. Please wait...")
    for row in reader:
        # print(row)
        if dblib.saveData(row['Time'], row['Temperature(C)'], row['Humidity(%RH)']):
            rowwritten = rowwritten + 1
        else:
            rowskipped = rowskipped + 1
    print("" + str(rowwritten) + " rows written in db")
    print("" + str(rowskipped) + " rows skipped")
