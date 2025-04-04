-- Auto Generated (Do not modify) 4927926FEB1D243D38ECBF5DCB3820B636876B1B79EA412A687B1B45FA43A580
/**************************************************************************************
Description:    This script creates NYTaxi views and stored procedures
**************************************************************************************/

/***************************************************************
Create a view to find the preferred method of payment and associated amount processed in 2013 year
*****************************************************************/

CREATE VIEW [dbo].[vw_PaymentAnalysis] AS
SELECT
    PaymentType
    ,COUNT(T.PaymentType) AS PaymentsCount
    ,SUM(TotalAmount) AS TotalAmountProcessed
FROM dbo.Trip AS T
JOIN dbo.[Date] AS D
    ON T.[DateID]=D.[DateID]
WHERE YEAR(D.[Date])=2013
GROUP BY    
    PaymentType