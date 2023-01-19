USE [Th2Sensor]
GO

/****** Object:  StoredProcedure [dbo].[CalcMonthlyAverage]    Script Date: 2023-01-19 9:04:56 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[CalcMonthlyAverage]
	@MonthAdd varchar(20)
	
AS

INSERT INTO dbo.MonthlyStats (Date, TempAvg, TempMax, TempMin, HumiAvg, HumiMax, HumiMin)
VALUES (
	@MonthAdd 
	,(SELECT ROUND(AVG(Temperature),2) FROM DBO.Data WHERE Date like '%' + @MonthAdd + '%')
	,(SELECT ROUND(MAX(Temperature),2) FROM DBO.Data WHERE Date like '%' + @MonthAdd + '%')
	,(SELECT ROUND(MIN(Temperature),2) FROM DBO.Data WHERE Date like '%' + @MonthAdd + '%')
	,(SELECT ROUND(AVG(Humidity),2) FROM DBO.Data WHERE Date like '%' + @MonthAdd + '%')
	,(SELECT ROUND(MAX(Humidity),2) FROM DBO.Data WHERE Date like '%' + @MonthAdd + '%')
	,(SELECT ROUND(MIN(Humidity),2) FROM DBO.Data WHERE Date like '%' + @MonthAdd + '%'))

UPDATE dbo.AvgProcessing
	SET lastMonthlyProcessing = @MonthAdd
GO



CREATE PROCEDURE [dbo].[CalcAverage] AS

DECLARE @DateAdd AS varchar(20)

SELECT @DateAdd = lastProcessing 
FROM dbo.AvgProcessing

DECLARE @NewDate AS varchar(20) = CONVERT(varchar(20), DATEADD(day, 1, @DateAdd) , 23)

INSERT INTO dbo.Stats (Date, TempAvg, TempMax, TempMin, HumiAvg, HumiMax, HumiMin)
VALUES (
	@NewDate
	,(SELECT ROUND(AVG(Temperature),2) FROM DBO.Data WHERE Date like '%' + @NewDate + '%')
	,(SELECT ROUND(MAX(Temperature),2) FROM DBO.Data WHERE Date like '%' + @NewDate + '%')
	,(SELECT ROUND(MIN(Temperature),2) FROM DBO.Data WHERE Date like '%' + @NewDate + '%')
	,(SELECT ROUND(AVG(Humidity),2) FROM DBO.Data WHERE Date like '%' + @NewDate + '%')
	,(SELECT ROUND(MAX(Humidity),2) FROM DBO.Data WHERE Date like '%' + @NewDate + '%')
	,(SELECT ROUND(MIN(Humidity),2) FROM DBO.Data WHERE Date like '%' + @NewDate + '%'))

UPDATE dbo.AvgProcessing
	SET lastProcessing = @NewDate
GO


