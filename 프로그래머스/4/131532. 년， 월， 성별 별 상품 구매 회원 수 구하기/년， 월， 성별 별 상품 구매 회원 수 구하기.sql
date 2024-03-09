SELECT TO_NUMBER(TO_CHAR(OS.SALES_DATE,'YYYY')) YEAR
      ,TO_NUMBER(TO_CHAR(OS.SALES_DATE,'MM')) MONTH
      ,UI.GENDER, COUNT(DISTINCT OS.USER_ID) USERS
FROM USER_INFO UI INNER JOIN ONLINE_SALE OS ON (UI.USER_ID=OS.USER_ID)
WHERE UI.GENDER IS NOT NULL
GROUP BY TO_NUMBER(TO_CHAR(OS.SALES_DATE,'YYYY'))
        ,TO_NUMBER(TO_CHAR(OS.SALES_DATE,'MM'))
        ,UI.GENDER
ORDER BY TO_NUMBER(TO_CHAR(OS.SALES_DATE,'YYYY'))
        ,TO_NUMBER(TO_CHAR(OS.SALES_DATE,'MM'))
        ,UI.GENDER
