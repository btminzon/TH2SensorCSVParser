import pymssql

########################
# DB: Th2Sensor
#
# Tables:
#
#   Table: dbo.Data
#   Columns:
#    *  Date
#       Temperature
#       Humidity
#
#########################


class Dblib:

    def __init__(self):
        try:
            self.con = pymssql.connect(server='192.168.0.105', port=1434, timeout =20, user='dataParser',
                                       password='Temsrules1', database="Th2Sensor")
            self.cur = self.con.cursor()
            self.connected = True
            # print("Connected to DB")
        except Exception as e:
            self.connected = False
            print("Failed to connect to DB: ".format(e))

    def getDate(self, date):
        if self.connected:
            self.cur.execute("SELECT Date FROM dbo.Data WHERE Date = %s", str(date))
            dat = self.cur.fetchone()
            # if dat is not None:
            # print("Date already in DB. Fetched: %s", dat)
            return dat
        else:
            print("getDate: Not connected to DB")

    def setDate(self, date):
        if self.connected:
            self.cur.execute("INSERT INTO dbo.Data (Date) VALUES (%s)", (str(date)))
            self.con.commit()
        else:
            print("setDate: Not connected to DB")

    def getTemperature(self, date):
        if self.connected:
            self.cur.execute("SELECT Temperature FROM dbo.Data WHERE Date = %s", str(date))
            temp = self.cur.fetchone()[0]
            # if temp is not None:
            # print("Temperature already in DB. Fetched: " + str(temp))
            return temp
        else:
            print("getTemeprature: Not connected to DB")

    def setTemperature(self, date, temperature):
        if self.connected:
            self.cur.execute("UPDATE dbo.Data SET Temperature = %s WHERE Date = %s", (str(temperature), str(date)))
            self.con.commit()
        else:
            print("setTemperature: Not connected to DB")

    def getHumidity(self, date):
        if self.connected:
            self.cur.execute("SELECT Humidity FROM dbo.Data WHERE Date = %s", str(date))
            humi = self.cur.fetchone()[0]
            return humi
        else:
            print("getHumidity: Not connected to DB")

    def setHumidity(self, date, humidity):
        if self.connected:
            self.cur.execute("UPDATE dbo.Data SET Humidity = %s WHERE Date = %s", (str(humidity), str(date)))
            self.con.commit()
        else:
            print("setHumidity: Not connected to DB")

    def setData(self, date, temperature, humidity):
        if self.connected:
            self.cur.execute("INSERT INTO dbo.Data (Date, Temperature, Humidity) VALUES (%s, %s, %s)",
                             (str(date), str(temperature), str(humidity)))
            self.con.commit()
        else:
            print("setData: Not connected to DB")

    def getNumberPointsPerDay(self, date):
        if self.connected:
            self.cur.execute("SELECT count(Date) from dbo.Data where Date like '{0}%'".format(date))
            count = self.cur.fetchone()[0]
            return int(count)
        else:
            print("getNumberPointsPerDay: Not connected to DB")

    def execsp(self, date):
        if self.connected:
            self.cur.execute("EXEC dbo.CalcAverage @DateAdd ='{0}'".format(date))
        else:
            print("execStoreProcedure: Not connected to DB")


def saveData(date, temperature, humidity):
    lib = Dblib()
    dat = lib.getDate(date)
    if dat is None:
        lib.setData(date, temperature, humidity)
        return True
    else:
        ret = 0
        temp = lib.getTemperature(date)
        if temp is None:
            lib.setTemperature(date, temperature)
            ret = 1
        humi = lib.getHumidity(date)
        if humi is None:
            lib.setHumidity(date, humidity)
            ret = 1
        if ret:
            return True
        else:
            return False


def getdailyEntried(date):
    lib = Dblib()
    return lib.getNumberPointsPerDay(date)


def execStoreProcedure(date):
    lib = Dblib()
    lib.execsp(date)






