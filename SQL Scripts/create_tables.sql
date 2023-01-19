USE [Th2Sensor]
GO

/****** Object:  Table [dbo].[Stats]    Script Date: 2023-01-19 9:06:05 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Stats](
	[Date] [varchar](10) NOT NULL,
	[TempAvg] [float] NOT NULL,
	[TempMax] [float] NOT NULL,
	[TempMin] [float] NOT NULL,
	[HumiAvg] [float] NOT NULL,
	[HumiMax] [float] NOT NULL,
	[HumiMin] [float] NOT NULL,
 CONSTRAINT [PK__Stats__1FCAD5C1D361DABF] PRIMARY KEY CLUSTERED 
(
	[Date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE TABLE [dbo].[Data](
	[Date] [varchar](50) NOT NULL,
	[Temperature] [float] NULL,
	[Humidity] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[Date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE TABLE [dbo].[MonthlyStats](
	[Date] [varchar](10) NOT NULL,
	[TempAvg] [float] NOT NULL,
	[TempMax] [float] NOT NULL,
	[TempMin] [float] NOT NULL,
	[HumiAvg] [float] NOT NULL,
	[HumiMax] [float] NOT NULL,
	[HumiMin] [float] NOT NULL,
 CONSTRAINT [PK_dbo.MonthlyStats] PRIMARY KEY CLUSTERED 
(
	[Date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE TABLE [dbo].[AvgProcessing](
	[lastProcessing] [varchar](10) NOT NULL,
	[lastMonthlyProcessing] [varchar](10) NOT NULL
) ON [PRIMARY]
GO
