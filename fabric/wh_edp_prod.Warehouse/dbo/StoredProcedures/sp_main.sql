CREATE   PROCEDURE [dbo].[sp_main]
AS
BEGIN
    SET NOCOUNT ON;

    EXEC sp_upsert_orderupdated_row;
    EXEC sp_upsert_orderupdated_payment;
    EXEC sp_upsert_orderupdated_order
END;