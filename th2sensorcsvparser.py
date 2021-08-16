import csv
import dblib

lines = []
with open('door.csv', 'r') as mycsv:
    reader = csv.DictReader((x.replace('\0', '').replace('ÿþ', '') for x in mycsv), delimiter='\t')
    colwritten = 0
    for row in reader:
        # print(row)
        if dblib.saveData(row['Time'], row['Temperature(C)'], row['Humidity(%RH)']):
            colwritten = colwritten + 1
    print("Written " + str(colwritten) + " columns at db")
