SELECT P.PRODUCT_CODE, P.PRICE * OS.AMOUNT SALES
FROM PRODUCT P INNER JOIN (
                            SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AMOUNT
                            FROM OFFLINE_SALE 
                            GROUP BY PRODUCT_ID
                          ) OS ON (P.PRODUCT_ID	= OS.PRODUCT_ID)
ORDER BY 2 DESC, 1 ASC