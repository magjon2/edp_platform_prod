CREATE TABLE [dbo].[sg_testorder] (

	[orderNumber] varchar(100) NULL, 
	[orderDate] varchar(100) NULL, 
	[salesBrand] varchar(100) NULL, 
	[country] varchar(100) NULL, 
	[currency] varchar(100) NULL, 
	[source_name] varchar(100) NULL, 
	[source_title] varchar(100) NULL, 
	[EventProcessedUtcTime] varchar(100) NULL, 
	[PartitionId] varchar(100) NULL, 
	[EventEnqueuedUtcTime] varchar(100) NULL, 
	[InsertTimestamp] datetime2(6) NULL, 
	[rn] bigint NULL
);