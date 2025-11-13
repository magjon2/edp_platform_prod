CREATE TABLE [dbo].[orderupdated_payment] (

	[pspReference] varchar(8000) NULL, 
	[EventEnqueuedUtcTime] datetime2(6) NULL, 
	[updated_datetime] datetime2(6) NULL, 
	[status_value] varchar(8000) NULL, 
	[title] varchar(8000) NULL, 
	[psp] varchar(8000) NULL, 
	[method] varchar(8000) NULL, 
	[alternative] varchar(8000) NULL, 
	[amount] float NULL, 
	[order_bk] varchar(8000) NULL, 
	[payment_bk] varchar(8000) NULL, 
	[orderNumber] varchar(8000) NULL, 
	[rn] bigint NULL
);