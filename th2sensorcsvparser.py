import csv
import dblib

lines = []


def percentage(part, whole):
    percent = 100 * float(part)/float(whole)
    return "%.2f" % percent + "%"


with open('door.csv', 'r') as mycsv:
    reader = csv.DictReader((x.replace('\0', '').replace('ÿþ', '') for x in mycsv), delimiter='\t')
    readercopy = reader
    rowwritten = 0
    rowskipped = 0
    rows = list(reader)
    totalrows = len(rows)
    for i, row in enumerate(rows):
        if dblib.saveData(row['Time'], row['Temperature(C)'], row['Humidity(%RH)']):
            rowwritten = rowwritten + 1
        else:
            rowskipped = rowskipped + 1
        if i + 1 == totalrows:
            print("Writting in db. Please wait...%s" % percentage(i+1, totalrows) + " Done!")
        else:
            print("Writting in db. Please wait...%s" % percentage(i+1, totalrows), end='\r')
    print("" + str(rowwritten) + " rows written in db")
    print("" + str(rowskipped) + " rows skipped")
