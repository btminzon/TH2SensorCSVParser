USE Th2Sensor;

CREATE TABLE Stats (
	Date varchar(10) NOT NULL,
	TempAvg float NOT NULL,
	TempMax float NOT NULL,
	TempMin float NOT NULL,
	HumiAvg float NOT NULL,
	HumiMax float NOT NULL,
	HumiMin float NOT NULL,
	PRIMARY KEY (Date)
);



CREATE TABLE Data (
	Date varchar(50) NOT NULL,
	Temperature float NULL,
	Humidity float NULL,
	PRIMARY KEY (Date)
);


CREATE TABLE MonthlyStats (
	Date varchar(10) NOT NULL,
	TempAvg float NOT NULL,
	TempMax float NOT NULL,
	TempMin float NOT NULL,
	HumiAvg float NOT NULL,
	HumiMax float NOT NULL,
	HumiMin float NOT NULL,
	PRIMARY KEY (Date)
);


CREATE TABLE AvgProcessing (
	lastProcessing varchar(10) NOT NULL,
	lastMonthlyProcessing varchar(10) NOT NULL
);
