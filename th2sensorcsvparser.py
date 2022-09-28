import csv
import datetime
import dblib

lines = []


def percentage(part, whole):
    percent = 100 * float(part)/float(whole)
    return "%.2f" % percent + "%"


if __name__ == '__main__':
    with open('Door.csv', 'r') as mycsv:
        next(mycsv)  # Skip the MAC Address in the first line
        reader = csv.DictReader((x.replace('\0', '').replace('ÿþ', '') for x in mycsv), delimiter='\t')
        rowwritten = 0
        rowskipped = 0
        dateList = []
        rows = list(reader)
        totalrows = len(rows)
        for i, row in enumerate(rows):
            if row['Time'] not in dateList:
                sampleParsed = row['Time'].split(' ')[0].split('-')
                dateList.append(datetime.datetime(int(sampleParsed[0]), int(sampleParsed[1]), int(sampleParsed[2])))
            if dblib.saveData(row['Time'], row['Temperature(C)'], row['Humidity(%RH)']):
                rowwritten = rowwritten + 1
            else:
                rowskipped = rowskipped + 1
            if i + 1 == totalrows:
                print("Writting in db. Please wait...%s" % percentage(i+1, totalrows) + " Done!")
            else:
                print("Writting in db. Please wait...%s" % percentage(i+1, totalrows), end='\r')

        # Find the oldes date in the CSV file
        datecandidate = min(dateList).strftime("%Y-%m-%d")

        # print("Updating Statistical table...", end='\r')
        # expected is 144 entries in DB per day. If so, day is complete so run the SP
        # if dblib.getdailyEntried(datecandidate) == 144:
        #    dblib.execStoreProcedure(datecandidate)
        # print("Updating Statistical table...done")

        print("" + str(rowwritten) + " rows written in db")
        print("" + str(rowskipped) + " rows skipped")
